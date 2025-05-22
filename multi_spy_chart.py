import pandas as pd
from lightweight_charts import Chart
import pytz
from datetime import datetime, timedelta, time
import requests

def prepare_data(file_path):
    """Load and prepare data for display from a CSV file"""
    df = pd.read_csv(file_path)
    
    # Convert the timestamp to proper format if needed
    if 'time' in df.columns and df['time'].dtype != 'datetime64[ns]':
        # Check if the time column contains Unix timestamps
        if pd.to_numeric(df['time'], errors='coerce').notnull().all():
            # Convert from milliseconds to seconds if needed
            if df['time'].iloc[0] > 1000000000000:  # If in milliseconds
                df['time'] = pd.to_datetime(df['time'], unit='ms')
            else:  # If in seconds
                df['time'] = pd.to_datetime(df['time'], unit='s')
        else:
            # If time is in string format like '2023-05-20 09:30:00'
            df['time'] = pd.to_datetime(df['time'])
    
    return df

def fetch_polygon_data(symbol='SPY', timeframe='5minute', limit=7):
    """Fetch data from Polygon API"""
    # Polygon API key
    api_key = 'qdB8qbiJQcVUwqF3SqXxHJKVIABG4Saf'
    
    # Calculate date range - for 5 minute data, we limit to 7 days to avoid too many data points
    # and possible API limits
    end_date = datetime.now()
    start_date = end_date - timedelta(days=limit)
    
    # Format dates for API
    start_str = start_date.strftime('%Y-%m-%d')
    end_str = end_date.strftime('%Y-%m-%d')
    
    print(f"Fetching {symbol} {timeframe} data from Polygon.io ({start_str} to {end_str})")
    
    # Format the URL for Polygon.io API - use 5 for 5 minute timeframe
    url = f"https://api.polygon.io/v2/aggs/ticker/{symbol}/range/5/minute/{start_str}/{end_str}"
    
    # Request parameters
    params = {
        'adjusted': 'true',
        'sort': 'asc',
        'limit': 50000,  # Increased limit for intraday data
        'apiKey': api_key
    }
    
    try:
        # Make the API request
        response = requests.get(url, params=params)
        
        if response.status_code == 200:
            data = response.json()
            
            if data.get('resultsCount', 0) > 0:
                # Convert to pandas DataFrame
                bars = pd.DataFrame(data['results'])
                
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
                
                # Filter to only include market hours (8:30 AM - 5:00 PM ET)
                # Using time() directly since we imported it properly
                original_count = len(bars)
                bars = bars[(bars['timestamp'].dt.time >= time(13, 30)) & 
                           (bars['timestamp'].dt.time <= time(19, 55))]
                print(f"Filtered from {original_count} to {len(bars)} rows (market hours only)")
                
                # Filter to only include weekdays
                original_count = len(bars)
                bars = bars[bars['timestamp'].dt.dayofweek < 5]  # 0=Monday, 4=Friday
                print(f"Filtered from {original_count} to {len(bars)} rows (weekdays only)")
                
                # Create time column in the format expected by the chart
                # IMPORTANT: Convert to string to avoid JSON serialization issues
                if timeframe.lower() in ['minute', '5minute', '15minute', '30minute', '1hour']:
                    bars['time'] = bars['timestamp'].dt.strftime('%Y-%m-%d %H:%M:%S')
                else:
                    bars['time'] = bars['timestamp'].dt.strftime('%Y-%m-%d')
                
                # Drop the timestamp column to avoid serialization issues
                bars = bars.drop('timestamp', axis=1)
                
                print(f"Successfully loaded {len(bars)} {timeframe} candles from Polygon")
                return bars
            else:
                print("No data available from Polygon API")
                return None
        else:
            print(f"API request failed: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error fetching Polygon data: {e}")
        return None

def calculate_sma(data, period=20):
    """Calculate Simple Moving Average from candle data"""
    # Create a DataFrame with time and SMA columns
    df = data.copy()
    df['SMA'] = df['close'].rolling(window=period).mean()
    
    # Return a DataFrame with time and the SMA value (properly named)
    return pd.DataFrame({
        'time': df['time'],
        f'SMA {period}': df['SMA']
    }).dropna()

