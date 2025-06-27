// Indicator Chart Manager for technical indicators

import { BaseChartManager } from './BaseChartManager.js';
import { CONFIG } from '../config.js';
import { MarkerUtils } from '../utils/markerUtils.js';

export class IndicatorChartManager extends BaseChartManager {
    constructor() {
        super();
        
        // Indicator Series
        this.indicators = new Map(); // Map to store all indicators
    }
      /**
     * Initialize with parent chart to sync time scale
     * @param {Object} parentChart - Parent chart instance to sync with
     */
    initWithParent(parentChart) {
        if (parentChart && parentChart.chart) {
            this.parentChart = parentChart;
            this.chart = parentChart.chart; // Share the same chart instance
        }
    }
    
    /**
     * Add a MACD indicator to the chart
     * @param {number} paneIndex - Pane index for the indicator
     * @returns {Object} MACD components
     */
    addMACDIndicator(paneIndex = 1) {
        if (!this.chart) {
            console.error('Chart not initialized');
            return null;
        }
        
        const macdComponents = {
            histogram: this.addSeries(LightweightCharts.HistogramSeries, {
                id: 'macd_histogram',
                color: '#26a69a',
                priceFormat: {
                    type: 'price',
                    precision: 2,
                    minMove: 0.01,
                },
                title: 'MACD Histogram',
                showLastValue: false,
            }, paneIndex),
            
            macdLine: this.addSeries(LightweightCharts.LineSeries, {
                id: 'macd_line',
                color: '#2962FF',
                lineWidth: 2,
                priceLineVisible: false,
                title: 'MACD Line',
                lastValueVisible: true,
            }, paneIndex),
            
            signalLine: this.addSeries(LightweightCharts.LineSeries, {
                id: 'macd_signal',
                color: '#FF6D00',
                lineWidth: 2,
                priceLineVisible: false,
                title: 'Signal Line',
                lastValueVisible: true,
            }, paneIndex)
        };
        
        // Store the MACD indicator
        this.indicators.set('macd', {
            type: 'macd',
            components: macdComponents,
            paneIndex
        });
        
        return macdComponents;
    }
      /**
     * Add an RSI indicator to the chart
     * @param {number} paneIndex - Pane index for the indicator
     * @param {Object} options - RSI options
     * @returns {Object} RSI series
     */
    addRSIIndicator(paneIndex = 1, options = {}) {
        if (!this.chart) {
            console.error('Chart not initialized');
            return null;
        }
        
        // Default options
        const defaultOptions = {
            color: '#7E57C2',
            lineWidth: 2,
            priceFormat: {
                type: 'price',
                precision: 2,
                minMove: 0.01,
            },
            title: 'RSI (14)',
            lastValueVisible: true,
            // Ensure the scale range is appropriate for RSI
            autoscaleInfoProvider: () => ({
                priceRange: {
                    minValue: 0,
                    maxValue: 100
                }
            })
        };
        
        // Merge options
        const rsiOptions = { ...defaultOptions, ...options };
          // Create RSI line series
        const rsiSeries = this.addSeries(LightweightCharts.LineSeries, {
            id: 'rsi_line',
            ...rsiOptions
        }, paneIndex);
        
        // Add overbought and oversold lines
        const overboughtLevel = this.addSeries(LightweightCharts.LineSeries, {
            id: 'rsi_overbought',
            color: 'rgba(255, 82, 82, 0.5)',
            lineWidth: 1,
            lineStyle: 1, // dashed
            priceLineVisible: false,
            lastValueVisible: false,
            title: 'Overbought',
        }, paneIndex);
        
        const oversoldLevel = this.addSeries(LightweightCharts.LineSeries, {
            id: 'rsi_oversold',
            color: 'rgba(76, 175, 80, 0.5)',
            lineWidth: 1,
            lineStyle: 1, // dashed
            priceLineVisible: false,
            lastValueVisible: false,
            title: 'Oversold',
        }, paneIndex);
          // Set constant levels with fixed timestamps that cover a wide range
        const now = Math.floor(Date.now() / 1000);
        const twoYearsAgo = now - (2 * 365 * 24 * 60 * 60); // 2 years ago
        
        // Use static timeframe that covers a wide range
        const overboughtData = [
            { time: twoYearsAgo, value: 70 },
            { time: now, value: 70 }
        ];
        
        const oversoldData = [
            { time: twoYearsAgo, value: 30 },
            { time: now, value: 30 }
        ];
        
        // Set the level data
        overboughtLevel.setData(overboughtData);
        oversoldLevel.setData(oversoldData);
          // Create components object to return
        const rsiComponents = {
            rsi_line: rsiSeries,  // Use consistent ID: rsi_line
            // Remove the legacy 'rsi' reference to avoid confusion
            overboughtLevel: overboughtLevel,
            oversoldLevel: oversoldLevel
        };
        
        // Store the RSI indicator
        this.indicators.set('rsi', {
            type: 'rsi',
            components: rsiComponents,
            paneIndex
        });
        
        console.log('RSI indicator created with components:', Object.keys(rsiComponents));
        return rsiComponents;
    }
    
