"""
Visualization tools for strategy analysis
"""
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
from dotenv import load_dotenv
from alpaca_trade_api.rest import REST
import config
from utils import get_minute_data, get_hourly_data, calculate_indicators, calculate_hour_trend

# Load environment variables
load_dotenv()

# Initialize Alpaca API
API_KEY = os.getenv("ALPACA_API_KEY")
API_SECRET = os.getenv("ALPACA_API_SECRET")
PAPER = os.getenv("ALPACA_PAPER", "True").lower() in ("true", "1", "t")
BASE_URL = "https://paper-api.alpaca.markets" if PAPER else "https://api.alpaca.markets"

api = REST(API_KEY, API_SECRET, BASE_URL, api_version='v2')

def plot_strategy_indicators(days_back=5):
    """
    Plot strategy indicators for visual analysis
    """
    # Get hourly data for trend
    hourly_data = get_hourly_data(api, config.SYMBOL, lookback=days_back*2)
    hourly_data = calculate_indicators(
        hourly_data,
        config.ULTRAFAST_PERIOD,
        config.FAST_PERIOD,
        config.SLOW_PERIOD,
        config.RSI_PERIOD,
        config.MACD_FAST_LENGTH,
        config.MACD_SLOW_LENGTH,
        config.MACD_SIGNAL_SMOOTHING
    )
    
    # Get minute data for signals
    minute_data = get_minute_data(api, config.SYMBOL, lookback=days_back)
    minute_data = calculate_indicators(
        minute_data,
        config.ULTRAFAST_PERIOD,
        config.FAST_PERIOD,
        config.SLOW_PERIOD,
        config.RSI_PERIOD,
        config.MACD_FAST_LENGTH,
        config.MACD_SLOW_LENGTH,
        config.MACD_SIGNAL_SMOOTHING
    )
    
    # Calculate trend states for each hour
    hourly_data['trend_state'] = 0
    for i in range(1, len(hourly_data)):
        trend_state = 0
        if hourly_data['is_bullish'].iloc[i] and hourly_data['close_above'].iloc[i]:
            trend_state = 1
        elif not hourly_data['is_bullish'].iloc[i] and hourly_data['close_below'].iloc[i]:
            trend_state = -1
        hourly_data.loc[hourly_data.index[i], 'trend_state'] = trend_state
    
    # Create subplots
    fig, axs = plt.subplots(3, 1, figsize=(12, 14), gridspec_kw={'height_ratios': [3, 1, 1]})
    
    # Format dates
    date_format = DateFormatter('%Y-%m-%d %H:%M')
    
    # Plot 1: Price and Moving Averages
    axs[0].set_title(f'{config.SYMBOL} Price and Moving Averages')
    axs[0].plot(minute_data.index, minute_data['close'], label='Price', color='black', alpha=0.7)
    axs[0].plot(minute_data.index, minute_data['ultrafast_sma'], label=f'Ultra-Fast SMA ({config.ULTRAFAST_PERIOD})', color='yellow', alpha=0.6)
    axs[0].plot(minute_data.index, minute_data['fast_sma'], label=f'Fast SMA ({config.FAST_PERIOD})', color='magenta', alpha=0.6)
    axs[0].plot(minute_data.index, minute_data['slow_sma'], label=f'Slow SMA ({config.SLOW_PERIOD})', color='blue', alpha=0.6)
    
    # Highlight 1-hour trend background
    hour_markers = pd.date_range(start=minute_data.index[0], end=minute_data.index[-1], freq='1H')
    
    for i in range(len(hour_markers)-1):
        hour_start = hour_markers[i]
        hour_end = hour_markers[i+1]
        
        # Find the trend state for this hour
        hour_idx = hourly_data.index.get_indexer([hour_start], method='nearest')[0]
        if hour_idx < len(hourly_data):
            trend_state = hourly_data['trend_state'].iloc[hour_idx]
            
            # Set background color based on trend state
            if trend_state == 1:
                axs[0].axvspan(hour_start, hour_end, alpha=0.1, color='green')
            elif trend_state == -1:
                axs[0].axvspan(hour_start, hour_end, alpha=0.1, color='red')
    
    # Identify potential buy/sell signals
    buy_signals = []
    sell_signals = []
    
    # Simplified signal logic for visualization
    for i in range(2, len(minute_data)):
        # MACD crossovers
        macd_crossover = (minute_data['macd'].iloc[i-1] <= minute_data['macd_signal'].iloc[i-1]) and (minute_data['macd'].iloc[i] > minute_data['macd_signal'].iloc[i])
        macd_crossunder = (minute_data['macd'].iloc[i-1] >= minute_data['macd_signal'].iloc[i-1]) and (minute_data['macd'].iloc[i] < minute_data['macd_signal'].iloc[i])
        
        # RSI conditions
        rsi_oversold = minute_data['rsi'].iloc[i] < config.RSI_OVERSOLD
        rsi_overbought = minute_data['rsi'].iloc[i] > config.RSI_OVERBOUGHT
        
        # Buy signal (simplified for visualization)
        if macd_crossover and minute_data['rsi'].iloc[i] < 50:
            buy_signals.append(minute_data.index[i])
        
        # Sell signal (simplified for visualization)
        if macd_crossunder and minute_data['rsi'].iloc[i] > 50:
            sell_signals.append(minute_data.index[i])
    
    # Plot buy/sell signals
    for signal in buy_signals:
        axs[0].scatter(signal, minute_data.loc[signal, 'close'], color='green', marker='^', s=100)
    
    for signal in sell_signals:
        axs[0].scatter(signal, minute_data.loc[signal, 'close'], color='red', marker='v', s=100)
    
    axs[0].xaxis.set_major_formatter(date_format)
    axs[0].grid(True, alpha=0.3)
    axs[0].legend()
    
    # Plot 2: RSI
    axs[1].set_title('RSI')
    axs[1].plot(minute_data.index, minute_data['rsi'], color='purple')
    axs[1].axhline(y=config.RSI_OVERBOUGHT, color='r', linestyle='--', alpha=0.5)
    axs[1].axhline(y=config.RSI_OVERSOLD, color='g', linestyle='--', alpha=0.5)
    axs[1].axhline(y=50, color='k', linestyle='-', alpha=0.2)
    axs[1].fill_between(minute_data.index, minute_data['rsi'], config.RSI_OVERBOUGHT, 
                        where=(minute_data['rsi'] >= config.RSI_OVERBOUGHT), color='red', alpha=0.3)
    axs[1].fill_between(minute_data.index, minute_data['rsi'], config.RSI_OVERSOLD, 
                        where=(minute_data['rsi'] <= config.RSI_OVERSOLD), color='green', alpha=0.3)
    axs[1].set_ylim(0, 100)
    axs[1].xaxis.set_major_formatter(date_format)
    axs[1].grid(True, alpha=0.3)
    
    # Plot 3: MACD
    axs[2].set_title('MACD')
    axs[2].plot(minute_data.index, minute_data['macd'], label='MACD', color='blue')
    axs[2].plot(minute_data.index, minute_data['macd_signal'], label='Signal', color='red')
    axs[2].bar(minute_data.index, minute_data['macd'] - minute_data['macd_signal'], 
               color=['green' if x >= 0 else 'red' for x in minute_data['macd'] - minute_data['macd_signal']], 
               alpha=0.5, width=0.0005)
    axs[2].axhline(y=0, color='k', linestyle='-', alpha=0.3)
    axs[2].xaxis.set_major_formatter(date_format)
    axs[2].grid(True, alpha=0.3)
    axs[2].legend()
    
    # Adjust layout
    plt.tight_layout()
    
    # Save the plot
    plt.savefig('strategy_analysis.png', dpi=300)
    
    # Show the plot
    plt.show()
    
    print(f"Plot saved as 'strategy_analysis.png'")

