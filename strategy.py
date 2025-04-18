"""
Simplified Strategy Implementation for Alpaca Markets
Based on the TradingView Pine Script strategy with small profit targets
"""
import os
import time
import logging
import schedule
from datetime import datetime, timedelta
import pandas as pd
import numpy as np
from dotenv import load_dotenv
from alpaca_trade_api.rest import REST, TimeFrame
import config
from utils import get_hourly_data, get_minute_data, calculate_hour_trend, calculate_indicators, handle_api_rate_limits, calculate_max_shares

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("strategy.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger()

# Load environment variables
load_dotenv()

# Initialize Alpaca API
API_KEY = os.getenv("ALPACA_API_KEY")
API_SECRET = os.getenv("ALPACA_API_SECRET")
PAPER = os.getenv("ALPACA_PAPER", "True").lower() in ("true", "1", "t")
BASE_URL = "https://paper-api.alpaca.markets" if PAPER else "https://api.alpaca.markets"

api = REST(API_KEY, API_SECRET, BASE_URL, api_version='v2')

# State tracking
last_buy_rsi_bar = None
last_sell_rsi_bar = None
position_value = 0
lookback_window = config.LOOKBACK_WINDOW
consecutive_losses = 0
last_trade_result = None

def check_market_hours():
    """Check if the market is open"""
    clock = api.get_clock()
    return clock.is_open

def check_trading_condition():
    """Check if we should be trading (market open, not near close)"""
    if not check_market_hours():
        logger.info("Market is closed. Waiting for market to open.")
        return False
    
    # Don't trade in the last 5 minutes of the day
    clock = api.get_clock()
    closing_time = clock.next_close.replace(tzinfo=None)
    current_time = datetime.now()
    
    if (closing_time - current_time).total_seconds() < 300:  # Less than 5 minutes to close
        logger.info("Less than 5 minutes to market close. Not trading.")
        return False
    
    # Check for consecutive losses
    global consecutive_losses
    if consecutive_losses >= config.MAX_CONSECUTIVE_LOSSES:
        logger.warning(f"Reached maximum consecutive losses ({config.MAX_CONSECUTIVE_LOSSES}). Pausing trading.")
        return False
    
    return True

def get_current_position():
    """Get current position for the symbol"""
    try:
        position = api.get_position(config.SYMBOL)
        return int(float(position.qty))
    except Exception:
        return 0

def cancel_all_orders():
    """Cancel all open orders for the symbol"""
    try:
        api.cancel_all_orders()
        logger.info("Canceled all open orders")
    except Exception as e:
        logger.error(f"Error canceling orders: {str(e)}")

def check_volume_sufficient(df):
    """
    Check if the volume is sufficient for trading
    """
    recent_volume = df['volume'].iloc[-1]
    if recent_volume < config.MIN_VOLUME_THRESHOLD:
        logger.info(f"Volume too low for trading: {recent_volume} < {config.MIN_VOLUME_THRESHOLD}")
        return False
    return True

def determine_position_size(latest_close):
    """
    Determine position size based on risk parameters
    """
    if not config.USE_DYNAMIC_POSITION_SIZING:
        return config.QUANTITY
    
    try:
        # Get account equity
        account = api.get_account()
        equity = float(account.equity)
        
        # Calculate risk amount
        risk_amount = equity * (config.RISK_PER_TRADE_PCT / 100)
        
        # Calculate position size based on stop loss
        price_risk = latest_close * config.STOP_LOSS
        position_size = risk_amount / price_risk
        
        # Apply maximum position size constraint
        position_size = min(position_size, config.MAX_POSITION_SIZE)
        
        # Round to 3 decimal places for fractional shares
        position_size = round(position_size, 3)
        
        # Ensure minimum position size
        position_size = max(position_size, 0.001)
        
        logger.info(f"Dynamic position sizing: {position_size} shares based on ${equity} equity")
        return position_size
    
    except Exception as e:
        logger.error(f"Error in position sizing: {str(e)}, using default quantity")
        return config.QUANTITY

def update_trade_stats(is_profitable):
    """
    Update trading statistics after a trade completes
    """
    global consecutive_losses, last_trade_result
    
    if is_profitable:
        consecutive_losses = 0
        last_trade_result = "win"
        logger.info("Trade was profitable. Resetting consecutive losses.")
    else:
        consecutive_losses += 1
        last_trade_result = "loss"
        logger.warning(f"Trade was unprofitable. Consecutive losses: {consecutive_losses}")

def run_strategy():
    """Main strategy execution function"""
    global last_buy_rsi_bar, last_sell_rsi_bar
    
    if not check_trading_condition():
        return
    
    try:
        logger.info(f"Running strategy for {config.SYMBOL}")
        
        # On startup, cancel all existing orders if configured
        if config.CANCEL_ALL_ON_STARTUP:
            cancel_all_orders()
            # Turn off the flag after first run
            config.CANCEL_ALL_ON_STARTUP = False
        
        # Get current position
        current_position = get_current_position()
        logger.info(f"Current position: {current_position} shares")
        
        # Get 1-hour data for trend determination
        hourly_data = get_hourly_data(api, config.SYMBOL)
        trend_state = calculate_hour_trend(hourly_data, config.FAST_PERIOD, config.SLOW_PERIOD)
        logger.info(f"1-hour trend state: {trend_state}")
        
        # Get minute data for signal generation
        minute_data = get_minute_data(api, config.SYMBOL)
        
        # Calculate all indicators
        df = calculate_indicators(
            minute_data,
            config.ULTRAFAST_PERIOD,
            config.FAST_PERIOD,
            config.SLOW_PERIOD,
            config.RSI_PERIOD,
            config.MACD_FAST_LENGTH,
            config.MACD_SLOW_LENGTH,
            config.MACD_SIGNAL_SMOOTHING
        )
        
        # Check if volume is sufficient
        if not check_volume_sufficient(df):
            return
        
        # Get the latest bar data
        latest_bar = df.iloc[-1]
        latest_close = latest_bar['close']
        current_bar_index = len(df) - 1
        
        # Update RSI signals
        if df['rsi'].iloc[-1] < config.RSI_OVERSOLD:
            last_buy_rsi_bar = current_bar_index
            logger.info(f"RSI oversold condition detected. RSI: {df['rsi'].iloc[-1]:.2f}")
        
        if df['rsi'].iloc[-1] > config.RSI_OVERBOUGHT:
            last_sell_rsi_bar = current_bar_index
            logger.info(f"RSI overbought condition detected. RSI: {df['rsi'].iloc[-1]:.2f}")
        
        # Check if RSI signals are still valid (within lookback window)
        if last_buy_rsi_bar is not None and (current_bar_index - last_buy_rsi_bar > lookback_window):
            last_buy_rsi_bar = None
            logger.info("Buy RSI signal expired (outside lookback window)")
        
        if last_sell_rsi_bar is not None and (current_bar_index - last_sell_rsi_bar > lookback_window):
            last_sell_rsi_bar = None
            logger.info("Sell RSI signal expired (outside lookback window)")
        
        # Check for MACD crossovers - Using exact Pine Script logic
        macd_crossover = (df['macd'].iloc[-2] <= df['macd_signal'].iloc[-2]) and (df['macd'].iloc[-1] > df['macd_signal'].iloc[-1])
        macd_crossunder = (df['macd'].iloc[-2] >= df['macd_signal'].iloc[-2]) and (df['macd'].iloc[-1] < df['macd_signal'].iloc[-1])
        
        # Generate composite signals - Exactly matching Pine Script
        composite_buy = macd_crossover and (last_buy_rsi_bar is not None)
        composite_sell = macd_crossunder and (last_sell_rsi_bar is not None)
        
        # Reset RSI signals after composite signals are generated
        if composite_buy:
            last_buy_rsi_bar = None
            logger.info("RSI buy signal used in composite signal and reset")
            
        if composite_sell:
            last_sell_rsi_bar = None
            logger.info("RSI sell signal used in composite signal and reset")
        
        # Determine entry conditions with trend filtering - Matching Pine Script
        enter_long = composite_buy and (trend_state == 1 or trend_state == 0) and current_position <= 0
        enter_short = composite_sell and (trend_state == -1 or trend_state == 0) and current_position >= 0
        
        # Calculate position size
        position_size = determine_position_size(latest_close)
        
        # Calculate profit targets and stop losses
        if enter_long:
            # Close any existing short position
            if current_position < 0:
                logger.info(f"Closing short position: {current_position} shares")
                api.submit_order(
                    symbol=config.SYMBOL,
                    qty=abs(current_position),
                    side='buy',
                    type='market',
                    time_in_force='gtc'
                )
            
            # Enter long position
            logger.info(f"LONG signal triggered at {latest_close:.2f}")
            
            # Calculate targets exactly as in Pine Script
            limit_price = round(latest_close * (1 + config.PROFIT_TARGET), 2)
            stop_price = round(latest_close * (1 - config.STOP_LOSS), 2)
            
            logger.info(f"Entering LONG position: {position_size} shares at {latest_close:.2f}")
            logger.info(f"Target: {limit_price:.2f}, Stop: {stop_price:.2f}")
            
            # Account for real market conditions - add small buffer to prevent immediate stops
            stop_limit_price = stop_price - config.SLIPPAGE_BUFFER
            
            try:
                # Submit entry order with bracket (take profit and stop loss)
                api.submit_order(
                    symbol=config.SYMBOL,
                    qty=position_size,
                    side='buy',
                    type='market',
                    time_in_force='gtc',
                    order_class='bracket',
                    take_profit={
                        'limit_price': limit_price
                    },
                    stop_loss={
                        'stop_price': stop_price,
                        'limit_price': stop_limit_price
                    }
                )
                logger.info("Long order submitted successfully")
            except Exception as e:
                logger.error(f"Error submitting long order: {str(e)}")
            
        elif enter_short:
            # Close any existing long position
            if current_position > 0:
                logger.info(f"Closing long position: {current_position} shares")
                api.submit_order(
                    symbol=config.SYMBOL,
                    qty=current_position,
                    side='sell',
                    type='market',
                    time_in_force='gtc'
                )
            
            # Enter short position
            logger.info(f"SHORT signal triggered at {latest_close:.2f}")
            
            # Calculate targets exactly as in Pine Script
            limit_price = round(latest_close * (1 - config.PROFIT_TARGET), 2)
            stop_price = round(latest_close * (1 + config.STOP_LOSS), 2)
            
            logger.info(f"Entering SHORT position: {position_size} shares at {latest_close:.2f}")
            logger.info(f"Target: {limit_price:.2f}, Stop: {stop_price:.2f}")
            
            # Account for real market conditions - add small buffer to prevent immediate stops
            stop_limit_price = stop_price + config.SLIPPAGE_BUFFER
            
            try:
                # Submit entry order with bracket (take profit and stop loss)
                api.submit_order(
                    symbol=config.SYMBOL,
                    qty=position_size,
                    side='sell',
                    type='market',
                    time_in_force='gtc',
                    order_class='bracket',
                    take_profit={
                        'limit_price': limit_price
                    },
                    stop_loss={
                        'stop_price': stop_price,
                        'limit_price': stop_limit_price
                    }
                )
                logger.info("Short order submitted successfully")
            except Exception as e:
                logger.error(f"Error submitting short order: {str(e)}")
        
        else:
            logger.info("No trading signals detected")
        
        # Check for completed trades and update statistics
        try:
            # Get recently filled orders
            yesterday = datetime.now() - timedelta(days=1)
            orders = api.list_orders(
                status='closed',
                limit=100,
                after=yesterday.isoformat()
            )
            
            # Process filled orders to update statistics
            for order in orders:
                if order.symbol != config.SYMBOL:
                    continue
                
                # Check if this is a main order (not a take-profit or stop-loss)
                if not hasattr(order, 'legs') or not order.legs:
                    continue
                
                # If we've made it here, this is a bracket order that was completed
                if order.status == 'filled':
                    # Find out if it was profitable (either take profit hit or stop loss hit)
                    for child_order in api.list_orders(
                        parent_id=order.id,
                        status='filled',
                        nested=True
                    ):
                        if child_order.type == 'limit':  # Take profit was hit
                            update_trade_stats(True)
                            break
                        elif child_order.type == 'stop':  # Stop loss was hit
                            update_trade_stats(False)
                            break
        
        except Exception as e:
            logger.error(f"Error checking completed trades: {str(e)}")
        
        # Additional real-market check: check if we have any open orders that are stale
        open_orders = api.list_orders(status='open', symbols=[config.SYMBOL])
        now = datetime.now()
        
        for order in open_orders:
            # Check if order is older than configured minutes and is not a bracket child
            order_time = pd.to_datetime(order.submitted_at).replace(tzinfo=None)
            if (now - order_time).total_seconds() > (config.STALE_ORDER_MINUTES * 60) and order.type != 'limit' and order.type != 'stop':
                logger.info(f"Canceling stale order: {order.id}")
                try:
                    api.cancel_order(order.id)
                except Exception as e:
                    logger.error(f"Error canceling order: {str(e)}")
        
    except Exception as e:
        logger.error(f"Error running strategy: {str(e)}")

# Apply rate limit handling if configured
if config.API_RATE_LIMIT_HANDLER:
    run_strategy = handle_api_rate_limits(run_strategy)

def main():
    """Main function to schedule and run the strategy"""
    logger.info("Starting Simplified Scalping Strategy")
    logger.info(f"Trading {config.SYMBOL} with base quantity {config.QUANTITY}")
    
    if API_KEY is None or API_SECRET is None:
        logger.error("API key or secret not found. Please check your .env file.")
        return
    
    # Run the strategy once on startup
    run_strategy()
    
    # Schedule the strategy to run every minute during market hours
    schedule.every(1).minutes.do(run_strategy)
    
    # Sleep interval (seconds)
    sleep_interval = 1
    
    # Main loop with enhanced error handling for real market conditions
    while True:
        try:
            schedule.run_pending()
            time.sleep(sleep_interval)
        except Exception as e:
            logger.error(f"Error in main loop: {str(e)}")
            logger.info("Waiting 60 seconds before retrying...")
            time.sleep(60)  # Wait longer on error to prevent API rate limits

if __name__ == "__main__":
    main() 