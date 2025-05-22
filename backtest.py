"""
Backtesting module for AlgoAlp - tests the strategy on historical data
"""

import os
import sys
import argparse
import datetime
import logging
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
from dotenv import load_dotenv
import time

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# API Keys
POLYGON_API_KEY = os.getenv("POLYGON_API_KEY", "qdB8qbiJQcVUwqF3SqXxHJKVIABG4Saf")

class Backtest:
    def __init__(self, symbol, start_date, end_date, initial_capital, position_size):
        self.symbol = symbol
        self.start_date = start_date
        self.end_date = end_date
        self.initial_capital = initial_capital
        self.position_size = position_size
        self.data = None
        self.signals = pd.DataFrame()
        self.portfolio = pd.DataFrame()
        self.data_source = "Unknown"  # Track which data source was used
        self.timeframe = "Unknown"    # Track which timeframe was used
        
    def fetch_data(self, data_source='polygon'):
        """Fetch historical data with fallback options"""
        # Format dates properly for API calls (YYYY-MM-DD)
        start_str = self.start_date.strftime('%Y-%m-%d')
        end_str = self.end_date.strftime('%Y-%m-%d')
        
        logger.info(f"Backtesting period: {start_str} to {end_str}")
        
        # Adding buffer days for EMA calculation
        buffer_start = self.start_date - datetime.timedelta(days=30)
        buffer_start_str = buffer_start.strftime('%Y-%m-%d')
        
        if data_source == 'polygon':
            if self.fetch_polygon_data(buffer_start_str, end_str):
                return True
        
        # Try Yahoo Finance as a fallback
        if self.fetch_yahoo_data(buffer_start_str, end_str):
            return True
            
        logger.error("Could not retrieve data from any source. Please check your API keys and dates.")
        return False
        
    def fetch_polygon_data(self, start_date, end_date):
        """Fetch historical data from Polygon.io API"""
        # Try different timeframes
        timeframes = ["minute", "hour", "day"]
        multipliers = [5, 1, 1]  # 5-min, 1-hour, 1-day
        
        for i, timeframe in enumerate(timeframes):
            multiplier = multipliers[i]
            
            try:
                logger.info(f"Fetching {multiplier}-{timeframe} data for {self.symbol} from {start_date} to {end_date}")
                
                # Format the URL for Polygon.io API
                url = f"https://api.polygon.io/v2/aggs/ticker/{self.symbol}/range/{multiplier}/{timeframe}/{start_date}/{end_date}"
                
                # Request parameters
                params = {
                    'adjusted': 'true',
                    'sort': 'asc',
                    'limit': 50000,
                    'apiKey': POLYGON_API_KEY
                }
                
                # Make the API request
                response = requests.get(url, params=params)
                
                # Check if request was successful
                if response.status_code == 200:
                    data = response.json()
                    
                    # Check if we have results
                    if data['resultsCount'] > 0:
                        # Convert to pandas DataFrame
                        df = pd.DataFrame(data['results'])
                        
                        # Rename columns to match expected format
                        df.rename(columns={
                            'o': 'open',
                            'h': 'high',
                            'l': 'low',
                            'c': 'close',
                            'v': 'volume',
                            't': 'timestamp'
                        }, inplace=True)
                        
                        # Convert timestamp from milliseconds to datetime
                        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
                        
                        # Set timestamp as index
                        df.set_index('timestamp', inplace=True)
                        
                        # Keep only necessary columns
                        df = df[['open', 'high', 'low', 'close', 'volume']]
                        
                        logger.info(f"Successfully retrieved {len(df)} {multiplier}-{timeframe} bars from Polygon.io")
                        
                        self.data = df
                        self.data_source = "Polygon.io"
                        self.timeframe = f"{multiplier}-{timeframe}"
                        return True
                    else:
                        logger.warning(f"No data available for {self.symbol} in the specified period with {multiplier}-{timeframe} timeframe")
                else:
                    logger.error(f"Failed to get data from Polygon.io: {response.status_code} - {response.text}")
                    
                    # If rate limit is hit, wait and try again
                    if response.status_code == 429:
                        logger.info("Rate limit hit, waiting 60 seconds before trying again...")
                        time.sleep(60)
                        return self.fetch_polygon_data(start_date, end_date)
            
            except Exception as e:
                logger.error(f"Error fetching data from Polygon.io: {str(e)}")
        
        logger.warning("Could not retrieve data from Polygon.io with any timeframe")
        return False
        
    def fetch_yahoo_data(self, start_date, end_date):
        """Fetch historical data from Yahoo Finance"""
        try:
            logger.info(f"Trying to fetch data from Yahoo Finance for {self.symbol}")
            
            # Install yfinance if not present
            try:
                import yfinance as yf
            except ImportError:
                logger.info("Installing yfinance package...")
                import subprocess
                subprocess.check_call([sys.executable, "-m", "pip", "install", "yfinance"])
                import yfinance as yf
            
            # Try to get data with different intervals
            intervals = ["1h", "1d"]
            
            for interval in intervals:
                try:
                    logger.info(f"Fetching {interval} data from Yahoo Finance")
                    
                    data = yf.download(
                        self.symbol,
                        start=start_date,
                        end=end_date,
                        interval=interval,
                        progress=False
                    )
                    
                    if not data.empty:
                        # Rename columns to match expected format
                        data.rename(columns={
                            'Open': 'open',
                            'High': 'high',
                            'Low': 'low',
                            'Close': 'close',
                            'Volume': 'volume'
                        }, inplace=True)
                        
                        # Use only required columns
                        self.data = data[['open', 'high', 'low', 'close', 'volume']]
                        self.data_source = "Yahoo Finance"
                        self.timeframe = interval
                        
                        logger.info(f"Successfully retrieved {len(self.data)} bars from Yahoo Finance")
                        return True
                except Exception as e:
                    logger.error(f"Error fetching {interval} data from Yahoo Finance: {e}")
            
            logger.warning("Could not retrieve data from Yahoo Finance with any interval")
            return False
            
        except Exception as e:
            logger.error(f"Failed to use Yahoo Finance: {e}")
            return False

    def clean_market_data(self):
        """Remove non-market hours and weekends from the data"""
        if self.data is None or self.data.empty:
            return False
            
        logger.info(f"Cleaning data: removing weekends and non-market hours")
        df = self.data.copy()
        
        # Filter out weekends (0=Monday, 6=Sunday)
        df = df[df.index.dayofweek < 5]
        
        # For intraday data, keep only market hours (9:30 AM - 4:00 PM ET)
        if self.timeframe.lower() not in ['day', '1day', '1d']:
            df = df[(df.index.time >= datetime.time(9, 30)) & 
                   (df.index.time <= datetime.time(16, 0))]
        
        if df.empty:
            logger.warning("No data left after filtering for market hours")
            return False
            
        logger.info(f"Data cleaned: {len(df)} bars remaining after filtering")
        self.data = df
        return True

    def calculate_indicators(self):
        """Calculate technical indicators for the strategy"""
        if self.data is None or self.data.empty:
            logger.error("No data available to calculate indicators")
            return False
        
        # First clean the data to remove weekends and non-market hours
        if not self.clean_market_data():
            logger.warning("Could not clean market data, proceeding with raw data")
        
        df = self.data.copy()
        
        logger.info(f"Calculating indicators on {len(df)} bars of {self.timeframe} data")
        
        # Calculate EMA indicators
        df['ema9'] = df['close'].ewm(span=9, adjust=False).mean()
        df['ema21'] = df['close'].ewm(span=21, adjust=False).mean()
        df['ema50'] = df['close'].ewm(span=50, adjust=False).mean()
        df['ema200'] = df['close'].ewm(span=200, adjust=False).mean()
        
        # Calculate MACD
        df['macd'] = df['close'].ewm(span=12, adjust=False).mean() - df['close'].ewm(span=26, adjust=False).mean()
        df['macd_signal'] = df['macd'].ewm(span=9, adjust=False).mean()
        df['macd_hist'] = df['macd'] - df['macd_signal']
        
        # Calculate RSI
        delta = df['close'].diff()
        gain = delta.clip(lower=0)
        loss = -delta.clip(upper=0)
        avg_gain = gain.rolling(window=14).mean()
        avg_loss = loss.rolling(window=14).mean()
        
        # Handle division by zero
        rs = avg_gain / avg_loss.replace(0, np.finfo(float).eps)
        df['rsi'] = 100 - (100 / (1 + rs))
        
        # Filter data to start_date since we added buffer for calculations
        # Convert start_date to pandas Timestamp for proper comparison
        start_ts = pd.Timestamp(self.start_date.strftime('%Y-%m-%d'))
        df = df[df.index >= start_ts]
        
        # Drop any NaN values that might have been created
        df = df.dropna()
        
        if df.empty:
            logger.error("Not enough data points after calculating indicators")
            return False
            
        logger.info(f"Successfully calculated indicators. {len(df)} data points available for backtesting.")
        self.data = df
        return True
    
    def generate_signals(self):
        """Generate buy/sell signals"""
        if self.data is None or self.data.empty:
            logger.error("No data available to generate signals")
            return False
            
        df = self.data.copy()
        
        # Initialize signal columns
        df['signal'] = 0  # 1 for buy, -1 for sell, 0 for hold
        df['position'] = 0
        
        # Generate signals based on EMA crossovers and MACD
        for i in range(1, len(df)):
            # Buy conditions
            ema_cross_up = (df['ema9'].iloc[i-1] < df['ema21'].iloc[i-1]) and (df['ema9'].iloc[i] > df['ema21'].iloc[i])
            ema_trend_up = df['ema50'].iloc[i] > df['ema200'].iloc[i]
            macd_cross_up = (df['macd_hist'].iloc[i-1] < 0) and (df['macd_hist'].iloc[i] > 0)
            rsi_not_overbought = df['rsi'].iloc[i] < 70
            
            # Sell conditions
            ema_cross_down = (df['ema9'].iloc[i-1] > df['ema21'].iloc[i-1]) and (df['ema9'].iloc[i] < df['ema21'].iloc[i])
            macd_cross_down = (df['macd_hist'].iloc[i-1] > 0) and (df['macd_hist'].iloc[i] < 0)
            rsi_overbought = df['rsi'].iloc[i] > 70
            
            # Combined conditions
            if ema_cross_up and ema_trend_up and (macd_cross_up or df['macd_hist'].iloc[i] > 0) and rsi_not_overbought:
                df.loc[df.index[i], 'signal'] = 1
            elif (ema_cross_down or macd_cross_down or rsi_overbought) and df['position'].iloc[i-1] > 0:
                df.loc[df.index[i], 'signal'] = -1
            
            # Update position
            if df['signal'].iloc[i] == 1:  # Buy signal
                df.loc[df.index[i], 'position'] = 1
            elif df['signal'].iloc[i] == -1:  # Sell signal
                df.loc[df.index[i], 'position'] = 0
            else:  # Hold previous position
                df.loc[df.index[i], 'position'] = df['position'].iloc[i-1]
        
        self.signals = df
        logger.info(f"Generated signals: {len(df[df['signal'] == 1])} buy signals, {len(df[df['signal'] == -1])} sell signals")
        return True
        
    def backtest_strategy(self):
        """Run the backtest simulation"""
        if self.signals.empty:
            logger.error("No signals generated for backtesting")
            return False
            
        # Create portfolio dataframe
        portfolio = self.signals[['close']].copy()
        portfolio['signal'] = self.signals['signal']
        portfolio['position'] = self.signals['position']
        
        # Initialize portfolio metrics
        portfolio['holdings'] = portfolio['position'] * self.position_size * portfolio['close']
        portfolio['cash'] = self.initial_capital
        
        # Track trades
        trades = []
        shares_held = 0
        
        # Simulate trading
        for i in range(1, len(portfolio)):
            # Update cash based on previous position
            portfolio.loc[portfolio.index[i], 'cash'] = portfolio['cash'].iloc[i-1]
            
            # Buy
            if portfolio['signal'].iloc[i] == 1 and shares_held == 0:
                shares_to_buy = self.position_size
                cost = shares_to_buy * portfolio['close'].iloc[i]
                
                if cost <= portfolio['cash'].iloc[i]:
                    portfolio.loc[portfolio.index[i], 'cash'] -= cost
                    shares_held = shares_to_buy
                    
                    trades.append({
                        'date': portfolio.index[i],
                        'type': 'BUY',
                        'price': portfolio['close'].iloc[i],
                        'shares': shares_to_buy,
                        'value': cost
                    })
                    logger.debug(f"BUY: {shares_to_buy} shares at ${portfolio['close'].iloc[i]:.2f}")
            
            # Sell
            elif portfolio['signal'].iloc[i] == -1 and shares_held > 0:
                proceeds = shares_held * portfolio['close'].iloc[i]
                portfolio.loc[portfolio.index[i], 'cash'] += proceeds
                
                trades.append({
                    'date': portfolio.index[i],
                    'type': 'SELL',
                    'price': portfolio['close'].iloc[i],
                    'shares': shares_held,
                    'value': proceeds
                })
                logger.debug(f"SELL: {shares_held} shares at ${portfolio['close'].iloc[i]:.2f}")
                
                shares_held = 0
            
            # Update holdings value
            portfolio.loc[portfolio.index[i], 'holdings'] = shares_held * portfolio['close'].iloc[i]
        
        # Calculate total portfolio value
        portfolio['total'] = portfolio['cash'] + portfolio['holdings']
        
        # Calculate daily returns
        portfolio['returns'] = portfolio['total'].pct_change()
        
        self.portfolio = portfolio
        self.trades = trades
        
        logger.info(f"Backtest complete: {len(trades)} trades executed")
        return True
        
    def calculate_performance(self):
        """Calculate performance metrics"""
        if self.portfolio.empty:
            logger.error("No portfolio data to calculate performance")
            return None
            
        # Calculate metrics
        total_days = (self.portfolio.index[-1] - self.portfolio.index[0]).days
        if total_days == 0:  # Avoid division by zero for intraday tests
            total_days = 1
        
        # Starting and ending portfolio value
        start_value = self.portfolio['total'].iloc[0]
        end_value = self.portfolio['total'].iloc[-1]
        
        # Total return
        total_return = (end_value - start_value) / start_value * 100
        
        # Annualized return
        annual_return = ((1 + total_return/100) ** (365/total_days) - 1) * 100
        
        # Daily returns
        daily_returns = self.portfolio['returns'].dropna()
        
        # Standard deviation of returns
        std_dev = daily_returns.std() * (252 ** 0.5) * 100  # Annualized
        
        # Maximum drawdown
        cumulative_returns = (1 + daily_returns).cumprod()
        running_max = cumulative_returns.cummax()
        drawdowns = (cumulative_returns / running_max - 1) * 100
        max_drawdown = drawdowns.min()
        
        # Sharpe ratio (assuming risk-free rate of 0%)
        sharpe = annual_return / std_dev if std_dev > 0 else 0
        
        # Win rate
        trades_df = pd.DataFrame(self.trades)
        if len(trades_df) > 0 and 'type' in trades_df.columns:
            buy_trades = trades_df[trades_df['type'] == 'BUY'].copy()
            sell_trades = trades_df[trades_df['type'] == 'SELL'].copy()
            
            if len(buy_trades) > 0 and len(sell_trades) > 0:
                # Pair trades and calculate profit/loss
                buy_trades.reset_index(drop=True, inplace=True)
                sell_trades.reset_index(drop=True, inplace=True)
                
                # Make sure we have equal number of buys and sells
                min_trades = min(len(buy_trades), len(sell_trades))
                buy_trades = buy_trades.iloc[:min_trades]
                sell_trades = sell_trades.iloc[:min_trades]
                
                # Calculate profit/loss per trade
                profits = (sell_trades['price'] * sell_trades['shares']) - (buy_trades['price'] * buy_trades['shares'])
                winning_trades = len(profits[profits > 0])
                win_rate = winning_trades / len(profits) * 100 if len(profits) > 0 else 0
            else:
                win_rate = 0
        else:
            win_rate = 0
        
        # Number of trades
        num_trades = len(trades_df) // 2  # Buy-sell pairs
        
        return {
            'start_date': self.portfolio.index[0],
            'end_date': self.portfolio.index[-1], 
            'total_days': total_days,
            'start_value': start_value,
            'end_value': end_value,
            'total_return_pct': total_return,
            'annual_return_pct': annual_return,
            'max_drawdown_pct': max_drawdown,
            'volatility_pct': std_dev,
            'sharpe_ratio': sharpe,
            'num_trades': num_trades,
            'win_rate_pct': win_rate,
            'data_source': self.data_source,
            'timeframe': self.timeframe,
            'data_points': len(self.data)
        }
    
    def plot_results(self):
        """Generate performance charts"""
        if self.portfolio.empty:
            logger.error("No portfolio data to plot")
            return False
        
        try:
            plt.figure(figsize=(14, 10))
            
            # Plot 1: Portfolio Value
            plt.subplot(3, 1, 1)
            
            # Instead of connecting all points, resample to business days
            portfolio_daily = self.portfolio['total'].resample('B').last()
            # Fill missing values with the previous value
            portfolio_daily = portfolio_daily.fillna(method='ffill')
            plt.plot(portfolio_daily.index, portfolio_daily.values)
            
            plt.title('Portfolio Value Over Time')
            plt.ylabel('Portfolio Value ($)')
            plt.grid(True)
            
            # Plot 2: Price with Buy/Sell signals
            plt.subplot(3, 1, 2)
            
            # Resample price data to business days for better visualization
            if self.timeframe.lower() not in ['day', '1day', '1d'] and len(self.signals) > 100:
                # For intraday data, resample to daily for cleaner charts
                price_resampled = self.signals['close'].resample('B').last().fillna(method='ffill')
                plt.plot(price_resampled.index, price_resampled.values, 'b-')
            else:
                # For daily data or shorter timeframes, use the original data
                # but connect only trading days
                price_data = self.signals['close']
                business_days = price_data.index.to_series().dt.dayofweek < 5
                trading_days_price = price_data[business_days]
                
                plt.plot(trading_days_price.index, trading_days_price.values, 'b-')
            
            # Plot buy signals
            buy_signals = self.signals[self.signals['signal'] == 1]
            if not buy_signals.empty:
                plt.scatter(buy_signals.index, buy_signals['close'], color='green', marker='^', s=100, label='Buy')
            
            # Plot sell signals
            sell_signals = self.signals[self.signals['signal'] == -1]
            if not sell_signals.empty:
                plt.scatter(sell_signals.index, sell_signals['close'], color='red', marker='v', s=100, label='Sell')
            
            plt.title(f'{self.symbol} Price with Signals')
            plt.ylabel('Price ($)')
            plt.legend()
            plt.grid(True)
            
            # Plot 3: Drawdown
            plt.subplot(3, 1, 3)
            
            # Calculate drawdown on business day resampled data for smoother chart
            daily_returns = portfolio_daily.pct_change().dropna()
            cumulative_returns = (1 + daily_returns).cumprod()
            running_max = cumulative_returns.cummax()
            drawdowns = (cumulative_returns / running_max - 1) * 100
            
            plt.fill_between(drawdowns.index, drawdowns.values, 0, color='red', alpha=0.3)
            plt.title('Portfolio Drawdown')
            plt.ylabel('Drawdown (%)')
            plt.grid(True)
            
            # Add x-axis formatting to all subplots to better display dates
            for i in range(1, 4):
                plt.subplot(3, 1, i)
                ax = plt.gca()
                # Set major ticks to display only business days
                ax.xaxis.set_major_locator(plt.MaxNLocator(10))
                # Format the date labels
                plt.gcf().autofmt_xdate()
                
                # Add date formatter
                from matplotlib.dates import DateFormatter
                date_format = DateFormatter('%Y-%m-%d')
                ax.xaxis.set_major_formatter(date_format)
            
            plt.tight_layout()
            
            # Save figure
            filename = f'backtest_{self.symbol}_{self.start_date.strftime("%Y%m%d")}_{self.end_date.strftime("%Y%m%d")}.png'
            plt.savefig(filename)
            logger.info(f"Results chart saved as {filename}")
            
            # Show figure
            plt.show()
            return True
            
        except Exception as e:
            logger.error(f"Error generating plots: {e}")
            logger.exception("Plot generation failed with traceback:")
            return False
        
    def print_performance(self, metrics):
        """Print performance summary"""
        if not metrics:
            return
            
        print("\n" + "="*50)
        print(f"BACKTEST RESULTS: {self.symbol}")
        print("="*50)
        print(f"Period: {metrics['start_date'].date()} to {metrics['end_date'].date()} ({metrics['total_days']} days)")
        print(f"Starting Capital: ${metrics['start_value']:.2f}")
        print(f"Ending Capital: ${metrics['end_value']:.2f}")
        print(f"Total Return: {metrics['total_return_pct']:.2f}%")
        print(f"Annualized Return: {metrics['annual_return_pct']:.2f}%")
        print(f"Max Drawdown: {metrics['max_drawdown_pct']:.2f}%")
        print(f"Volatility (annualized): {metrics['volatility_pct']:.2f}%")
        print(f"Sharpe Ratio: {metrics['sharpe_ratio']:.2f}")
        print(f"Number of Trades: {metrics['num_trades']}")
        print(f"Win Rate: {metrics['win_rate_pct']:.2f}%")
        print("-"*50)
        print(f"Data Source: {metrics['data_source']}")
        print(f"Timeframe: {metrics['timeframe']}")
        print(f"Data Points: {metrics['data_points']}")
        print("="*50)
        
    def run(self, data_source='polygon'):
        """Execute the full backtest"""
        logger.info(f"Starting backtest for {self.symbol}")
        
        if not self.fetch_data(data_source):
            logger.error("Failed to fetch historical data")
            return False
        
        if not self.calculate_indicators():
            logger.error("Failed to calculate indicators")
            return False
        
        if not self.generate_signals():
            logger.error("Failed to generate signals")
            return False
        
        if not self.backtest_strategy():
            logger.error("Failed to run backtest")
            return False
        
        metrics = self.calculate_performance()
        if metrics:
            self.print_performance(metrics)
            self.plot_results()
            return True
        else:
            logger.error("Failed to calculate performance metrics")
            return False


