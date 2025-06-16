// Chart markers and visualization utilities

export class MarkerUtils {    /**
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
          // Use sorting field that's appropriate for finding crossovers
        // We use display time (not originalTime) as that's what our data is indexed by
        const sortedMacdData = [...macdLineData].sort((a, b) => a.time - b.time);
        const sortedSignalData = [...signalLineData].sort((a, b) => a.time - b.time);
        
        // Create a map of signal line values by time for quick lookups
        const signalByTime = new Map();
        sortedSignalData.forEach(point => {
            signalByTime.set(point.time, point.value);
        });
        
        console.log('Sample MACD data point:', sortedMacdData[0]);
        
        // Loop through MACD line data to detect crossovers with signal line
        for (let i = 1; i < sortedMacdData.length; i++) { // Start at 1 to have previous values
            const currentTime = sortedMacdData[i].time;
            const currentMacd = sortedMacdData[i].value;
            const prevTime = sortedMacdData[i-1].time;
            const prevMacd = sortedMacdData[i-1].value;
            
            // Get signal values for current and previous time point
            const currentSignal = signalByTime.get(currentTime);
            const prevSignal = signalByTime.get(prevTime);
            
            // Skip if we don't have signal values for comparison
            if (currentSignal === undefined || prevSignal === undefined) {
                continue;
            }
            
            // Log some points for debugging
            if (i % 100 === 0) {
                console.log(`Checking point ${i}/${sortedMacdData.length}:`, 
                    `Time: ${new Date(currentTime * 1000).toISOString()},`,
                    `MACD: ${prevMacd.toFixed(4)} → ${currentMacd.toFixed(4)},`,
                    `Signal: ${prevSignal.toFixed(4)} → ${currentSignal.toFixed(4)}`);
            }
            
            // Bullish Crossover: MACD crosses above Signal
            // This happens when MACD was below/equal to Signal and is now above
            if (prevMacd <= prevSignal && currentMacd > currentSignal) {
                crossovers.push({
                    time: currentTime,
                    type: 'bullish',
                    value: currentMacd, // For vertical positioning
                    macdValue: currentMacd,
                    signalValue: currentSignal
                });
                console.log(`Bullish MACD Crossover detected at ${new Date(currentTime * 1000).toISOString()} - MACD=${currentMacd.toFixed(4)}, Signal=${currentSignal.toFixed(4)}`);
            }
            // Bearish Crossover: MACD crosses below Signal
            // This happens when MACD was above/equal to Signal and is now below
            else if (prevMacd >= prevSignal && currentMacd < currentSignal) {
                crossovers.push({
                    time: currentTime,
                    type: 'bearish',
                    value: currentMacd, // For vertical positioning
                    macdValue: currentMacd,
                    signalValue: currentSignal
                });
                console.log(`Bearish MACD Crossover detected at ${new Date(currentTime * 1000).toISOString()} - MACD=${currentMacd.toFixed(4)}, Signal=${currentSignal.toFixed(4)}`);
            }
        }
        
        console.log(`MACD crossover detection completed: ${crossovers.length} crossovers found`);
        if (crossovers.length > 0) {
            console.log('First few crossovers:');
            crossovers.slice(0, 3).forEach((crossover, i) => {
                console.log(`  Crossover #${i+1}: ${crossover.type} at ${new Date(crossover.time * 1000).toISOString()}`);
            });
        }
        
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
        
        console.log(`Creating MACD crossover markers for ${crossovers.length} events`);        // Format markers exactly according to the Lightweight Charts documentation
        return crossovers.map(crossover => {
            // Format the time object according to library requirements
            // The library expects time as an object {year, month, day} or a timestamp (number)
            const timeObj = new Date(crossover.time * 1000);
            
            return {
                // Use timestamp as number for simplicity
                time: crossover.time,
                
                // Position markers appropriately based on crossover type
                // Bullish (MACD crossing above signal) should be below the bar with an up arrow
                // Bearish (MACD crossing below signal) should be above the bar with a down arrow
                position: crossover.type === 'bullish' ? 'belowBar' : 'aboveBar',
                
                // Use green for bullish, red for bearish
                color: crossover.type === 'bullish' ? '#26a69a' : '#ef5350',
                
                // Use arrow shapes to indicate direction
                shape: crossover.type === 'bullish' ? 'arrowUp' : 'arrowDown',
                
                // Add text label for the marker
                text: crossover.type === 'bullish' ? 'Buy' : 'Sell',
                
                // Enable tooltip display
                tooltip: crossover.type === 'bullish' 
                    ? 'Bullish MACD Crossover' 
                    : 'Bearish MACD Crossover',
                
                // Add ID for easier debugging
                id: `macd-${crossover.type}-${crossover.time}`
            };
        });
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
