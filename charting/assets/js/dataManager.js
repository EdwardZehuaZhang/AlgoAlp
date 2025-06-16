// Data loading and API management

import { CONFIG } from './config.js';
import { DataUtils, IndicatorUtils, MarkerUtils, TimeUtils } from './utils.js';

export class DataManager {
    constructor(chartManager) {
        this.chartManager = chartManager;
    }
    
    /**
     * Load data from CSV file
     */
    async loadCSVData() {
        try {
            console.log('Loading CSV data...');
            const response = await fetch(CONFIG.CSV_FILE_PATH);
            const text = await response.text();
              // Load ALL CSV data (full 2-year dataset)
            const rawData = DataUtils.parseCSV(text);
            console.log('CSV data loaded (full dataset):', rawData.length, 'total points');
            
            // Filter to market hours only (9:30 AM - 4:00 PM)
            const data = DataUtils.filterMarketHours(rawData);
            console.log('CSV data filtered to market hours:', data.length, 'total points');
            
            if (data.length > 0) {
                console.log('CSV - First timestamp (raw):', data[0].time);
                console.log('CSV - First timestamp (date):', new Date(data[0].time * 1000));
                console.log('CSV - Last timestamp (date):', new Date(data[data.length-1].time * 1000));
                console.log('CSV - Date range:', new Date(data[0].time * 1000).toDateString(), 'to', new Date(data[data.length-1].time * 1000).toDateString());
            }
            
            // Calculate SMAs for filtered dataset
            const sma20Data = IndicatorUtils.calculateSMA(data, CONFIG.SMA_PERIODS.SHORT);
            const sma50Data = IndicatorUtils.calculateSMA(data, CONFIG.SMA_PERIODS.LONG);
            const sma200Data = IndicatorUtils.calculateSMA(data, CONFIG.SMA_PERIODS.EXTRA_LONG);
              // Calculate MACD for third pane (complete MACD with all components)
            const macdData = IndicatorUtils.calculateMACDComplete(data);
            
            // Calculate RSI for fourth pane
            const rsiData = IndicatorUtils.calculateRSI(data, 14); // 14-period RSI is standard
              
            // Calculate dynamic bar colors based on SMA crossovers
            const coloringResult = IndicatorUtils.calculateBarColors(data, sma50Data, sma200Data);
            const crossoverMarkers = MarkerUtils.createCrossoverMarkers(coloringResult.crossovers);
            
            console.log('CSV - SMA calculations: SMA20:', sma20Data.length, 'SMA50:', sma50Data.length, 'SMA200:', sma200Data.length);
            console.log('CSV - MACD data: Histogram:', macdData.histogram.length, 'MACD Line:', macdData.macdLine.length, 'Signal Line:', macdData.signalLine.length);
            console.log('CSV - RSI data:', rsiData.length, 'points');
            console.log('CSV - Bar coloring: Applied colors to', coloringResult.coloredData.length, 'bars, found', coloringResult.crossovers.length, 'crossovers');
            
            // Update chart with colored data and markers
            this.chartManager.updateCSVChart(coloringResult.coloredData, sma20Data, sma50Data, sma200Data, crossoverMarkers);
            
            // Update MACD chart with all components
            this.chartManager.updateMACDChart(macdData.histogram, macdData.macdLine, macdData.signalLine);
            
            // Update RSI chart
            this.chartManager.updateRSIChart(rsiData);
            
        } catch (error) {
            console.error('Error loading CSV data:', error);
            document.getElementById('main-loading').textContent = 'Error loading CSV data. Check console for details.';
        }
    }
    
    /**
     * Load data from Polygon API
     */
    async loadPolygonData() {
        try {
            console.log('Loading Polygon data...');
            const apiKey = CONFIG.POLYGON_API_KEY;
            const startDate = CONFIG.DATE_RANGE.START;
            const endDate = CONFIG.DATE_RANGE.END;
            const symbol = 'SPY';
            const multiplier = 5;
            const timespan = 'minute';
            
            const url = `https://api.polygon.io/v2/aggs/ticker/${symbol}/range/${multiplier}/${timespan}/${startDate}/${endDate}?apiKey=${apiKey}&limit=50000`;
              console.log('Polygon API URL:', url);
            document.getElementById('sub-loading').textContent = 'Fetching data from Polygon API...';
              let apiData;
            try {
                const response = await fetch(url);
                
                if (!response.ok) {
                    throw new Error(`HTTP error: ${response.status} - ${response.statusText}`);
                }
                
                apiData = await response.json();
                
                if (apiData.status === 'ERROR' || !apiData.results) {
                    throw new Error(apiData.error || 'Unknown API error');
                }
            } catch (networkError) {
                console.error('Network error when fetching Polygon data:', networkError);
                document.getElementById('sub-loading').textContent = 'Polygon API connection failed. Internet connection issue or API may be down.';
                // Return early since we can't proceed without data
                return;
            }
            
            document.getElementById('sub-loading').textContent = 'Processing Polygon data...';
            
            // Transform API data to chart format
            const data = DataUtils.transformPolygonData(apiData.results);
            console.log('Polygon data loaded:', data.length, 'total points');
            
            if (data.length > 0) {
                console.log('Polygon - First timestamp (raw):', data[0].time);
                console.log('Polygon - First timestamp (date):', new Date(data[0].time * 1000));
                console.log('Polygon - Last timestamp (date):', new Date(data[data.length-1].time * 1000));
                console.log('Polygon - Date range:', new Date(data[0].time * 1000).toDateString(), 'to', new Date(data[data.length-1].time * 1000).toDateString());
            }
            
            // Filter to market hours only
            const marketHoursData = DataUtils.filterMarketHours(data);
            console.log('Filtered to market hours:', marketHoursData.length, 'data points');
                    
            // Calculate SMAs for Polygon data
            const sma20Data = IndicatorUtils.calculateSMA(marketHoursData, CONFIG.SMA_PERIODS.SHORT);            const sma50Data = IndicatorUtils.calculateSMA(marketHoursData, CONFIG.SMA_PERIODS.LONG);
            const sma200Data = IndicatorUtils.calculateSMA(marketHoursData, CONFIG.SMA_PERIODS.EXTRA_LONG);
            
            // Calculate MACD for third pane
            const macdData = IndicatorUtils.calculateMACDComplete(marketHoursData);
            
            // Calculate RSI for fourth pane
            const rsiData = IndicatorUtils.calculateRSI(marketHoursData, 14);
            
            console.log('Polygon - SMA calculations: SMA20:', sma20Data.length, 'SMA50:', sma50Data.length, 'SMA200:', sma200Data.length);
            console.log('Polygon - MACD data:', macdData.histogram.length, 'points');
            console.log('Polygon - RSI data:', rsiData.length, 'points');
                
            // Update chart with Polygon data
            this.chartManager.updatePolygonChart(marketHoursData, sma20Data, sma50Data, sma200Data);
            
            // Update indicator charts
            this.chartManager.updateMACDChart(macdData.histogram, macdData.macdLine, macdData.signalLine);
            this.chartManager.updateRSIChart(rsiData);
            
        } catch (error) {
            console.error('Error loading Polygon data:', error);
            document.getElementById('sub-loading').textContent = 'Error loading Polygon data. Check console for details.';
            
            // If this is a rate limit error or authentication error, provide specific guidance
            if (error.message && (error.message.includes('rate limit') || error.message.includes('auth'))) {
                document.getElementById('sub-loading').textContent += ' API key may be invalid or rate limited.';
            }
        }
    }
}
