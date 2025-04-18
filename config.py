"""
Configuration parameters for the scalping strategy
"""

# Trading parameters
SYMBOL = "SPY"  # Trading symbol
QUANTITY = 0.5  # Quantity to trade for testing

# Strategy parameters
ULTRAFAST_PERIOD = 20  # Ultrafast SMA period
FAST_PERIOD = 50  # Fast SMA period
SLOW_PERIOD = 200  # Slow SMA period
RSI_PERIOD = 14  # RSI period
RSI_OVERBOUGHT = 70  # RSI overbought level
RSI_OVERSOLD = 30  # RSI oversold level
MACD_FAST_LENGTH = 12  # MACD fast length
MACD_SLOW_LENGTH = 26  # MACD slow length
MACD_SIGNAL_SMOOTHING = 9  # MACD signal smoothing
LOOKBACK_WINDOW = 20  # Lookback window for composite signals

# Position management
PROFIT_TARGET = 0.001  # Profit target (0.1%)
STOP_LOSS = 0.001  # Stop loss (0.1%)

# Risk management 
RISK_PER_TRADE_PCT = 1.0  # Percentage of account to risk per trade (1%)
USE_DYNAMIC_POSITION_SIZING = False  # Set to True to enable dynamic position sizing
MAX_POSITION_SIZE = 5  # Maximum position size regardless of account equity

# Real market condition parameters
SLIPPAGE_BUFFER = 0.01  # Extra buffer for slippage in dollars
MIN_VOLUME_THRESHOLD = 1000  # Minimum volume required for trading
STALE_ORDER_MINUTES = 10  # Cancel orders older than this many minutes
MAX_CONSECUTIVE_LOSSES = 3  # Maximum consecutive losses before pausing trading
API_RATE_LIMIT_HANDLER = True  # Enable handling of API rate limits
CANCEL_ALL_ON_STARTUP = True  # Cancel all open orders on strategy startup 