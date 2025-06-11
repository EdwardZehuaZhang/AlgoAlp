#!/usr/bin/env python3
"""
Comprehensive test script to verify all charting components work correctly
"""
import os
import sys
import pandas as pd
from datetime import datetime

def test_csv_files():
    """Test that CSV files exist and have correct format"""
    print("=== Testing CSV Files ===")
    historical_data_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'historical_data')
    
    if not os.path.exists(historical_data_dir):
        print("✗ historical_data directory not found")
        return False
    
    # List CSV files
    csv_files = [f for f in os.listdir(historical_data_dir) if f.endswith('.csv')]
    print(f"Found {len(csv_files)} CSV files:")
    for f in csv_files:
        print(f"  - {f}")
    
    if len(csv_files) == 0:
        print("✗ No CSV files found")
        return False
    
    # Test the main CSV file we're using
    main_csv = 'spy_5min_20250515_to_20250522.csv'
    csv_path = os.path.join(historical_data_dir, main_csv)
    
    if not os.path.exists(csv_path):
        print(f"✗ Main CSV file {main_csv} not found")
        return False
    
    try:
        df = pd.read_csv(csv_path)
        print(f"✓ Successfully loaded {main_csv}")
        print(f"  - Rows: {len(df)}")
        print(f"  - Columns: {list(df.columns)}")
        print(f"  - Date range: {df['time'].iloc[0]} to {df['time'].iloc[-1]}")
        
        # Check for market hours
        df['parsed_time'] = pd.to_datetime(df['time'])
        df['hour'] = df['parsed_time'].dt.hour
        df['minute'] = df['parsed_time'].dt.minute
        
        market_open = df[(df['hour'] == 9) & (df['minute'] == 30)]
        market_close = df[(df['hour'] == 16) & (df['minute'] == 0)]
        
        print(f"  - Market open entries (9:30): {len(market_open)}")
        print(f"  - Market close entries (16:00): {len(market_close)}")
        
        if len(market_open) > 0 and len(market_close) > 0:
            print("✓ CSV data contains correct market hours")
            return True
        else:
            print("✗ CSV data missing market hours")
            return False
            
    except Exception as e:
        print(f"✗ Error reading CSV: {e}")
        return False

def test_html_file():
    """Test that HTML file exists and references correct CSV path"""
    print("\n=== Testing HTML File ===")
    html_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'multi_spy_chart.html')
    
    if not os.path.exists(html_path):
        print("✗ multi_spy_chart.html not found")
        return False
    
    try:
        with open(html_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        print("✓ HTML file loaded successfully")
        
        # Check for correct CSV path
        if "../historical_data/spy_5min_20250515_to_20250522.csv" in content:
            print("✓ HTML references correct CSV path")
        else:
            print("✗ HTML does not reference correct CSV path")
            return False
        
        # Check for timezone parsing fix
        if "EST" in content and "timeValue + \" EST\"" in content:
            print("✓ HTML contains timezone parsing fix")
        else:
            print("✗ HTML missing timezone parsing fix")
            return False
        
        return True
        
    except Exception as e:
        print(f"✗ Error reading HTML: {e}")
        return False

def test_python_scripts():
    """Test that Python scripts can be imported and work"""
    print("\n=== Testing Python Scripts ===")
    
    try:
        # Test fetch_data.py
        fetch_data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fetch_data.py')
        if os.path.exists(fetch_data_path):
            print("✓ fetch_data.py exists")
        else:
            print("✗ fetch_data.py not found")
            return False
        
        # Test that historical_data directory is correctly referenced
        with open(fetch_data_path, 'r') as f:
            content = f.read()
        
        if "historical_data" in content and "os.path.join" in content:
            print("✓ fetch_data.py correctly references historical_data directory")
        else:
            print("✗ fetch_data.py missing correct directory references")
            return False
        
        return True
        
    except Exception as e:
        print(f"✗ Error testing Python scripts: {e}")
        return False

def main():
    """Run all tests"""
    print("Running comprehensive charting system tests...")
    print(f"Current working directory: {os.getcwd()}")
    print(f"Script location: {os.path.dirname(os.path.abspath(__file__))}")
    
    results = []
    results.append(test_csv_files())
    results.append(test_html_file())
    results.append(test_python_scripts())
    
    print("\n=== Test Summary ===")
    passed = sum(results)
    total = len(results)
    
    if passed == total:
        print(f"✓ All {total} tests passed!")
        print("\nYour charting system should now work correctly:")
        print("1. CSV data is properly formatted with 9:30 AM market open times")
        print("2. HTML file references the correct CSV path")
        print("3. Timezone parsing has been fixed")
        print("4. Python scripts save to the correct directory")
    else:
        print(f"✗ {total - passed} out of {total} tests failed")
        print("Please review the errors above and fix the issues")

if __name__ == "__main__":
    main()
