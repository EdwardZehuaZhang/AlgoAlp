"""
Utility functions for AlgoAlp trading application
"""

import pandas as pd
import numpy as np
import requests
import logging
from datetime import datetime, timedelta
import os
import json
from dotenv import load_dotenv
import alpaca_trade_api as tradeapi
from ta.trend import SMAIndicator, MACD
from ta.momentum import RSIIndicator
import time

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

def get_alpaca_api():
    """Create and return an Alpaca API client"""
    api = tradeapi.REST(
        os.getenv('ALPACA_API_KEY'),
        os.getenv('ALPACA_API_SECRET'),
        os.getenv('ALPACA_BASE_URL', 'https://paper-api.alpaca.markets')
    )
    return api

def get_market_hours():
    """Check if the market is currently open"""
    api = get_alpaca_api()
    clock = api.get_clock()
    
    is_open = clock.is_open
    next_open = clock.next_open.strftime('%Y-%m-%d %H:%M:%S')
    next_close = clock.next_close.strftime('%Y-%m-%d %H:%M:%S')
    
    return {
        "is_open": is_open,
        "next_open": next_open,
        "next_close": next_close
    }

def format_trade_data(price, quantity, side, symbol):
    """Format trade data for logging and notifications"""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    return {
        "timestamp": timestamp,
        "symbol": symbol,
        "side": side,
        "quantity": quantity,
        "price": price,
        "total_value": round(price * quantity, 2)
    }

def calculate_position_size(account, symbol, risk_percent=1.0):
    """Calculate position size based on account equity and risk percentage"""
    try:
        api = get_alpaca_api()
        
        # Get account equity
        account = api.get_account()
        equity = float(account.equity)
        
        # Get current price
        latest_trade = api.get_latest_trade(symbol)
        price = latest_trade.price
        
        # Calculate risk amount
        risk_amount = equity * (risk_percent / 100)
        
        # Calculate position size
        position_size = int(risk_amount / price)
        
        return max(1, position_size)  # Minimum 1 share
        
    except Exception as e:
        logger.error(f"Error calculating position size: {str(e)}")
        return 1  # Default to 1 share on error

def send_notification(message, webhook_url=None):
    """Send a notification to Discord or other webhook service"""
    if not webhook_url:
        webhook_url = os.getenv('DISCORD_WEBHOOK_URL')
        
    if not webhook_url:
        logger.warning("No webhook URL provided for notification")
        return False
        
    try:
        payload = {
            "username": "AlgoAlp Trader",
            "avatar_url": "https://cdn-icons-png.flaticon.com/512/2431/2431438.png",
            "content": message
        }
        
        response = requests.post(webhook_url, json=payload)
        
        if response.status_code == 204:
            logger.info("Notification sent successfully")
            return True
        else:
            logger.warning(f"Failed to send notification: {response.status_code}")
            return False
            
    except Exception as e:
        logger.error(f"Error sending notification: {str(e)}")
        return False

def log_trade(trade_data, log_file="trade_history.json"):
    """Log trade to a JSON file"""
    try:
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(log_file) if os.path.dirname(log_file) else '.', exist_ok=True)
        
        # Load existing trades
        trades = []
        if os.path.exists(log_file):
            with open(log_file, 'r') as f:
                trades = json.load(f)
                
        # Add new trade
        trades.append(trade_data)
        
        # Save updated trades
        with open(log_file, 'w') as f:
            json.dump(trades, f, indent=2)
            
        logger.info(f"Trade logged successfully to {log_file}")
        return True
        
    except Exception as e:
        logger.error(f"Error logging trade: {str(e)}")
        return False

