#!/usr/bin/env python3
"""
MACD (Moving Average Convergence Divergence) Indicator
======================================================

This module calculates and plots the MACD indicator using SPY CSV data.

MACD Components:
- MACD Line: 12-period EMA - 26-period EMA
- Signal Line: 9-period EMA of MACD Line
- Histogram: MACD Line - Signal Line

Trading Signals:
- Bullish: MACD crosses above Signal Line
- Bearish: MACD crosses below Signal Line
- Momentum: MACD crosses above/below zero line
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

class MACDIndicator:
    """
    MACD (Moving Average Convergence Divergence) Indicator Calculator
    """
    
    def __init__(self, fast_period=12, slow_period=26, signal_period=9):
        """
        Initialize MACD with standard parameters
        
        Args:
            fast_period (int): Short-term EMA period (default: 12)
            slow_period (int): Long-term EMA period (default: 26)
            signal_period (int): Signal line EMA period (default: 9)
        """
        self.fast_period = fast_period
        self.slow_period = slow_period
        self.signal_period = signal_period
        self.data = None
        
    def load_csv_data(self, csv_path):
        """
        Load SPY data from CSV file
        
        Args:
            csv_path (str): Path to CSV file
            
        Returns:
            pd.DataFrame: Loaded and processed data
        """
        print(f"Loading data from: {csv_path}")
        
        # Load CSV data
        self.data = pd.read_csv(csv_path)
        
        # Convert timestamp to datetime
        self.data['datetime'] = pd.to_datetime(self.data['timestamp'], unit='s')
        self.data.set_index('datetime', inplace=True)
        
        # Ensure we have required columns
        required_cols = ['open', 'high', 'low', 'close', 'volume']
        for col in required_cols:
            if col not in self.data.columns:
                raise ValueError(f"Missing required column: {col}")
        
        print(f"Loaded {len(self.data)} data points")
        print(f"Date range: {self.data.index[0]} to {self.data.index[-1]}")
        
        return self.data
    
    def calculate_ema(self, series, period):
        """
        Calculate Exponential Moving Average
        
        Args:
            series (pd.Series): Price series
            period (int): EMA period
            
        Returns:
            pd.Series: EMA values
        """
        return series.ewm(span=period, adjust=False).mean()
    
    def calculate_macd(self):
        """
        Calculate MACD components
        
        Returns:
            dict: Dictionary containing MACD components
        """
        if self.data is None:
            raise ValueError("Data not loaded. Call load_csv_data() first.")
        
        # Calculate EMAs
        self.data['EMA_fast'] = self.calculate_ema(self.data['close'], self.fast_period)
        self.data['EMA_slow'] = self.calculate_ema(self.data['close'], self.slow_period)
        
        # Calculate MACD Line
        self.data['MACD'] = self.data['EMA_fast'] - self.data['EMA_slow']
        
        # Calculate Signal Line
        self.data['Signal'] = self.calculate_ema(self.data['MACD'], self.signal_period)
        
        # Calculate Histogram
        self.data['Histogram'] = self.data['MACD'] - self.data['Signal']
        
        return {
            'MACD': self.data['MACD'],
            'Signal': self.data['Signal'],
            'Histogram': self.data['Histogram']
        }
    
    def detect_crossovers(self, lookback_periods=5):
        """
        Detect MACD crossovers and generate signals
        
        Args:
            lookback_periods (int): Number of recent periods to analyze
            
        Returns:
            dict: Crossover information
        """
        if 'MACD' not in self.data.columns:
            self.calculate_macd()
        
        # Get recent data
        recent_data = self.data.tail(lookback_periods)
        
        # Check for crossovers in recent data
        crossovers = []
        
        for i in range(1, len(recent_data)):
            prev_macd = recent_data['MACD'].iloc[i-1]
            prev_signal = recent_data['Signal'].iloc[i-1]
            curr_macd = recent_data['MACD'].iloc[i]
            curr_signal = recent_data['Signal'].iloc[i]
            
            if prev_macd <= prev_signal and curr_macd > curr_signal:
                crossovers.append({
                    'type': 'bullish',
                    'datetime': recent_data.index[i],
                    'price': recent_data['close'].iloc[i],
                    'macd': curr_macd,
                    'signal': curr_signal
                })
            elif prev_macd >= prev_signal and curr_macd < curr_signal:
                crossovers.append({
                    'type': 'bearish',
                    'datetime': recent_data.index[i],
                    'price': recent_data['close'].iloc[i],
                    'macd': curr_macd,
                    'signal': curr_signal
                })
        
        # Check zero line crossovers
        zero_crossovers = []
        for i in range(1, len(recent_data)):
            prev_macd = recent_data['MACD'].iloc[i-1]
            curr_macd = recent_data['MACD'].iloc[i]
            
            if prev_macd <= 0 and curr_macd > 0:
                zero_crossovers.append({
                    'type': 'bullish_zero',
                    'datetime': recent_data.index[i],
                    'price': recent_data['close'].iloc[i],
                    'macd': curr_macd
                })
            elif prev_macd >= 0 and curr_macd < 0:
                zero_crossovers.append({
                    'type': 'bearish_zero',
                    'datetime': recent_data.index[i],
                    'price': recent_data['close'].iloc[i],
                    'macd': curr_macd
                })
        
        return {
            'signal_crossovers': crossovers,
            'zero_crossovers': zero_crossovers,
            'latest_values': {
                'datetime': recent_data.index[-1],
                'price': recent_data['close'].iloc[-1],
                'macd': recent_data['MACD'].iloc[-1],
                'signal': recent_data['Signal'].iloc[-1],
                'histogram': recent_data['Histogram'].iloc[-1]
            }
        }
    
    def plot_macd(self, days_to_show=30, save_path=None):
        """
        Plot MACD indicator with price data
        
        Args:
            days_to_show (int): Number of recent days to display
            save_path (str): Path to save the plot (optional)
        """
        if 'MACD' not in self.data.columns:
            self.calculate_macd()
        
        # Filter data to recent days
        end_date = self.data.index[-1]
        start_date = end_date - pd.Timedelta(days=days_to_show)
        plot_data = self.data[self.data.index >= start_date].copy()
        
        # Create figure with subplots
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(15, 10), 
                                       gridspec_kw={'height_ratios': [2, 1]})
        
        # Plot 1: Price with EMAs
        ax1.plot(plot_data.index, plot_data['close'], label='SPY Close', color='black', linewidth=1.5)
        ax1.plot(plot_data.index, plot_data['EMA_fast'], label=f'EMA {self.fast_period}', color='blue', alpha=0.7)
        ax1.plot(plot_data.index, plot_data['EMA_slow'], label=f'EMA {self.slow_period}', color='red', alpha=0.7)
        
        ax1.set_title(f'SPY Price with EMAs (Last {days_to_show} days)', fontsize=14, fontweight='bold')
        ax1.set_ylabel('Price ($)', fontsize=12)
        ax1.legend(loc='upper left')
        ax1.grid(True, alpha=0.3)
        
        # Plot 2: MACD
        ax2.plot(plot_data.index, plot_data['MACD'], label='MACD Line', color='blue', linewidth=2)
        ax2.plot(plot_data.index, plot_data['Signal'], label='Signal Line', color='red', linewidth=2)
        
        # Histogram
        colors = ['green' if x >= 0 else 'red' for x in plot_data['Histogram']]
        ax2.bar(plot_data.index, plot_data['Histogram'], label='Histogram', 
                color=colors, alpha=0.6, width=pd.Timedelta(hours=2))
        
        # Zero line
        ax2.axhline(y=0, color='black', linestyle='-', alpha=0.5)
        
        ax2.set_title(f'MACD Indicator ({self.fast_period}, {self.slow_period}, {self.signal_period})', 
                      fontsize=14, fontweight='bold')
        ax2.set_ylabel('MACD', fontsize=12)
        ax2.set_xlabel('Date', fontsize=12)
        ax2.legend(loc='upper left')
        ax2.grid(True, alpha=0.3)
        
        # Format x-axis
        for ax in [ax1, ax2]:
            ax.xaxis.set_major_formatter(mdates.DateFormatter('%m/%d'))
            ax.xaxis.set_major_locator(mdates.DayLocator(interval=max(1, days_to_show//10)))
            plt.setp(ax.xaxis.get_majorticklabels(), rotation=45)
        
        plt.tight_layout()
        
        # Save plot if path provided
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"Plot saved to: {save_path}")
        
        plt.show()
    
    def generate_summary(self):
        """
        Generate a summary of current MACD status
        
        Returns:
            str: Formatted summary
        """
        if 'MACD' not in self.data.columns:
            self.calculate_macd()
        
        crossovers = self.detect_crossovers(lookback_periods=10)
        latest = crossovers['latest_values']
        
        summary = f"""
