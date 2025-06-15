// Chart interaction manager for handling user interactions with charts

import { CONFIG } from '../config.js';

export class ChartInteractionManager {
    constructor(chartManager) {
        this.chartManager = chartManager;
        this.eventHandlers = new Map();
        this.subscribers = new Map();
    }
    
    /**
     * Initialize interaction handlers for the chart
     */
    init() {
        if (!this.chartManager || !this.chartManager.chart) {
            console.error('Chart not initialized');
            return false;
        }
        
        this.setupCrosshairMove();
        this.setupClickHandlers();
        this.setupTimeScaleEvents();
        
        return true;
    }
    
    /**
     * Setup crosshair move handler
     */
    setupCrosshairMove() {
        if (!this.chartManager.chart) return;
        
        const crosshairHandler = param => {
            if (!param.point || !param.time) return;
            
            // Get series data at the crosshair position
            const seriesData = new Map();
            
            for (const [id, seriesInfo] of this.chartManager.seriesMap.entries()) {
                const price = seriesInfo.series.coordinateToPrice(param.point.y);
                seriesData.set(id, {
                    price,
                    time: param.time,
                    series: seriesInfo.series
                });
            }
            
            // Publish the event to subscribers
            this.publish('crosshairMove', {
                point: param.point,
                time: param.time,
                seriesData
            });
        };
        
        this.chartManager.chart.subscribeCrosshairMove(crosshairHandler);
        this.eventHandlers.set('crosshairMove', crosshairHandler);
    }
    
    /**
     * Setup click handlers for the chart
     */
    setupClickHandlers() {
        if (!this.chartManager.chart) return;
        
        // Click handler
        const clickHandler = param => {
            if (!param.point) return;
            
            // Check if any series was clicked
            const seriesData = new Map();
            
            for (const [id, seriesInfo] of this.chartManager.seriesMap.entries()) {
                const price = seriesInfo.series.coordinateToPrice(param.point.y);
                seriesData.set(id, {
                    price,
                    time: param.time,
                    series: seriesInfo.series
                });
            }
            
            // Publish the event to subscribers
            this.publish('click', {
                point: param.point,
                time: param.time,
                seriesData
            });
        };
        
        this.chartManager.chart.subscribeClick(clickHandler);
        this.eventHandlers.set('click', clickHandler);
    }
    
    /**
     * Setup time scale events
     */
    setupTimeScaleEvents() {
        if (!this.chartManager.chart) return;
        
        // Visible range changed
        const visibleRangeHandler = param => {
            this.publish('visibleRangeChanged', param);
        };
        
        this.chartManager.chart.timeScale().subscribeVisibleLogicalRangeChange(visibleRangeHandler);
        this.eventHandlers.set('visibleRangeChanged', visibleRangeHandler);
    }
    
    /**
     * Subscribe to chart events
     * @param {string} eventName - Name of the event
     * @param {Function} callback - Callback function
     * @returns {string} Subscription ID
     */
    subscribe(eventName, callback) {
        if (typeof callback !== 'function') {
            console.error('Callback must be a function');
            return null;
        }
        
        if (!this.subscribers.has(eventName)) {
            this.subscribers.set(eventName, new Map());
        }
        
        const eventSubscribers = this.subscribers.get(eventName);
        const subscriptionId = `${eventName}_${Date.now()}_${Math.floor(Math.random() * 1000)}`;
        
        eventSubscribers.set(subscriptionId, callback);
        return subscriptionId;
    }
    
    /**
     * Unsubscribe from chart events
     * @param {string} subscriptionId - Subscription ID
     * @returns {boolean} True if unsubscribed, false otherwise
     */
    unsubscribe(subscriptionId) {
        for (const [eventName, eventSubscribers] of this.subscribers.entries()) {
            if (eventSubscribers.has(subscriptionId)) {
                eventSubscribers.delete(subscriptionId);
                return true;
            }
        }
        
        return false;
    }
    
    /**
     * Publish an event to subscribers
     * @param {string} eventName - Name of the event
     * @param {Object} data - Event data
     */
    publish(eventName, data) {
        if (!this.subscribers.has(eventName)) return;
        
        const eventSubscribers = this.subscribers.get(eventName);
        for (const callback of eventSubscribers.values()) {
            try {
                callback(data);
            } catch (error) {
                console.error(`Error in ${eventName} subscriber:`, error);
            }
        }
    }
    
    /**
     * Create a tooltip HTML element for displaying data
     * @returns {HTMLElement} Tooltip element
     */
    createTooltip() {
        const tooltip = document.createElement('div');
        tooltip.className = 'lightweight-chart-tooltip';
        tooltip.style.position = 'absolute';
        tooltip.style.display = 'none';
        tooltip.style.padding = '8px';
        tooltip.style.backgroundColor = 'rgba(20, 21, 26, 0.9)';
        tooltip.style.color = '#fff';
        tooltip.style.borderRadius = '4px';
        tooltip.style.fontSize = '12px';
        tooltip.style.pointerEvents = 'none';
        tooltip.style.zIndex = '1000';
        tooltip.style.whiteSpace = 'nowrap';
        tooltip.style.boxShadow = '0 2px 5px rgba(0, 0, 0, 0.5)';
        
        document.body.appendChild(tooltip);
        return tooltip;
    }
    
    /**
     * Enable tooltip display on crosshair move
     * @param {Function} tooltipFormatter - Callback to format tooltip content
     * @returns {HTMLElement} Tooltip element
     */
    enableTooltip(tooltipFormatter) {
        const tooltip = this.createTooltip();
        
        // Subscribe to crosshair move event
        this.subscribe('crosshairMove', param => {
            if (!param.point) {
                tooltip.style.display = 'none';
                return;
            }
            
            // Position tooltip near the crosshair
            const x = param.point.x + this.chartManager.container.getBoundingClientRect().left + 10;
            const y = param.point.y + this.chartManager.container.getBoundingClientRect().top - 50;
            
            tooltip.style.left = `${x}px`;
            tooltip.style.top = `${y}px`;
            
            // Format tooltip content
            if (typeof tooltipFormatter === 'function') {
                tooltip.innerHTML = tooltipFormatter(param);
            } else {
                // Default formatter
                let content = '';
                
                if (param.time) {
                    const date = new Date(param.time * 1000);
                    content += `<div>${date.toLocaleString()}</div>`;
                }
                
                for (const [id, data] of param.seriesData.entries()) {
                    content += `<div>${id}: ${data.price !== undefined ? data.price.toFixed(2) : 'N/A'}</div>`;
                }
                
                tooltip.innerHTML = content;
            }
            
            tooltip.style.display = 'block';
        });
        
        return tooltip;
    }
    
    /**
     * Clean up resources
     */
    destroy() {
        // Unsubscribe from chart events
        if (this.chartManager.chart) {
            for (const [eventName, handler] of this.eventHandlers.entries()) {
                if (eventName === 'crosshairMove') {
                    this.chartManager.chart.unsubscribeCrosshairMove(handler);
                } else if (eventName === 'click') {
                    this.chartManager.chart.unsubscribeClick(handler);
                } else if (eventName === 'visibleRangeChanged') {
                    this.chartManager.chart.timeScale().unsubscribeVisibleLogicalRangeChange(handler);
                }
            }
        }
        
        // Clear event handlers and subscribers
        this.eventHandlers.clear();
        this.subscribers.clear();
    }
}
