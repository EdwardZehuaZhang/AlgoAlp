#!/usr/bin/env python3
"""
Verify timezone conversion is working correctly
"""
import pandas as pd
import datetime
import os

# Read CSV file from historical_data folder
csv_file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'historical_data', 'spy_5min_20250515_to_20250522.csv')


try:
    df = pd.read_csv(csv_file)
    print("=== CSV Data Verification ===")
    print(f"Total rows: {len(df)}")
    print(f"First timestamp: {df['time'].iloc[0]}")
    print(f"Last timestamp: {df['time'].iloc[-1]}")
    
    # Parse first timestamp to verify it's correct
    first_time = pd.to_datetime(df['time'].iloc[0])
    print(f"First time parsed: {first_time}")
    print(f"Day of week: {first_time.strftime('%A')}")
    print(f"Time: {first_time.strftime('%H:%M:%S')}")
    
    # Check if times are in correct market hours
    df['parsed_time'] = pd.to_datetime(df['time'])
    df['hour'] = df['parsed_time'].dt.hour
    df['minute'] = df['parsed_time'].dt.minute
    
    print(f"\nTime range verification:")
    print(f"Earliest hour: {df['hour'].min()}:{df['minute'].min():02d}")
    print(f"Latest hour: {df['hour'].max()}:{df['minute'].max():02d}")
    
    # Check for 9:30 AM start
    market_open = df[(df['hour'] == 9) & (df['minute'] == 30)]
    if len(market_open) > 0:
        print(f"✓ Found 9:30 AM entries: {len(market_open)}")
    else:
        print("✗ No 9:30 AM entries found")
    
    # Check for 4:00 PM end
    market_close = df[(df['hour'] == 16) & (df['minute'] == 0)]
    if len(market_close) > 0:
        print(f"✓ Found 4:00 PM entries: {len(market_close)}")
    else:
        print("✗ No 4:00 PM entries found")
        
except FileNotFoundError:
    print(f"CSV file {csv_file} not found")
except Exception as e:
    print(f"Error: {e}")