    /**
     * Update MACD data
     * @param {Array} histogramData - MACD histogram data
     * @param {Array} macdLineData - MACD line data
     * @param {Array} signalLineData - Signal line data
     */    updateMACDData(histogramData, macdLineData, signalLineData) {
        if (!this.indicators || !this.indicators.has('macd')) {
            console.error('MACD indicator not found');
            return false;
        }
        
        try {
            const macdInfo = this.indicators.get('macd');
            if (!macdInfo || !macdInfo.components) {
                console.error('MACD components not found');
                return false;
            }
            
            const macdComponents = macdInfo.components;
            
            if (histogramData && histogramData.length > 0) {
                macdComponents.histogram.setData(histogramData);
            }
            
            if (macdLineData && macdLineData.length > 0) {
                macdComponents.macdLine.setData(macdLineData);
            }
            
            if (signalLineData && signalLineData.length > 0) {
                macdComponents.signalLine.setData(signalLineData);
            }
            
            return true;
        } catch (error) {
            console.error('Error updating MACD data:', error);
            return false;
        }
    }    /**
     * Update RSI data
     * @param {Array} rsiData - RSI data points (should be filtered to market hours)
     */
    updateRSIData(rsiData) {
        if (!rsiData || rsiData.length === 0) {
            console.log('No RSI data provided to update');
            return;
        }
        
        const rsiIndicator = this.indicators.get('rsi');
        
        if (!rsiIndicator || !rsiIndicator.components || !rsiIndicator.components.rsi_line) {
            console.log('RSI indicator not found, creating it now');
            const components = this.addRSIIndicator(3); // Use pane index 3 (fourth pane)
            
            if (!components || !components.rsi_line) {
                console.error('Failed to create RSI indicator components');
                return;
            }
            
            console.log(`Updating RSI data with ${rsiData.length} points`);
            // Always use rsi_line for consistency
            const rsiSeries = components.rsi_line;
            console.log('RSI series ID:', rsiSeries.options ? rsiSeries.options().id : 'unknown');
            rsiSeries.setData(rsiData);
            return;
        }
        
        // Always use rsi_line for consistency
        const rsiSeries = rsiIndicator.components.rsi_line;
        
        if (!rsiSeries) {
            console.error('RSI series not found in components');
            return;
        }
        
        // Set the RSI data
        console.log(`Updating RSI data with ${rsiData.length} points`);
        rsiSeries.setData(rsiData);
        
        // Debug RSI data range
        const min = Math.min(...rsiData.map(d => d.value));
        const max = Math.max(...rsiData.map(d => d.value));
        console.log(`RSI data range in IndicatorChartManager: min=${min.toFixed(2)}, max=${max.toFixed(2)}`);
        
        // Ensure the price scale is fixed for RSI (0-100)
        try {
            // Try to apply to the rsi component directly
            if (rsiSeries.applyOptions) {
                rsiSeries.applyOptions({
                    autoscaleInfoProvider: () => ({
                        priceRange: {
                            minValue: 0,
                            maxValue: 100
                        }
                    })
                });
            }
            
            // Calculate and add RSI crossover markers
            try {
                const thresholds = { above70: 0, below30: 0, between3070: 0 };
                rsiData.forEach(point => {
                    if (point.value > 70) thresholds.above70++;
                    else if (point.value < 30) thresholds.below30++;
                    else thresholds.between3070++;
                });
                
                if (thresholds.below30 > 0 || thresholds.above70 > 0) {
                    console.log(`RSI threshold distribution from IndicatorChartManager: ${thresholds.below30} points below 30, ${thresholds.above70} points above 70`);
                    console.log('RSI data has potential crossover points, calculating markers...');
                    
                    const crossovers = MarkerUtils.calculateRSICrossovers(rsiData);
                    
                    if (crossovers.length > 0) {
                        console.log(`Found ${crossovers.length} RSI crossovers in IndicatorChartManager`);
                        const markers = MarkerUtils.createRSICrossoverMarkers(crossovers);
                        this.addRSIMarkers(markers);
                    }
                }
            } catch (markerError) {
                console.warn('Error adding RSI markers from updateRSIData:', markerError);
            }
        } catch (error) {
            console.warn('Could not fix RSI price scale:', error);
        }
    }
    
    /**
     * Set markers on an indicator
     * @param {string} indicatorType - Indicator type ('macd', 'rsi', etc.)
     * @param {string} component - Component name ('main', 'histogram', etc.)
     * @param {Array} markers - Marker objects
     */
    setIndicatorMarkers(indicatorType, component, markers) {
        if (!this.indicators.has(indicatorType)) {
            console.error(`Indicator ${indicatorType} not found`);
            return false;
        }
        
        try {
            const components = this.indicators.get(indicatorType).components;
            
            if (!components[component]) {
                console.error(`Component ${component} not found in ${indicatorType} indicator`);
                return false;
            }
            
            components[component].setMarkers(markers);
            return true;
        } catch (error) {
            console.error(`Error setting markers for ${indicatorType}/${component}:`, error);
            return false;
        }
    }
    