MACD Indicator Summary - SPY
============================
Parameters: Fast EMA({self.fast_period}), Slow EMA({self.slow_period}), Signal({self.signal_period})

Latest Values ({latest['datetime'].strftime('%Y-%m-%d %H:%M')}):
├─ Price: ${latest['price']:.2f}
├─ MACD: {latest['macd']:.4f}
├─ Signal: {latest['signal']:.4f}
└─ Histogram: {latest['histogram']:.4f}

Current Status:
├─ MACD vs Signal: {'BULLISH' if latest['macd'] > latest['signal'] else 'BEARISH'}
├─ MACD vs Zero: {'POSITIVE' if latest['macd'] > 0 else 'NEGATIVE'}
└─ Trend: {'UPWARD' if latest['histogram'] > 0 else 'DOWNWARD'} Momentum

Recent Crossovers (Last 10 periods):
"""
        
        # Add signal crossovers
        if crossovers['signal_crossovers']:
            for cross in crossovers['signal_crossovers']:
                summary += f"├─ {cross['type'].upper()}: {cross['datetime'].strftime('%m/%d %H:%M')} @ ${cross['price']:.2f}\n"
        else:
            summary += "├─ No recent signal crossovers\n"
        
        # Add zero crossovers
        if crossovers['zero_crossovers']:
            for cross in crossovers['zero_crossovers']:
                summary += f"└─ {cross['type'].upper()}: {cross['datetime'].strftime('%m/%d %H:%M')} @ ${cross['price']:.2f}\n"
        else:
            summary += "└─ No recent zero line crossovers\n"
        
        return summary


def main():
    """
    Main function to demonstrate MACD indicator
    """
    # Initialize MACD indicator
    macd = MACDIndicator(fast_period=12, slow_period=26, signal_period=9)
    
    # Load the most recent CSV data
    csv_path = '../historical_data/spy_5min_merged_complete_20250611.csv'
    
    try:
        # Load data
        macd.load_csv_data(csv_path)
        
        # Calculate MACD
        macd_components = macd.calculate_macd()
        
        # Generate summary
        summary = macd.generate_summary()
        print(summary)
        
        # Plot MACD (last 30 days)
        plot_save_path = 'macd_analysis_spy.png'
        macd.plot_macd(days_to_show=30, save_path=plot_save_path)
        
        # Detect and print recent crossovers
        crossovers = macd.detect_crossovers(lookback_periods=5)
        
        print("\nRecent Crossover Analysis:")
        print("=" * 50)
        
        if crossovers['signal_crossovers']:
            print("Signal Line Crossovers:")
            for cross in crossovers['signal_crossovers']:
                print(f"  {cross['type'].upper()}: {cross['datetime']} @ ${cross['price']:.2f}")
        
        if crossovers['zero_crossovers']:
            print("Zero Line Crossovers:")
            for cross in crossovers['zero_crossovers']:
                print(f"  {cross['type'].upper()}: {cross['datetime']} @ ${cross['price']:.2f}")
        
        if not crossovers['signal_crossovers'] and not crossovers['zero_crossovers']:
            print("No recent crossovers detected.")
            
    except Exception as e:
        print(f"Error: {e}")
        print("Make sure the CSV file exists and has the correct format.")


if __name__ == "__main__":
    main()
