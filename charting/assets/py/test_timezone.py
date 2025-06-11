#!/usr/bin/env python3
"""
Test script to debug timezone handling
"""
import pandas as pd
import datetime

# Test timestamp conversion
test_timestamp = 1717329000000  # Example timestamp in milliseconds (from Polygon)

print("=== Testing Timezone Conversion ===")
print(f"Original timestamp (ms): {test_timestamp}")

# Convert like we do in our script
dt_utc = pd.to_datetime(test_timestamp, unit='ms', utc=True)
print(f"UTC datetime: {dt_utc}")

# Convert to Eastern Time
dt_et = dt_utc.tz_convert('US/Eastern')
print(f"Eastern Time: {dt_et}")

# Extract time components
print(f"ET Time: {dt_et.time()}")
print(f"ET Hour: {dt_et.hour}")
print(f"ET Minute: {dt_et.minute}")

# Check if it's in market hours
market_start = datetime.time(9, 30)
market_end = datetime.time(16, 0)
is_market_hours = market_start <= dt_et.time() <= market_end
print(f"Is market hours (9:30-16:00 ET): {is_market_hours}")

# Test formatting
formatted_time = dt_et.strftime('%Y-%m-%d %H:%M:%S')
print(f"Formatted for CSV: {formatted_time}")

print("\n=== Testing Recent Data ===")
# Test with a recent timestamp that should be June 2, 2025 at 9:30 AM ET
recent_timestamp = 1748691000000  # Should be around June 2, 2025 9:30 AM ET

dt_utc_recent = pd.to_datetime(recent_timestamp, unit='ms', utc=True)
dt_et_recent = dt_utc_recent.tz_convert('US/Eastern')

print(f"Recent UTC: {dt_utc_recent}")
print(f"Recent ET: {dt_et_recent}")
print(f"Recent formatted: {dt_et_recent.strftime('%Y-%m-%d %H:%M:%S')}")
