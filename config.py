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