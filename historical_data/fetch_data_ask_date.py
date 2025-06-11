
import os
import sys
import datetime
import pandas as pd
import requests

# Configure API Key
POLYGON_API_KEY = os.getenv("POLYGON_API_KEY", "qdB8qbiJQcVUwqF3SqXxHJKVIABG4Saf")

def fetch_spy_5min_data(start_date_str='2025-06-02', end_date_str='2025-06-07'):
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
                }, inplace=True)                # Convert timestamp from milliseconds to datetime (UTC)
                bars['timestamp'] = pd.to_datetime(bars['timestamp'], unit='ms', utc=True)
                
                # Convert to Eastern Time for proper market hours filtering
                bars['timestamp_et'] = bars['timestamp'].dt.tz_convert('US/Eastern')
                
                # Debug: Print some timestamp info
                if len(bars) > 0:
                    print(f"First UTC timestamp: {bars['timestamp'].iloc[0]}")
                    print(f"First ET timestamp: {bars['timestamp_et'].iloc[0]}")
                
                # Filter to only include market hours (9:30 AM - 4:00 PM ET)
                original_count = len(bars)
                market_start = datetime.time(9, 30)  # 9:30 AM ET
                market_end = datetime.time(16, 0)    # 4:00 PM ET
                
                bars = bars[(bars['timestamp_et'].dt.time >= market_start) & 
                           (bars['timestamp_et'].dt.time <= market_end)]
                print(f"Filtered from {original_count} to {len(bars)} rows (market hours 9:30 AM - 4:00 PM ET)")# Filter to only include weekdays
                original_count = len(bars)
                bars = bars[bars['timestamp_et'].dt.dayofweek < 5]  # 0=Monday, 4=Friday
                print(f"Filtered from {original_count} to {len(bars)} rows (weekdays only)")
                
                # Convert timestamp to Eastern Time for CSV output (this is what TradingView shows)
                bars['time'] = bars['timestamp_et'].dt.strftime('%Y-%m-%d %H:%M:%S')
                
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
    
    try:        # Generate filename if not provided
        if filename is None:
            # Extract date from first and last time entries (format: "YYYY-MM-DD HH:MM:SS")
            start_date = data['time'].iloc[0].split(' ')[0].replace('-', '')
            end_date = data['time'].iloc[-1].split(' ')[0].replace('-', '')
            filename = f"spy_5min_{start_date}_to_{end_date}.csv"
          # Save to CSV in historical_data folder
        historical_data_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'historical_data')
        os.makedirs(historical_data_dir, exist_ok=True)
        csv_path = os.path.join(historical_data_dir, filename)
        data.to_csv(csv_path, index=False)
        
        print(f"Successfully saved {len(data)} candles to {csv_path}")
        return True
    except Exception as e:
        print(f"Error saving data to CSV: {e}")
        return False

def get_user_dates():
    """Get date range from user input"""
    print("\n" + "="*50)
    print("SPY 5-Minute Data Downloader")
    print("="*50)
    
    while True:
        try:
            print("\nEnter the date range for SPY data download:")
            print("Format: YYYY-MM-DD (e.g., 2025-06-02)")
            
            start_date = input("Start date: ").strip()
            end_date = input("End date: ").strip()
            
            # Validate date format
            start_dt = datetime.datetime.strptime(start_date, '%Y-%m-%d')
            end_dt = datetime.datetime.strptime(end_date, '%Y-%m-%d')
            
            # Check if start date is before end date
            if start_dt >= end_dt:
                print("Error: Start date must be before end date!")
                continue
                
            # Check if date range is not too far in the future or past
            today = datetime.datetime.now()
            if start_dt > today:
                print("Warning: Start date is in the future!")
                
            # Confirm the date range
            days_diff = (end_dt - start_dt).days
            print(f"\nDate range: {start_date} to {end_date} ({days_diff} days)")
            confirm = input("Proceed with this date range? (y/n): ").strip().lower()
            
            if confirm in ['y', 'yes']:
                return start_date, end_date
            else:
                print("Please enter new dates...")
                
        except ValueError:
            print("Error: Invalid date format! Please use YYYY-MM-DD format.")
        except KeyboardInterrupt:
            print("\nOperation cancelled by user.")
            sys.exit(0)

def main():
    """Main function"""
    try:
        print("Starting SPY 5-minute data download...")
        
        # Get date range from user
        start_date, end_date = get_user_dates()
        
        # Get SPY data
        spy_data = fetch_spy_5min_data(start_date, end_date)
        
        # Save to CSV
        if spy_data is not None and not spy_data.empty:
            filename = f"spy_5min_{start_date.replace('-', '')}_to_{end_date.replace('-', '')}.csv"
            success = save_to_csv(spy_data, filename)
            
            if success:                # Display sample of the data
                print("\nSample of the downloaded data:")
                print(spy_data.head())
                print(f"\nData shape: {spy_data.shape}")
                print(f"Date range in data: {spy_data['time'].iloc[0]} to {spy_data['time'].iloc[-1]}")
            else:
                print("Failed to save data to CSV")
        else:
            print("Failed to retrieve SPY data")
        
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
