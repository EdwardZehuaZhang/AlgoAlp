// Main Chart Manager for SPY charts with multiple panes

import { CONFIG } from '../config.js';
import { PriceChartManager } from './PriceChartManager.js';
import { IndicatorChartManager } from './IndicatorChartManager.js';
import { ChartInteractionManager } from './ChartInteractionManager.js';
import { MarkerUtils } from '../utils/markerUtils.js';

export class ChartManager {
    constructor() {
        // Main components
        this.priceChart = new PriceChartManager();
        this.indicatorChart = null; // Will be initialized with the price chart
        this.interactionManager = null; // Will be initialized after charts
        
        // Series references
        this.csvSeries = null;
        this.polygonSeries = null;
        this.csvSMA20Line = null;
        this.csvSMA50Line = null;
        this.csvSMA200Line = null;
        this.polygonSMA20Line = null;
        this.polygonSMA50Line = null;
        this.polygonSMA200Line = null;
          // MACD Indicator series for third pane
        this.macdHistogramSeries = null;  // MACD Histogram for pane 2
        this.macdLineSeries = null;       // MACD Line for pane 2
        this.macdSignalSeries = null;     // MACD Signal Line for pane 2
        this.macdMarkers = null;          // MACD crossover markers
        
        // RSI Indicator series for fourth pane
        this.rsiSeries = null;           // RSI Line for pane 3
        this.rsiOverboughtLine = null;    // RSI Overbought Level (70)
        this.rsiOversoldLine = null;      // RSI Oversold Level (30)
        
        // Series markers for crossover events
        this.csvMarkers = null;           // CSV series markers
        this.polygonMarkers = null;       // Polygon series markers
        this.goldenDeathCrossMarkers = null;    // Golden/Death cross markers for polygon series
        this.goldenDeathCrossMarkersPlugin = null;  // Plugin reference for golden/death cross markers
    }
    
    /**
     * Initialize the chart with multiple panes
     */
    createCharts() {
        this.createSingleChartWithPanes();
        this.setupEventListeners();
    }
    
    /**
     * Create a single chart with multiple panes
     */
    createSingleChartWithPanes() {
        const container = document.getElementById('main-chart-container');
        
        console.log('Creating chart in container:', container.id);
        
        const chartOptions = {
            width: container.clientWidth,
            height: container.clientHeight,
            layout: {
                background: { color: CONFIG.CHART.COLORS.BACKGROUND },
                textColor: CONFIG.CHART.COLORS.TEXT,
                panes: {
                    separatorColor: '#2E2E2E',
                    separatorHoverColor: 'rgba(41, 98, 255, 0.2)',
                    enableResize: true,
                }
            },
            grid: {
                vertLines: { color: CONFIG.CHART.COLORS.GRID },
                horzLines: { color: CONFIG.CHART.COLORS.GRID },
            },
            rightPriceScale: {
                borderColor: CONFIG.CHART.COLORS.BORDER,
            },            timeScale: {
                borderColor: CONFIG.CHART.COLORS.BORDER,
                timeVisible: true,
                secondsVisible: false,
                // Don't use automatic time conversion
                fixRightEdge: true,
                fixLeftEdge: true,
                // Use the custom formatter to ensure correct time display
                tickMarkFormatter: (timestamp) => {
                    // Create a date object and use UTC methods to avoid timezone conversions
                    const date = new Date(timestamp * 1000);
                    const hours = date.getUTCHours();
                    const minutes = date.getUTCMinutes();
                    return `${hours.toString().padStart(2, '0')}:${minutes.toString().padStart(2, '0')}`;
                },
            },
            localization: {
                // Force to use UTC for all time calculations
                locale: 'en-US',
                timeZone: 'UTC',
            },
            crosshair: {
                mode: LightweightCharts.CrosshairMode.Normal,
                vertLine: {
                    color: CONFIG.CHART.COLORS.CROSSHAIR,
                },
                horzLine: {
                    color: CONFIG.CHART.COLORS.CROSSHAIR,
                },
            },
        };
        
        // Initialize main chart
        console.log('Initializing price chart...');
        const success = this.priceChart.initChart(container.id, chartOptions);
        
        if (!success) {
            console.error('Failed to initialize price chart');
            return;
        }
        
        console.log('Price chart initialized successfully');
        
        // Create basic series structure
        this.createInitialSeries();
        
        // Set up interaction manager
        console.log('Setting up interaction manager...');
        this.interactionManager = new ChartInteractionManager(this.priceChart);
        this.interactionManager.init();
        
        console.log('Chart initialization completed');
    }
    
