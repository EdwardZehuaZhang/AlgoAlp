// Configuration constants for the SPY Multi-Chart application

export const CONFIG = {
    // API Configuration
    POLYGON_API_KEY: 'qdB8qbiJQcVUwqF3SqXxHJKVIABG4Saf',
    
    // File paths
    CSV_FILE_PATH: '../historical_data/spy_5min_merged_complete_20250611.csv',
    
    // Chart dimensions and styling
    CHART: {
        MAIN_HEIGHT_RATIO: 0.7,
        SUB_HEIGHT_RATIO: 0.3,
          // Color schemes
        COLORS: {            CSV_CHART: {
                UP_COLOR: '#089981',
                DOWN_COLOR: '#F23645',
                WICK_UP_COLOR: '#089981',
                WICK_DOWN_COLOR: '#F23645',
                SMA20_COLOR: 'rgba(253, 216, 53, 0.4)',
                SMA50_COLOR: 'rgba(224, 64, 251, 0.5)',
                SMA200_COLOR: 'rgba(41, 98, 255, 0.5)'  // 200-day SMA
            },            POLYGON_CHART: {
                UP_COLOR: '#089981',
                DOWN_COLOR: '#F23645',
                WICK_UP_COLOR: '#089981',
                WICK_DOWN_COLOR: '#F23645',
                SMA20_COLOR: 'rgba(253, 216, 53, 0.4)',
                SMA50_COLOR: 'rgba(224, 64, 251, 0.5)',
                SMA200_COLOR: 'rgba(41, 98, 255, 0.5)'  // 200-day SMA for Polygon chart
            },
            BACKGROUND: '#0f0f0f',
            TEXT: '#DDD',
            GRID: '#F0f3fa0f',
            BORDER: '#555',
            CROSSHAIR: '#9598A1'
        }
    },    // Date range for Polygon API (limited by free tier)
    DATE_RANGE: {
        START: '2025-05-02',  // Extended range to get maximum data from Polygon
        END: '2025-06-12'     // End date from CSV
    },
    
    // Market hours (in ET)
    MARKET_HOURS: {
        OPEN_MINUTES: 570,  // 9:30 AM
        CLOSE_MINUTES: 960  // 4:00 PM
    },
      // SMA periods
    SMA_PERIODS: {
        SHORT: 20,
        LONG: 50,
        EXTRA_LONG: 200
    }
};