if __name__ == '__main__':
    # Create the main chart with full width, 70% height 
    main_chart = Chart(inner_width=1.0, inner_height=0.7, toolbox=True)
    
    # Create a subchart that will be synchronized with the main chart
    # This subchart will take the same width but 30% of the height
    subchart = main_chart.create_subchart(
        width=1.0, 
        height=0.3, 
        sync=True,  # Synchronize with main chart
        toolbox=False
    )
    
    # Load same data for both charts to ensure proper synchronization
    polygon_data = fetch_polygon_data(symbol='SPY', timeframe='5minute', limit=7)
    csv_data = prepare_data('spy_5min_20250515_to_20250522.csv')
    
    # Select data source - use the same data source for both charts to ensure synchronization
    chart_data = polygon_data if polygon_data is not None else csv_data
    
    # Configure main chart (top chart)
    main_chart.layout(
        background_color='#000000',  # Changed from #131722 to black
        text_color='#D9D9D9',
        font_size=12
    )
    main_chart.candle_style(
        up_color='#26a69a', 
        down_color='#ef5350',
        border_up_color='#26a69a', 
        border_down_color='#ef5350',
        wick_up_color='#26a69a', 
        wick_down_color='#ef5350'
    )
    main_chart.volume_config(
        up_color='rgba(38, 166, 154, 0.5)', 
        down_color='rgba(239, 83, 80, 0.5)'
    )
    #main_chart.watermark('SPY 5-Minute (Top)', color='rgba(180, 180, 220, 0.3)')
    main_chart.legend(visible=True, font_size=11)
    
    # Set data for the main chart
    main_chart.set(chart_data)
    
    # Calculate and add the 20-bar SMA to the main chart (make it yellow and thin)
    sma20_data = calculate_sma(chart_data, period=20)
    # Create line with yellow color
    sma20_line = main_chart.create_line('SMA 20', color='#FFFF00', width=0.2, price_line =False, price_label=False)
    sma20_line.set(sma20_data)
    
    # Calculate and add the 50-bar SMA to the main chart (make it pink)
    sma50_data = calculate_sma(chart_data, period=50)
    # Create line with pink color
    sma50_line = main_chart.create_line('SMA 50', color='#FF69B4', width=0.2, price_line =False, price_label=False)
    sma50_line.set(sma50_data)
    
    # Calculate and add the 200-bar SMA to the main chart (blue line)
    sma200_data = calculate_sma(chart_data, period=200)
    # Create line with style parameters directly in the constructor
    sma200_line = main_chart.create_line('SMA 200', color='#2962FF', width=0.2, price_line =False, price_label=False)
    sma200_line.set(sma200_data)
    
    # Configure the subchart (bottom chart)
    subchart.layout(
        background_color='#000000',  # Changed from #131722 to black
        text_color='#D9D9D9',
        font_size=12
    )
    subchart.candle_style(
        up_color='rgba(38, 166, 154, 0.7)', 
        down_color='rgba(239, 83, 80, 0.7)',
        border_up_color='#26a69a', 
        border_down_color='#ef5350',
        wick_up_color='#26a69a', 
        wick_down_color='#ef5350'
    )
    # Configure volume for subchart
    subchart.volume_config(
        up_color='rgba(38, 166, 154, 0.5)', 
        down_color='rgba(239, 83, 80, 0.5)'
    )
    #subchart.watermark('SPY 5-Minute (Bottom)', color='rgba(180, 180, 220, 0.3)')
    
    # Set the same data for the subchart to ensure proper synchronization
    subchart.set(chart_data)
    
    # Hide the time scale on the subchart since it's synchronized with the main chart
    subchart.time_scale(visible=False)
    
    # Configure the price scaling to ensure proper synchronization
    main_chart.price_scale(
        auto_scale=True,
        mode=1,  # 0 = Normal, 1 = Logarithmic
        border_visible=True
    )
    subchart.price_scale(
        auto_scale=True,
        mode=1,  # Match the main chart's scale mode
        border_visible=True
    )
    
    # Add some horizontal lines for reference on the main chart
    # Get the max and min values for the data range
    #max_price = chart_data['high'].max()
    #min_price = chart_data['low'].min()
    #mid_price = (max_price + min_price) / 2
    
    # Add horizontal lines at significant levels
    #main_chart.horizontal_line(max_price, color='rgba(255, 255, 255, 0.5)', width=1, style='dashed', text='Max')
    #main_chart.horizontal_line(min_price, color='rgba(255, 255, 255, 0.5)', width=1, style='dashed', text='Min')
    #main_chart.horizontal_line(mid_price, color='rgba(255, 255, 255, 0.7)', width=1, style='dashed', text='Mid')
    
    # Show the chart (blocking until closed)
    main_chart.show(block=True)
