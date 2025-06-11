"""
Setup script for AlgoAlp trading application
"""
import os
import subprocess
import sys
import platform
from setuptools import setup, find_packages

# Check Python version
if sys.version_info < (3, 7):
    print("AlgoAlp requires Python 3.7 or higher")
    sys.exit(1)

# Requirements
requirements = [
    "flask>=2.0.0",
    "gunicorn>=20.1.0",
    "alpaca-trade-api>=2.1.0",
    "python-dotenv>=0.19.0",
    "requests>=2.26.0",
    "pandas>=1.3.0",
    "numpy>=1.20.0",
    "matplotlib>=3.4.0",
    "mplfinance>=0.12.7a17"
]

# Setup basic configuration
setup(
    name="AlgoAlp",
    version="0.1.0",
    description="Automated trading system using TradingView alerts with Alpaca Markets",
    author="AlgoAlp",
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">=3.7",
)

# Create .env file if it doesn't exist
if not os.path.exists('.env'):
    print("Creating .env file...")
    with open('.env', 'w') as f:
        f.write("""# AlgoAlp Environment Variables

# Alpaca API Credentials
ALPACA_API_KEY=your_api_key_here
ALPACA_API_SECRET=your_api_secret_here
ALPACA_BASE_URL=https://paper-api.alpaca.markets

# Webhook Security
WEBHOOK_PASSPHRASE=your_secure_passphrase

# Discord Integration (Optional)
DISCORD_WEBHOOK_URL=your_discord_webhook_url_here
""")
    print("Please edit the .env file with your API keys and preferences")

# Create directories for data and charts
os.makedirs('charts', exist_ok=True)
print("Created charts directory for saving visualizations")

# Check if ngrok is installed (optional)
try:
    subprocess.check_call(['ngrok', '--version'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("ngrok is installed")
except:
    if platform.system() == 'Windows':
        print("To use ngrok for local webhook testing, download it from: https://ngrok.com/download")
    else:
        print("To install ngrok for local webhook testing:")
        print("  brew install ngrok (on macOS)")
        print("  or download from: https://ngrok.com/download")

print("\nSetup complete! You can now start the webhook server with: python webhook_server.py")