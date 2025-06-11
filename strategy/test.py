# filepath: combined_spy_charts.py
import pandas as pd
from lightweight_charts import Chart

if __name__ == '__main__':
    # Create the main chart
    main_chart = Chart(inner_width=0.5, inner_height=1.0, width=1200, height=800)
    
    # Create the subchart with the same height but placed to the right
    polygon_chart = main_chart.create_subchart(position='right', width=0.5, height=1.0)
    
    # Configure timescale for both charts
    main_chart.time_scale(time_visible=True, seconds_visible=False)
    polygon_chart.time_scale(time_visible=True, seconds_visible=False)
    
    # Load CSV data for the first chart (from display_spy_chart.py)
    df = pd.read_csv('spy_daily_candles_20250520.csv')
    
    # Convert timestamp if needed
    if 'time' in df.columns and df['time'].dtype != 'datetime64[ns]':
        if pd.to_numeric(df['time'], errors='coerce').notnull().all():
            if df['time'].iloc[0] > 1000000000000:  # If in milliseconds
                df['time'] = pd.to_datetime(df['time'], unit='ms')
            else:  # If in seconds
                df['time'] = pd.to_datetime(df['time'], unit='s')
        else:
            df['time'] = pd.to_datetime(df['time'])
    
    # Set data for the first chart
    main_chart.set(df)
    main_chart.watermark('Local CSV Data')
    
    # Configure Polygon.io data for the second chart (from plot_spy_chart.py)
    polygon_chart.polygon.api_key('qdB8qbiJQcVUwqF3SqXxHJKVIABG4Saf')
    polygon_chart.polygon.stock(
        symbol='SPY',
        timeframe='5min',
        start_date='2025-05-15'
    )
    polygon_chart.watermark('Polygon.io Data')
    
    # Show the charts
    main_chart.show(block=True)