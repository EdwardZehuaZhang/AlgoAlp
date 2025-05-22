"""
Script to download S&P 500 5-minute candle data and save to CSV
Specifically fetches data from May 15 to May 22
"""

import os
import sys
import datetime
import pandas as pd
import requests

# Configure API Key
POLYGON_API_KEY = os.getenv("POLYGON_API_KEY", "qdB8qbiJQcVUwqF3SqXxHJKVIABG4Saf")

def fetch_spy_5min_data(start_date_str='2025-05-15', end_date_str='2025-05-22'):
    """Fetch SPY 5-minute candle data from Polygon.io for a specific date range"""
    
    print(f"Fetching SPY 5-minute candles from {start_date_str} to {end_date_str}")
    
    # Format the URL for Polygon.io API (using 5-minute data)
    url = f"https://api.polygon.io/v2/aggs/ticker/SPY/range/5/minute/{start_date_str}/{end_date_str}"
    
    # Request parameters
    params = {
        'adjusted': 'true',
        'sort': 'asc',  # Get in ascending order for CSV
        'limit': 10000,  # Maximum limit for most API tiers
        'apiKey': POLYGON_API_KEY
    }
    
    try:
        # Make the API request
        print("Making API request...")
        response = requests.get(url, params=params)
        print(f"Response status code: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            results_count = data.get('resultsCount', 0)
            
            if results_count > 0:
                # Convert to pandas DataFrame
                bars = pd.DataFrame(data['results'])
                print(f"Successfully retrieved {len(bars)} 5-minute candles")
                
                # Rename columns to match expected format
                bars.rename(columns={
                    'o': 'open',
                    'h': 'high',
                    'l': 'low',
                    'c': 'close',
                    'v': 'volume',
                    't': 'timestamp'
                }, inplace=True)
                
                # Convert timestamp from milliseconds to datetime
                bars['timestamp'] = pd.to_datetime(bars['timestamp'], unit='ms')
                
                # Filter to only include market hours (13:30 - 19:55 UTC, matching multi_spy_chart.py)
                original_count = len(bars)
                bars = bars[(bars['timestamp'].dt.time >= datetime.time(13, 30)) & 
                           (bars['timestamp'].dt.time <= datetime.time(19, 55))]
                print(f"Filtered from {original_count} to {len(bars)} rows (market hours only)")
                
                # Filter to only include weekdays
                original_count = len(bars)
                bars = bars[bars['timestamp'].dt.dayofweek < 5]  # 0=Monday, 4=Friday
                print(f"Filtered from {original_count} to {len(bars)} rows (weekdays only)")
                
                # Select only the required columns in the specified order
                result = bars[['time', 'open', 'high', 'low', 'close', 'volume']]
                
                return result
            else:
                print("No data available in the API response")
                return None
        else:
            print(f"API request failed with status code: {response.status_code}")
            print(f"Response text: {response.text}")
            return None
    except Exception as e:
        print(f"Exception during API request: {e}")
        return None

def save_to_csv(data, filename=None):
    """Save the data to a CSV file"""
    if data is None or data.empty:
        print("No data to save to CSV")
        return False
    
    try:
        # Generate filename if not provided
        if filename is None:
            start_date = data['time'].iloc[0].split(' ')[0].replace('-', '')
            end_date = data['time'].iloc[-1].split(' ')[0].replace('-', '')
            filename = f"spy_5min_{start_date}_to_{end_date}.csv"
        
        # Save to CSV
        csv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
        data.to_csv(csv_path, index=False)
        
        print(f"Successfully saved {len(data)} candles to {csv_path}")
        return True
    except Exception as e:
        print(f"Error saving data to CSV: {e}")
        return False

def main():
    """Main function"""
    try:
        print("Starting SPY 5-minute data download...")
        
        # Specific date range: May 15 to May 22, 2025
        start_date = "2025-05-15"
        end_date = "2025-05-22"
        
        # Get SPY data
        spy_data = fetch_spy_5min_data(start_date, end_date)
        
        # Save to CSV
        if spy_data is not None and not spy_data.empty:
            filename = f"spy_5min_{start_date.replace('-', '')}_to_{end_date.replace('-', '')}.csv"
            save_to_csv(spy_data, filename)
            
            # Display sample of the data
            print("\nSample of the downloaded data:")
            print(spy_data.head())
        else:
            print("Failed to retrieve SPY data")
        
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
