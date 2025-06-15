// Main application controller

import { CONFIG } from './config.js';
import { ChartManager } from './chartManager.js';
import { DataManager } from './dataManager.js';

class SpyChartApp {
    constructor() {
        this.chartManager = new ChartManager();
        this.dataManager = new DataManager(this.chartManager);
    }
    
    /**
     * Initialize the application
     */
    init() {
        this.chartManager.createCharts();
        this.setupEventListeners();
        this.setDataSource('both'); // Default to both sources
    }
    
    /**
     * Setup event listeners for UI controls
     */
    setupEventListeners() {
        document.getElementById('btn-load-both').addEventListener('click', () => {
            this.setDataSource('both');
        });
        
        document.getElementById('btn-csv-only').addEventListener('click', () => {
            this.setDataSource('csv');
        });
        
        document.getElementById('btn-polygon-only').addEventListener('click', () => {
            this.setDataSource('polygon');
        });
    }
    
    /**
     * Set the data source and load data
     * @param {string} source - Data source: 'both', 'csv', or 'polygon'
     */
    setDataSource(source) {
        // Update active button styling
        document.getElementById('btn-load-both').classList.toggle('active', source === 'both');
        document.getElementById('btn-csv-only').classList.toggle('active', source === 'csv');
        document.getElementById('btn-polygon-only').classList.toggle('active', source === 'polygon');
        
        // Show loading messages
        if (source === 'both' || source === 'csv') {
            document.getElementById('main-loading').style.display = 'block';
        }
        
        if (source === 'both' || source === 'polygon') {
            document.getElementById('sub-loading').style.display = 'block';
            document.getElementById('sub-loading').textContent = 'Loading Polygon data...';
        }
        
        // Clear any existing data
        this.chartManager.clearCharts();
        
        // Load the requested data sources
        if (source === 'both' || source === 'csv') {
            this.dataManager.loadCSVData();
        }
        
        if (source === 'both' || source === 'polygon') {
            this.dataManager.loadPolygonData();
        }
        
        // Show/hide series based on selected data source
        this.chartManager.showDataSource(source);
    }
}

// Initialize the application when the DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    const app = new SpyChartApp();
    app.init();
});
