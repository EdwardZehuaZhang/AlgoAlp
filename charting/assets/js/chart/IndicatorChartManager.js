// Indicator Chart Manager for technical indicators

import { BaseChartManager } from './BaseChartManager.js';
import { CONFIG } from '../config.js';

try {
    if (timeRange) {
        const oversoldData = [
            { time: timeRange.from, value: 30 },
            { time: timeRange.to, value: 30 }
        ];

        const overboughtData = [
            { time: timeRange.from, value: 70 },
            { time: timeRange.to, value: 70 }
        ];

        overboughtLevel.setData(overboughtData);
        oversoldLevel.setData(oversoldData);
    } else {
        // Fallback to hardcoded range (will be updated when data arrives)
        const now = Math.floor(Date.now() / 1000);
        const oneYearAgo = now - (365 * 24 * 60 * 60);

        const overboughtData = [
            { time: oneYearAgo, value: 70 },
            { time: now, value: 70 }
        ];

        const oversoldData = [
            { time: oneYearAgo, value: 30 },
            { time: now, value: 30 }
        ];

        overboughtLevel.setData(overboughtData);
        oversoldLevel.setData(oversoldData);
    }
} catch (error) {
    console.error('Error setting RSI level lines:', error);
}


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
            id: 'rsi',
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
            rsi: rsiSeries,
            overboughtLevel: overboughtLevel,
            oversoldLevel: oversoldLevel
        };
        
        // Store the RSI indicator
        this.indicators.set('rsi', {
            type: 'rsi',
            components: rsiComponents,
            paneIndex
        });
        
        return rsiComponents;
        this.indicators.set('rsi', {
            type: 'rsi',
            components: {
                main: rsiSeries,
                overbought: overboughtLevel,
                oversold: oversoldLevel
            },
            paneIndex
        });
        
        return {
            main: rsiSeries,
            overbought: overboughtLevel,
            oversold: oversoldLevel
        };
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
    }
      /**
     * Update RSI data
     * @param {Array} rsiData - RSI data points (should be filtered to market hours)
     */
    updateRSIData(rsiData) {
        if (!rsiData || rsiData.length === 0) {
            console.log('No RSI data provided to update');
            return;
        }
        
        const rsiIndicator = this.indicators.get('rsi');
        
        if (!rsiIndicator || !rsiIndicator.components || !rsiIndicator.components.rsi) {
            console.log('RSI indicator not found, creating it now');
            const components = this.addRSIIndicator(3); // Use pane index 3 (fourth pane)
            
            if (!components || !components.rsi) {
                console.error('Failed to create RSI indicator components');
                return;
            }
            
            console.log(`Updating RSI data with ${rsiData.length} points`);
            components.rsi.setData(rsiData);
            return;
        }
        
        // Set the RSI data
        console.log(`Updating RSI data with ${rsiData.length} points`);
        rsiIndicator.components.rsi.setData(rsiData);
        
        // Ensure the price scale is fixed for RSI (0-100)
        try {
            const paneOptions = {
                scaleMargins: {
                    top: 0.1,
                    bottom: 0.1,
                }
            };
            
            // Try to apply to the rsi component directly
            if (rsiIndicator.components.rsi.applyOptions) {
                rsiIndicator.components.rsi.applyOptions({
                    autoscaleInfoProvider: () => ({
                        priceRange: {
                            minValue: 0,
                            maxValue: 100
                        }
                    })
                });
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
}