    /**
     * Create initial series structure
     */
    createInitialSeries() {
        // Create base chart first
        this.chart = this.priceChart.chart; // Reference for compatibility
        
        // First make sure we have enough panes (at least 3: CSV, Polygon, MACD)
        if (typeof this.chart.addPane === 'function') {
            try {
                // Add two more panes (we already have the default pane 0)
                this.chart.addPane({ height: 200 }); // Polygon pane (index 1)
                this.chart.addPane({ height: 150 }); // MACD pane (index 2)
                console.log('Created 3-pane layout for charts');
            } catch (error) {
                console.warn('Error creating additional panes:', error);
            }
        }
        
        // Add CSV data series to pane 0 (default pane)
        this.csvSeries = this.priceChart.addSeries(LightweightCharts.BarSeries, {
            id: 'csv_series',
            upColor: CONFIG.CHART.COLORS.CSV_CHART.UP_COLOR,
            downColor: CONFIG.CHART.COLORS.CSV_CHART.DOWN_COLOR,
            openVisible: true,  // Show open lines on bars
            thinBars: true,     // Prevent bars from becoming too thick when zooming
            title: 'CSV History',
        }, 0); // Pane index 0
        
        // Add CSV SMA lines to the same pane        
        this.csvSMA20Line = this.priceChart.addSeries(LightweightCharts.LineSeries, {
            id: 'csv_sma20',
            color: CONFIG.CHART.COLORS.CSV_CHART.SMA20_COLOR,
            lineWidth: 2,
            priceLineVisible: false,
            title: 'CSV SMA 20',
        }, 0); // Pane index 0

        this.csvSMA50Line = this.priceChart.addSeries(LightweightCharts.LineSeries, {
            id: 'csv_sma50',
            color: CONFIG.CHART.COLORS.CSV_CHART.SMA50_COLOR,
            lineWidth: 2,
            priceLineVisible: false,
            title: 'CSV SMA 50',
        }, 0); // Pane index 0

        this.csvSMA200Line = this.priceChart.addSeries(LightweightCharts.LineSeries, {
            id: 'csv_sma200',
            color: CONFIG.CHART.COLORS.CSV_CHART.SMA200_COLOR,
            lineWidth: 2,
            priceLineVisible: false,
            title: 'CSV SMA 200',
        }, 0); // Pane index 0

        // Add Polygon data series to pane 1 (separate from CSV)
        this.polygonSeries = this.priceChart.addSeries(LightweightCharts.BarSeries, {
            id: 'polygon_series',
            upColor: CONFIG.CHART.COLORS.POLYGON_CHART.UP_COLOR,
            downColor: CONFIG.CHART.COLORS.POLYGON_CHART.DOWN_COLOR,
            openVisible: true,
            thinBars: true,
            title: 'Polygon API',
        }, 1); // Pane index 1 (second pane)

        // Add Polygon SMA lines to pane 1 (same as Polygon data)
        this.polygonSMA20Line = this.priceChart.addSeries(LightweightCharts.LineSeries, {
            id: 'polygon_sma20',
            color: CONFIG.CHART.COLORS.POLYGON_CHART.SMA20_COLOR,
            lineWidth: 2,
            priceLineVisible: false,
            title: 'Polygon SMA 20',
        }, 1); // Pane index 1 (second pane)

        this.polygonSMA50Line = this.priceChart.addSeries(LightweightCharts.LineSeries, {
            id: 'polygon_sma50',
            color: CONFIG.CHART.COLORS.POLYGON_CHART.SMA50_COLOR,
            lineWidth: 2,
            priceLineVisible: false,
            title: 'Polygon SMA 50',
        }, 1); // Pane index 1 (second pane)

        this.polygonSMA200Line = this.priceChart.addSeries(LightweightCharts.LineSeries, {
            id: 'polygon_sma200',
            color: CONFIG.CHART.COLORS.POLYGON_CHART.SMA200_COLOR,
            lineWidth: 2,
            priceLineVisible: false,
            title: 'Polygon SMA 200',
        }, 1); // Pane index 1 (second pane)
        
        // Create MACD indicator in pane 2
        this.indicatorChart = new IndicatorChartManager();
        
        // Ensure the indicator chart uses the same underlying chart instance
        if (this.priceChart && this.priceChart.chart) {
            console.log('Initializing indicator chart with parent chart');
            this.indicatorChart.initWithParent(this.priceChart);
            
            // Add MACD indicator to pane 2 (third pane)
            try {
                const macdComponents = this.indicatorChart.addMACDIndicator(2);
                if (macdComponents) {
                    console.log('MACD components created successfully');
                    this.macdHistogramSeries = macdComponents.histogram;
                    this.macdLineSeries = macdComponents.macdLine;
                    this.macdSignalSeries = macdComponents.signalLine;
                } else {
                    console.warn('MACD components not created, possibly chart not initialized');
                }
            } catch (error) {
                console.error('Error adding MACD indicator:', error);
            }
        } else {
            console.error('Cannot initialize indicator chart: main chart not available');
        }
    }
    
