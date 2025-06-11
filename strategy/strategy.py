"""
Main trading strategy implementation for AlgoAlp
"""

import os
import sys
import time
import logging
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import alpaca_trade_api as tradeapi
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# Initialize Alpaca API
API_KEY = os.getenv("ALPACA_API_KEY")
API_SECRET = os.getenv("ALPACA_API_SECRET")
PAPER = os.getenv("ALPACA_PAPER", "True").lower() in ("true", "1", "t")
BASE_URL = "https://paper-api.alpaca.markets" if PAPER else "https://api.alpaca.markets"

# Strategy configuration
SYMBOL = "SPY"
TIMEFRAME = "5Min"
QUANTITY = 0.5
MIN_VOLUME = 1000  # Minimum volume threshold for valid bars

class ScalpingStrategy:
    def __init__(self, symbol=SYMBOL, qty=QUANTITY):
        self.symbol = symbol
        self.qty = qty
        self.position = 0
        self.api = None
        self.initialize_api()
        self.last_trade_time = None
        
    def initialize_api(self):
        """Initialize connection to Alpaca API"""
        try:
            self.api = tradeapi.REST(API_KEY, API_SECRET, BASE_URL, api_version='v2')
            logger.info(f"Trading {self.symbol} with base quantity {self.qty}")
        except Exception as e:
            logger.error(f"Error initializing Alpaca API: {e}")
            sys.exit(1)
    
    def is_market_open(self):
        """Check if the market is open"""
        try:
            clock = self.api.get_clock()
            # Fix: Use is_open instead of open
            return clock.is_open  
        except Exception as e:
            logger.error(f"Error checking market times: {e}")
            # If we can't determine market status, assume market is open to continue trading
            return True
    
    def get_position(self):
        """Get current position"""
        try:
            positions = self.api.list_positions()
            for position in positions:
                if position.symbol == self.symbol:
                    self.position = float(position.qty)
                    return self.position
            self.position = 0
            return 0
        except Exception as e:
            if "no positions" in str(e).lower():
                self.position = 0
                return 0
            logger.error(f"Error getting position: {e}")
            return self.position
    
    def cancel_all_orders(self):
        """Cancel all open orders"""
        try:
            self.api.cancel_all_orders()
            logger.info("Canceled all open orders")
        except Exception as e:
            logger.error(f"Error canceling orders: {e}")
    
    def get_historical_data(self, timeframe, limit=100):
        """Get historical price data"""
        try:
            bars = self.api.get_bars(
                self.symbol, 
                timeframe,
                limit=limit,
                adjustment='raw'
            ).df
            
            if bars.empty:
                logger.warning(f"No {timeframe} data available for {self.symbol}")
                return None
                
            return bars
        except Exception as e:
            logger.error(f"Error getting {timeframe} historical data: {e}")
            return None
    
    def calculate_indicators(self, bars):
        """Calculate technical indicators"""
        if bars is None or bars.empty:
            return None
            
        # Add indicators
        bars['ema9'] = bars['close'].ewm(span=9, adjust=False).mean()
        bars['ema21'] = bars['close'].ewm(span=21, adjust=False).mean()
        bars['ema50'] = bars['close'].ewm(span=50, adjust=False).mean()
        
        # Calculate MACD
        bars['macd'] = bars['close'].ewm(span=12, adjust=False).mean() - bars['close'].ewm(span=26, adjust=False).mean()
        bars['macd_signal'] = bars['macd'].ewm(span=9, adjust=False).mean()
        bars['macd_hist'] = bars['macd'] - bars['macd_signal']
        
        # Calculate RSI
        delta = bars['close'].diff()
        gain = delta.clip(lower=0)
        loss = -delta.clip(upper=0)
        avg_gain = gain.rolling(window=14).mean()
        avg_loss = loss.rolling(window=14).mean()
        rs = avg_gain / avg_loss.replace(0, np.finfo(float).eps)
        bars['rsi'] = 100 - (100 / (1 + rs))
        
        return bars
    
    def check_entry_conditions(self, bars):
        """Check for buy conditions"""
        if bars is None or bars.empty or len(bars) < 50:
            return False
        
        last_bar = bars.iloc[-1]
        prev_bar = bars.iloc[-2]
        
        # Check volume
        if last_bar['volume'] < MIN_VOLUME:
            logger.info(f"Volume too low for trading: {last_bar['volume']} < {MIN_VOLUME}")
            return False
        
        # EMA crossover: 9 crosses above 21
        ema_cross_up = (prev_bar['ema9'] <= prev_bar['ema21']) and (last_bar['ema9'] > last_bar['ema21'])
        
        # Trend: 50 EMA is rising
        ema50_rising = last_bar['ema50'] > bars['ema50'].iloc[-5]
        
        # MACD: Histogram is positive or crossing above signal
        macd_positive = last_bar['macd_hist'] > 0
        macd_cross_up = (prev_bar['macd_hist'] <= 0) and (last_bar['macd_hist'] > 0)
        
        # RSI: Not overbought
        rsi_not_overbought = last_bar['rsi'] < 70
        
        # Combined entry condition
        entry_condition = (ema_cross_up or macd_cross_up) and ema50_rising and rsi_not_overbought
        
        if entry_condition:
            logger.info(f"Entry conditions met: EMA Cross: {ema_cross_up}, MACD: {macd_positive or macd_cross_up}, RSI: {rsi_not_overbought}")
        
        return entry_condition
    
    def check_exit_conditions(self, bars):
        """Check for sell conditions"""
        if bars is None or bars.empty or len(bars) < 50:
            return False
            
        last_bar = bars.iloc[-1]
        prev_bar = bars.iloc[-2]
        
        # EMA crossover: 9 crosses below 21
        ema_cross_down = (prev_bar['ema9'] >= prev_bar['ema21']) and (last_bar['ema9'] < last_bar['ema21'])
        
        # MACD: Histogram is negative or crossing below signal
        macd_negative = last_bar['macd_hist'] < 0
        macd_cross_down = (prev_bar['macd_hist'] >= 0) and (last_bar['macd_hist'] < 0)
        
        # RSI: Overbought
        rsi_overbought = last_bar['rsi'] > 70
        
        # Combined exit condition
        exit_condition = ema_cross_down or macd_cross_down or rsi_overbought
        
        if exit_condition:
            logger.info(f"Exit conditions met: EMA Cross Down: {ema_cross_down}, MACD Down: {macd_negative or macd_cross_down}, RSI Overbought: {rsi_overbought}")
        
        return exit_condition
    
    def check_trend(self):
        """Check longer-term trend using 1-hour timeframe"""
        try:
            # Get 1-hour data
            hour_bars = self.get_historical_data('1Hour', 100)
            
            if hour_bars is None or hour_bars.empty:
                return 0  # Neutral if no data
            
            # Calculate hourly EMAs
            hour_bars['ema50'] = hour_bars['close'].ewm(span=50, adjust=False).mean()
            hour_bars['ema200'] = hour_bars['close'].ewm(span=200, adjust=False).mean()
            
            # Check trend based on EMAs
            last_bar = hour_bars.iloc[-1]
            
            if last_bar['ema50'] > last_bar['ema200']:
                logger.info("1-hour trend state: 1")
                return 1  # Bullish trend
            elif last_bar['ema50'] < last_bar['ema200']:
                logger.info("1-hour trend state: -1")
                return -1  # Bearish trend
            else:
                logger.info("1-hour trend state: 0")
                return 0  # Neutral trend
                
        except Exception as e:
            logger.error(f"Error checking trend: {e}")
            return 0  # Default to neutral on error
    
    def submit_order(self, side, qty):
        """Submit order to Alpaca"""
        try:
            self.api.submit_order(
                symbol=self.symbol,
                qty=qty,
                side=side,
                type='market',
                time_in_force='day'
            )
            logger.info(f"Submitted {side} order for {qty} shares of {self.symbol}")
            self.last_trade_time = datetime.now()
            return True
        except Exception as e:
            logger.error(f"Error submitting {side} order: {e}")
            return False
    
    def run_strategy(self):
        """Main strategy execution loop"""
        logger.info(f"Running strategy for {self.symbol}")
        
        # Cancel any existing orders
        self.cancel_all_orders()
        
        # Check current position
        position = self.get_position()
        logger.info(f"Current position: {position} shares")
        
        # Check market trend
        trend = self.check_trend()
        
        # Only trade in bullish trend or neutral (not in bearish)
        if trend < 0:
            logger.info("Bearish trend detected, skipping trading cycle")
            return
        
        # Get latest 5-minute data
        bars = self.get_historical_data(TIMEFRAME)
        
        if bars is None or bars.empty:
            logger.warning("No data available, skipping trading cycle")
            return
            
        # Calculate indicators
        bars = self.calculate_indicators(bars)
        
        if bars is None:
            return
            
        # Trading logic
        if position <= 0:
            # Check for buy conditions
            if self.check_entry_conditions(bars):
                logger.info(f"Buy signal triggered for {self.symbol}")
                self.submit_order('buy', self.qty)
        else:
            # Check for sell conditions
            if self.check_exit_conditions(bars):
                logger.info(f"Sell signal triggered for {self.symbol}")
                self.submit_order('sell', position)
    
    def run(self):
        """Run the strategy once"""
        try:
            # Check if market is open
            if not self.is_market_open():
                logger.info("Market is closed, exiting strategy")
                return
                
            self.run_strategy()
            
        except KeyboardInterrupt:
            logger.info("Strategy stopped by user")
        except Exception as e:
            logger.error(f"Error running strategy: {e}")

def main():
    """Main function"""
    logger.info("Starting Simplified Scalping Strategy")
    
    strategy = ScalpingStrategy(SYMBOL, QUANTITY)
    strategy.run()

if __name__ == "__main__":
    main()