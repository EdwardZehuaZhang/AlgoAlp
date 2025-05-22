"""
Visualization module for AlgoAlp trading application
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import mplfinance as mpf
import numpy as np
import os
from datetime import datetime, timedelta
import json
import argparse
from utils import get_alpaca_api

def fetch_price_data(symbol="SPY", timeframe="1Day", limit=100):
    """Fetch historical price data from Alpaca"""
    api = get_alpaca_api()
    
    # Calculate dates
    end_date = datetime.now()
    start_date = end_date - timedelta(days=limit)
    
    # Fetch data
    bars = api.get_bars(
        symbol,
        timeframe,
        start=start_date.isoformat(),
        end=end_date.isoformat(),
        adjustment='all'
    ).df
    
    return bars

def add_indicators(df):
    """Add technical indicators to the dataframe"""
    # Calculate SMAs
    df['sma20'] = df['close'].rolling(window=20).mean()
    df['sma50'] = df['close'].rolling(window=50).mean()
    df['sma200'] = df['close'].rolling(window=200).mean()
    
    # Calculate RSI
    delta = df['close'].diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    
    avg_gain = gain.rolling(window=14).mean()
    avg_loss = loss.rolling(window=14).mean()
    
    rs = avg_gain / avg_loss.replace(0, 0.00001)  # Avoid division by zero
    df['rsi'] = 100 - (100 / (1 + rs))
    
    # Calculate MACD
    exp1 = df['close'].ewm(span=12, adjust=False).mean()
    exp2 = df['close'].ewm(span=26, adjust=False).mean()
    df['macd'] = exp1 - exp2
    df['macd_signal'] = df['macd'].ewm(span=9, adjust=False).mean()
    df['macd_hist'] = df['macd'] - df['macd_signal']
    
    return df

def plot_strategy_chart(data, trades=None, save_path=None):
    """Plot a chart with price, indicators, and trade signals"""
    # Add indicators
    data = add_indicators(data)
    
    # Create a new figure with subplots
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 10), gridspec_kw={'height_ratios': [3, 1, 1]})
    
    # Plot price and SMAs
    data['close'].plot(ax=ax1, color='black', label='Price')
    data['sma20'].plot(ax=ax1, color='blue', label='SMA 20')
    data['sma50'].plot(ax=ax1, color='orange', label='SMA 50')
    data['sma200'].plot(ax=ax1, color='red', label='SMA 200')
    
    # Add trades if provided
    if trades is not None:
        for trade in trades:
            trade_time = pd.to_datetime(trade['timestamp'])
            if trade['side'].lower() == 'buy':
                ax1.axvline(x=trade_time, color='green', linestyle='--', alpha=0.7)
                ax1.plot(trade_time, trade['price'], 'g^', markersize=10)
            else:
                ax1.axvline(x=trade_time, color='red', linestyle='--', alpha=0.7)
                ax1.plot(trade_time, trade['price'], 'rv', markersize=10)
    
    # Plot RSI
    data['rsi'].plot(ax=ax2, color='purple', label='RSI')
    ax2.axhline(y=70, color='red', linestyle='--', alpha=0.5)
    ax2.axhline(y=30, color='green', linestyle='--', alpha=0.5)
    ax2.set_ylim(0, 100)
    ax2.set_ylabel('RSI')
    ax2.legend()
    
    # Plot MACD
    data['macd'].plot(ax=ax3, color='blue', label='MACD')
    data['macd_signal'].plot(ax=ax3, color='red', label='Signal')
    ax3.bar(data.index, data['macd_hist'], color=['green' if x > 0 else 'red' for x in data['macd_hist']], alpha=0.5)
    ax3.set_ylabel('MACD')
    ax3.legend()
    
    # Format x-axis
    for ax in [ax1, ax2, ax3]:
        ax.grid(True, alpha=0.3)
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        ax.tick_params(axis='x', rotation=45)
    
    # Add title and legend
    ax1.set_title(f'AlgoAlp Strategy Chart - {data.index[0].strftime("%Y-%m-%d")} to {data.index[-1].strftime("%Y-%m-%d")}')
    ax1.legend()
    ax1.set_ylabel('Price')
    
    # Adjust layout
    fig.tight_layout()
    
    # Save if path provided
    if save_path:
        plt.savefig(save_path)
        print(f"Chart saved to {save_path}")
    
    plt.show()

def plot_performance_chart(trades_file="trade_history.json", save_path=None):
    """Plot performance metrics from trade history"""
    # Load trades
    if not os.path.exists(trades_file):
        print(f"No trade history file found at {trades_file}")
        return
        
    with open(trades_file, 'r') as f:
        trades = json.load(f)
    
    if not trades:
        print("No trades found in history file")
        return
        
    # Convert to DataFrame
    df = pd.DataFrame(trades)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df.set_index('timestamp', inplace=True)
    df.sort_index(inplace=True)
    
    # Calculate performance metrics
    df['cumulative_profit'] = 0
    
    # Determine profits/losses
    for i, trade in enumerate(trades):
        if i % 2 == 0 and i+1 < len(trades):  # Buy trade with a matching sell
            buy_price = trade['price']
            sell_price = trades[i+1]['price']
            quantity = trade['quantity']
            profit = (sell_price - buy_price) * quantity
            df.loc[pd.to_datetime(trades[i+1]['timestamp']), 'trade_profit'] = profit
    
    # Calculate cumulative profit
    df['trade_profit'] = df.get('trade_profit', 0)
    df['cumulative_profit'] = df['trade_profit'].cumsum()
    
    # Plot performance chart
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))
    
    # Plot cumulative profit
    df['cumulative_profit'].plot(ax=ax1, color='blue')
    ax1.set_title('AlgoAlp Trading Performance')
    ax1.set_ylabel('Cumulative Profit ($)')
    ax1.grid(True, alpha=0.3)
    
    # Plot trade profits
    if 'trade_profit' in df.columns:
        colors = ['green' if x > 0 else 'red' for x in df['trade_profit']]
        ax2.bar(df.index, df['trade_profit'], color=colors)
        ax2.set_ylabel('Trade Profit/Loss ($)')
        ax2.grid(True, alpha=0.3)
    
    # Format x-axis
    for ax in [ax1, ax2]:
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        ax.tick_params(axis='x', rotation=45)
    
    # Adjust layout
    fig.tight_layout()
    
    # Save if path provided
    if save_path:
        plt.savefig(save_path)
        print(f"Performance chart saved to {save_path}")
    
    plt.show()

def main():
    """Main function to run visualization"""
    parser = argparse.ArgumentParser(description="AlgoAlp Visualization Tool")
    parser.add_argument('--symbol', default='SPY', help='Symbol to visualize')
    parser.add_argument('--days', type=int, default=60, help='Number of days of data to fetch')
    parser.add_argument('--trades', default='trade_history.json', help='Trade history file')
    parser.add_argument('--save', help='Path to save chart image')
    parser.add_argument('--type', choices=['strategy', 'performance', 'both'], default='both', help='Type of chart to generate')
    
    args = parser.parse_args()
    
    if args.type in ['strategy', 'both']:
        print(f"Fetching {args.days} days of data for {args.symbol}...")
        data = fetch_price_data(args.symbol, limit=args.days)
        
        # Load trades if file exists
        trades = None
        if os.path.exists(args.trades):
            with open(args.trades, 'r') as f:
                trades = json.load(f)
                
        save_path = args.save if args.type != 'both' else f"{os.path.splitext(args.save)[0]}_strategy.png" if args.save else None
        plot_strategy_chart(data, trades, save_path)
    
    if args.type in ['performance', 'both']:
        save_path = args.save if args.type != 'both' else f"{os.path.splitext(args.save)[0]}_performance.png" if args.save else None
        plot_performance_chart(args.trades, save_path)

if __name__ == "__main__":
    main()