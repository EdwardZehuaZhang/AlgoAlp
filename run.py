"""
Runner script for AlgoAlp - provides a menu to run all components
"""
import os
import sys
import subprocess
import time
import importlib
import config

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    """Print the header banner"""
    clear_screen()
    print("\n" + "="*50)
    print("             ALGOALP TRADING SUITE")
    print("="*50)
    print("\nPython Scalping Strategy for Alpaca Markets")
    print("\n" + "-"*50)

def print_menu():
    """Print the main menu"""
    print("\nPlease select an option:")
    print("1. Run Trading Strategy")
    print("2. Visualize Strategy Indicators")
    print("3. Generate Performance Report")
    print("4. Check API Connection")
    print("5. Setup Environment")
    print("6. Initialize Git Repository")
    print("7. Edit Configuration")
    print("8. Position Sizing Settings")
    print("9. Run Strategy Backtest")
    print("10. Quit")
    return input("\nEnter your choice (1-10): ")

def run_strategy():
    """Run the main trading strategy"""
    print("\nStarting trading strategy...")
    try:
        subprocess.run([sys.executable, "strategy.py"])
    except KeyboardInterrupt:
        print("\nStrategy stopped by user.")
    input("\nPress Enter to return to the menu...")

def visualize_strategy():
    """Run the visualization tool"""
    print("\nGenerating strategy visualizations...")
    try:
        subprocess.run([sys.executable, "visualize.py"])
    except KeyboardInterrupt:
        print("\nVisualization stopped by user.")
    input("\nPress Enter to return to the menu...")

def generate_report():
    """Run the performance report generator"""
    print("\nGenerating performance report...")
    try:
        # Allow user to specify the number of days
        days = input("Enter number of days to analyze (default: 30): ")
        days = int(days) if days.strip() else 30
        
        if days <= 0:
            print("Invalid number of days. Using default (30).")
            days = 30
            
        subprocess.run([sys.executable, "monitor.py", str(days)])
    except KeyboardInterrupt:
        print("\nReport generation stopped by user.")
    except ValueError:
        print("Invalid input. Using default of 30 days.")
        subprocess.run([sys.executable, "monitor.py", "30"])
    
    input("\nPress Enter to return to the menu...")

def check_api():
    """Check the Alpaca API connection"""
    print("\nChecking Alpaca API connection...")
    
    # Simple script to check API connection
    check_script = """
import os
from dotenv import load_dotenv
from alpaca_trade_api.rest import REST
import sys
import datetime

# Load environment variables
load_dotenv()

# Initialize Alpaca API
API_KEY = os.getenv("ALPACA_API_KEY")
API_SECRET = os.getenv("ALPACA_API_SECRET")
PAPER = os.getenv("ALPACA_PAPER", "True").lower() in ("true", "1", "t")
BASE_URL = "https://paper-api.alpaca.markets" if PAPER else "https://api.alpaca.markets"

if not API_KEY or not API_SECRET:
    print("Error: API key or secret not found in .env file")
    sys.exit(1)

try:
    api = REST(API_KEY, API_SECRET, BASE_URL, api_version='v2')
    account = api.get_account()
    
    print("\\nAPI Connection Successful!")
    print(f"Account ID: {account.id}")
    print(f"Status: {account.status}")
    print(f"Equity: ${float(account.equity):.2f}")
    print(f"Cash: ${float(account.cash):.2f}")
    print(f"Buying Power: ${float(account.buying_power):.2f}")
    print(f"Paper Account: {PAPER}")
    
    # Check market status
    clock = api.get_clock()
    print(f"\\nMarket is {'OPEN' if clock.is_open else 'CLOSED'}")
    
    # Check SPY latest price using IEX feed
    try:
        spy = api.get_latest_trade("SPY", feed='iex')  # Explicitly use IEX feed
        print(f"SPY Latest Price (IEX): ${float(spy.price):.2f}")
    except Exception as e:
        if "subscription" in str(e).lower():
            print("Note: Using IEX feed as SIP requires subscription")
            try:
                # Try without specifying feed
                spy = api.get_latest_trade("SPY")
                print(f"SPY Latest Price: ${float(spy.price):.2f}")
            except:
                print("Could not retrieve latest price")
        else:
            print(f"Error getting latest trade: {e}")
    
    # Check data availability for historical bars
    try:
        print("\\nChecking historical data availability...")
        today = datetime.datetime.now()
        week_ago = (today - datetime.timedelta(days=7)).strftime('%Y-%m-%d')
        bars = api.get_bars("SPY", "1Day", start=week_ago, limit=5, feed='iex').df
        print(f"Successfully retrieved {len(bars)} days of historical data using IEX feed")
    except Exception as e:
        print(f"Note: {e}")
        print("Trying without specifying feed...")
        try:
            bars = api.get_bars("SPY", "1Day", start=week_ago, limit=5).df
            print(f"Successfully retrieved {len(bars)} days of historical data")
        except Exception as e2:
            print(f"Error retrieving historical data: {e2}")
    
    print("\\nConnection test completed successfully!")
    
except Exception as e:
    print(f"\\nError connecting to Alpaca API: {e}")
    print("\\nPlease check your API keys in the .env file")
    sys.exit(1)
"""
    
    try:
        with open("temp_api_check.py", "w") as f:
            f.write(check_script)
        
        subprocess.run([sys.executable, "temp_api_check.py"])
        
        # Clean up
        if os.path.exists("temp_api_check.py"):
            os.remove("temp_api_check.py")
    except Exception as e:
        print(f"\nError running API check: {e}")
    
    input("\nPress Enter to return to the menu...")

