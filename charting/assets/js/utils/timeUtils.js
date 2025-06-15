// Time and date related utilities

export class TimeUtils {
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
    
    /**
     * Format timestamp for display
     * @param {number} timestamp - Unix timestamp in seconds
     * @param {string} format - Format type ('date', 'time', 'datetime')
     * @returns {string} Formatted date/time string
     */
    static formatTimestamp(timestamp, format = 'datetime') {
        const date = new Date(timestamp * 1000);
        const options = {};
        
        switch (format) {
            case 'date':
                options.year = 'numeric';
                options.month = 'short';
                options.day = 'numeric';
                break;
            case 'time':
                options.hour = 'numeric';
                options.minute = '2-digit';
                options.hour12 = true;
                break;
            case 'datetime':
            default:
                options.year = 'numeric';
                options.month = 'short';
                options.day = 'numeric';
                options.hour = 'numeric';
                options.minute = '2-digit';
                options.hour12 = true;
                break;
        }
        
        return new Intl.DateTimeFormat('en-US', options).format(date);
    }
    
    /**
     * Get market sessions for a given date
     * @param {Date} date - Date to check
     * @returns {Object} Object containing market session timestamps
     */
    static getMarketSessions(date) {
        const year = date.getFullYear();
        const month = date.getMonth();
        const day = date.getDate();
        
        // Create base date objects for market sessions
        const preMarket = new Date(year, month, day, 4, 0, 0); // 4:00 AM ET
        const marketOpen = new Date(year, month, day, 9, 30, 0); // 9:30 AM ET
        const marketClose = new Date(year, month, day, 16, 0, 0); // 4:00 PM ET
        const afterHours = new Date(year, month, day, 20, 0, 0); // 8:00 PM ET
        
        return {
            preMarket: Math.floor(preMarket.getTime() / 1000),
            marketOpen: Math.floor(marketOpen.getTime() / 1000),
            marketClose: Math.floor(marketClose.getTime() / 1000),
            afterHours: Math.floor(afterHours.getTime() / 1000)
        };
    }
}