    /**
     * Set up event listeners for the chart
     */
    setupEventListeners() {
        // Handle window resize
        window.addEventListener('resize', () => {
            if (this.chart) {
                const container = document.getElementById('main-chart-container');
                this.chart.resize(container.clientWidth, container.clientHeight);
            }
        });
    }
    
    /**
     * Update CSV chart data
     * @param {Array} data - CSV bar data
     * @param {Array} sma20Data - SMA 20 data
     * @param {Array} sma50Data - SMA 50 data
     * @param {Array} sma200Data - SMA 200 data
     * @param {Array} markers - Optional markers
     */
    updateCSVChart(data, sma20Data, sma50Data, sma200Data, markers = []) {
        if (this.csvSeries) {
            this.csvSeries.setData(data);
        }
        
        if (this.csvSMA20Line && sma20Data) {
            this.csvSMA20Line.setData(sma20Data);
        }
        
        if (this.csvSMA50Line && sma50Data) {
            this.csvSMA50Line.setData(sma50Data);
        }
        
        if (this.csvSMA200Line && sma200Data) {
            this.csvSMA200Line.setData(sma200Data);
        }
        
        if (markers && markers.length > 0) {
            this.csvMarkers = markers;
            this._setMarkersSafely(this.csvSeries, markers, 'csv_series');
        }
        
        // Hide loading indicator
        document.getElementById('main-loading').style.display = 'none';
    }
    
    /**
     * Update Polygon chart data
     * @param {Array} data - Polygon bar data
     * @param {Array} sma20Data - SMA 20 data
     * @param {Array} sma50Data - SMA 50 data
     * @param {Array} sma200Data - SMA 200 data
     * @param {Array} markers - Optional markers
     */    updatePolygonChart(data, sma20Data, sma50Data, sma200Data, markers = []) {
        console.log('Applying manual 4-hour shift to Polygon data timestamps');
        
        // Manually adjust all timestamps by subtracting 4 hours
        const shiftedData = this._shiftTimestamps(data);
        const shiftedSMA20 = this._shiftTimestamps(sma20Data);
        const shiftedSMA50 = this._shiftTimestamps(sma50Data);
        const shiftedSMA200 = this._shiftTimestamps(sma200Data);
        
        // Log first few items to verify the shift
        if (data.length > 0 && shiftedData.length > 0) {
            console.log('Original first timestamp:', data[0].time, '→', new Date(data[0].time * 1000).toLocaleTimeString());
            console.log('Shifted first timestamp:', shiftedData[0].time, '→', new Date(shiftedData[0].time * 1000).toLocaleTimeString());
        }
        
        if (this.polygonSeries) {
            this.polygonSeries.setData(shiftedData);
        }
        
        if (this.polygonSMA20Line && shiftedSMA20) {
            this.polygonSMA20Line.setData(shiftedSMA20);
        }
        
        if (this.polygonSMA50Line && shiftedSMA50) {
            this.polygonSMA50Line.setData(shiftedSMA50);
        }
        
        if (this.polygonSMA200Line && shiftedSMA200) {
            this.polygonSMA200Line.setData(shiftedSMA200);
        }
        
        // Add Golden Cross and Death Cross markers to the polygon chart
        if (shiftedSMA50 && shiftedSMA200 && shiftedSMA50.length > 0 && shiftedSMA200.length > 0) {
            console.log('Adding Golden/Death cross markers to polygon chart...');
            try {
                this.addGoldenDeathCrossMarkers(shiftedSMA50, shiftedSMA200);
            } catch (error) {
                console.error('Error adding Golden/Death cross markers to polygon chart:', error);
            }
        } else {
            console.log('Skipping Golden/Death cross markers - insufficient SMA data');
        }
          if (markers && markers.length > 0) {
            // Shift marker timestamps too
            const shiftedMarkers = markers.map(marker => {
                return {
                    ...marker,
                    time: marker.time - (4 * 3600) // Subtract 4 hours in seconds
                };
            });
            
            this.polygonMarkers = shiftedMarkers;
            this._setMarkersSafely(this.polygonSeries, shiftedMarkers, 'polygon_series');
        }
        
        // Hide loading indicator
        document.getElementById('sub-loading').style.display = 'none';
    }
    
