import pandas as pd
from lightweight_charts import Chart


if __name__ == '__main__':
    
    chart = Chart()
    
    # Columns: time | open | high | low | close | volume 
    # Using 5-minute data instead of daily data
    df = pd.read_csv('spy_daily_candles_20250520.csv')
    
    # Convert the timestamp to proper format if needed
    # If your data is in Unix timestamp (milliseconds)
    if 'time' in df.columns and df['time'].dtype != 'datetime64[ns]':
        # Check if the time column contains Unix timestamps
        if pd.to_numeric(df['time'], errors='coerce').notnull().all():
            # Convert from milliseconds to seconds if needed (adjust as necessary)
            if df['time'].iloc[0] > 1000000000000:  # If in milliseconds
                df['time'] = pd.to_datetime(df['time'], unit='ms')
            else:  # If in seconds
                df['time'] = pd.to_datetime(df['time'], unit='s')
        else:
            # If time is in string format like '2023-05-20 09:30:00'
            df['time'] = pd.to_datetime(df['time'])
    
    # Set chart properties for 5-minute timeframe
    chart.set(df)
    chart.time_scale(time_visible=True, seconds_visible=False)
    
    # Optionally, you can set the visible range to focus on a specific period
    # chart.time_scale(bar_spacing=6)  # Adjust spacing between bars
    
    chart.show(block=True)
