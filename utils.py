"""
Utility functions for the trading strategy
"""
import pandas as pd
import numpy as np
from ta.trend import SMAIndicator, MACD
from ta.momentum import RSIIndicator
import datetime
import time

def get_hourly_data(api, symbol, lookback=100):
    """
    Get hourly historical data for a symbol
    """
    end = datetime.datetime.now()
    start = end - datetime.timedelta(days=lookback)
    
    barset = api.get_bars(
        symbol,
        "1Hour",
        start=start.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
        end=end.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
        limit=10000
    ).df
    
    return barset

def get_minute_data(api, symbol, lookback=300):
    """
    Get minute historical data for a symbol
    """
    end = datetime.datetime.now()
    start = end - datetime.timedelta(days=lookback)
    
    barset = api.get_bars(
        symbol,
        "1Min",
        start=start.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
        end=end.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
        limit=10000
    ).df
    
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