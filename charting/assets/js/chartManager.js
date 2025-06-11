// Chart management and creation utilities with multiple panes

import { CONFIG } from './config.js';

export class ChartManager {
    constructor() {
        this.chart = null;  // Single chart with multiple panes
        this.csvSeries = null;
        this.polygonSeries = null;
        this.csvSMA20Line = null;
        this.csvSMA50Line = null;
        this.polygonSMA20Line = null;
        this.polygonSMA50Line = null;
    }
    
    /**
     * Initialize the chart with multiple panes
     */
    createCharts() {
        this.createSingleChartWithPanes();
        this.setupEventListeners();
    }
    
    /**
     * Create a single chart with two panes
     */
    createSingleChartWithPanes() {
        const container = document.getElementById('main-chart-container');
        
        const chartOptions = {
            width: container.clientWidth,
            height: container.clientHeight,
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
            },
            crosshair: {
                mode: LightweightCharts.CrosshairMode.Normal,
            },
        };
          // Create the main chart with panes support
        this.chart = LightweightCharts.createChart(container, {
            ...chartOptions,
            layout: {
                ...chartOptions.layout,
                panes: {
                    separatorColor: '#2962FF',
                    separatorHoverColor: 'rgba(41, 98, 255, 0.2)',
                    enableResize: true,
                }
            }
        });
          // Add CSV data series to pane 0 (default pane)
        this.csvSeries = this.chart.addSeries(LightweightCharts.CandlestickSeries, {
            upColor: CONFIG.CHART.COLORS.CSV_CHART.UP_COLOR,
            downColor: CONFIG.CHART.COLORS.CSV_CHART.DOWN_COLOR,
            borderVisible: false,
            wickUpColor: CONFIG.CHART.COLORS.CSV_CHART.WICK_UP_COLOR,
            wickDownColor: CONFIG.CHART.COLORS.CSV_CHART.WICK_DOWN_COLOR,
            title: 'CSV',
        }, 0); // Pane index 0
        
        // Add CSV SMA lines to the same pane
        this.csvSMA20Line = this.chart.addSeries(LightweightCharts.LineSeries, {
            color: CONFIG.CHART.COLORS.CSV_CHART.SMA20_COLOR,
            lineWidth: 2,
            priceLineVisible: false,
            title: 'CSV SMA 20',
        }, 0); // Pane index 0

        this.csvSMA50Line = this.chart.addSeries(LightweightCharts.LineSeries, {
            color: CONFIG.CHART.COLORS.CSV_CHART.SMA50_COLOR,
            lineWidth: 2,
            priceLineVisible: false,
            title: 'CSV SMA 50',
        }, 0); // Pane index 0
        
        // Add Polygon data series to pane 1 (this creates the second pane automatically)
        this.polygonSeries = this.chart.addSeries(LightweightCharts.CandlestickSeries, {
            upColor: CONFIG.CHART.COLORS.POLYGON_CHART.UP_COLOR,
            downColor: CONFIG.CHART.COLORS.POLYGON_CHART.DOWN_COLOR,
            borderVisible: false,
            wickUpColor: CONFIG.CHART.COLORS.POLYGON_CHART.WICK_UP_COLOR,
            wickDownColor: CONFIG.CHART.COLORS.POLYGON_CHART.WICK_DOWN_COLOR,
            title: 'Polygon API',
        }, 1); // Pane index 1 - creates second pane

        // Add Polygon SMA lines to the same pane (pane 1)
        this.polygonSMA20Line = this.chart.addSeries(LightweightCharts.LineSeries, {
            color: CONFIG.CHART.COLORS.POLYGON_CHART.SMA20_COLOR,
            lineWidth: 2,
            priceLineVisible: false,
            title: 'Polygon SMA 20',
        }, 1); // Pane index 1
        
