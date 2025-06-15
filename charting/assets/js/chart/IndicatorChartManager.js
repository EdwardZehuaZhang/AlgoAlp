// Indicator Chart Manager for technical indicators

import { BaseChartManager } from './BaseChartManager.js';
import { CONFIG } from '../config.js';

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
        
        // Set constant levels
        const timeRange = this.chart.timeScale().getVisibleLogicalRange();
        if (timeRange) {
            // Use the visible time range
            const overboughtData = [
                { time: timeRange.from, value: 70 },
                { time: timeRange.to, value: 70 }
            ];
            
            const oversoldData = [
                { time: timeRange.from, value: 30 },
                { time: timeRange.to, value: 30 }
            ];
            
            overboughtLevel.setData(overboughtData);
            oversoldLevel.setData(oversoldData);
        }
        
        // Store the RSI indicator
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
     * @param {Array} rsiData - RSI data points
     */
    updateRSIData(rsiData) {
        if (!this.indicators.has('rsi')) {
            console.error('RSI indicator not found');
            return false;
        }
        
        try {
            const rsiComponents = this.indicators.get('rsi').components;
            
            if (rsiData && rsiData.length > 0) {
                rsiComponents.main.setData(rsiData);
                
                // Update overbought/oversold lines to match time range
                const timeStart = rsiData[0].time;
                const timeEnd = rsiData[rsiData.length - 1].time;
                
                const overboughtData = [
                    { time: timeStart, value: 70 },
                    { time: timeEnd, value: 70 }
                ];
                
                const oversoldData = [
                    { time: timeStart, value: 30 },
                    { time: timeEnd, value: 30 }
                ];
                
                rsiComponents.overbought.setData(overboughtData);
                rsiComponents.oversold.setData(oversoldData);
            }
            
            return true;
        } catch (error) {
            console.error('Error updating RSI data:', error);
            return false;
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
}
