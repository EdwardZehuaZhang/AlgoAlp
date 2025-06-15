#!/usr/bin/env python3
"""
RSI (Relative Strength Index) Indicator
=======================================

This module calculates and plots the RSI indicator using SPY CSV data.

RSI Components:
- Uses price changes to measure momentum
- Compares the magnitude of recent gains to recent losses
- Formula: RSI = 100 - (100 / (1 + RS))
  where RS = Average Gain / Average Loss

Trading Signals:
- Overbought: RSI above 70 (typically signals potential sell)
- Oversold: RSI below 30 (typically signals potential buy)
- Divergence: When price makes new high/low but RSI doesn't
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import numpy as np
import os
import sys

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class RSIIndicator:
    """
    RSI (Relative Strength Index) Indicator Calculator
    """
    
    def __init__(self, period=14):
        """
        Initialize RSI with standard parameters
        
        Args:
            period (int): RSI calculation period (default: 14)
        """        
        self.period = period
        self.data = None
        
    def load_csv_data(self, csv_path):
        """
        Load SPY data from CSV file
        
        Args:
            
              (str): Path to CSV file
            
        Returns:
            pd.DataFrame: Loaded and processed data
        """
        print(f"Loading data from: {csv_path}")
        
        # Load CSV and set index to datetime
        data = pd.read_csv(csv_path)
        
        # Check for column formats
        date_col = None
        close_col = None
        
        # Look for time/date column
        for col in ['Date', 'date', 'Time', 'time', 'datetime']:
            if col in data.columns:
                date_col = col
                break
        
        # Look for close column
        for col in ['Close', 'close']:
            if col in data.columns:
                close_col = col
                break
        
        if date_col is None or close_col is None:
            raise ValueError("CSV must contain date/time and close price columns")
        
        # Standardize column names
        data = data.rename(columns={date_col: 'Date', close_col: 'Close'})
        
        # Convert Date to datetime
        data['Date'] = pd.to_datetime(data['Date'])
        
        # Set Date as index
        data.set_index('Date', inplace=True)
        
        # Sort by date
        data.sort_index(inplace=True)
        
        self.data = data
        return data
    
    def calculate_rsi(self, close_series=None):
        """
        Calculate RSI based on closing prices
        
        Args:
            close_series (pd.Series, optional): Close price series, 
                                               if None, uses self.data['Close']
        
        Returns:
            pd.Series: RSI values
        """
        if close_series is None:
            if self.data is None:
                raise ValueError("No data loaded. Call load_csv_data first or provide a close_series.")
            close_series = self.data['Close']
            
        # Calculate price changes
        price_diff = close_series.diff()
        
        # Create two copies for gains and losses
        gains = price_diff.copy()
        losses = price_diff.copy()
        
        # Zero out losses in gains series
        gains[gains < 0] = 0
        
        # Zero out gains in losses series and make positive
        losses[losses > 0] = 0
        losses = abs(losses)
        
        # Calculate initial average gains and losses over the period
        avg_gain = gains.rolling(window=self.period).mean()
        avg_loss = losses.rolling(window=self.period).mean()
        
        # Calculate RS (Relative Strength)
        rs = avg_gain / avg_loss
        
        # Calculate RSI
        rsi = 100 - (100 / (1 + rs))
        
        return rsi
    
    def calculate_wilder_rsi(self, close_series=None):
        """
        Calculate RSI using Wilder's smoothing method (more accurate)
        
        Args:
            close_series (pd.Series, optional): Close price series, 
                                               if None, uses self.data['Close']
        
        Returns:
            pd.Series: RSI values
        """
        if close_series is None:
            if self.data is None:
                raise ValueError("No data loaded. Call load_csv_data first or provide a close_series.")
            close_series = self.data['Close']
        
        # Calculate price changes
        price_diff = close_series.diff()
        
        # Create two copies for gains and losses
        gains = price_diff.copy()
        losses = price_diff.copy()
        
        # Zero out losses in gains series
        gains[gains < 0] = 0
        
        # Zero out gains in losses series and make positive
        losses[losses > 0] = 0
        losses = abs(losses)
        
        # First average gain and loss - simple average for the first period
        first_avg_gain = gains.rolling(window=self.period).mean().iloc[self.period]
        first_avg_loss = losses.rolling(window=self.period).mean().iloc[self.period]
        
        # Setup Series for avg_gain and avg_loss
        avg_gain = pd.Series(index=close_series.index)
        avg_loss = pd.Series(index=close_series.index)
        
        # Set first values
        avg_gain.iloc[self.period] = first_avg_gain
        avg_loss.iloc[self.period] = first_avg_loss
        
        # Calculate smoothed averages according to Wilder's formula
        for i in range(self.period + 1, len(close_series)):
            avg_gain.iloc[i] = ((self.period - 1) * avg_gain.iloc[i-1] + gains.iloc[i]) / self.period
            avg_loss.iloc[i] = ((self.period - 1) * avg_loss.iloc[i-1] + losses.iloc[i]) / self.period
        
        # Calculate RS (Relative Strength)
        rs = avg_gain / avg_loss
        
        # Calculate RSI
        rsi = 100 - (100 / (1 + rs))
        
        return rsi
    
    def calculate(self, use_wilder=True):
        """
        Calculate RSI and add to data
        
        Args:
            use_wilder (bool): Whether to use Wilder's smoothing method (default: True)
        
        Returns:
            pd.DataFrame: Data with RSI column added
        """
        if self.data is None:
            raise ValueError("No data loaded. Call load_csv_data first.")
            
        # Calculate RSI
        if use_wilder:
            self.data['RSI'] = self.calculate_wilder_rsi()
        else:
            self.data['RSI'] = self.calculate_rsi()
            
        return self.data
    
    def plot_rsi(self, output_path=None, show_plot=True):
        """
        Plot RSI indicator with price
        
        Args:
            output_path (str, optional): Path to save the plot image
            show_plot (bool): Whether to display the plot (default: True)
            
        Returns:
            tuple: Figure and axes objects
        """
        if self.data is None or 'RSI' not in self.data.columns:
            raise ValueError("RSI not calculated. Call calculate() first.")
        
        # Create figure and subplots
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), gridspec_kw={'height_ratios': [3, 1]})
        
        # Plot price on top subplot
        ax1.plot(self.data.index, self.data['Close'], color='blue', linewidth=1.5)
        ax1.set_title('Price and RSI Indicator', fontsize=15)
        ax1.set_ylabel('Price', fontsize=12)
        ax1.grid(True, alpha=0.3)
        
        # Set x-axis to dates
        ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        ax1.xaxis.set_major_locator(mdates.MonthLocator())
        
        # Plot RSI on bottom subplot
        ax2.plot(self.data.index, self.data['RSI'], color='purple', linewidth=1.5)
        ax2.axhline(y=70, color='r', linestyle='--', alpha=0.5)
        ax2.axhline(y=30, color='g', linestyle='--', alpha=0.5)
        ax2.fill_between(self.data.index, 70, self.data['RSI'], 
                         where=(self.data['RSI'] >= 70), 
                         color='r', alpha=0.3)
        ax2.fill_between(self.data.index, 30, self.data['RSI'], 
                         where=(self.data['RSI'] <= 30), 
                         color='g', alpha=0.3)
        ax2.set_ylabel('RSI', fontsize=12)
        ax2.grid(True, alpha=0.3)
        ax2.set_ylim(0, 100)
        
        # Set x-axis limits to match
        ax2.set_xlim(ax1.get_xlim())
        
        # Set x-axis to dates
        ax2.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        ax2.xaxis.set_major_locator(mdates.MonthLocator())
        
        # Rotate date labels for better readability
        plt.setp(ax2.xaxis.get_majorticklabels(), rotation=45)
        
        # Tight layout
        plt.tight_layout()
        
        # Save if output path is provided
        if output_path:
            plt.savefig(output_path, dpi=300, bbox_inches='tight')
            print(f"Plot saved to: {output_path}")
            
        # Show plot if requested
        if show_plot:
            plt.show()
            
        return fig, (ax1, ax2)
    
    def get_signals(self, overbought=70, oversold=30):
        """
        Get buy/sell signals based on RSI thresholds
        
        Args:
            overbought (int): RSI level considered overbought (default: 70)
            oversold (int): RSI level considered oversold (default: 30)
            
        Returns:
            pd.DataFrame: DataFrame with Buy and Sell signals
        """
        if self.data is None or 'RSI' not in self.data.columns:
            raise ValueError("RSI not calculated. Call calculate() first.")
            
        signals = pd.DataFrame(index=self.data.index)
        signals['Price'] = self.data['Close']
        signals['RSI'] = self.data['RSI']
        
        # Initialize signals
        signals['Buy'] = 0
        signals['Sell'] = 0
        
        # Generate buy signal when RSI crosses below oversold level
        signals['Buy'] = np.where(
            (signals['RSI'] < oversold) & 
            (signals['RSI'].shift(1) >= oversold), 
            1, 0
        )
        
        # Generate sell signal when RSI crosses above overbought level
        signals['Sell'] = np.where(
            (signals['RSI'] > overbought) & 
            (signals['RSI'].shift(1) <= overbought), 
            1, 0
        )
        
        return signals
        
    def plot_signals(self, signals=None, output_path=None, show_plot=True):
        """
        Plot RSI indicator with buy/sell signals
        
        Args:
            signals (pd.DataFrame, optional): Signals dataframe from get_signals()
            output_path (str, optional): Path to save the plot image
            show_plot (bool): Whether to display the plot (default: True)
            
        Returns:
            tuple: Figure and axes objects
        """
        if signals is None:
            signals = self.get_signals()
        
        # Create figure and subplots
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10), gridspec_kw={'height_ratios': [3, 1]})
        
        # Plot price on top subplot
        ax1.plot(signals.index, signals['Price'], color='blue', linewidth=1.5)
        ax1.set_title('Price with Buy/Sell Signals based on RSI', fontsize=15)
        ax1.set_ylabel('Price', fontsize=12)
        ax1.grid(True, alpha=0.3)
        
        # Plot buy signals
        buy_signals = signals[signals['Buy'] == 1]
        if not buy_signals.empty:
            ax1.scatter(buy_signals.index, buy_signals['Price'], 
                       marker='^', color='green', s=100, label='Buy Signal')
        
        # Plot sell signals
        sell_signals = signals[signals['Sell'] == 1]
        if not sell_signals.empty:
            ax1.scatter(sell_signals.index, sell_signals['Price'], 
                       marker='v', color='red', s=100, label='Sell Signal')
        
        # Add legend
        ax1.legend()
        
        # Plot RSI on bottom subplot
        ax2.plot(signals.index, signals['RSI'], color='purple', linewidth=1.5)
        ax2.axhline(y=70, color='r', linestyle='--', alpha=0.5, label='Overbought (70)')
        ax2.axhline(y=30, color='g', linestyle='--', alpha=0.5, label='Oversold (30)')
        ax2.fill_between(signals.index, 70, signals['RSI'], 
                         where=(signals['RSI'] >= 70), 
                         color='r', alpha=0.3)
        ax2.fill_between(signals.index, 30, signals['RSI'], 
                         where=(signals['RSI'] <= 30), 
                         color='g', alpha=0.3)
        ax2.set_ylabel('RSI', fontsize=12)
        ax2.grid(True, alpha=0.3)
        ax2.set_ylim(0, 100)
        ax2.legend(loc='upper left')
        
        # Mark signals on RSI chart too
        if not buy_signals.empty:
            ax2.scatter(buy_signals.index, buy_signals['RSI'], 
                       marker='^', color='green', s=80)
        if not sell_signals.empty:
            ax2.scatter(sell_signals.index, sell_signals['RSI'], 
                       marker='v', color='red', s=80)
        
        # Set x-axis limits to match
        ax2.set_xlim(ax1.get_xlim())
        
        # Set x-axis to dates
        ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        ax2.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        
        # Adjust locator based on the date range
        date_range = (signals.index[-1] - signals.index[0]).days
        if date_range > 365*2:
            locator = mdates.YearLocator()
        elif date_range > 180:
            locator = mdates.MonthLocator(interval=3)  # Quarterly
        else:
            locator = mdates.MonthLocator()  # Monthly
            
        ax1.xaxis.set_major_locator(locator)
        ax2.xaxis.set_major_locator(locator)
        
        # Rotate date labels for better readability
        plt.setp(ax2.xaxis.get_majorticklabels(), rotation=45)
        
        # Tight layout
        plt.tight_layout()
        
        # Save if output path is provided
        if output_path:
            plt.savefig(output_path, dpi=300, bbox_inches='tight')
            print(f"Plot saved to: {output_path}")
            
        # Show plot if requested
        if show_plot:
            plt.show()
            
        return fig, (ax1, ax2)
    
    def backtest_signals(self):
        """
        Simple backtest of RSI strategy
        
        Returns:
            dict: Performance metrics
        """
        signals = self.get_signals()
        
        # Create position column (1 for long, -1 for short, 0 for no position)
        signals['Position'] = 0
        
        # Set positions based on signals
        for i in range(len(signals)):
            if signals['Buy'].iloc[i] == 1:
                signals.loc[signals.index[i]:, 'Position'] = 1
            elif signals['Sell'].iloc[i] == 1:
                signals.loc[signals.index[i]:, 'Position'] = -1
        
        # Calculate returns
        signals['Returns'] = signals['Price'].pct_change()
        signals['Strategy'] = signals['Position'].shift(1) * signals['Returns']
        
        # Calculate cumulative returns
        signals['CumReturns'] = (1 + signals['Returns']).cumprod()
        signals['CumStrategy'] = (1 + signals['Strategy']).cumprod()
        
        # Calculate metrics
        total_return = signals['CumStrategy'].iloc[-1] - 1
        annualized_return = (1 + total_return) ** (252 / len(signals)) - 1
        
        # Calculate max drawdown
        roll_max = signals['CumStrategy'].cummax()
        drawdown = (signals['CumStrategy'] / roll_max) - 1
        max_drawdown = drawdown.min()
        
        # Calculate Sharpe ratio (assuming risk-free rate of 0)
        sharpe_ratio = signals['Strategy'].mean() / signals['Strategy'].std() * np.sqrt(252)
        
        # Count trades
        trades = signals['Position'].diff().fillna(0) != 0
        num_trades = trades.sum()
        
        metrics = {
            'Total Return': total_return,
            'Annualized Return': annualized_return,
            'Max Drawdown': max_drawdown,
            'Sharpe Ratio': sharpe_ratio,
            'Number of Trades': num_trades
        }
        
        return metrics, signals