def parse_args():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(description='AlgoAlp Strategy Backtester')
    
    parser.add_argument('--symbol', type=str, required=True,
                        help='Symbol to backtest')
    
    # Either use days or start date
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--days', type=int, default=90,
                      help='Number of days to look back')
    group.add_argument('--start', type=str,
                      help='Start date (YYYY-MM-DD)')
    
    parser.add_argument('--end', type=str,
                      help='End date (YYYY-MM-DD)')
    parser.add_argument('--capital', type=float, default=10000,
                      help='Initial capital')
    parser.add_argument('--shares', type=float, default=10,
                      help='Number of shares per trade')
    
    # Add option for data source
    parser.add_argument('--source', type=str, choices=['polygon', 'yahoo'], default='polygon',
                      help='Data source (polygon or yahoo)')
    
    return parser.parse_args()


def main():
    """Main function"""
    args = parse_args()
    
    # Parse dates
    end_date = datetime.datetime.now()
    if args.end:
        try:
            end_date = datetime.datetime.strptime(args.end, '%Y-%m-%d')
        except ValueError:
            logger.error("Invalid end date format. Please use YYYY-MM-DD")
            sys.exit(1)
    
    if args.start:
        try:
            start_date = datetime.datetime.strptime(args.start, '%Y-%m-%d')
        except ValueError:
            logger.error("Invalid start date format. Please use YYYY-MM-DD")
            sys.exit(1)
    else:
        start_date = end_date - datetime.timedelta(days=args.days)
    
    # Install required packages if not present
    try:
        import importlib
        required_packages = ["yfinance", "requests"]
        for package in required_packages:
            try:
                importlib.import_module(package)
            except ImportError:
                logger.info(f"Installing required package: {package}")
                import subprocess
                subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    except Exception as e:
        logger.warning(f"Could not auto-install packages: {e}")
        logger.warning("If you encounter errors, manually install required packages with: pip install yfinance requests")
    
    # Create and run backtest
    backtest = Backtest(
        symbol=args.symbol,
        start_date=start_date,
        end_date=end_date,
        initial_capital=args.capital,
        position_size=args.shares
    )
    
    # Run backtest with specified data source
    backtest.run(args.source)


if __name__ == "__main__":
    main()
