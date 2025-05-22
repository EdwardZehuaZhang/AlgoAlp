# AlgoAlp Usage Guide

This guide will help you set up and run your AlgoAlp trading strategy with Alpaca.

## Setup Process

### 1. Create an Alpaca Account

1. Visit [Alpaca Markets](https://app.alpaca.markets/signup) to sign up
2. Choose "Paper Trading" for testing without risking real money
3. Navigate to the dashboard and click on your profile icon
4. Select "API Keys" to view your credentials

### 2. Configure Environment

1. Clone or download this repository to your local machine
2. Open the `.env` file in the repository
3. Update it with your Alpaca API keys:
   ```
   ALPACA_API_KEY=your_api_key_here
   ALPACA_API_SECRET=your_api_secret_here
   ALPACA_PAPER=True  # Keep as True for paper trading
   ```

### 3. Install Dependencies

Run the setup script to install all required packages:

```bash
python setup.py
```

This will:
- Check your Python version (3.7+ required)
- Install all dependencies from requirements.txt
- Verify your .env file exists

## Running the Strategy

### Initial Testing

1. Run the strategy in paper trading mode:
   ```bash
   python strategy.py
   ```

2. The strategy will:
   - Connect to Alpaca's paper trading API
   - Start monitoring SPY based on your configured indicators
   - Execute trades according to the strategy rules
   - Log all activities in the terminal and strategy.log file

### Backtesting Your Strategy

To evaluate how your strategy would have performed historically:

```bash
python backtest.py --symbol SPY --days 90 --capital 10000
```

Options:
- `--symbol`: The stock symbol to backtest (default: SPY)
- `--start`: Start date in YYYY-MM-DD format
- `--end`: End date in YYYY-MM-DD format
- `--days`: Number of days to look back if no start date (default: 90)
- `--capital`: Initial capital for the backtest (default: 10000)
- `--shares`: Position size in shares (default: from config)
- `--source`: Data source to use (default: polygon)

You can also run a backtest through the interactive menu:

```bash
python run.py
```

Then select option 9 for backtesting.

The backtest will:
- Retrieve historical data for the specified period
- Apply the same strategy logic as the live trading
- Generate detailed performance metrics
- Create visualization charts of trades and equity curve

### Market Data Considerations

AlgoAlp works with free Alpaca accounts by defaulting to:
- IEX exchange data instead of SIP (consolidated) data
- Alternative data sources like Polygon.io when needed
- Yahoo Finance as a fallback option for backtests

Note that without an Alpaca premium subscription:
- Only IEX exchange data is available for real-time data
- Historical data has some limitations
- The script handles these constraints automatically

### Visualizing Results

To see how your strategy is performing:

```bash
python visualize.py
```

This will:
- Generate charts showing price action, indicators, and signals
- Display a performance summary of your trading activity
- Save visualization images for later review

### Performance Monitoring

For detailed performance metrics:

```bash
python monitor.py
```

This will:
- Calculate key trading statistics (win rate, profit factor, etc.)
- Generate visual performance charts
- Show account balance and position information
- Track and report your trading history

## Customizing the Strategy

### Basic Configuration

Open `config.py` to adjust strategy parameters:

- Change the trading symbol (default is SPY)
- Adjust the quantity traded
- Modify technical indicator periods
- Change profit targets and stop loss levels

### Real Market Enhancements

The following settings are available for real-market trading:

```python
# Risk management 
RISK_PER_TRADE_PCT = 1.0  # Percentage of account to risk per trade
USE_DYNAMIC_POSITION_SIZING = False  # Enable for dynamic sizing
MAX_POSITION_SIZE = 5  # Maximum position size cap

# Real market condition parameters
SLIPPAGE_BUFFER = 0.01  # Buffer for slippage
MIN_VOLUME_THRESHOLD = 1000  # Minimum trading volume required
STALE_ORDER_MINUTES = 10  # Cancel orders older than this
MAX_CONSECUTIVE_LOSSES = 3  # Pause after consecutive losses
```

### Advanced Risk Management

The strategy includes several features to manage risk:

1. **Dynamic Position Sizing** - Automatically sizes positions based on your account equity and risk per trade percentage
2. **Volume Filtering** - Only trades when sufficient volume is present
3. **Consecutive Loss Tracking** - Temporarily pauses trading after a defined number of consecutive losses
4. **Stale Order Management** - Cancels orders that have been open too long
5. **API Rate Limit Handling** - Automatically handles API rate limits with exponential backoff

## Deployment Options

### Local Machine

- Keep the script running on your local computer
- Schedule it to run during market hours using your OS's task scheduler

### Cloud Deployment

For more reliable execution, consider:

- AWS Lightsail or EC2 instance
- Heroku free tier
- Google Cloud Platform

## Important Notes

- This is for educational purposes only
- Past performance does not guarantee future results
- Paper trading does not account for all real-world factors
- The 0.1% profit target strategy may not be profitable after all costs in real trading
- Even with our real market enhancements, always monitor the strategy regularly

## Troubleshooting

If you encounter issues:

1. Check the log files (strategy.log, monitor.log) for error messages
2. Verify your API keys are correct in the .env file
3. Ensure you have a stable internet connection
4. Confirm that the market is open during testing
5. Make sure your account has sufficient buying power
6. If you see "subscription does not permit" errors, the script will automatically fall back to IEX data

## Support

If you need additional help or want to report an issue:
1. Open an issue on GitHub
2. Check the Alpaca API documentation for specific API questions