def plot_backtest_performance():
    """
    Plot performance metrics based on account history
    """
    try:
        # Get account activities
        activities = api.get_account_activities(activity_types='FILL')
        
        if not activities:
            print("No trading activity found in the account")
            return
        
        # Convert to DataFrame
        df = pd.DataFrame([{
            'symbol': activity.symbol,
            'timestamp': activity.timestamp,
            'price': float(activity.price),
            'qty': float(activity.qty),
            'side': activity.side,
            'transaction_type': activity.type
        } for activity in activities if activity.symbol == config.SYMBOL])
        
        if df.empty:
            print(f"No trading activity found for {config.SYMBOL}")
            return
        
        # Sort by timestamp
        df = df.sort_values('timestamp')
        
        # Calculate cumulative position and P&L
        df['position'] = df['qty'] * (df['side'] == 'buy').astype(int) - df['qty'] * (df['side'] == 'sell').astype(int)
        df['cumulative_position'] = df['position'].cumsum()
        
        # Calculate trade values
        df['trade_value'] = df['price'] * df['qty']
        
        # Identify round trips (buy then sell)
        position_changes = []
        current_position = 0
        
        for _, row in df.iterrows():
            current_position += row['position']
            position_changes.append(current_position)
        
        df['current_position'] = position_changes
        
        # Create subplots
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
        
        # Plot 1: Price and Fills
        ax1.set_title(f'{config.SYMBOL} Price and Trades')
        
        # Get price history
        end_time = df['timestamp'].max()
        start_time = df['timestamp'].min() - pd.Timedelta(days=1)
        
        minute_data = api.get_bars(
            config.SYMBOL,
            '1Min',
            start=start_time.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
            end=end_time.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
            limit=10000
        ).df
        
        if not minute_data.empty:
            ax1.plot(minute_data.index, minute_data['close'], label='Price', color='black', alpha=0.7)
        
            # Plot buys and sells
            buy_df = df[df['side'] == 'buy']
            sell_df = df[df['side'] == 'sell']
            
            for _, row in buy_df.iterrows():
                ax1.scatter(row['timestamp'], row['price'], color='green', marker='^', s=100)
            
            for _, row in sell_df.iterrows():
                ax1.scatter(row['timestamp'], row['price'], color='red', marker='v', s=100)
        
            # Format dates
            date_format = DateFormatter('%Y-%m-%d %H:%M')
            ax1.xaxis.set_major_formatter(date_format)
            ax1.grid(True, alpha=0.3)
            ax1.legend()
        
        # Plot 2: P&L Over Time
        ax2.set_title('Cumulative Position and P&L')
        
        # Calculate running P&L (simplified)
        if len(df) > 1:
            # Create a running record of buys and sells for P&L calculation
            running_buys = []
            running_sells = []
            pnl = []
            cumulative_pnl = 0
            
            for _, row in df.iterrows():
                if row['side'] == 'buy':
                    running_buys.append((row['price'], row['qty']))
                else:  # sell
                    qty_to_sell = row['qty']
                    sell_price = row['price']
                    
                    while qty_to_sell > 0 and running_buys:
                        buy_price, buy_qty = running_buys[0]
                        
                        if buy_qty <= qty_to_sell:
                            # Use the entire buy
                            qty_matched = buy_qty
                            running_buys.pop(0)
                        else:
                            # Use part of the buy
                            qty_matched = qty_to_sell
                            running_buys[0] = (buy_price, buy_qty - qty_matched)
                        
                        # Calculate P&L for this portion
                        trade_pnl = (sell_price - buy_price) * qty_matched
                        cumulative_pnl += trade_pnl
                        qty_to_sell -= qty_matched
                
                pnl.append(cumulative_pnl)
            
            df['cumulative_pnl'] = pnl
            
            # Plot cumulative P&L
            ax2.plot(df['timestamp'], df['cumulative_pnl'], label='Cumulative P&L ($)', color='blue')
            ax2.axhline(y=0, color='k', linestyle='-', alpha=0.3)
            
            # Add a second y-axis for position
            ax2_position = ax2.twinx()
            ax2_position.plot(df['timestamp'], df['cumulative_position'], label='Position Size', color='orange', alpha=0.6)
            ax2_position.set_ylabel('Position Size (Shares)', color='orange')
            
            # Format dates
            ax2.xaxis.set_major_formatter(date_format)
            ax2.grid(True, alpha=0.3)
            
            # Legends
            lines1, labels1 = ax2.get_legend_handles_labels()
            lines2, labels2 = ax2_position.get_legend_handles_labels()
            ax2.legend(lines1 + lines2, labels1 + labels2, loc='upper left')
        
        # Adjust layout
        plt.tight_layout()
        
        # Save the plot
        plt.savefig('performance_analysis.png', dpi=300)
        
        # Show the plot
        plt.show()
        
        print(f"Plot saved as 'performance_analysis.png'")
        
        # Print summary statistics
        if 'cumulative_pnl' in df.columns:
            print("\nPerformance Summary:")
            print(f"Total P&L: ${df['cumulative_pnl'].iloc[-1]:.2f}")
            print(f"Number of trades: {len(df) // 2}")  # Assuming each trade has a buy and sell
        
    except Exception as e:
        print(f"Error plotting backtest performance: {str(e)}")

if __name__ == "__main__":
    print("Visualizing strategy indicators...")
    plot_strategy_indicators()
    
    print("\nPlotting backtest performance...")
    plot_backtest_performance() 