def get_hourly_data(api, symbol, lookback=100):
    """
    Get hourly historical data for a symbol using IEX feed
    """
    end = datetime.now()
    start = end - timedelta(days=lookback)
    
    # Format dates without microseconds for Alpaca API
    start_str = start.strftime("%Y-%m-%d")
    end_str = end.strftime("%Y-%m-%d")
    
    try:
        barset = api.get_bars(
            symbol,
            "1Hour",
            start=start_str,
            end=end_str,
            limit=10000,
            feed='iex'  # Explicitly request IEX data
        ).df
        
        if len(barset) == 0:
            print(f"Warning: No hourly data returned for {symbol}. Trying without feed parameter...")
            # Try again without specifying feed as a fallback
            barset = api.get_bars(
                symbol,
                "1Hour",
                start=start_str,
                end=end_str,
                limit=10000
            ).df
    except Exception as e:
        print(f"Error getting hourly data: {e}")
        # Try again without specifying feed as a fallback
        try:
            barset = api.get_bars(
                symbol,
                "1Hour",
                start=start_str,
                end=end_str,
                limit=10000
            ).df
        except Exception as fallback_e:
            print(f"Fallback also failed: {fallback_e}")
            barset = pd.DataFrame()  # Return empty DataFrame if all attempts fail
    
    return barset

def get_minute_data(api, symbol, lookback=300):
    """
    Get minute historical data for a symbol using IEX feed
    """
    end = datetime.now()
    start = end - timedelta(days=lookback)
    
    # Format dates without microseconds for Alpaca API
    start_str = start.strftime("%Y-%m-%d")
    end_str = end.strftime("%Y-%m-%d")
    
    try:
        barset = api.get_bars(
            symbol,
            "1Min",
            start=start_str,
            end=end_str,
            limit=10000,
            feed='iex'  # Explicitly request IEX data
        ).df
        
        if len(barset) == 0:
            print(f"Warning: No minute data returned for {symbol}. Trying without feed parameter...")
            # Try again without specifying feed as a fallback
            barset = api.get_bars(
                symbol,
                "1Min",
                start=start_str,
                end=end_str,
                limit=10000
            ).df
    except Exception as e:
        print(f"Error getting minute data: {e}")
        # Try again without specifying feed as a fallback
        try:
            barset = api.get_bars(
                symbol,
                "1Min",
                start=start_str,
                end=end_str,
                limit=10000
            ).df
        except Exception as fallback_e:
            print(f"Fallback also failed: {fallback_e}")
            barset = pd.DataFrame()  # Return empty DataFrame if all attempts fail
    
    return barset

def calculate_hour_trend(df, fast_period, slow_period):
    """
    Calculate the 1-hour trend state based on moving averages
    Returns: 1 (bullish), -1 (bearish), or 0 (neutral)
    """
    # Calculate fast and slow SMAs
    df['fast_sma'] = SMAIndicator(close=df['close'], window=fast_period).sma_indicator()
    df['slow_sma'] = SMAIndicator(close=df['close'], window=slow_period).sma_indicator()
    
    # Determine crosses
    df['golden_cross'] = (df['fast_sma'] > df['slow_sma']) & (df['fast_sma'].shift(1) <= df['slow_sma'].shift(1))
    df['death_cross'] = (df['fast_sma'] < df['slow_sma']) & (df['fast_sma'].shift(1) >= df['slow_sma'].shift(1))
    
    # Initialize bullish state column
    if 'is_bullish' not in df.columns:
        df['is_bullish'] = False
    
    # Update bullish state based on crosses
    for i in range(1, len(df)):
        if df['golden_cross'].iloc[i]:
            df.loc[df.index[i], 'is_bullish'] = True
        elif df['death_cross'].iloc[i]:
            df.loc[df.index[i], 'is_bullish'] = False
        else:
            df.loc[df.index[i], 'is_bullish'] = df['is_bullish'].iloc[i-1]
    
    # Determine close above/below conditions
    df['close_above'] = (df['close'] > df['fast_sma']) & (df['close'] > df['slow_sma'])
    df['close_below'] = (df['close'] < df['fast_sma']) & (df['close'] < df['slow_sma'])
    
    # Determine trend state
    df['trend_state'] = 0  # neutral by default
    df.loc[(df['is_bullish'] == True) & (df['close_above'] == True), 'trend_state'] = 1  # bullish
    df.loc[(df['is_bullish'] == False) & (df['close_below'] == True), 'trend_state'] = -1  # bearish
    
    return df['trend_state'].iloc[-1]

