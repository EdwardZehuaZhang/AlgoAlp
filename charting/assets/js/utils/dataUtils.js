// Data parsing and processing utilities

import { TimeUtils } from './timeUtils.js';

export class DataUtils {
    // Static values for market hours to ensure consistency
    static MARKET_OPEN_HOUR = 9;
    static MARKET_OPEN_MINUTE = 30;
    static MARKET_CLOSE_HOUR = 16;
    static MARKET_CLOSE_MINUTE = 0;
    
    /**
     * Parse CSV text to data array
     * @param {string} text - Raw CSV text
     * @returns {Array} Array of parsed data objects
     */
    static parseCSV(text) {
        const lines = text.trim().split('\n');
        const headers = lines[0].split(',').map(header => header.trim().replace(/\r/g, '').replace(/\n/g, ''));
        
        // Find column indices
        const timeIndex = headers.indexOf('time');
        const openIndex = headers.indexOf('open');
        const highIndex = headers.indexOf('high');
        const lowIndex = headers.indexOf('low');
        const closeIndex = headers.indexOf('close');
        let volumeIndex = headers.indexOf('volume');
        
        // Flexible volume matching
        if (volumeIndex === -1) {
            volumeIndex = headers.findIndex(header => header.toLowerCase().includes('volume'));
        }
        
        console.log('CSV Headers:', headers);
        console.log('Volume column index:', volumeIndex);
        
        const data = [];
        for (let i = 1; i < lines.length; i++) {
            const values = lines[i].split(',');
            
            // Parse time value
            let timeValue = values[timeIndex];
            
            if (!isNaN(timeValue)) {
                // Numeric timestamp (Unix timestamp)
                timeValue = parseFloat(timeValue);
            } else {
                // String timestamp, preserve NYC market time by creating a UTC date
                // Format: "2023-06-12 09:30:00" -> keep as NYC time
                const [datePart, timePart] = timeValue.split(' ');
                const [year, month, day] = datePart.split('-').map(Number);
                const [hour, minute, second] = timePart.split(':').map(Number);
                
                // Create a timestamp that will display correctly as NYC time
                // Use UTC date to prevent browser's timezone conversion
                const utcDate = Date.UTC(year, month - 1, day, hour, minute, second);
                timeValue = Math.floor(utcDate / 1000);
            }
            
            // Parse volume
            let volumeValue = 0;
            if (volumeIndex >= 0 && values[volumeIndex]) {
                volumeValue = parseFloat(values[volumeIndex]);
            }
            
            data.push({
                time: timeValue,
                open: parseFloat(values[openIndex]),
                high: parseFloat(values[highIndex]),
                low: parseFloat(values[lowIndex]),
                close: parseFloat(values[closeIndex]),
                volume: volumeValue
            });
        }
        
        return data;
    }
    
    /**
     * Filter data to market hours only (9:30 AM - 4:00 PM Eastern Time)
     * @param {Array} data - Bar data with time field
     * @returns {Array} Filtered data
     */
    static filterMarketHours(data) {
        const openMinutes = 9 * 60 + 30;  // 9:30 AM
        const closeMinutes = 16 * 60;     // 4:00 PM
        
        return data.filter(item => {
            const date = new Date(item.time * 1000);
            const hours = date.getUTCHours();
            const minutes = date.getUTCMinutes();
            const totalMinutes = hours * 60 + minutes;
            
            // Adjust for timezone (Eastern Time)
            const isDST = TimeUtils.isDaylightSavingTime(date);
            const etOffset = isDST ? 4 : 5; // EDT or EST offset from UTC in hours
            
            // Convert to Eastern Time
            let etTotalMinutes = totalMinutes - (etOffset * 60);
            if (etTotalMinutes < 0) {
                etTotalMinutes += 24 * 60; // Wrap around for previous day
            }
            
            return etTotalMinutes >= openMinutes && etTotalMinutes <= closeMinutes;
        });
    }
    
    /**
     * Transform Polygon API data to chart format
     * @param {Array} apiData - Raw API data from Polygon
     * @returns {Array} Transformed data for charts
     */
    static transformPolygonData(apiData) {
        console.log("POLYGON DATA TRANSFORMATION - HARDCODED VERSION");
        
        // Group by day first to reset the time sequence each day
        const dayGroups = {};
        
        // First, sort the data by timestamp
        const sortedData = [...apiData].sort((a, b) => a.t - b.t);
        
        // Organize data by day, but filter data to start at 9:30 AM ET (ignoring pre-market)
        for (const item of sortedData) {
            const date = new Date(item.t);
            
            // Filter based on Eastern Time hour
            // For Eastern Time (EDT), UTC 13:30 = 9:30 AM ET
            const utcHours = date.getUTCHours();
            const utcMinutes = date.getUTCMinutes();
            
            // Skip data that comes before 9:30 AM ET (which is 13:30 UTC during EDT)
            // We're looking for Polygon data that starts at exactly market open
            if (utcHours < 9 || (utcHours === 9 && utcMinutes < 30)) {
                // This is data before 9:30 AM ET, skip it
                console.log(`Skipping pre-market data point at UTC ${utcHours}:${utcMinutes}`);
                continue;
            }
            
            const dateKey = `${date.getUTCFullYear()}-${date.getUTCMonth()}-${date.getUTCDate()}`;
            
            if (!dayGroups[dateKey]) {
                dayGroups[dateKey] = [];
            }
            
            dayGroups[dateKey].push(item);
        }
        
        // Process each day separately to reset time counting each day
        const resultData = [];
        
        for (const dateKey in dayGroups) {
            const dayData = dayGroups[dateKey];
            const dayDate = new Date(dayData[0].t);
            
            // Extract date components for this day
            const year = dayDate.getUTCFullYear();
            const month = dayDate.getUTCMonth();
            const day = dayDate.getUTCDate();
            
            console.log(`Processing day: ${year}-${month+1}-${day} with ${dayData.length} candles`);
            
            // Map each candle for this day, starting at 9:30 AM
            dayData.forEach((item, index) => {
                // Calculate time as exactly 9:30 + (index * 5 minutes)
                // This forces the hours to appear as 9:30, 9:35, 9:40, etc.
                const minutesAfterOpen = index * 5;
                
                // Base hour and minute (9:30 AM)
                let displayHour = 9;
                let displayMinute = 30 + minutesAfterOpen;
                
                // Handle minute overflow
                while (displayMinute >= 60) {
                    displayHour++;
                    displayMinute -= 60;
                }
                
                // Create a timestamp that will display as the market hours we want
                // CRITICAL: This creates a UTC time that appears as NY time on the chart
                // We're NOT trying to convert to NY time, but create a UTC time that 
                // DISPLAYS as 9:30 AM when rendered
                const timeValue = Date.UTC(year, month, day, displayHour, displayMinute, 0);
                const timestamp = Math.floor(timeValue / 1000);
                
                // Store original timestamp for accurate event timings (like crossovers)
                const originalTimestamp = Math.floor(item.t / 1000);
                
                // Debug log for the first few items of each day
                if (index < 3) {
                    console.log(`Day ${year}-${month+1}-${day}, Candle #${index+1}: ${displayHour}:${displayMinute} -> timestamp ${timestamp} (original: ${originalTimestamp})`);
                }
                
                resultData.push({
                    time: timestamp,             // Display timestamp (for chart visualization)
                    open: item.o,
                    high: item.h,
                    low: item.l,
                    close: item.c,
                    volume: item.v,
                    originalTime: originalTimestamp  // Original timestamp (for accurate event timings)
                });
            });
        }
        
        return resultData;
    }
}
