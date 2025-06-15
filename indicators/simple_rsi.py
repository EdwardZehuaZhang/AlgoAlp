#!/usr/bin/env python3
"""
RSI and Candlestick Plotter for SPY Data
=======================================

This script calculates RSI and plots it alongside candlesticks for June 5th, 2025.

Features:
- Loads data from the complete SPY dataset
- Calculates 14-period RSI using Wilder's method
- Plots candlestick chart with volume bars
- Adds RSI indicator chart below
- Highlights overbought and oversold conditions
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.patches import Rectangle
from datetime import datetime
import os
import sys

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def load_data(csv_path, target_date=None, include_previous=False):
    """
    Load and prepare data from CSV file
    
    Args:
        csv_path (str): Path to CSV file
        target_date (str): Optional specific date to filter for (YYYY-MM-DD)
        include_previous (bool): Whether to include previous day's data for RSI calculation
        
    Returns:
        pd.DataFrame, pd.DataFrame: Complete DataFrame for calculations, Filtered DataFrame for display
    """
    print(f"Loading data from: {csv_path}")
    
    # Load CSV
    data = pd.read_csv(csv_path)
    print(f"Available columns: {list(data.columns)}")
      
    # Convert time to datetime
    data['datetime'] = pd.to_datetime(data['time'])
    
    # Save complete data for RSI calculation first
    calc_data = data.copy()
    
    # Filter for target date for display purposes
    display_data = None
    if target_date:
        target = pd.to_datetime(target_date).date()
        display_data = data[data['datetime'].dt.date == target].copy()
        
        # If we need previous day's data for calculations
        if include_previous:
            # Find previous trading day
            prev_day = data[data['datetime'].dt.date < target].copy()
            if not prev_day.empty:
                # Get the most recent previous day
                max_prev_date = prev_day['datetime'].dt.date.max()
                # Take only the previous day's data + target day for RSI calculations
                calc_data = data[(data['datetime'].dt.date == max_prev_date) | 
                                (data['datetime'].dt.date == target)].copy()
                print(f"Including data from previous day {max_prev_date} for RSI calculation")
                
    # If no target date specified, display data is the same as calc data
    if display_data is None:
        display_data = data.copy()
        print(f"Filtered to {len(data)} rows for {target_date}")
      # Then filter to market hours only (9:30 AM to 4:00 PM ET)
    calc_data = calc_data[
        (calc_data['datetime'].dt.time >= pd.Timestamp('09:30:00').time()) &
        (calc_data['datetime'].dt.time <= pd.Timestamp('16:00:00').time())
    ].copy()
    
    display_data = display_data[
        (display_data['datetime'].dt.time >= pd.Timestamp('09:30:00').time()) &
        (display_data['datetime'].dt.time <= pd.Timestamp('16:00:00').time())
    ].copy()
    
    # Check if we have data for the entire trading day
    if target_date and len(display_data) > 0:
        market_open = pd.Timestamp(f"{target_date} 09:30:00")
        first_data_point = display_data['datetime'].min()
        if first_data_point > market_open:
            print(f"WARNING: First data point is at {first_data_point.time()}, market opens at 09:30:00")
            print(f"Missing {(first_data_point - market_open).seconds // 60} minutes of early trading data")
    
    # Sort by datetime
    calc_data.sort_values('datetime', inplace=True)
    display_data.sort_values('datetime', inplace=True)
    
    # Round timestamps to nearest minute for cleaner display
    calc_data['datetime'] = calc_data['datetime'].dt.floor('1min')
    display_data['datetime'] = display_data['datetime'].dt.floor('1min')
    
    print(f"Calculation data: {len(calc_data)} rows from {calc_data['datetime'].min()} to {calc_data['datetime'].max()}")
    print(f"Display data: {len(display_data)} rows from {display_data['datetime'].min()} to {display_data['datetime'].max()}")
    
    return calc_data, display_data

def calculate_rsi(data, period=14, price_col='close'):
    """
    Calculate RSI using Wilder's method
    
    Args:
        data (pd.DataFrame): DataFrame with price data
        period (int): RSI period (default: 14)
        price_col (str): Column name for price data
        
    Returns:
        pd.Series: RSI values
    """    # Make a copy of the dataframe to avoid modifying the original
    df = data.copy()
    
    # Calculate price differences
    df['diff'] = df[price_col].diff()
    
    # Create gain and loss columns
    df['gain'] = np.where(df['diff'] > 0, df['diff'], 0)
    df['loss'] = np.where(df['diff'] < 0, abs(df['diff']), 0)
    
    # First average gain and loss (simple average)
    if len(df) > period:
        avg_gain = df['gain'].iloc[1:period+1].mean()
        avg_loss = df['loss'].iloc[1:period+1].mean()
    else:
        print(f"Warning: Not enough data for {period}-period RSI. Need at least {period+1} data points.")
        return pd.Series(np.nan, index=df.index)  # Return NaN for all values
    
    # Initialize RSI Series
    rsi_values = pd.Series(index=df.index)
    rsi_values.iloc[:period] = np.nan  # First period values are NaN
    
    # Calculate first RSI value
    if avg_loss == 0:
        rsi_values.iloc[period] = 100
    else:
        rs = avg_gain / avg_loss
        rsi_values.iloc[period] = 100 - (100 / (1 + rs))
    
    # Calculate remaining RSI values using Wilder's smoothing method
    for i in range(period + 1, len(df)):
        avg_gain = ((period - 1) * avg_gain + df['gain'].iloc[i]) / period
        avg_loss = ((period - 1) * avg_loss + df['loss'].iloc[i]) / period
        
        if avg_loss == 0:
            rsi_values.iloc[i] = 100
        else:
            rs = avg_gain / avg_loss
            rsi_values.iloc[i] = 100 - (100 / (1 + rs))
    
    return rsi_values

def plot_candlesticks(ax, data):
    """
    Plot candlesticks
    
    Args:
        ax: matplotlib axis
        data: DataFrame with OHLC data
    """
    print(f"Plotting {len(data)} candlesticks from {data['datetime'].min()} to {data['datetime'].max()}")
    
    # Calculate candle width based on time intervals
    if len(data) > 1:
        time_diff = (data['datetime'].iloc[1] - data['datetime'].iloc[0])
        candle_width = time_diff * 0.8  # 80% of time interval
    else:
        # Default to 5 minutes if we can't calculate
        candle_width = pd.Timedelta(minutes=5)
    
    print(f"Candle width: {candle_width}")
    
    # Ensure y-axis has some padding
    prices = []
    
    # Plot each candlestick
    for idx, row in data.iterrows():
        date = mdates.date2num(row['datetime'])
        open_price = row['open']
        high_price = row['high']
        low_price = row['low']
        close_price = row['close']
        
        prices.extend([open_price, high_price, low_price, close_price])
        
        # Determine candle color - green for bullish, red for bearish
        color = '#00C851' if close_price >= open_price else '#FF4444'
        
        # Draw the wick (high-low line)
        ax.plot([date, date], [low_price, high_price], color='black', linewidth=1.2, alpha=0.8)
        
        # Draw the body (open-close rectangle)
        body_height = abs(close_price - open_price)
        body_bottom = min(open_price, close_price)
        
        # Create rectangle for candle body
        width_in_days = candle_width.total_seconds() / 86400  # Convert to days for matplotlib
        rect = Rectangle(
            (date - width_in_days/2, body_bottom), 
            width_in_days, 
            body_height,
            facecolor=color, 
            edgecolor='black', 
            alpha=0.8, 
            linewidth=0.5
        )
        ax.add_patch(rect)
    
    # Set appropriate y-axis limits with some padding
    if prices:
        price_min = min(prices)
        price_max = max(prices)
        price_range = price_max - price_min
        ax.set_ylim(price_min - price_range * 0.05, price_max + price_range * 0.05)

def plot_volume(ax, data, colormap=None):
    """
    Add volume bars to the volume axis (separate from price axis)
    
    Args:
        ax: matplotlib axis (should be a separate or twin axis)
        data: DataFrame with volume data
        colormap: Optional colormap for volume bars
    """
    # Calculate bar width based on time intervals
    if len(data) > 1:
        time_diff = (data['datetime'].iloc[1] - data['datetime'].iloc[0])
        bar_width = time_diff * 0.8  # 80% of time interval
    else:
        # Default to 5 minutes if we can't calculate
        bar_width = pd.Timedelta(minutes=5)
    
    # Get max volume for scaling
    max_vol = data['volume'].max()
    
    # Use native matplotlib bar plotting for better performance
    dates = [mdates.date2num(d) for d in data['datetime']]
    width_in_days = bar_width.total_seconds() / 86400  # Convert to days for matplotlib
    
    # Create arrays for colors
    colors = ['#00C85180' if c >= o else '#FF444480' for o, c in zip(data['open'], data['close'])]
    
    # Plot volume bars
    ax.bar(dates, data['volume'], width=width_in_days, color=colors, alpha=0.7)
    
    # Set up volume axis
    ax.set_ylim(0, max_vol * 1.2)  # Add 20% padding at top
    
    # Use scientific notation for large volume numbers
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f"{x:.1e}" if x > 1e6 else f"{x:,.0f}"))
    
    # Add volume label to the right side
    ax.yaxis.set_label_position("right")
    ax.set_ylabel('Volume', rotation=270, labelpad=15)
    
    # Make volume ticks less prominent
    ax.tick_params(axis='y', colors='gray')

def plot_rsi_with_candlesticks(data, rsi_values, save_path=None):
    """
    Plot RSI with candlesticks
    
    Args:
        data: DataFrame with price data
        rsi_values: Series with RSI values
        save_path: Path to save the plot image
    """
    # Create figure with 2 subplots, RSI takes 1/3 of the height
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10), 
                                  gridspec_kw={'height_ratios': [2, 1]},
                                  sharex=True)
    
    # Format the datetime axis for both plots
    plt.xticks(rotation=45, ha='right')
    
    # Determine date for title
    date_str = data['datetime'].iloc[0].strftime('%Y-%m-%d')    # Plot candlesticks on top subplot (main axis)
    plot_candlesticks(ax1, data)
    
    # Add price labels and grid to main axis
    ax1.set_ylabel('Price ($)', fontsize=12)
    ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x:.2f}'))
    ax1.grid(True, alpha=0.3, which='both')
    ax1.set_title(f'SPY Intraday Chart - {date_str}', fontsize=16, fontweight='bold')
      # Plot RSI on bottom subplot (filter out NaN values)
    valid_mask = ~rsi_values.isna()
    if valid_mask.any():
        valid_dates = data.loc[valid_mask, 'datetime']
        valid_rsi = rsi_values[valid_mask]
        ax2.plot(valid_dates, valid_rsi, color='purple', linewidth=1.5, label='RSI(14)')
    else:
        print("Warning: No valid RSI values to plot")
    
    # Add overbought/oversold lines and fill
    ax2.axhline(70, color='r', linestyle='--', alpha=0.5)
    ax2.axhline(30, color='g', linestyle='--', alpha=0.5)
    ax2.axhline(50, color='k', linestyle='-', alpha=0.2)  # Centerline
    
    # Fill overbought and oversold regions
    ax2.fill_between(data['datetime'], 70, 100, alpha=0.1, color='r')
    ax2.fill_between(data['datetime'], 0, 30, alpha=0.1, color='g')
    
    # Add RSI labels and grid
    ax2.set_ylim(0, 100)
    ax2.set_ylabel('RSI', fontsize=12)
    ax2.grid(True, alpha=0.3, which='both')
    
    # Add legend to RSI chart
    ax2.legend(loc='upper left')
    
    # Format x-axis
    formatter = mdates.DateFormatter('%H:%M')
    ax2.xaxis.set_major_formatter(formatter)
    ax2.xaxis.set_major_locator(mdates.HourLocator())
    ax2.xaxis.set_minor_locator(mdates.MinuteLocator(byminute=[15, 30, 45]))
    
    plt.tight_layout()
    
    # Save if path provided
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Chart saved to: {save_path}")
    
    plt.show()

def main():
    """Main function"""
    # Define paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.dirname(script_dir)
    data_dir = os.path.join(base_dir, 'historical_data')
    output_dir = os.path.join(base_dir, 'backtesting')
      # Save directly to base directory instead of backtesting
      # Define data file path
    csv_path = os.path.join(data_dir, 'spy_5min_merged_complete_20250611.csv')
    
    # Target date
    target_date = '2025-06-05'
    
    try:
        # Load data for June 5th, 2025 and include previous day for RSI calculation
        calc_data, display_data = load_data(csv_path, target_date, include_previous=True)
        
        if len(display_data) == 0:
            print(f"No data found for {target_date}")
            return
        
        print(f"Loaded {len(display_data)} data points for display on {target_date}")
        print(f"Time range for display: {display_data['datetime'].min()} to {display_data['datetime'].max()}")
        
        # Calculate RSI using the calculation data (which includes previous day)
        rsi_all = calculate_rsi(calc_data, period=14)
        print("RSI calculation complete")
        
        # Map the RSI values back to the display data
        rsi_values = pd.Series(index=display_data.index)
        
        # Create a mapping from datetime to RSI value
        rsi_dict = {}
        for idx, dt in enumerate(calc_data['datetime']):
            if not pd.isna(rsi_all.iloc[idx]):
                rsi_dict[dt] = rsi_all.iloc[idx]
        
        # Apply the mapping to get RSI values for display data
        for idx, row in display_data.iterrows():
            dt = row['datetime']
            if dt in rsi_dict:
                rsi_values.loc[idx] = rsi_dict[dt]
          # Keep all data points even if RSI is NaN at the beginning
        valid_rsi = rsi_values.copy()
        
        if len(display_data) == 0:
            print("Not enough data to calculate RSI")
            return
          # Plot RSI with candlesticks - save directly to base directory
        output_path = os.path.join(base_dir, f'spy_rsi_candlesticks_{target_date.replace("-", "")}.png')
        plot_rsi_with_candlesticks(display_data, valid_rsi, output_path)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
