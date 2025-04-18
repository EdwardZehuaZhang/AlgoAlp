"""
Utility functions for the trading strategy
"""
import pandas as pd
import numpy as np
from ta.trend import SMAIndicator, MACD
from ta.momentum import RSIIndicator
import datetime

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
    
    # Calculate MACD
    macd = MACD(
        close=df['close'], 
        window_slow=macd_slow, 
        window_fast=macd_fast, 
        window_sign=macd_signal
    )
    df['macd'] = macd.macd()
    df['macd_signal'] = macd.macd_signal()
    
    # Calculate candle colors based on conditions
    df['close_above'] = (df['close'] > df['fast_sma']) & (df['close'] > df['slow_sma'])
    df['close_below'] = (df['close'] < df['fast_sma']) & (df['close'] < df['slow_sma'])
    
    return df 