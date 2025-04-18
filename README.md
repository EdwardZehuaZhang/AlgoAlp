# AlgoAlp

A Python implementation of a scalping trading strategy for Alpaca Markets.

## Overview
This project converts a TradingView Pine Script strategy to Python using Alpaca API for automated trading. The strategy uses multiple moving averages, RSI, and MACD indicators along with trend filtering to execute trades with small profit targets.

## Features
- Multi-timeframe analysis (1-hour trend filtering)
- Technical indicators (SMA, RSI, MACD)
- Small profit target scalping strategy
- Paper trading implementation
- Real-time market data processing
- Risk management with dynamic position sizing
- Performance monitoring and reporting

## Enhanced for Real Market Trading
- Volume-based trading filters
- Slippage handling with configurable buffer
- Dynamic position sizing based on account equity
- API rate limit handling with exponential backoff
- Stale order management
- Consecutive loss tracking
- Detailed performance metrics and visualization

## Quick Start

The easiest way to get started is to use the interactive menu:

```bash
python run.py
```

This will give you a user-friendly interface to:
- Run the trading strategy
- Visualize indicators
- Generate performance reports
- Check your API connection
- Edit configuration
- Set up your environment

## Setup
1. Create an Alpaca Markets account
2. Get your API keys
3. Install required packages with `python setup.py`
4. Edit your configuration in `config.py`
5. Run the strategy with `python strategy.py`

## Monitoring Performance
Track your strategy's performance with:
```bash
python monitor.py
```
This will generate detailed performance statistics and visualizations.

## Usage
```bash
python strategy.py  # Run the main strategy
python visualize.py # Visualize indicators and signals
python monitor.py   # Generate performance reports
```

## Disclaimer
This is for educational purposes only. Trading involves risk of financial loss. Past performance is not indicative of future results. 