    /**
     * Update MACD chart
     * @param {Array} histogramData - MACD histogram data
     * @param {Array} macdLineData - MACD line data
     * @param {Array} signalLineData - Signal line data
     */    updateMACDChart(histogramData, macdLineData, signalLineData) {
        if (!this.indicatorChart) {
            console.warn('Indicator chart not initialized, attempting to initialize it now...');
            
            // Try to initialize the indicator chart if it doesn't exist
            this.indicatorChart = new IndicatorChartManager();
            if (this.priceChart && this.priceChart.chart) {
                this.indicatorChart.initWithParent(this.priceChart);
                
                // Try to create MACD components
                try {
                    const macdComponents = this.indicatorChart.addMACDIndicator(2);
                    if (macdComponents) {
                        this.macdHistogramSeries = macdComponents.histogram;
                        this.macdLineSeries = macdComponents.macdLine;
                        this.macdSignalSeries = macdComponents.signalLine;
                        console.log('MACD components initialized on-demand');
                    } else {
                        console.warn('Failed to create MACD components on-demand');
                    }
                } catch (error) {
                    console.error('Error creating MACD components on-demand:', error);
                }
            } else {
                console.error('Cannot initialize indicator chart: price chart not available');
                return;
            }
        }
          // Apply the same 4-hour shift to MACD data
        // But preserve the original timestamps in a separate field for crossover detection
        const shiftedHistogram = this._shiftTimestamps(histogramData, 4, true);
        const shiftedMacdLine = this._shiftTimestamps(macdLineData, 4, true);
        const shiftedSignalLine = this._shiftTimestamps(signalLineData, 4, true);
        
        // Now attempt to update the MACD data
        try {
            // Direct updates if we have the series references
            if (this.macdHistogramSeries && shiftedHistogram && shiftedHistogram.length > 0) {
                console.log('Updating MACD histogram directly');
                this.macdHistogramSeries.setData(shiftedHistogram);
            }
            
            if (this.macdLineSeries && shiftedMacdLine && shiftedMacdLine.length > 0) {
                console.log('Updating MACD line directly');
                this.macdLineSeries.setData(shiftedMacdLine);
            }
            
            if (this.macdSignalSeries && shiftedSignalLine && shiftedSignalLine.length > 0) {
                console.log('Updating MACD signal line directly');
                this.macdSignalSeries.setData(shiftedSignalLine);
            }
              // Try through the indicator chart's update method
            try {
                this.indicatorChart.updateMACDData(histogramData, macdLineData, signalLineData);
            } catch (error) {
                console.warn('Error using indicator chart update method:', error);
                // Already tried direct updates above, so not doing anything else here
            }
            
            // Add MACD crossover markers if we have both line series
            if (shiftedMacdLine && shiftedMacdLine.length > 0 && 
                shiftedSignalLine && shiftedSignalLine.length > 0) {
                // We need to pass the original (unshifted) data since the addMACDMarkers method 
                // will apply the time shift internally
                this.addMACDMarkers(macdLineData, signalLineData);
            }
            
        } catch (error) {
            console.error('Error updating MACD chart:', error);
        }
    }    /**
     * Add MACD crossover markers
     * @param {Array} macdLineData - MACD line data
     * @param {Array} signalLineData - Signal line data
     */
    addMACDMarkers(macdLineData, signalLineData) {
        if (!macdLineData || !signalLineData || macdLineData.length === 0 || signalLineData.length === 0) {
            console.log('Cannot add MACD markers: Missing or empty data');
            return;
        }
        
        console.log('Adding MACD crossover markers...');
        
        try {
            // Calculate crossover points
            const crossovers = MarkerUtils.calculateMACDCrossovers(macdLineData, signalLineData);
            console.log(`Found ${crossovers.length} MACD crossovers`);
            
            if (crossovers.length === 0) {
                console.log('No MACD crossovers found - nothing to display');
                return;
            }
              // Don't apply time shift here - use the correct display time that's already set
            // This is crucial - the time in crossovers already matches our chart display time
            const shiftedCrossovers = crossovers;
            
            // Log some crossovers for debugging
            if (shiftedCrossovers.length > 0) {
                console.log('First few MACD crossovers:');
                shiftedCrossovers.slice(0, 3).forEach((c, i) => {
                    console.log(`Crossover ${i+1} - ${c.type} at ${new Date(c.time * 1000).toLocaleTimeString()}`);
                });
            }
            
            // Create formatted markers for the chart
            const markers = MarkerUtils.createMACDCrossoverMarkers(shiftedCrossovers);
            
            if (!this.macdLineSeries) {
                console.warn('MACD line series not available for setting markers');
                return;
            }
            
            // Store marker reference
            this.macdMarkers = markers;
            
            // Use the proper createSeriesMarkers function from the LightweightCharts library
            // This is the key change - using createSeriesMarkers instead of setMarkers
            try {
                console.log('Applying MACD crossovers using createSeriesMarkers...');
                console.log('Markers:', markers.slice(0, 3)); // Log first few markers for debug
                  if (typeof window.createSeriesMarkers === 'function') {
                    // Use the global createSeriesMarkers function
                    console.log('Using global window.createSeriesMarkers function');
                    this.macdMarkersPlugin = window.createSeriesMarkers(this.macdLineSeries, markers);
                    console.log('MACD markers successfully created with createSeriesMarkers');
                } else {
                    console.warn('createSeriesMarkers function not available, trying alternative method');
                    
                    // Fall back to direct method if available
                    if (typeof this.macdLineSeries.setMarkers === 'function') {
                        this.macdLineSeries.setMarkers(markers);
                        console.log('MACD markers set with direct setMarkers method');
                    } else if (this.indicatorChart && typeof this.indicatorChart.addMACDMarkers === 'function') {
                        // Try through the indicator chart if it has a method for it
                        this.indicatorChart.addMACDMarkers(markers);
                        console.log('MACD markers added through indicator chart');
                    } else {
                        console.error('No method available to add MACD markers');
                    }
                }
            } catch (markerError) {
                console.error('Error applying MACD markers:', markerError);
                
                // Last resort: try the older _setMarkersSafely method
                console.log('Attempting to set MACD crossover markers through wrapper');
                this._setMarkersSafely(this.macdLineSeries, markers, 'macd_line');
            }
            
            console.log(`MACD crossover markers added: ${markers.length} markers`);
        } catch (error) {
            console.error('Error adding MACD crossover markers:', error);
        }
    }
      /**
     * Clear all chart data
     */
    clearCharts() {
        // Clear price chart data
        if (this.csvSeries) this.csvSeries.setData([]);
        if (this.csvSMA20Line) this.csvSMA20Line.setData([]);
        if (this.csvSMA50Line) this.csvSMA50Line.setData([]);
        if (this.csvSMA200Line) this.csvSMA200Line.setData([]);
        
        if (this.polygonSeries) this.polygonSeries.setData([]);
        if (this.polygonSMA20Line) this.polygonSMA20Line.setData([]);
        if (this.polygonSMA50Line) this.polygonSMA50Line.setData([]);
        if (this.polygonSMA200Line) this.polygonSMA200Line.setData([]);
        
        // Clear markers
        this.csvMarkers = null;
        this.polygonMarkers = null;
        this.goldenDeathCrossMarkers = null;
        
        // Clean up marker plugins
        if (this.goldenDeathCrossMarkersPlugin) {
            try {
                this.goldenDeathCrossMarkersPlugin.setMarkers([]);
            } catch (e) {
                console.warn('Error clearing golden/death cross markers:', e);
            }
            this.goldenDeathCrossMarkersPlugin = null;
        }
        
        // Clear indicator data
        if (this.indicatorChart) {
            this.indicatorChart.updateMACDData([], [], []);
            this.indicatorChart.updateRSIData([]);
        }
        
        // Clear series references
        if (this.rsiSeries) this.rsiSeries.setData([]);
    }
    
