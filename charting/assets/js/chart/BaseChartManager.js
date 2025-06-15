// Base chart management class

import { CONFIG } from '../config.js';

export class BaseChartManager {
    constructor() {
        this.chart = null;
        this.container = null;
        this.seriesMap = new Map(); // Store all series with their IDs
        this.resizeObserver = null;
    }
    
    /**
     * Initialize chart container and create base chart
     * @param {string} containerId - ID of the container element
     * @param {Object} options - Chart options
     */
    initChart(containerId, options = {}) {
        this.container = document.getElementById(containerId);
        if (!this.container) {
            console.error(`Container element ${containerId} not found`);
            return false;
        }
        
        // Default chart options
        const defaultOptions = {
            width: this.container.clientWidth,
            height: this.container.clientHeight,
            layout: {
                background: { color: CONFIG.CHART.COLORS.BACKGROUND },
                textColor: CONFIG.CHART.COLORS.TEXT,
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
                // Fixed formatter that ignores timezone completely
                tickMarkFormatter: (timestamp) => {
                    // IMPORTANT: Use explicit time formatting, ignoring local timezone
                    // This converts the timestamp directly to hours and minutes
                    // 0 = midnight, 9.5 = 9:30 AM, 16 = 4:00 PM
                    
                    // Create a new date object with the timestamp
                    const date = new Date(timestamp * 1000);
                    
                    // Get hours and minutes using UTC methods (no timezone adjustment)
                    const hours = date.getUTCHours();
                    const minutes = date.getUTCMinutes();
                    
                    // Format as HH:MM
                    const formattedTime = `${hours.toString().padStart(2, '0')}:${minutes.toString().padStart(2, '0')}`;
                    
                    // For debugging first few conversions
                    if (timestamp % 3600 === 0) { // Log only on hour marks
                        console.log(`Time tick conversion: ${timestamp} -> ${formattedTime}`);
                    }
                    
                    return formattedTime;
                },
            },
            localization: {
                // Use UTC timezone to prevent automatic conversions
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
        
        // Merge default options with provided options
        const chartOptions = {
            ...defaultOptions,
            ...options,
            layout: {
                ...defaultOptions.layout,
                ...options.layout,
                panes: {
                    separatorColor: '#2E2E2E',
                    separatorHoverColor: 'rgba(41, 98, 255, 0.2)',
                    enableResize: true,
                    ...(options.layout && options.layout.panes)
                }
            }
        };
          // Create chart
        try {
            this.chart = LightweightCharts.createChart(this.container, chartOptions);
            
            // Create a baseline layout with at least two panes
            if (this.chart && typeof this.chart.addPane === 'function') {
                // Add a second pane for indicators (typically MACD or RSI)
                try {
                    this.chart.addPane({ height: 150 });
                    console.log('Created initial two-pane layout');
                } catch (paneError) {
                    console.warn('Could not add second pane:', paneError);
                }
            }
            
            this.setupResizeHandler();
            return true;
        } catch (error) {
            console.error('Error creating chart:', error);
            return false;
        }
    }
    
    /**
     * Setup handler for container resizing
     */
    setupResizeHandler() {
        // Use ResizeObserver if available
        if (typeof ResizeObserver !== 'undefined') {
            this.resizeObserver = new ResizeObserver(entries => {
                if (entries.length === 0 || !this.chart) return;
                
                const newRect = entries[0].contentRect;
                this.chart.resize(newRect.width, newRect.height);
            });
            
            this.resizeObserver.observe(this.container);
        } else {
            // Fallback to window resize event
            const resizeHandler = () => {
                if (!this.chart || !this.container) return;
                this.chart.resize(
                    this.container.clientWidth,
                    this.container.clientHeight
                );
            };
            
            window.addEventListener('resize', resizeHandler);
        }
    }
    
    /**
     * Add a series to the chart
     * @param {Function} seriesType - Series type constructor from LightweightCharts
     * @param {Object} options - Series options
     * @param {number} paneIndex - Index of the pane to add the series to (default: 0)
     * @returns {Object} The created series
     */
    addSeries(seriesType, options, paneIndex = 0) {
        if (!this.chart) {
            console.error('Chart not initialized');
            return null;
        }
        
        try {
            const series = this.chart.addSeries(seriesType, options, paneIndex);
            // Store series with a generated ID if needed
            const id = options.id || `series_${Math.floor(Math.random() * 1000000)}`;
            this.seriesMap.set(id, {
                series,
                type: seriesType.name,
                options,
                paneIndex
            });
            return series;
        } catch (error) {
            console.error('Error adding series:', error);
            return null;
        }
    }
    
    /**
     * Get a series by its ID
     * @param {string} id - The series ID
     * @returns {Object} The series object or null if not found
     */
    getSeries(id) {
        const seriesInfo = this.seriesMap.get(id);
        return seriesInfo ? seriesInfo.series : null;
    }
    
    /**
     * Remove a series from the chart
     * @param {string} id - The series ID
     * @returns {boolean} True if the series was removed, false otherwise
     */
    removeSeries(id) {
        const seriesInfo = this.seriesMap.get(id);
        if (!seriesInfo) return false;
        
        try {
            this.chart.removeSeries(seriesInfo.series);
            this.seriesMap.delete(id);
            return true;
        } catch (error) {
            console.error(`Error removing series ${id}:`, error);
            return false;
        }
    }
    
    /**
     * Set series data
     * @param {string} id - The series ID
     * @param {Array} data - The data to set for the series
     * @returns {boolean} True if the data was set, false otherwise
     */
    setSeriesData(id, data) {
        const series = this.getSeries(id);
        if (!series) return false;
        
        try {
            series.setData(data);
            return true;
        } catch (error) {
            console.error(`Error setting data for series ${id}:`, error);
            return false;
        }
    }
    
    /**
     * Set series markers
     * @param {string} id - The series ID
     * @param {Array} markers - The markers to set for the series
     * @returns {boolean} True if the markers were set, false otherwise
     */
    setSeriesMarkers(id, markers) {
        const series = this.getSeries(id);
        if (!series) return false;
        
        try {
            series.setMarkers(markers);
            return true;
        } catch (error) {
            console.error(`Error setting markers for series ${id}:`, error);
            return false;
        }
    }
    
    /**
     * Clear all data from the chart
     */
    clearChart() {
        if (!this.chart) return;
        
        // Remove all series
        for (const [id, seriesInfo] of this.seriesMap.entries()) {
            try {
                this.chart.removeSeries(seriesInfo.series);
            } catch (error) {
                console.error(`Error removing series ${id}:`, error);
            }
        }
        
        // Clear the series map
        this.seriesMap.clear();
    }
    
    /**
     * Destroy the chart and clean up resources
     */
    destroy() {
        // Clean up resize observer if it exists
        if (this.resizeObserver) {
            this.resizeObserver.disconnect();
            this.resizeObserver = null;
        }
        
        // Clear all series
        this.clearChart();
        
        // Remove the chart
        if (this.chart) {
            this.chart.remove();
            this.chart = null;
        }
    }
}
