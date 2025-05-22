from lightweight_charts import Chart

if __name__ == '__main__':
    chart = Chart()
    
    # Set NY time zone for the chart using the time_scale method instead
    # The timezone parameter should be used with time_scale, not layout
    chart.time_scale(
        time_visible=True,
        seconds_visible=False,
    )
    
    chart.polygon.api_key('qdB8qbiJQcVUwqF3SqXxHJKVIABG4Saf')
    chart.polygon.stock(
        symbol='SPY',
        timeframe='5min',
        start_date='2025-05-15'
    )
    
    chart.show(block=True)