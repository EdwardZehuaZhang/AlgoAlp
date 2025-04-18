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
from utils import get_hourly_data, get_minute_data, calculate_hour_trend, calculate_indicators

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
    
    return True

def get_current_position():
    """Get current position for the symbol"""
    try:
        position = api.get_position(config.SYMBOL)
        return int(float(position.qty))
    except Exception:
        return 0

def run_strategy():
    """Main strategy execution function"""
    global last_buy_rsi_bar, last_sell_rsi_bar
    
    if not check_trading_condition():
        return
    
    try:
        logger.info(f"Running strategy for {config.SYMBOL}")
        
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
        
        # Get the latest bar data
        latest_bar = df.iloc[-1]
        latest_close = latest_bar['close']
        current_bar_index = len(df) - 1
        
        # Update RSI signals
        if latest_bar['rsi'] < config.RSI_OVERSOLD:
            last_buy_rsi_bar = current_bar_index
            logger.info(f"RSI oversold condition detected. RSI: {latest_bar['rsi']:.2f}")
        
        if latest_bar['rsi'] > config.RSI_OVERBOUGHT:
            last_sell_rsi_bar = current_bar_index
            logger.info(f"RSI overbought condition detected. RSI: {latest_bar['rsi']:.2f}")
        
        # Check if RSI signals are still valid (within lookback window)
        if last_buy_rsi_bar is not None and (current_bar_index - last_buy_rsi_bar > lookback_window):
            last_buy_rsi_bar = None
            logger.info("Buy RSI signal expired (outside lookback window)")
        
        if last_sell_rsi_bar is not None and (current_bar_index - last_sell_rsi_bar > lookback_window):
            last_sell_rsi_bar = None
            logger.info("Sell RSI signal expired (outside lookback window)")
        
        # Check for MACD crossovers
        macd_crossover = (df['macd'].iloc[-2] <= df['macd_signal'].iloc[-2]) and (df['macd'].iloc[-1] > df['macd_signal'].iloc[-1])
        macd_crossunder = (df['macd'].iloc[-2] >= df['macd_signal'].iloc[-2]) and (df['macd'].iloc[-1] < df['macd_signal'].iloc[-1])
        
        # Generate composite signals
        composite_buy = macd_crossover and (last_buy_rsi_bar is not None)
        composite_sell = macd_crossunder and (last_sell_rsi_bar is not None)
        
        # Determine entry conditions with trend filtering
        enter_long = composite_buy and (trend_state == 1 or trend_state == 0) and current_position <= 0
        enter_short = composite_sell and (trend_state == -1 or trend_state == 0) and current_position >= 0
        
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
            
            # Submit order
            limit_price = round(latest_close * (1 + config.PROFIT_TARGET), 2)
            stop_price = round(latest_close * (1 - config.STOP_LOSS), 2)
            
            logger.info(f"Entering LONG position: {config.QUANTITY} shares at {latest_close:.2f}")
            logger.info(f"Target: {limit_price:.2f}, Stop: {stop_price:.2f}")
            
            # Submit entry order
            api.submit_order(
                symbol=config.SYMBOL,
                qty=config.QUANTITY,
                side='buy',
                type='market',
                time_in_force='gtc',
                order_class='bracket',
                take_profit={
                    'limit_price': limit_price
                },
                stop_loss={
                    'stop_price': stop_price,
                    'limit_price': stop_price - 0.01  # Use stop limit to prevent slippage
                }
            )
            
            # Reset RSI buy signal
            last_buy_rsi_bar = None
            
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
            
            # Submit order
            limit_price = round(latest_close * (1 - config.PROFIT_TARGET), 2)
            stop_price = round(latest_close * (1 + config.STOP_LOSS), 2)
            
            logger.info(f"Entering SHORT position: {config.QUANTITY} shares at {latest_close:.2f}")
            logger.info(f"Target: {limit_price:.2f}, Stop: {stop_price:.2f}")
            
            # Submit entry order
            api.submit_order(
                symbol=config.SYMBOL,
                qty=config.QUANTITY,
                side='sell',
                type='market',
                time_in_force='gtc',
                order_class='bracket',
                take_profit={
                    'limit_price': limit_price
                },
                stop_loss={
                    'stop_price': stop_price,
                    'limit_price': stop_price + 0.01  # Use stop limit to prevent slippage
                }
            )
            
            # Reset RSI sell signal
            last_sell_rsi_bar = None
        
        else:
            logger.info("No trading signals detected")
        
    except Exception as e:
        logger.error(f"Error running strategy: {str(e)}")

def main():
    """Main function to schedule and run the strategy"""
    logger.info("Starting Simplified Scalping Strategy")
    logger.info(f"Trading {config.SYMBOL} with quantity {config.QUANTITY}")
    
    if API_KEY is None or API_SECRET is None:
        logger.error("API key or secret not found. Please check your .env file.")
        return
    
    # Run the strategy once on startup
    run_strategy()
    
    # Schedule the strategy to run every minute during market hours
    schedule.every(1).minutes.do(run_strategy)
    
    # Main loop
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main() 