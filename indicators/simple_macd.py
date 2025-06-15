#!/usr/bin/env python3
"""
Simple MACD Calculator for SPY Data
===================================

This script calculates MACD using pandas and plots it with matplotlib.
Based on the tutorial requirements for Moving Average Convergence Divergence.

Key Features:
- Calculates 12-period and 26-period EMAs
- Computes MACD line (12EMA - 26EMA)
- Computes Signal line (9-period EMA of MACD)
- Detects crossovers in last two rows
- Plots results using matplotlib
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.patches import Rectangle
import numpy as np
from datetime import datetime
import os

def load_spy_data(csv_path):
    """Load SPY data from CSV file"""
    print(f"Loading SPY data from: {csv_path}")
    
    # Load CSV
    data = pd.read_csv(csv_path)
    
    # Check what columns we actually have
    print(f"Available columns: {list(data.columns)}")
    
    # Convert time to datetime for better plotting
    # The CSV already has datetime strings, not Unix timestamps
    data['datetime'] = pd.to_datetime(data['time'])
    
    # Filter out weekends (Saturday=5, Sunday=6)
    data = data[data['datetime'].dt.dayofweek < 5].copy()
    
    # Filter to market hours only (9:30 AM to 4:00 PM ET)
    data = data[
        (data['datetime'].dt.time >= pd.Timestamp('09:30:00').time()) &
        (data['datetime'].dt.time <= pd.Timestamp('16:00:00').time())
    ].copy()
    
    # Rename columns to match tutorial format
    data = data.rename(columns={
        'close': 'Close',
        'open': 'Open', 
        'high': 'High',
        'low': 'Low',
        'volume': 'Volume'
    })
    
    print(f"Loaded {len(data)} data points (weekdays, market hours only)")
    print(f"Date range: {data['datetime'].iloc[0]} to {data['datetime'].iloc[-1]}")
    
    return data

def calculate_macd(data):
    """
    Calculate MACD following the tutorial methodology
    
    Args:
        data: DataFrame with Close prices
        
    Returns:
        DataFrame with MACD components added
    """
    print("Calculating MACD components...")
    
    # Calculate the 12-period EMA (Fast EMA)
    data['EMA12'] = data['Close'].ewm(span=12, adjust=False).mean()
    
    # Calculate the 26-period EMA (Slow EMA)
    data['EMA26'] = data['Close'].ewm(span=26, adjust=False).mean()
    
    # Calculate MACD (the difference between 12-period EMA and 26-period EMA)
    data['MACD'] = data['EMA12'] - data['EMA26']
    
    # Calculate the 9-period EMA of MACD (Signal Line)
    data['Signal_Line'] = data['MACD'].ewm(span=9, adjust=False).mean()
    
    # Calculate MACD Histogram (MACD - Signal Line)
    data['MACD_Histogram'] = data['MACD'] - data['Signal_Line']
    
    print("MACD calculation completed!")
    return data

def detect_crossovers(data):
    """
    Detect MACD crossovers in the last two rows
    Following the tutorial logic exactly
    """
    print("Checking for crossovers in last two rows...")
    
    # Get last two rows
    last_row = data.iloc[-1]
    second_last_row = data.iloc[-2]
    
    # Check for crossovers
    if second_last_row['MACD'] > second_last_row['Signal_Line'] and last_row['MACD'] < last_row['Signal_Line']:
        result = 'Cross Below Signal Line'
        signal_type = 'BEARISH'
    elif second_last_row['MACD'] < second_last_row['Signal_Line'] and last_row['MACD'] > last_row['Signal_Line']:
        result = 'Cross Above Signal Line'
        signal_type = 'BULLISH'
    else:
        result = 'No Crossover'
        signal_type = 'NEUTRAL'
    
    print(f"Crossover Analysis: {result}")
    
    # Print detailed information
    print(f"\nDetailed Analysis:")
    print(f"Second Last Row ({second_last_row['datetime']}):")
    print(f"  MACD: {second_last_row['MACD']:.6f}")
    print(f"  Signal: {second_last_row['Signal_Line']:.6f}")
    print(f"  Price: ${second_last_row['Close']:.2f}")
    
    print(f"\nLast Row ({last_row['datetime']}):")
    print(f"  MACD: {last_row['MACD']:.6f}")
    print(f"  Signal: {last_row['Signal_Line']:.6f}")
    print(f"  Price: ${last_row['Close']:.2f}")
    print(f"  Signal Type: {signal_type}")
    return result, signal_type

def plot_candlesticks(ax, data):
    """
    Plot candlesticks manually using matplotlib
    
    Args:
        ax: matplotlib axis
        data: DataFrame with OHLC data
    """
    # Calculate candle width (80% of time interval)
    time_diff = data['datetime'].iloc[1] - data['datetime'].iloc[0]
    candle_width = time_diff * 0.8
    
    for idx, row in data.iterrows():
        date = mdates.date2num(row['datetime'])
        open_price = row['Open']
        high_price = row['High']
        low_price = row['Low']
        close_price = row['Close']
        
        # Determine candle color
        color = '#00C851' if close_price >= open_price else '#FF4444'  # Green for up, Red for down
        
        # Draw the wick (high-low line)
        ax.plot([date, date], [low_price, high_price], color='black', linewidth=1, alpha=0.8)
        
        # Draw the body (open-close rectangle)
        body_height = abs(close_price - open_price)
        body_bottom = min(open_price, close_price)
        
        # Create rectangle for candle body
        rect = Rectangle((date - candle_width.total_seconds()/(2*86400), body_bottom), 
                        candle_width.total_seconds()/86400, body_height,
                        facecolor=color, edgecolor='black', alpha=0.8, linewidth=0.5)
        ax.add_patch(rect)

def plot_macd_analysis(data, save_plot=True):
    """
    Plot MACD analysis for July 5th trading day
    
    Args:
        data: DataFrame with MACD data
        save_plot: Whether to save the plot
    """
    print("Creating MACD plot for July 5th...")
    
    # Filter for July 5th specifically
    target_date = pd.Timestamp('2025-06-05').date()
    single_day_data = data[data['datetime'].dt.date == target_date].copy()
    
    if len(single_day_data) == 0:
        print(f"No data found for June 5th, 2025. Available dates:")
        available_dates = data['datetime'].dt.date.unique()
        print(f"First few dates: {sorted(available_dates)[:10]}")
        print(f"Last few dates: {sorted(available_dates)[-10:]}")
        return
    
    print(f"Plotting data for: June 5th, 2025")
    print(f"Number of 5-minute candles: {len(single_day_data)}")
      # Create figure with subplots
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(16, 12), sharex=True)
      # Plot 1: Candlestick Chart
    plot_candlesticks(ax1, single_day_data)
    
    ax1.set_title(f'SPY Candlesticks - June 5th, 2025', fontsize=16, fontweight='bold')
    ax1.set_ylabel('Price ($)', fontsize=12)
    ax1.legend(loc='upper left')
    ax1.grid(True, alpha=0.3)
    
    # Format price axis
    ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x:.2f}'))
    
    # Plot 2: MACD Indicator
    ax2.plot(single_day_data['datetime'], single_day_data['MACD'], 
             label='MACD Line', color='blue', linewidth=2.5)
    ax2.plot(single_day_data['datetime'], single_day_data['Signal_Line'], 
             label='Signal Line', color='red', linewidth=2.5)
    
    # MACD Histogram with better colors
    colors = ['#00C851' if x >= 0 else '#FF4444' for x in single_day_data['MACD_Histogram']]
    ax2.bar(single_day_data['datetime'], single_day_data['MACD_Histogram'], 
            label='MACD Histogram', color=colors, alpha=0.7, width=pd.Timedelta(minutes=3))
    
    # Zero line
    ax2.axhline(y=0, color='black', linestyle='-', alpha=0.8, linewidth=1)
    
    # Highlight crossovers
    if len(single_day_data) >= 2:
        for i in range(1, len(single_day_data)):
            prev_macd = single_day_data.iloc[i-1]['MACD']
            prev_signal = single_day_data.iloc[i-1]['Signal_Line']
            curr_macd = single_day_data.iloc[i]['MACD']
            curr_signal = single_day_data.iloc[i]['Signal_Line']
            
            # Check for bullish crossover (MACD crosses above Signal)
            if prev_macd <= prev_signal and curr_macd > curr_signal:
                ax2.scatter(single_day_data.iloc[i]['datetime'], curr_macd, 
                           color='green', s=100, marker='^', zorder=5, label='Bullish Cross')
            
            # Check for bearish crossover (MACD crosses below Signal)
            elif prev_macd >= prev_signal and curr_macd < curr_signal:
                ax2.scatter(single_day_data.iloc[i]['datetime'], curr_macd, 
                           color='red', s=100, marker='v', zorder=5, label='Bearish Cross')
    
    ax2.set_title(f'MACD Indicator (12, 26, 9) - 5-Minute Intervals', fontsize=16, fontweight='bold')
    ax2.set_ylabel('MACD Value', fontsize=12)
    ax2.set_xlabel('Time', fontsize=12)
    ax2.legend(loc='upper left')
    ax2.grid(True, alpha=0.3)
      # Format time axis to show hours and minutes
    ax2.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
    ax2.xaxis.set_major_locator(mdates.HourLocator(interval=1))
    ax2.xaxis.set_minor_locator(mdates.MinuteLocator(interval=30))
    
    # Also format the candlestick chart time axis
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
    ax1.xaxis.set_major_locator(mdates.HourLocator(interval=1))
    
    # Rotate time labels
    plt.xticks(rotation=45)
    plt.tight_layout()
      # Save plot
    if save_plot:
        filename = f'spy_macd_july5th_{datetime.now().strftime("%Y%m%d_%H%M%S")}.png'
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        print(f"Plot saved as: {filename}")
    
    plt.show()

def print_macd_summary(data):
    """Print a comprehensive MACD summary"""
    latest = data.iloc[-1]
    
    print("\n" + "="*60)
    print("MACD ANALYSIS SUMMARY - SPY")
    print("="*60)
    print(f"Analysis Date: {latest['datetime']}")
    print(f"Current Price: ${latest['Close']:.2f}")
    print(f"")
    print(f"MACD Components:")
    print(f"├─ 12-Period EMA: ${latest['EMA12']:.4f}")
    print(f"├─ 26-Period EMA: ${latest['EMA26']:.4f}")
    print(f"├─ MACD Line: {latest['MACD']:.6f}")
    print(f"├─ Signal Line: {latest['Signal_Line']:.6f}")
    print(f"└─ Histogram: {latest['MACD_Histogram']:.6f}")
    print(f"")
    
    # Trend analysis
    macd_trend = "BULLISH" if latest['MACD'] > latest['Signal_Line'] else "BEARISH"
    momentum = "POSITIVE" if latest['MACD'] > 0 else "NEGATIVE"
    
    print(f"Technical Analysis:")
    print(f"├─ MACD vs Signal: {macd_trend}")
    print(f"├─ MACD vs Zero: {momentum}")
    print(f"└─ Histogram Trend: {'EXPANDING' if latest['MACD_Histogram'] > 0 else 'CONTRACTING'}")
    print("="*60)

def main():
    """Main execution function"""
    print("SPY MACD Indicator Analysis")
    print("="*40)
    
    # Path to CSV data
    csv_path = './historical_data/spy_5min_merged_complete_20250611.csv'
    
    try:
        # Step 1: Load SPY data
        data = load_spy_data(csv_path)
        
        # Step 2: Calculate MACD components
        data = calculate_macd(data)
        
        # Step 3: Detect crossovers (following tutorial)
        crossover_result, signal_type = detect_crossovers(data)
        
        # Step 4: Print summary
        print_macd_summary(data)
          # Step 5: Create plots (single trading day)
        plot_macd_analysis(data, save_plot=True)
        
        print(f"\nFinal Result: {crossover_result}")
        print(f"Signal Type: {signal_type}")
        
    except FileNotFoundError:
        print(f"Error: Could not find CSV file at {csv_path}")
        print("Please check the file path and try again.")
    except Exception as e:
        print(f"Error occurred: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