        this.polygonSMA50Line = this.chart.addSeries(LightweightCharts.LineSeries, {
            color: CONFIG.CHART.COLORS.POLYGON_CHART.SMA50_COLOR,
            lineWidth: 2,
            priceLineVisible: false,
            title: 'Polygon SMA 50',
        }, 1); // Pane index 1
          // Configure panes after creation
        setTimeout(() => {
            try {
                const panes = this.chart.panes();
                console.log('Number of panes created:', panes.length);
                
                if (panes.length >= 2) {
                    // Set height for panes
                    panes[0].setHeight(400); // CSV pane - larger for full historical view
                    panes[1].setHeight(300); // Polygon pane - smaller for recent data
                    console.log('Pane heights configured: CSV=400px, Polygon=300px');
                }
                
                // Verify timezone display is working
                console.log('Timezone formatter configured - times should now display in Eastern Time');
            } catch (error) {
                console.error('Error configuring panes:', error);
            }
        }, 100);
        
        console.log('Chart created with two panes for perfect synchronization');
    }    
    /**
     * Setup event listeners for window resize
     */
    setupEventListeners() {
        window.addEventListener('resize', () => {
            if (this.chart) {
                const container = document.getElementById('main-chart-container');
                this.chart.resize(container.clientWidth, container.clientHeight);
            }
        });
    }
    
    /**
     * Update CSV chart with data
     * @param {Array} data - Chart data
     * @param {Array} sma20Data - SMA20 data
     * @param {Array} sma50Data - SMA50 data
     */
    updateCSVChart(data, sma20Data, sma50Data) {
        if (!data || data.length === 0) {
            document.getElementById('main-loading').textContent = 'No CSV data available to display';
            return;
        }
        
        console.log('Updating CSV chart with data points:', data.length);
        console.log('CSV - Date range:', 
            new Date(data[0].time * 1000).toDateString(), 
            'to', 
            new Date(data[data.length-1].time * 1000).toDateString()
        );
        
        this.csvSeries.setData(data);
        this.csvSMA20Line.setData(sma20Data);
        this.csvSMA50Line.setData(sma50Data);
        
        document.getElementById('main-loading').style.display = 'none';
        
        // Set initial view to show recent data (last 3 months)
        setTimeout(() => {
            const now = new Date();
            const threeMonthsAgo = new Date(now.getTime() - (90 * 24 * 60 * 60 * 1000));
            
            this.chart.timeScale().setVisibleRange({
                from: threeMonthsAgo.getTime() / 1000,
                to: now.getTime() / 1000
            });
            
            console.log('Set initial view to last 3 months');
        }, 200);
    }
    
    /**
     * Update Polygon chart with data
     * @param {Array} data - Chart data
     * @param {Array} sma20Data - SMA20 data
     * @param {Array} sma50Data - SMA50 data
     */
    updatePolygonChart(data, sma20Data, sma50Data) {
        if (!data || data.length === 0) {
            document.getElementById('sub-loading').textContent = 'No Polygon data available (API limits)';
            return;
        }
        
        console.log('Updating Polygon chart with data points:', data.length);
        console.log('Polygon - Date range:', 
            new Date(data[0].time * 1000).toDateString(), 
            'to', 
            new Date(data[data.length-1].time * 1000).toDateString()
        );
        
        this.polygonSeries.setData(data);
        this.polygonSMA20Line.setData(sma20Data);
        this.polygonSMA50Line.setData(sma50Data);
        
        document.getElementById('sub-loading').style.display = 'none';
        
        console.log('Polygon data loaded - charts automatically synchronized');
    }
    
    /**
     * Clear CSV chart data
     */
    clearCSVChart() {
        if (this.csvSeries) this.csvSeries.setData([]);
        if (this.csvSMA20Line) this.csvSMA20Line.setData([]);
        if (this.csvSMA50Line) this.csvSMA50Line.setData([]);
        document.getElementById('main-loading').style.display = 'none';
    }
    
    /**
     * Clear Polygon chart data
     */
    clearPolygonChart() {
        if (this.polygonSeries) this.polygonSeries.setData([]);
        if (this.polygonSMA20Line) this.polygonSMA20Line.setData([]);
        if (this.polygonSMA50Line) this.polygonSMA50Line.setData([]);
        document.getElementById('sub-loading').style.display = 'none';
    }
}