    /**
     * Show or hide a specific data source
     * @param {string} source - Data source ('csv', 'polygon', 'both')
     */
    showDataSource(source) {
        // Show/hide CSV data
        const showCSV = source === 'csv' || source === 'both';
        if (this.csvSeries) this.csvSeries.applyOptions({ visible: showCSV });
        if (this.csvSMA20Line) this.csvSMA20Line.applyOptions({ visible: showCSV });
        if (this.csvSMA50Line) this.csvSMA50Line.applyOptions({ visible: showCSV });
        if (this.csvSMA200Line) this.csvSMA200Line.applyOptions({ visible: showCSV });
        
        // Show/hide Polygon data
        const showPolygon = source === 'polygon' || source === 'both';
        if (this.polygonSeries) this.polygonSeries.applyOptions({ visible: showPolygon });
        if (this.polygonSMA20Line) this.polygonSMA20Line.applyOptions({ visible: showPolygon });
        if (this.polygonSMA50Line) this.polygonSMA50Line.applyOptions({ visible: showPolygon });
        if (this.polygonSMA200Line) this.polygonSMA200Line.applyOptions({ visible: showPolygon });
    }
    
    /**
     * Clean up resources
     */
    destroy() {
        // Clean up interaction manager
        if (this.interactionManager) {
            this.interactionManager.destroy();
        }
        
        // Clean up charts
        if (this.indicatorChart) {
            this.indicatorChart.destroy();
        }
        
        if (this.priceChart) {
            this.priceChart.destroy();
        }
    }
      /**
     * Helper method to properly set markers on a series
     * @param {Object} series - The series object to set markers on
     * @param {Array} markers - The markers to set
     * @param {string} seriesId - Series identifier for logging
     * @returns {boolean} True if markers were set successfully
     * @private
     */
    _setMarkersSafely(series, markers, seriesId) {
        // Basic input validation
        if (!series) {
            console.warn(`Cannot set markers: series object (${seriesId}) is not defined`);
            return false;
        }
        
        if (!markers || !markers.length) {
            console.warn(`Cannot set markers: empty markers array for ${seriesId}`);
            return false;
        }
        
        // Don't try to add markers to candlestick series as they don't support them in v5
        if (seriesId === 'csv_series' || seriesId === 'polygon_series') {
            console.log(`Skipping marker addition for ${seriesId} - candlestick series doesn't support markers in this version`);
            return false;
        }
        
        console.log(`Attempting to set ${markers.length} markers on ${seriesId}`);
        console.log('First marker:', markers[0]);
        
        try {
            // Use createSeriesMarkers for Lightweight Charts v5+
            if (typeof window.createSeriesMarkers === 'function') {
                console.log(`Setting ${markers.length} markers on ${seriesId} using createSeriesMarkers`);
                window.createSeriesMarkers(series, markers);
                return true;
            }
            
            // Try direct method next (for backwards compatibility)
            if (typeof series.setMarkers === 'function') {
                console.log(`Setting ${markers.length} markers on ${seriesId} using setMarkers()`);
                series.setMarkers(markers);
                return true;
            } 
            
            // Try through the series API if available
            else if (series.api && typeof series.api.setMarkers === 'function') {
                console.log(`Setting ${markers.length} markers on ${seriesId} using series.api`);
                series.api.setMarkers(markers);
                return true;
            }
            
            // If all else fails
            console.warn(`Could not set markers on ${seriesId}: No compatible method found`);
            return false;
        } catch (error) {
            console.error(`Error setting markers on ${seriesId}:`, error);
            console.error(error.stack);
            return false;
        }
    }
      /**
     * Helper method to shift timestamps by a fixed offset (for timezone correction)
     * @param {Array} data - Data points with time field
     * @param {number} hourOffset - Hours to subtract from timestamp (default 4 for ET adjustment)
     * @param {boolean} preserveOriginal - Whether to preserve original timestamps in a separate field (default false)
     * @returns {Array} New array with adjusted timestamps
     * @private
     */
    _shiftTimestamps(data, hourOffset = 4, preserveOriginal = false) {
        if (!data || data.length === 0) return [];
        
        // Calculate the offset in seconds
        const offsetSeconds = hourOffset * 3600;
        
        // Create a new array with adjusted timestamps
        return data.map(item => {
            // Create a shallow copy of the item
            const adjusted = { ...item };
            
            // If we should preserve the original time, store it before modifying
            if (preserveOriginal) {
                adjusted.originalTime = item.originalTime || item.time;
            }
            
            // Subtract the offset from the timestamp
            adjusted.time = item.time - offsetSeconds;
            
            return adjusted;
        });
    }
    