def setup_environment():
    """Run the setup script"""
    print("\nSetting up environment...")
    try:
        subprocess.run([sys.executable, "setup.py"])
    except KeyboardInterrupt:
        print("\nSetup stopped by user.")
    input("\nPress Enter to return to the menu...")

def init_repository():
    """Initialize git repository"""
    print("\nInitializing git repository...")
    try:
        subprocess.run([sys.executable, "init_repo.py"])
    except KeyboardInterrupt:
        print("\nInitialization stopped by user.")
    input("\nPress Enter to return to the menu...")

def edit_config():
    """Edit the configuration file"""
    print("\nOpening configuration file...")
    
    # Determine the best editor based on platform
    editor = None
    if os.name == 'nt':  # Windows
        # Try to use notepad or another common editor
        if os.path.exists("C:\\Windows\\System32\\notepad.exe"):
            editor = "notepad.exe"
    else:  # Unix-like
        # Try to use common editors in order of preference
        for ed in ["nano", "vim", "vi", "gedit"]:
            try:
                subprocess.run(["which", ed], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
                editor = ed
                break
            except (subprocess.SubprocessError, FileNotFoundError):
                continue
    
    if editor:
        try:
            subprocess.run([editor, "config.py"])
        except Exception as e:
            print(f"\nError opening editor: {e}")
            print("Please edit config.py manually with your preferred text editor.")
    else:
        print("\nCould not find a suitable text editor.")
        print("Please edit config.py manually with your preferred text editor.")
    
    input("\nPress Enter to return to the menu...")

def position_sizing_settings():
    """Configure position sizing settings"""
    # Reload config module to ensure we have the latest values
    importlib.reload(config)
    
    while True:
        clear_screen()
        print("\n" + "="*50)
        print("POSITION SIZING SETTINGS")
        print("="*50)
        
        # Display current settings
        print(f"\nCurrent Settings:")
        print(f"1. Position Sizing Mode: {'DYNAMIC' if config.USE_DYNAMIC_POSITION_SIZING else 'FIXED'}")
        print(f"2. Fixed Quantity: {config.QUANTITY} shares")
        print(f"3. Risk Per Trade: {config.RISK_PER_TRADE_PCT}%")
        print(f"4. Maximum Position Size: {config.MAX_POSITION_SIZE} shares")
        print("\n5. Return to Main Menu")
        
        choice = input("\nEnter option to change (1-5): ")
        
        if choice == '1':
            # Toggle position sizing mode
            mode = input("\nSelect position sizing mode (1-Dynamic, 2-Fixed): ")
            if mode == '1':
                update_config_value("USE_DYNAMIC_POSITION_SIZING", True)
                print("\nDynamic position sizing ENABLED")
            elif mode == '2':
                update_config_value("USE_DYNAMIC_POSITION_SIZING", False)
                print("\nFixed position sizing ENABLED")
            else:
                print("\nInvalid selection. No changes made.")
            
        elif choice == '2':
            # Update fixed quantity
            try:
                new_qty = float(input("\nEnter new fixed quantity (e.g., 5): "))
                if new_qty > 0:
                    update_config_value("QUANTITY", new_qty)
                    print(f"\nFixed quantity updated to {new_qty}")
                else:
                    print("\nQuantity must be greater than 0. No changes made.")
            except ValueError:
                print("\nInvalid input. No changes made.")
            
        elif choice == '3':
            # Update risk percentage
            try:
                new_risk = float(input("\nEnter new risk percentage (e.g., 1.0 for 1%): "))
                if 0 < new_risk <= 5:  # Limit risk to reasonable range
                    update_config_value("RISK_PER_TRADE_PCT", new_risk)
                    print(f"\nRisk percentage updated to {new_risk}%")
                else:
                    print("\nRisk must be between 0 and 5%. No changes made.")
            except ValueError:
                print("\nInvalid input. No changes made.")
                
        elif choice == '4':
            # Update max position size
            try:
                new_max = float(input("\nEnter new maximum position size: "))
                if new_max > 0:
                    update_config_value("MAX_POSITION_SIZE", new_max)
                    print(f"\nMaximum position size updated to {new_max}")
                else:
                    print("\nMaximum position size must be greater than 0. No changes made.")
            except ValueError:
                print("\nInvalid input. No changes made.")
                
        elif choice == '5':
            break
        else:
            print("\nInvalid choice. Please try again.")
        
        time.sleep(1)
        input("\nPress Enter to continue...")

def update_config_value(variable_name, new_value):
    """
    Update a variable in the config.py file
    """
    try:
        with open('config.py', 'r') as file:
            lines = file.readlines()
        
        with open('config.py', 'w') as file:
            for line in lines:
                if line.strip().startswith(variable_name + " ="):
                    # Format the new line based on the variable type
                    if isinstance(new_value, bool):
                        file.write(f"{variable_name} = {str(new_value)}  # Modified\n")
                    elif isinstance(new_value, (int, float)):
                        file.write(f"{variable_name} = {new_value}  # Modified\n")
                    else:
                        file.write(f'{variable_name} = "{new_value}"  # Modified\n')
                else:
                    file.write(line)
        
        # Reload config to reflect changes
        importlib.reload(config)
        return True
    except Exception as e:
        print(f"Error updating config: {str(e)}")
        return False

def run_backtest():
    """Run the backtest tool"""
    print("\nBacktesting AlgoAlp Strategy...")
    
    # Get backtest parameters from user
    symbol = input(f"Symbol to backtest (default={config.SYMBOL}): ") or config.SYMBOL
    
    lookback = input("Number of days to backtest (default=90): ")
    lookback = int(lookback) if lookback.strip() else 90
    
    start_date = input("Start date (YYYY-MM-DD) or leave blank to use lookback days: ")
    end_date = input("End date (YYYY-MM-DD) or leave blank for today: ")
    
    initial_capital = input("Initial capital (default=10000): ")
    initial_capital = float(initial_capital) if initial_capital.strip() else 10000
    
    position_size = input(f"Position size in shares (default={config.QUANTITY}): ")
    position_size = float(position_size) if position_size.strip() else config.QUANTITY
    
    # Ask for data source preference
    data_source = input("Data source (polygon/yahoo) - default=polygon: ").lower() or "polygon"
    if data_source not in ["polygon", "yahoo"]:
        data_source = "polygon"
    
    print("\nRunning backtest with these parameters:")
    print(f"Symbol: {symbol}")
    if start_date:
        print(f"Start date: {start_date}")
    else:
        print(f"Lookback: {lookback} days")
    print(f"End date: {end_date or 'today'}")
    print(f"Initial capital: ${initial_capital}")
    print(f"Position size: {position_size} shares")
    print(f"Data source: {data_source}")
    
    print("\nNote: The backtest will use 5-minute candles by default with Polygon.io,")
    print("      but may fall back to larger timeframes or Yahoo Finance data")
    print("      depending on API access and data availability.")
    
    # Build command
    cmd = [sys.executable, "backtest.py", "--symbol", symbol, "--source", data_source]
    
    if start_date:
        cmd.extend(["--start", start_date])
    else:
        cmd.extend(["--days", str(lookback)])
    
    if end_date:
        cmd.extend(["--end", end_date])
    
    cmd.extend(["--capital", str(initial_capital), "--shares", str(position_size)])
    
    # Run backtest
    try:
        subprocess.run(cmd)
    except KeyboardInterrupt:
        print("\nBacktest stopped by user.")
    except Exception as e:
        print(f"\nError running backtest: {e}")
        print("\nIf you're seeing API errors, try using --source yahoo")
        print("or check your Polygon.io API key in the environment variables.")
    
    input("\nPress Enter to return to the menu...")

def main():
    """Main function"""
    while True:
        print_header()
        choice = print_menu()
        
        if choice == "1":
            run_strategy()
        elif choice == "2":
            visualize_strategy()
        elif choice == "3":
            generate_report()
        elif choice == "4":
            check_api()
        elif choice == "5":
            setup_environment()
        elif choice == "6":
            init_repository()
        elif choice == "7":
            edit_config()
        elif choice == "8":
            position_sizing_settings()
        elif choice == "9":
            run_backtest()
        elif choice == "10":
            print("\nExiting AlgoAlp Trading Suite. Goodbye!")
            sys.exit(0)
        else:
            print("\nInvalid choice. Please try again.")
            time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting AlgoAlp Trading Suite. Goodbye!")
        sys.exit(0)