    /**
     * Add MACD crossover markers to the MACD line
     * @param {Array} markers - Array of marker objects
     * @returns {Object|null} The markers plugin or null if failed
     */
    addMACDMarkers(markers) {
        if (!this.chart) {
            console.error('Cannot add MACD markers: Chart not initialized');
            return null;
        }
        
        const macdIndicator = this.indicators.get('macd');
        
        if (!macdIndicator || !macdIndicator.components || !macdIndicator.components.macdLine) {
            console.error('Cannot add MACD markers: MACD indicator not found');
            return null;
        }
        
        const macdLineSeries = macdIndicator.components.macdLine;
        console.log('Adding MACD markers to MACD line series');
        
        try {            // Try to use window.createSeriesMarkers (which we exposed in index.html)
            if (typeof window.createSeriesMarkers === 'function') {
                console.log('Using window.createSeriesMarkers');
                return window.createSeriesMarkers(macdLineSeries, markers);
            }
            
            // Try directly from LightweightCharts global object
            if (typeof LightweightCharts !== 'undefined' && typeof LightweightCharts.createSeriesMarkers === 'function') {
                console.log('Using LightweightCharts.createSeriesMarkers');
                return LightweightCharts.createSeriesMarkers(macdLineSeries, markers);
            }
            
            // Try to use setMarkers method directly if available
            if (macdLineSeries && typeof macdLineSeries.setMarkers === 'function') {
                console.log('Using macdLineSeries.setMarkers directly');
                macdLineSeries.setMarkers(markers);
                return { markers };
            }
            
            console.error('No method available to add MACD markers');
            return null;
        } catch (error) {
            console.error('Error adding MACD markers:', error);
            return null;
        }
    }
        /**
     * Add RSI level crossover markers to the RSI line
     * @param {Array} markers - Array of marker objects
     * @returns {Object|null} The markers plugin or null if failed
     */
    addRSIMarkers(markers) {
        if (!this.chart) {
            console.error('Cannot add RSI markers: Chart not initialized');
            return null;
        }
        
        console.log('IndicatorChartManager.addRSIMarkers called with', markers.length, 'markers');
        
        if (!this.indicators.has('rsi')) {
            console.error('RSI indicator not found in indicators map');
            console.log('Available indicators:', Array.from(this.indicators.keys()));
            return null;
        }
        
        const rsiIndicator = this.indicators.get('rsi');
        
        if (!rsiIndicator || !rsiIndicator.components) {
            console.error('Invalid RSI indicator structure');
            return null;
        }
        
        // Always use rsi_line for consistency
        let rsiSeries = rsiIndicator.components.rsi_line;
        if (!rsiSeries) {
            console.error('RSI series not found with ID "rsi_line"');
            return null;
        }
        
        if (!rsiSeries) {
            console.error('RSI series not found in components');
            console.log('Available components:', Object.keys(rsiIndicator.components));
            return null;
        }
        
        console.log('Adding RSI markers to RSI line series');
        console.log('RSI series ID:', rsiSeries.options ? rsiSeries.options().id : 'unknown');
        
        // Log the first few markers
        console.log('First markers to add:');
        markers.slice(0, 3).forEach((m, i) => {
            console.log(`  Marker #${i+1}: time=${new Date(m.time * 1000).toLocaleDateString()}, position=${m.position}, text=${m.text}`);
        });
        
        try {
            // Try to use window.createSeriesMarkers (which we exposed in index.html)
            if (typeof window.createSeriesMarkers === 'function') {
                console.log('Using window.createSeriesMarkers for RSI');
                // Verify that rsiSeries has the correct interface
                if (!rsiSeries || typeof rsiSeries !== 'object') {
                    console.error('Invalid RSI series object:', rsiSeries);
                    return null;
                }
                
                // Log details about the series object
                console.log('RSI series for markers:', {
                    id: rsiSeries.options ? rsiSeries.options().id : 'unknown',
                    hasSetMarkers: typeof rsiSeries.setMarkers === 'function'
                });
                
                const result = window.createSeriesMarkers(rsiSeries, markers);
                console.log('RSI markers added successfully');
                return result;
            }
            
            // Try directly from LightweightCharts global object
            if (typeof LightweightCharts !== 'undefined' && typeof LightweightCharts.createSeriesMarkers === 'function') {
                console.log('Using LightweightCharts.createSeriesMarkers for RSI');
                const result = LightweightCharts.createSeriesMarkers(rsiSeries, markers);
                console.log('RSI markers added successfully with LightweightCharts.createSeriesMarkers');
                return result;
            }
            
            // Try to use setMarkers method directly if available
            if (rsiSeries && typeof rsiSeries.setMarkers === 'function') {
                console.log('Using rsiSeries.setMarkers directly');
                rsiSeries.setMarkers(markers);
                return { markers };
            }
            
            console.error('No method available to add RSI markers');
            return null;
        } catch (error) {
            console.error('Error adding RSI markers:', error);
            console.error('Error stack:', error.stack);
            return null;
        }
    }
}