    /**
     * Update RSI chart data
     * @param {Array} rsiData - RSI line data
     */
    updateRSIChart(rsiData) {
        if (!this.indicatorChart) {
            console.warn('Indicator chart not initialized, attempting to initialize it now...');
            
            // Try to initialize the indicator chart if it doesn't exist
            this.indicatorChart = new IndicatorChartManager();
            if (this.priceChart && this.priceChart.chart) {
                this.indicatorChart.initWithParent(this.priceChart);
                
                // Try to create RSI components
                try {
                    const rsiComponents = this.indicatorChart.addRSIIndicator(3); // Use pane index 3 (fourth pane)
                    if (rsiComponents) {
                        // Use the correct ID (rsi_line instead of rsi) to match the series created in IndicatorChartManager
                        this.rsiSeries = rsiComponents.rsi_line;
                        this.rsiOverboughtLine = rsiComponents.overboughtLevel;
                        this.rsiOversoldLine = rsiComponents.oversoldLevel;
                        console.log('RSI components initialized on-demand');
                        // Log the series ID for debugging
                        if (this.rsiSeries) {
                            console.log('RSI series ID:', this.rsiSeries.options ? this.rsiSeries.options().id : 'unknown');
                        }
                    } else {
                        console.warn('Failed to create RSI components on-demand');
                    }
                } catch (error) {
                    console.error('Error creating RSI components on-demand:', error);
                }
            } else {
                console.error('Cannot initialize indicator chart: price chart not available');
                return;
            }
        }
        
        // Apply the same 4-hour shift to RSI data
        const shiftedRsiData = this._shiftTimestamps(rsiData, 4, true);
        
        // Now attempt to update the RSI data
        try {
            // Direct update if we have the series reference
            if (this.rsiSeries && shiftedRsiData && shiftedRsiData.length > 0) {
                console.log('Updating RSI line directly');
                this.rsiSeries.setData(shiftedRsiData);
                
                // Log RSI data range for debugging
                const min = Math.min(...shiftedRsiData.map(d => d.value));
                const max = Math.max(...shiftedRsiData.map(d => d.value));
                console.log(`RSI data range: min=${min.toFixed(2)}, max=${max.toFixed(2)}`);
                
                // Log RSI values around the important thresholds (30 and 70)
                console.log('RSI values check:');
                const thresholds = { above70: 0, below30: 0, between3070: 0 };
                shiftedRsiData.forEach(point => {
                    if (point.value > 70) thresholds.above70++;
                    else if (point.value < 30) thresholds.below30++;
                    else thresholds.between3070++;
                });
                console.log(`RSI distribution: ${thresholds.below30} points below 30, ${thresholds.between3070} points between 30-70, ${thresholds.above70} points above 70`);
                
                // Add RSI level crossover markers
                this.addRSIMarkers(shiftedRsiData);
            }
            
            // Try through the indicator chart's update method
            try {
                this.indicatorChart.updateRSIData(shiftedRsiData);
            } catch (error) {
                console.warn('Error using indicator chart update method for RSI:', error);
                // Already tried direct update above
            }
            
        } catch (error) {
            console.error('Error updating RSI chart:', error);
        }
    }
      /**
     * Add RSI level crossover markers
     * @param {Array} rsiData - RSI line data
     */
    addRSIMarkers(rsiData) {
        console.log('=== RSI MARKERS DEBUG ===');
        
        // Basic checks and validation
        if (!rsiData || rsiData.length === 0) {
            console.log('Cannot add RSI markers: Missing or empty data');
            return;
        }
        
        console.log(`RSI Data: Length=${rsiData.length}, First point=${JSON.stringify(rsiData[0])}`);
        
        // Check RSI series
        if (!this.rsiSeries) {
            console.warn('RSI series not available for setting markers');
            return;
        }
        
        console.log('RSI series found:', this.rsiSeries);
        
        try {
            // Calculate RSI crossover points
            console.log('Calculating RSI crossovers...');
            const crossovers = MarkerUtils.calculateRSICrossovers(rsiData);
            console.log(`Found ${crossovers.length} RSI level crossovers`);
            
            if (crossovers.length === 0) {
                console.log('No RSI level crossovers found - nothing to display');
                return;
            }
            
            // Log crossover details
            console.log('RSI crossover details:');
            crossovers.slice(0, 5).forEach((c, i) => {
                console.log(`  Crossover #${i+1}: ${c.type} at ${new Date(c.time * 1000).toLocaleDateString()} ${new Date(c.time * 1000).toLocaleTimeString()} (RSI: ${c.value.toFixed(2)})`);
            });
            
            // Create formatted markers for the chart
            const markers = MarkerUtils.createRSICrossoverMarkers(crossovers);
            
            // Store marker reference
            this.rsiMarkers = markers;
            
            console.log(`Created ${markers.length} marker objects for RSI`);
            console.log('First few markers:', markers.slice(0, 2));
            
            // Directly use window.createSeriesMarkers with the RSI series and clear debug info
            if (typeof window.createSeriesMarkers === 'function') {
                console.log(`Applying ${markers.length} markers to RSI series using createSeriesMarkers`);
                
                try {
                    // Log details about the RSI series for debugging
                    console.log('RSI series for markers in ChartManager:', {
                        exists: !!this.rsiSeries,
                        id: this.rsiSeries && this.rsiSeries.options ? this.rsiSeries.options().id : 'unknown',
                        hasSetMarkers: this.rsiSeries && typeof this.rsiSeries.setMarkers === 'function'
                    });
                    
                    // Use the global function to create markers
                    this.rsiMarkersPlugin = window.createSeriesMarkers(this.rsiSeries, markers);
                    console.log('RSI markers successfully created with ID:', 
                        this.rsiSeries.options ? this.rsiSeries.options().id : 'unknown');
                } catch (e) {
                    console.error('Error creating RSI markers:', e);
                    
                    // Try to apply markers through the indicator chart
                    if (this.indicatorChart && typeof this.indicatorChart.addRSIMarkers === 'function') {
                        console.log('Attempting to add markers through IndicatorChartManager');
                        this.indicatorChart.addRSIMarkers(markers);
                    }
                }
            } else {
                console.error('window.createSeriesMarkers function is not available');
                
                // Try to apply markers through the indicator chart as fallback
                if (this.indicatorChart && typeof this.indicatorChart.addRSIMarkers === 'function') {
                    console.log('Attempting to add markers through IndicatorChartManager');
                    this.indicatorChart.addRSIMarkers(markers);
                }
            }
        } catch (error) {
            console.error('Error adding RSI level crossover markers:', error);
        }
        
        console.log('=== END RSI MARKERS DEBUG ===');
    }
    
