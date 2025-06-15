// Chart markers and visualization utilities

export class MarkerUtils {
    /**
     * Calculate MACD crossovers for marking on the MACD chart
     * @param {Array} macdLineData - MACD line data points
     * @param {Array} signalLineData - Signal line data points
     * @returns {Array} Array of crossover markers
     */
    static calculateMACDCrossovers(macdLineData, signalLineData) {
        if (!macdLineData || !signalLineData || macdLineData.length === 0 || signalLineData.length === 0) {
            return [];
        }
        
        console.log(`Calculating MACD crossovers with ${macdLineData.length} MACD points and ${signalLineData.length} Signal points`);
        
        const crossovers = [];
        
        // Create a map of signal line values by time for quick lookups
        const signalByTime = new Map();
        signalLineData.forEach(point => {
            signalByTime.set(point.time, point.value);
        });
        
        // Loop through MACD line data to detect crossovers with signal line
        for (let i = 1; i < macdLineData.length; i++) { // Start at 1 to have previous values
            const currentTime = macdLineData[i].time;
            const currentMacd = macdLineData[i].value;
            const prevTime = macdLineData[i-1].time;
            const prevMacd = macdLineData[i-1].value;
            
            // Get signal values for current and previous time point
            const currentSignal = signalByTime.get(currentTime);
            const prevSignal = signalByTime.get(prevTime);
            
            // Skip if we don't have signal values for comparison
            if (currentSignal === undefined || prevSignal === undefined) {
                continue;
            }
            
            if (prevMacd <= prevSignal && currentMacd > currentSignal) {
                crossovers.push({
                    time: currentTime,
                    type: 'bullish',
                    value: currentMacd // For vertical positioning
                });
                console.log(`Bullish MACD Crossover detected at ${new Date(currentTime * 1000).toISOString()}`);
            }
            // Bearish Crossover: MACD crosses below Signal
            else if (prevMacd >= prevSignal && currentMacd < currentSignal) {
                crossovers.push({
                    time: currentTime,
                    type: 'bearish',
                    value: currentMacd // For vertical positioning
                });
                console.log(`Bearish MACD Crossover detected at ${new Date(currentTime * 1000).toISOString()}`);
            }
        }
        
        console.log(`MACD crossover detection completed: ${crossovers.length} crossovers found`);
        return crossovers;
    }

    /**
     * Create series markers from MACD crossover events
     * @param {Array} crossovers - Array of MACD crossover events with time, type, and value
     * @returns {Array} Array of marker objects for Lightweight Charts
     */
    static createMACDCrossoverMarkers(crossovers) {
        if (!crossovers || crossovers.length === 0) {
            return [];
        }
        
        console.log(`Creating MACD crossover markers for ${crossovers.length} events`);
        
        return crossovers.map(crossover => ({
            time: crossover.time,
            position: crossover.type === 'bullish' ? 'belowBar' : 'aboveBar',
            color: crossover.type === 'bullish' ? '#26a69a' : '#ef5350',
            shape: crossover.type === 'bullish' ? 'arrowUp' : 'arrowDown',
            size: 1.5,
            text: crossover.type === 'bullish' ? 'Buy' : 'Sell',
        }));
    }
    
    /**
     * Create series markers from SMA crossover events (Golden/Death crosses)
     * @param {Array} crossovers - Array of crossover events with time and type
     * @returns {Array} Array of marker objects for Lightweight Charts
     */
    static createCrossoverMarkers(crossovers) {
        if (!crossovers || crossovers.length === 0) {
            return [];
        }
        
        console.log(`Creating markers for ${crossovers.length} SMA crossover events`);
        
        return crossovers.map(crossover => ({
            time: crossover.time,
            position: crossover.type === 'golden' ? 'belowBar' : 'aboveBar',
            color: crossover.type === 'golden' ? '#FFD700' : '#FF3333',
            shape: crossover.type === 'golden' ? 'circle' : 'square',
            size: 2,
            text: crossover.type === 'golden' ? 'Golden Cross' : 'Death Cross',
        }));
    }
    
    /**
     * Create volume profile visualization
     * @param {Array} data - Array of bar data points with OHLC and volume values
     * @param {number} numLevels - Number of price levels for the volume profile
     * @returns {Array} Array of volume profile data points for visualization
     */
    static calculateVolumeProfile(data, numLevels = 20) {
        if (!data || data.length === 0) {
            return [];
        }
        
        // Find price range
        let minPrice = Infinity;
        let maxPrice = -Infinity;
        
        for (const bar of data) {
            minPrice = Math.min(minPrice, bar.low);
            maxPrice = Math.max(maxPrice, bar.high);
        }
        
        // Create price levels
        const levelHeight = (maxPrice - minPrice) / numLevels;
        const volumeByLevel = new Array(numLevels).fill(0);
        
        // Aggregate volume by price level
        for (const bar of data) {
            const avgPrice = (bar.high + bar.low + bar.close) / 3;
            const levelIndex = Math.floor((avgPrice - minPrice) / levelHeight);
            
            // Ensure the index is within bounds
            const boundedIndex = Math.min(Math.max(levelIndex, 0), numLevels - 1);
            volumeByLevel[boundedIndex] += bar.volume;
        }
        
        // Create visualization data
        const profileData = volumeByLevel.map((volume, index) => ({
            price: minPrice + (index * levelHeight) + (levelHeight / 2),
            volume: volume
        }));
        
        return profileData;
    }
}
