"""
Simple script to automatically merge all SPY CSV files in the historical_data folder
"""

import os
import pandas as pd
import glob
from datetime import datetime

def merge_spy_csv_files():
    """Automatically find and merge all SPY CSV files"""
    
    print("SPY CSV File Merger")
    print("=" * 40)
      # Get the historical_data directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(script_dir)
    historical_data_dir = os.path.join(parent_dir, 'historical_data')
    
    # Debug: print the paths
    print(f"Script directory: {script_dir}")
    print(f"Parent directory: {parent_dir}")
    print(f"Looking for CSV files in: {historical_data_dir}")
    
    # Check if directory exists
    if not os.path.exists(historical_data_dir):
        print(f"Error: Directory does not exist: {historical_data_dir}")
        return
    
    # Find all SPY CSV files
    pattern = os.path.join(historical_data_dir, "spy_5min_*.csv")
    csv_files = glob.glob(pattern)
    
    # Filter out any already merged files
    csv_files = [f for f in csv_files if 'merged' not in os.path.basename(f).lower()]
    
    if not csv_files:
        print("No SPY CSV files found to merge!")
        return
    
    print(f"Found {len(csv_files)} CSV files:")
    for file in sorted(csv_files):
        filename = os.path.basename(file)
        print(f"  - {filename}")
    
    # Ask for confirmation
    confirm = input(f"\nMerge {len(csv_files)} files into one? (y/n): ").strip().lower()
    if confirm not in ['y', 'yes']:
        print("Operation cancelled.")
        return
    
    # Load and merge all files
    print("\nLoading files...")
    all_dataframes = []
    total_records = 0
    
    for file_path in sorted(csv_files):
        try:
            df = pd.read_csv(file_path)
            
            # Basic validation
            required_cols = ['time', 'open', 'high', 'low', 'close', 'volume']
            if all(col in df.columns for col in required_cols):
                all_dataframes.append(df)
                total_records += len(df)
                print(f"  ✓ Loaded {os.path.basename(file_path)}: {len(df)} records")
            else:
                print(f"  ✗ Skipped {os.path.basename(file_path)}: Missing required columns")
                
        except Exception as e:
            print(f"  ✗ Error loading {os.path.basename(file_path)}: {e}")
    
    if not all_dataframes:
        print("No valid files to merge!")
        return
    
    print(f"\nMerging {len(all_dataframes)} files with {total_records:,} total records...")
    
    # Concatenate all dataframes
    merged_df = pd.concat(all_dataframes, ignore_index=True)
    
    # Convert time to datetime for sorting and duplicate removal
    merged_df['datetime_temp'] = pd.to_datetime(merged_df['time'])
    
    # Remove duplicates based on timestamp
    original_count = len(merged_df)
    merged_df = merged_df.drop_duplicates(subset=['time'], keep='first')
    duplicates_removed = original_count - len(merged_df)
    
    if duplicates_removed > 0:
        print(f"Removed {duplicates_removed:,} duplicate records")
    
    # Sort by time
    merged_df = merged_df.sort_values('datetime_temp')
    merged_df = merged_df.drop('datetime_temp', axis=1)
    merged_df = merged_df.reset_index(drop=True)
    
    # Generate output filename with current date
    current_date = datetime.now().strftime('%Y%m%d')
    output_filename = f"spy_5min_merged_complete_{current_date}.csv"
    output_path = os.path.join(historical_data_dir, output_filename)
    
    # Save merged file
    print(f"\nSaving merged data to: {output_filename}")
    merged_df.to_csv(output_path, index=False)
    
    # Get file size
    file_size_mb = os.path.getsize(output_path) / (1024 * 1024)
    
    # Show summary
    print("\n" + "=" * 60)
    print("MERGE COMPLETE!")
    print("=" * 60)
    print(f"Merged {len(all_dataframes)} files")
    print(f"Total records: {len(merged_df):,}")
    print(f"Date range: {merged_df['time'].iloc[0]} to {merged_df['time'].iloc[-1]}")
    print(f"File size: {file_size_mb:.1f} MB")
    print(f"Output file: {output_filename}")
    
    # Basic statistics
    print(f"\nData Summary:")
    print(f"  Price range: ${merged_df['low'].min():.2f} - ${merged_df['high'].max():.2f}")
    print(f"  Average daily volume: {merged_df['volume'].mean():,.0f}")
    print(f"  Total volume: {merged_df['volume'].sum():,.0f}")
    
    # Estimate trading days (approximately 78 5-minute bars per trading day)
    estimated_days = len(merged_df) / 78
    print(f"  Estimated trading days: {estimated_days:.0f}")
    
    # Create a quick summary file
    summary_filename = f"spy_5min_merged_summary_{current_date}.txt"
    summary_path = os.path.join(historical_data_dir, summary_filename)
    
    with open(summary_path, 'w') as f:
        f.write(f"SPY 5-Minute Historical Data - Merge Summary\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"=" * 50 + "\n\n")
        f.write(f"Source Files: {len(all_dataframes)} CSV files\n")
        f.write(f"Total Records: {len(merged_df):,}\n")
        f.write(f"Duplicates Removed: {duplicates_removed:,}\n")
        f.write(f"Date Range: {merged_df['time'].iloc[0]} to {merged_df['time'].iloc[-1]}\n")
        f.write(f"Price Range: ${merged_df['low'].min():.2f} - ${merged_df['high'].max():.2f}\n")
        f.write(f"File Size: {file_size_mb:.1f} MB\n")
        f.write(f"Output File: {output_filename}\n")
        f.write(f"\nFirst 5 records:\n")
        f.write(merged_df.head().to_string(index=False))
        f.write(f"\n\nLast 5 records:\n")
        f.write(merged_df.tail().to_string(index=False))
    
    print(f"\n✓ Summary saved to: {summary_filename}")
    print(f"\nYou can now use '{output_filename}' with your charting applications!")

if __name__ == "__main__":
    merge_spy_csv_files()