def calculate_indicators(df, ultrafast_period, fast_period, slow_period, rsi_period, 
                        macd_fast, macd_slow, macd_signal):
    """
    Calculate all required technical indicators for the strategy
    """
    # Calculate SMAs
    df['ultrafast_sma'] = SMAIndicator(close=df['close'], window=ultrafast_period).sma_indicator()
    df['fast_sma'] = SMAIndicator(close=df['close'], window=fast_period).sma_indicator()
    df['slow_sma'] = SMAIndicator(close=df['close'], window=slow_period).sma_indicator()
    
    # Calculate golden and death crosses
    df['golden_cross'] = (df['fast_sma'] > df['slow_sma']) & (df['fast_sma'].shift(1) <= df['slow_sma'].shift(1))
    df['death_cross'] = (df['fast_sma'] < df['slow_sma']) & (df['fast_sma'].shift(1) >= df['slow_sma'].shift(1))
    
    # Initialize bullish state
    if 'is_bullish' not in df.columns:
        df['is_bullish'] = False
    
    # Update bullish state based on crosses
    for i in range(1, len(df)):
        if df['golden_cross'].iloc[i]:
            df.loc[df.index[i], 'is_bullish'] = True
        elif df['death_cross'].iloc[i]:
            df.loc[df.index[i], 'is_bullish'] = False
        else:
            df.loc[df.index[i], 'is_bullish'] = df['is_bullish'].iloc[i-1]
    
    # Calculate RSI
    df['rsi'] = RSIIndicator(close=df['close'], window=rsi_period).rsi()
    
    # Calculate MACD using EMA like in Pine Script
    # In Pine Script: macdLine = ta.ema(close, macdFastLength) - ta.ema(close, macdSlowLength)
    df['ema_fast'] = df['close'].ewm(span=macd_fast, adjust=False).mean()
    df['ema_slow'] = df['close'].ewm(span=macd_slow, adjust=False).mean()
    df['macd'] = df['ema_fast'] - df['ema_slow']
    df['macd_signal'] = df['macd'].ewm(span=macd_signal, adjust=False).mean()
    
    # Calculate candle colors based on conditions
    df['close_above'] = (df['close'] > df['fast_sma']) & (df['close'] > df['slow_sma'])
    df['close_below'] = (df['close'] < df['fast_sma']) & (df['close'] < df['slow_sma'])
    
    return df

def handle_api_rate_limits(func):
    """
    Decorator to handle Alpaca API rate limits
    """
    def wrapper(*args, **kwargs):
        max_retries = 3
        retry_delay = 2  # seconds
        
        for attempt in range(max_retries):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                if "rate limit" in str(e).lower() and attempt < max_retries - 1:
                    print(f"Rate limit hit, retrying in {retry_delay} seconds...")
                    time.sleep(retry_delay)
                    retry_delay *= 2  # Exponential backoff
                else:
                    raise
    
    return wrapper

def calculate_max_shares(api, symbol, risk_percent=1.0):
    """
    Calculate maximum shares to trade based on account equity and risk
    """
    try:
        account = api.get_account()
        equity = float(account.equity)
        
        # Get current price
        latest_trade = api.get_latest_trade(symbol)
        price = float(latest_trade.price)
        
        # Calculate position size based on risk
        max_position_value = equity * (risk_percent / 100)
        max_shares = int(max_position_value / price)
        
        return max_shares
    except Exception as e:
        print(f"Error calculating max shares: {str(e)}")
        return 1  # Default to 1 share on error