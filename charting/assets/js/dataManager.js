// Data loading and API management

import { CONFIG } from './config.js';
import { DataUtils } from './utils.js';

export class DataManager {
    constructor(chartManager) {
        this.chartManager = chartManager;
    }    /**
     * Load data from CSV file
     */
    async loadCSVData() {
        try {
            console.log('Loading CSV data...');
            const response = await fetch(CONFIG.CSV_FILE_PATH);
            const text = await response.text();
            
            // Load ALL CSV data (full 2-year dataset)
            const data = DataUtils.parseCSV(text);
            console.log('CSV data loaded (full dataset):', data.length, 'total points');
            
            if (data.length > 0) {
                console.log('CSV - First timestamp (raw):', data[0].time);
                console.log('CSV - First timestamp (date):', new Date(data[0].time * 1000));
                console.log('CSV - Last timestamp (date):', new Date(data[data.length-1].time * 1000));
                console.log('CSV - Date range:', new Date(data[0].time * 1000).toDateString(), 'to', new Date(data[data.length-1].time * 1000).toDateString());
            }
            
            // Calculate SMAs for full dataset
            const sma20Data = DataUtils.calculateSMA(data, CONFIG.SMA_PERIODS.SHORT);
            const sma50Data = DataUtils.calculateSMA(data, CONFIG.SMA_PERIODS.LONG);
            
            console.log('CSV - SMA calculations: SMA20:', sma20Data.length, 'SMA50:', sma50Data.length);
            
            // Update chart with full dataset
            this.chartManager.updateCSVChart(data, sma20Data, sma50Data);
            
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
            console.log(`Fetching Polygon data from ${CONFIG.DATE_RANGE.START} to ${CONFIG.DATE_RANGE.END}`);
            console.log('Note: Polygon free tier may not return all requested historical data');
            
            const url = `https://api.polygon.io/v2/aggs/ticker/SPY/range/5/minute/${CONFIG.DATE_RANGE.START}/${CONFIG.DATE_RANGE.END}`;
            
            const params = new URLSearchParams({
                adjusted: 'true',
                sort: 'asc',
                limit: '50000',
                apiKey: CONFIG.POLYGON_API_KEY
            });
            
            console.log(`Requesting: ${url}?${params.toString().replace(CONFIG.POLYGON_API_KEY, 'API_KEY_HIDDEN')}`);
            
            const response = await fetch(`${url}?${params.toString()}`);
            const json = await response.json();
            
            console.log('Polygon API response status:', json.status);
            
            if (json.results && json.results.length > 0) {
                console.log(`Received ${json.results.length} data points from Polygon API`);
                console.log('Polygon API data range:', 
                    new Date(json.results[0].t).toDateString(), 
                    'to', 
                    new Date(json.results[json.results.length-1].t).toDateString()
                );
                
                // Show debug info
                this.showDebugInfo(`Polygon: ${json.results.length} points (${new Date(json.results[0].t).toDateString()} - ${new Date(json.results[json.results.length-1].t).toDateString()})`);
                
                // Filter market hours
                const filteredData = DataUtils.filterMarketHours(
                    json.results, 
                    CONFIG.MARKET_HOURS.OPEN_MINUTES, 
                    CONFIG.MARKET_HOURS.CLOSE_MINUTES
                );
                
                console.log(`Filtered to ${filteredData.length} data points (market hours only)`);
                
                // Transform data
                const data = DataUtils.transformPolygonData(filteredData);
                
                console.log('Polygon - Processed data points:', data.length);
                if (data.length > 0) {
                    console.log('Polygon - First processed date:', new Date(data[0].time * 1000).toDateString());
                    console.log('Polygon - Last processed date:', new Date(data[data.length-1].time * 1000).toDateString());
                }
                
                // Calculate SMAs
                const sma20Data = DataUtils.calculateSMA(data, CONFIG.SMA_PERIODS.SHORT);
                const sma50Data = DataUtils.calculateSMA(data, CONFIG.SMA_PERIODS.LONG);
                
                // Update chart
                this.chartManager.updatePolygonChart(data, sma20Data, sma50Data);
                
            } else {
                console.warn('No results in Polygon API response. This might be due to:');
                console.warn('1. Free tier limits (typically ~2 years of data)');
                console.warn('2. Requested date range is too old');
                console.warn('3. API rate limits or other restrictions');
                
                // Show message on chart
                document.getElementById('sub-loading').textContent = 'No data available from Polygon API (free tier limits)';
                
                // Update debug info
                this.showDebugInfo('Polygon: No data (API limits)');
            }
            
        } catch (error) {
            console.error('Error loading Polygon data:', error);
            document.getElementById('sub-loading').textContent = 'Error loading data from Polygon. Check console for details.';
        }
    }
    
    /**
     * Show debug information on screen
     * @param {string} message - Debug message to display
     */
    showDebugInfo(message) {
        let debugDiv = document.getElementById('polygon-debug');
        if (!debugDiv) {
            debugDiv = document.createElement('div');
            debugDiv.id = 'polygon-debug';
            debugDiv.className = 'debug-info';
            document.body.appendChild(debugDiv);
        }
        debugDiv.textContent = message;
    }
}
