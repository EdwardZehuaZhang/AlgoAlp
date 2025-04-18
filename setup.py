"""
Setup script for the AlgoAlp project
"""
import os
import subprocess
import sys
import platform

def main():
    """Main setup function"""
    print("Setting up AlgoAlp trading environment...")
    
    # Check Python version
    python_version = sys.version.split()[0]
    print(f"Python version: {python_version}")
    
    if sys.version_info < (3, 7):
        print("Warning: This project requires Python 3.7 or higher.")
        sys.exit(1)
    
    # Install dependencies
    print("\nInstalling dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("Dependencies installed successfully.")
    except subprocess.CalledProcessError:
        print("Error installing dependencies. Please try manually with 'pip install -r requirements.txt'")
        sys.exit(1)
    
    # Check if .env file exists
    if not os.path.exists(".env"):
        print("\nWarning: .env file not found. Creating from template...")
        with open(".env", "w") as env_file:
            env_file.write("# Alpaca API credentials\n")
            env_file.write("ALPACA_API_KEY=your_api_key_here\n")
            env_file.write("ALPACA_API_SECRET=your_api_secret_here\n")
            env_file.write("ALPACA_PAPER=True  # Set to False for live trading\n")
        print(".env file created. Please update with your Alpaca API credentials.")
    else:
        print("\n.env file found.")
    
    print("\nSetup complete!")
    print("\nNext steps:")
    print("1. Update your .env file with your Alpaca API credentials")
    print("2. Run the strategy with 'python strategy.py'")
    print("3. Visualize results with 'python visualize.py'")

if __name__ == "__main__":
    main() 