// Utility functions for data processing and calculations

export class DataUtils {
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
                // Numeric timestamp
                timeValue = parseInt(timeValue);
                if (timeValue > 1000000000000) {
                    timeValue = timeValue / 1000;
                }            } else {
                  const [datePart, timePart] = timeValue.split(' ');
                const [year, month, day] = datePart.split('-').map(Number);
                const [hour, minute, second] = timePart.split(':').map(Number);
                
                // CSV time is already in Eastern Time format
                // Treat it as UTC so the chart displays it correctly
                const utcDate = new Date(Date.UTC(year, month - 1, day, hour, minute, second || 0));
                timeValue = utcDate.getTime() / 1000;
                
                if (i <= 3) {
                    console.log(`CSV Parse Debug - Entry ${i}:`);
                    console.log(`  Original CSV: ${values[timeIndex]} (Eastern Time)`);
                    console.log(`  Treating as UTC: ${utcDate.toISOString()}`);
                    console.log(`  Timestamp: ${timeValue}`);
                }
            }
            
            // Parse volume
            let volumeValue = 0;
            if (volumeIndex >= 0 && values[volumeIndex]) {
                volumeValue = parseFloat(values[volumeIndex]);
                if (isNaN(volumeValue)) volumeValue = 0;
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
     * Calculate Simple Moving Average
     * @param {Array} data - Array of price data
     * @param {number} period - SMA period
     * @returns {Array} Array of SMA data points
     */
    static calculateSMA(data, period) {
        const smaData = [];
        
        for (let i = 0; i < data.length; i++) {
            if (i < period - 1) {
                continue;
            }
            
            let sum = 0;
            for (let j = 0; j < period; j++) {
                sum += data[i - j].close;
            }
            
            smaData.push({
                time: data[i].time,
                value: sum / period
            });
        }
        
        return smaData;
    }
    
    /**
     * Filter data to market hours only
     * @param {Array} data - Array of data points with timestamp
     * @param {number} openMinutes - Market open time in minutes from midnight
     * @param {number} closeMinutes - Market close time in minutes from midnight
     * @returns {Array} Filtered data array
     */
    static filterMarketHours(data, openMinutes = 570, closeMinutes = 960) {
        return data.filter(item => {
            const utcDate = new Date(item.t);
            const etHours = utcDate.getUTCHours() - 4; // EDT offset
            const etMinutes = utcDate.getUTCMinutes();
            
            const adjustedHours = etHours < 0 ? etHours + 24 : etHours;
            const etTimeInMinutes = adjustedHours * 60 + etMinutes;
            
            return etTimeInMinutes >= openMinutes && etTimeInMinutes <= closeMinutes;
        });
    }
    
    /**
     * Transform Polygon API data to chart format
     * @param {Array} apiData - Raw API data from Polygon
     * @returns {Array} Transformed data for charts
     */
    static transformPolygonData(apiData) {
        return apiData.map(item => {
            let volume = item.v;
            if (volume === undefined || volume === null) {
                console.log('Missing volume for data point:', item);
                volume = 0;
            }
            
            // Convert UTC timestamp to Eastern Time
            const etTimestamp = item.t - (4 * 60 * 60 * 1000);
            
            return {
                time: etTimestamp / 1000,
                open: item.o,
                high: item.h,
                low: item.l,
                close: item.c,
                volume: volume
            };        });
    }
    
    /**
     * Check if a given date falls during Daylight Saving Time in Eastern timezone
     * @param {Date} date - Date to check
     * @returns {boolean} True if DST is in effect
     */
    static isDaylightSavingTime(date) {
        const year = date.getFullYear();
        
        // DST starts on second Sunday in March
        const march = new Date(year, 2, 1); // March 1st
        let dstStart = new Date(year, 2, 1);
        let sundayCount = 0;
        
        // Find second Sunday in March
        for (let d = 1; d <= 31; d++) {
            const checkDate = new Date(year, 2, d);
            if (checkDate.getDay() === 0) { // Sunday
                sundayCount++;
                if (sundayCount === 2) {
                    dstStart = checkDate;
                    break;
                }
            }
        }
        
        // DST ends on first Sunday in November
        const november = new Date(year, 10, 1); // November 1st
        let dstEnd = new Date(year, 10, 1);
        
        // Find first Sunday in November
        for (let d = 1; d <= 7; d++) {
            const checkDate = new Date(year, 10, d);
            if (checkDate.getDay() === 0) { // Sunday
                dstEnd = checkDate;
                break;
            }
        }
        
        // Check if date falls between DST start and end
        return date >= dstStart && date < dstEnd;
    }
}
