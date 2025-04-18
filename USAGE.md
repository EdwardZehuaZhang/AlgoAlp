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

### Visualizing Results

To see how your strategy is performing:

```bash
python visualize.py
```

This will:
- Generate charts showing price action, indicators, and signals
- Display a performance summary of your trading activity
- Save visualization images for later review

## Customizing the Strategy

### Modify Parameters

Open `config.py` to adjust strategy parameters:

- Change the trading symbol (default is SPY)
- Adjust the quantity traded
- Modify technical indicator periods
- Change profit targets and stop loss levels

### Backtesting

While this implementation doesn't include full backtesting capabilities, you can:

1. Run the strategy for a short period in paper trading
2. Use the visualization tools to review performance
3. Adjust parameters and repeat

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
- Paper trading does not account for all real-world factors like slippage
- The 0.1% profit target strategy may not be profitable after all costs in real trading

## Troubleshooting

If you encounter issues:

1. Check the log file (strategy.log) for detailed error messages
2. Verify your API keys are correct in the .env file
3. Ensure you have a stable internet connection
4. Confirm that the market is open during testing 