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
        COLORS: {
            CSV_CHART: {
                UP_COLOR: '#26a69a',
                DOWN_COLOR: '#ef5350',
                WICK_UP_COLOR: '#26a69a',
                WICK_DOWN_COLOR: '#ef5350',
                SMA20_COLOR: '#2962FF',
                SMA50_COLOR: '#FF6D00'
            },
            POLYGON_CHART: {
                UP_COLOR: '#4CAF50',
                DOWN_COLOR: '#F44336',
                WICK_UP_COLOR: '#4CAF50',
                WICK_DOWN_COLOR: '#F44336',
                SMA20_COLOR: '#9C27B0',
                SMA50_COLOR: '#00BCD4'
            },
            BACKGROUND: '#222',
            TEXT: '#DDD',
            GRID: '#444',
            BORDER: '#555'
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
        LONG: 50
    }
};
