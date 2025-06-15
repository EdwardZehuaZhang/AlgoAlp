// Price Chart Manager - Extends BaseChartManager to handle price charts

import { BaseChartManager } from './BaseChartManager.js';
import { CONFIG } from '../config.js';

export class PriceChartManager extends BaseChartManager {
    constructor() {
        super();
        
        // Price Series
        this.mainSeries = null;
        this.mainSeriesId = 'main_series';
        
        // Moving Averages
        this.smaLines = new Map();
    }
    
    /**
     * Initialize a price chart
     * @param {string} containerId - ID of the container element
     * @param {Object} options - Additional chart options
     */
    initPriceChart(containerId, options = {}) {
        // Initialize the base chart
        const success = this.initChart(containerId, options);
        if (!success) return false;
        
        // Add the main price series
        this.mainSeries = this.addSeries(LightweightCharts.CandlestickSeries, {
            id: this.mainSeriesId,
            upColor: CONFIG.CHART.COLORS.CSV_CHART.UP_COLOR,
            downColor: CONFIG.CHART.COLORS.CSV_CHART.DOWN_COLOR,
            wickUpColor: CONFIG.CHART.COLORS.CSV_CHART.WICK_UP_COLOR,
            wickDownColor: CONFIG.CHART.COLORS.CSV_CHART.WICK_DOWN_COLOR,
            borderVisible: false,
            title: 'Price',
            priceFormat: {
                type: 'price',
                precision: 2,
                minMove: 0.01,
            }
        }, 0);
        
        return !!this.mainSeries;
    }
    
    /**
     * Add a Moving Average line to the chart
     * @param {string} id - Unique ID for the MA line
     * @param {number} period - MA period (e.g., 20, 50, 200)
     * @param {string} color - Line color
     * @param {number} width - Line width
     * @param {number} paneIndex - Pane index (default: 0, same as price series)
     */
    addSMA(id, period, color, width = 2, paneIndex = 0) {
        const smaLine = this.addSeries(LightweightCharts.LineSeries, {
            id: `sma_${id}`,
            color: color,
            lineWidth: width,
            priceLineVisible: false,
            lastValueVisible: true,
            title: `SMA ${period}`,
        }, paneIndex);
        
        if (smaLine) {
            this.smaLines.set(id, {
                series: smaLine,
                period: period
            });
        }
        
        return smaLine;
    }
    
    /**
     * Update the main price series data
     * @param {Array} data - Price data array
     */
    updatePriceData(data) {
        if (!this.mainSeries || !data || data.length === 0) return false;
        
        try {
            this.mainSeries.setData(data);
            return true;
        } catch (error) {
            console.error('Error updating price data:', error);
            return false;
        }
    }
    
    /**
     * Update a specific SMA line with data
     * @param {string} id - SMA ID
     * @param {Array} data - SMA data points
     */
    updateSMA(id, data) {
        if (!this.smaLines.has(id)) {
            console.error(`SMA line with ID ${id} not found`);
            return false;
        }
        
        try {
            const smaInfo = this.smaLines.get(id);
            smaInfo.series.setData(data);
            return true;
        } catch (error) {
            console.error(`Error updating SMA ${id}:`, error);
            return false;
        }
    }
    
    /**
     * Set markers on the main price series
     * @param {Array} markers - Marker objects
     */
    setPriceMarkers(markers) {
        if (!this.mainSeries) return false;
        
        try {
            this.mainSeries.setMarkers(markers);
            return true;
        } catch (error) {
            console.error('Error setting price markers:', error);
            return false;
        }
    }
    
    /**
     * Apply dynamic coloring to price bars
     * @param {Array} coloredData - Array of bar data with color property
     */
    setColoredBars(coloredData) {
        if (!this.mainSeries || !coloredData) return false;
        
        try {
            this.mainSeries.setData(coloredData);
            return true;
        } catch (error) {
            console.error('Error setting colored bars:', error);
            return false;
        }
    }
}