    /**
     * Add Golden Cross and Death Cross markers to the polygon candlestick chart
     * @param {Array} sma50Data - SMA 50 data points
     * @param {Array} sma200Data - SMA 200 data points
     */
    addGoldenDeathCrossMarkers(sma50Data, sma200Data) {
        console.log('=== GOLDEN/DEATH CROSS MARKERS DEBUG ===');
        
        // Basic validation
        if (!sma50Data || sma50Data.length === 0) {
            console.log('Cannot add golden/death cross markers: Missing or empty SMA50 data');
            return;
        }
        
        if (!sma200Data || sma200Data.length === 0) {
            console.log('Cannot add golden/death cross markers: Missing or empty SMA200 data');
            return;
        }
        
        console.log(`SMA Data: SMA50 length=${sma50Data.length}, SMA200 length=${sma200Data.length}`);
        console.log('First SMA50 point:', JSON.stringify(sma50Data[0]));
        console.log('First SMA200 point:', JSON.stringify(sma200Data[0]));
        
        // Check polygon series
        if (!this.polygonSeries) {
            console.warn('Polygon series not available for setting golden/death cross markers');
            return;
        }
        
        try {
            // Calculate golden/death cross points
            console.log('Calculating Golden/Death crosses...');
            const crossovers = MarkerUtils.calculateGoldenDeathCrosses(sma50Data, sma200Data);
            console.log(`Found ${crossovers.length} Golden/Death crosses`);
            
            if (crossovers.length === 0) {
                console.log('No Golden/Death crosses found - nothing to display');
                return;
            }
            
            // Log crossover details
            console.log('Golden/Death cross details:');
            crossovers.slice(0, 5).forEach((c, i) => {
                console.log(`  Cross #${i+1}: ${c.type} at ${new Date(c.time * 1000).toLocaleDateString()} ${new Date(c.time * 1000).toLocaleTimeString()}`);
            });
            
            // Create formatted markers for the chart
            const markers = MarkerUtils.createGoldenDeathCrossMarkers(crossovers);
            
            // Store marker reference
            this.goldenDeathCrossMarkers = markers;
            
            console.log(`Created ${markers.length} marker objects for Golden/Death crosses`);
            console.log('First few markers:', markers.slice(0, 2));
            
            // Apply markers to polygon series using window.createSeriesMarkers
            if (typeof window.createSeriesMarkers === 'function') {
                console.log(`Applying ${markers.length} markers to polygon series using createSeriesMarkers`);
                
                try {
                    // Log details about the polygon series for debugging
                    console.log('Polygon series for markers:', {
                        exists: !!this.polygonSeries,
                        id: this.polygonSeries && this.polygonSeries.options ? this.polygonSeries.options().id : 'unknown',
                        hasSetMarkers: this.polygonSeries && typeof this.polygonSeries.setMarkers === 'function'
                    });
                    
                    // Use the global function to create markers
                    this.goldenDeathCrossMarkersPlugin = window.createSeriesMarkers(this.polygonSeries, markers);
                    console.log('Golden/Death cross markers successfully created on polygon series:', 
                        this.polygonSeries.options ? this.polygonSeries.options().id : 'unknown');
                } catch (e) {
                    console.error('Error creating Golden/Death cross markers:', e);
                }
            } else {
                console.error('window.createSeriesMarkers function is not available for Golden/Death crosses');
            }
            
        } catch (error) {
            console.error('Error adding Golden/Death cross markers:', error);
        }
    }
}
