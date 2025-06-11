"""
Script to automatically download SPY 5-minute historical data
Works backwards from today until API stops returning data (2-year limit for free users)
"""

import os
import sys
import datetime
import pandas as pd
import requests
import time

# Configure API Key
POLYGON_API_KEY = os.getenv("POLYGON_API_KEY", "qdB8qbiJQcVUwqF3SqXxHJKVIABG4Saf")

def fetch_spy_5min_data(start_date_str, end_date_str):
    """Fetch SPY 5-minute candle data from Polygon.io for a specific date range"""
    
    print(f"Fetching SPY 5-minute candles from {start_date_str} to {end_date_str}")
    
    # Format the URL for Polygon.io API (using 5-minute data)
    url = f"https://api.polygon.io/v2/aggs/ticker/SPY/range/5/minute/{start_date_str}/{end_date_str}"
    
    # Request parameters
    params = {
        'adjusted': 'true',
        'sort': 'asc',
        'limit': 10000,
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
                
                # Convert timestamp from milliseconds to datetime (UTC)
                bars['timestamp'] = pd.to_datetime(bars['timestamp'], unit='ms', utc=True)
                
                # Convert to Eastern Time for proper market hours filtering
                bars['timestamp_et'] = bars['timestamp'].dt.tz_convert('US/Eastern')
                
                # Filter to only include market hours (9:30 AM - 4:00 PM ET)
                original_count = len(bars)
                market_start = datetime.time(9, 30)
                market_end = datetime.time(16, 0)
                
                bars = bars[(bars['timestamp_et'].dt.time >= market_start) & 
                           (bars['timestamp_et'].dt.time <= market_end)]
                print(f"Filtered from {original_count} to {len(bars)} rows (market hours 9:30 AM - 4:00 PM ET)")
                
                # Filter to only include weekdays
                original_count = len(bars)
                bars = bars[bars['timestamp_et'].dt.dayofweek < 5]
                print(f"Filtered from {original_count} to {len(bars)} rows (weekdays only)")
                
                # Convert timestamp to Eastern Time for CSV output
                bars['time'] = bars['timestamp_et'].dt.strftime('%Y-%m-%d %H:%M:%S')
                
                # Select only the required columns in the specified order
                result = bars[['time', 'open', 'high', 'low', 'close', 'volume']]
                
                return result
            else:
                print("No data available in the API response")
                return None
        elif response.status_code == 429:
            print("Rate limit exceeded. Waiting 60 seconds...")
            time.sleep(60)
            return fetch_spy_5min_data(start_date_str, end_date_str)  # Retry
        else:
            print(f"API request failed with status code: {response.status_code}")
            print(f"Response text: {response.text}")
            return None
    except Exception as e:
        print(f"Exception during API request: {e}")
        return None

def save_to_csv(data, filename):
    """Save the data to a CSV file"""
    if data is None or data.empty:
        print("No data to save to CSV")
        return False
    
    try:
        # Save to CSV in historical_data folder
        historical_data_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'historical_data')
        os.makedirs(historical_data_dir, exist_ok=True)
        csv_path = os.path.join(historical_data_dir, filename)
        
        # Check if file already exists
        if os.path.exists(csv_path):
            print(f"File {filename} already exists. Skipping...")
            return True
        
        data.to_csv(csv_path, index=False)
        print(f"Successfully saved {len(data)} candles to {csv_path}")
        return True
    except Exception as e:
        print(f"Error saving data to CSV: {e}")
        return False

def get_date_ranges(start_date, chunk_days=25):
    """Generate date ranges working backwards from start_date"""
    current_end = start_date
    
    while True:
        current_start = current_end - datetime.timedelta(days=chunk_days)
        
        # Format dates for API
        start_str = current_start.strftime('%Y-%m-%d')
        end_str = current_end.strftime('%Y-%m-%d')
        
        yield start_str, end_str, current_start
        
        # Move to next chunk (working backwards)
        current_end = current_start - datetime.timedelta(days=1)

def download_all_historical_data():
    """Download all available historical data working backwards from today"""
    
    print("\n" + "="*60)
    print("SPY 5-Minute Historical Data Auto-Downloader")
    print("="*60)
    print("This script will download all available SPY 5-minute data")
    print("working backwards from today until the API stops returning data.")
    print("Free Polygon.io accounts have ~2 years of historical data.")
    print("="*60)
      # Start from yesterday (not today to avoid incomplete data)
    yesterday = datetime.datetime.now().date() - datetime.timedelta(days=1)
    print(f"Starting download from: {yesterday}")
    
    # Track statistics
    total_files_created = 0
    total_data_points = 0
    successful_chunks = 0
    failed_chunks = 0
      # Get date ranges (25-day chunks working backwards)
    for start_str, end_str, start_date in get_date_ranges(yesterday, chunk_days=28):
        
        print(f"\n--- Processing chunk: {start_str} to {end_str} ---")
        
        # Check if we've gone too far back (stop after 3 years to be safe)
        if (yesterday - start_date).days > (3 * 365):
            print("Reached 3-year limit. Stopping...")
            break
        
        try:
            # Fetch data for this chunk
            spy_data = fetch_spy_5min_data(start_str, end_str)
            
            if spy_data is not None and not spy_data.empty:
                # Generate filename
                start_clean = start_str.replace('-', '')
                end_clean = end_str.replace('-', '')
                filename = f"spy_5min_{start_clean}_to_{end_clean}.csv"
                
                # Save data
                if save_to_csv(spy_data, filename):
                    total_files_created += 1
                    total_data_points += len(spy_data)
                    successful_chunks += 1
                    
                    print(f"✓ Successfully saved {len(spy_data)} data points")
                    print(f"  Date range in data: {spy_data['time'].iloc[0]} to {spy_data['time'].iloc[-1]}")
                else:
                    failed_chunks += 1
                    print("✗ Failed to save data")
                    
            else:
                print("✗ No data returned from API - likely reached the limit")
                print("Stopping download...")
                break
                
        except Exception as e:
            print(f"✗ Error processing chunk {start_str} to {end_str}: {e}")
            failed_chunks += 1
            
            # If we get multiple failures in a row, we might have hit the limit
            if failed_chunks >= 3:
                print("Multiple consecutive failures. Likely reached data limit. Stopping...")
                break
        
        # Add small delay to be respectful to the API
        time.sleep(1)
        
        # Print progress
        print(f"Progress: {total_files_created} files created, {total_data_points:,} total data points")
    
    # Final summary
    print("\n" + "="*60)
    print("DOWNLOAD COMPLETE - SUMMARY")
    print("="*60)
    print(f"Total files created: {total_files_created}")
    print(f"Total data points downloaded: {total_data_points:,}")
    print(f"Successful chunks: {successful_chunks}")
    print(f"Failed chunks: {failed_chunks}")
    
    if total_files_created > 0:
        print(f"\nAll CSV files saved to: {os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'historical_data')}")
        print("\nYou can now use these files with the charting application!")
    else:
        print("\nNo data was downloaded. Check your API key and internet connection.")

def main():
    """Main function"""
    try:
        # Confirm before starting
        print("This will download ALL available SPY 5-minute historical data.")
        print("This may take several minutes and create many CSV files.")
        confirm = input("Do you want to proceed? (y/n): ").strip().lower()
        
        if confirm not in ['y', 'yes']:
            print("Operation cancelled.")
            return
        
        download_all_historical_data()
        
    except KeyboardInterrupt:
        print("\nDownload interrupted by user.")
        print("You can run this script again to continue from where it left off.")
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
