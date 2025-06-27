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
    
    /**
     * Calculate RSI level crossovers (overbought/oversold) for marking on the RSI chart
     * @param {Array} rsiData - RSI data points with time and value
     * @param {number} overboughtLevel - Overbought level (default 70)
     * @param {number} oversoldLevel - Oversold level (default 30)
     * @returns {Array} Array of RSI level crossover markers
     */
    static calculateRSICrossovers(rsiData, overboughtLevel = 70, oversoldLevel = 30) {
        if (!rsiData || rsiData.length === 0) {
            console.warn('RSI data is empty or undefined');
            return [];
        }
        
        console.log(`Calculating RSI level crossovers with ${rsiData.length} RSI points`);
        console.log('RSI data sample (first point):', JSON.stringify(rsiData[0]));
        
        // Check if the data has the required structure
        if (!rsiData[0].hasOwnProperty('value') || !rsiData[0].hasOwnProperty('time')) {
            console.error('RSI data points are missing required properties (time or value)');
            console.log('Properties available:', Object.keys(rsiData[0]));
            return [];
        }
        
        // Debug data range
        const values = rsiData.map(d => d.value);
        const minRsi = Math.min(...values);
        const maxRsi = Math.max(...values);
        console.log(`RSI value range: min=${minRsi.toFixed(2)}, max=${maxRsi.toFixed(2)}`);
        
        // Check if data crosses the thresholds
        const above70 = rsiData.some(d => d.value >= overboughtLevel);
        const below30 = rsiData.some(d => d.value <= oversoldLevel);
        console.log(`RSI data crosses thresholds: Above ${overboughtLevel}: ${above70}, Below ${oversoldLevel}: ${below30}`);
        
        const crossovers = [];
        
        // Sort RSI data by time
        const sortedRsiData = [...rsiData].sort((a, b) => a.time - b.time);
        
        // Loop through RSI data to detect crossovers with overbought/oversold levels
        for (let i = 1; i < sortedRsiData.length; i++) { // Start at 1 to have previous values
            const currentTime = sortedRsiData[i].time;
            const currentRsi = sortedRsiData[i].value;
            const prevRsi = sortedRsiData[i-1].value;
            
            // Overbought condition (crossing above 70)
            if (prevRsi < overboughtLevel && currentRsi >= overboughtLevel) {
                crossovers.push({
                    time: currentTime,
                    type: 'overbought',
                    value: currentRsi,
                    direction: 'up', // Direction of crossing
                    level: overboughtLevel
                });
                console.log(`RSI Overbought Crossover detected at ${new Date(currentTime * 1000).toISOString()} - RSI=${currentRsi.toFixed(2)}`);
            }
            
            // Oversold condition (crossing below 30)
            else if (prevRsi > oversoldLevel && currentRsi <= oversoldLevel) {
                crossovers.push({
                    time: currentTime,
                    type: 'oversold',
                    value: currentRsi,
                    direction: 'down', // Direction of crossing
                    level: oversoldLevel
                });
                console.log(`RSI Oversold Crossover detected at ${new Date(currentTime * 1000).toISOString()} - RSI=${currentRsi.toFixed(2)}`);
            }
            
            // Recovery from oversold (crossing back above 30)
            else if (prevRsi <= oversoldLevel && currentRsi > oversoldLevel) {
                crossovers.push({
                    time: currentTime,
                    type: 'oversold_exit',
                    value: currentRsi,
                    direction: 'up', // Direction of crossing
                    level: oversoldLevel
                });
                console.log(`RSI Oversold Exit detected at ${new Date(currentTime * 1000).toISOString()} - RSI=${currentRsi.toFixed(2)}`);
            }
            
            // Recovery from overbought (crossing back below 70)
            else if (prevRsi >= overboughtLevel && currentRsi < overboughtLevel) {
                crossovers.push({
                    time: currentTime,
                    type: 'overbought_exit',
                    value: currentRsi,
                    direction: 'down', // Direction of crossing
                    level: overboughtLevel
                });
                console.log(`RSI Overbought Exit detected at ${new Date(currentTime * 1000).toISOString()} - RSI=${currentRsi.toFixed(2)}`);
            }
        }
        
        console.log(`RSI crossover detection completed: ${crossovers.length} crossovers found`);
        if (crossovers.length > 0) {
            console.log('First few RSI crossovers:');
            crossovers.slice(0, 3).forEach((crossover, i) => {
                console.log(`  Crossover #${i+1}: ${crossover.type} at ${new Date(crossover.time * 1000).toISOString()}`);
            });
        }
        
        return crossovers;
    }

    /**
     * Create series markers from RSI level crossover events
     * @param {Array} crossovers - Array of RSI crossover events with time, type, and value
     * @returns {Array} Array of marker objects for Lightweight Charts
     */
    static createRSICrossoverMarkers(crossovers) {
        if (!crossovers || crossovers.length === 0) {
            console.log('No crossovers to create markers from');
            return [];
        }
        
        console.log(`Creating RSI crossover markers for ${crossovers.length} events`);
        console.log('First crossover for marker creation:', JSON.stringify(crossovers[0]));
        
        // Format markers according to the Lightweight Charts documentation
        return crossovers.map(crossover => {
            let color, shape, position, text, tooltip;
            
            // Configure marker appearance based on crossover type
            switch(crossover.type) {
                case 'overbought':
                    color = '#ef5350'; // Red for warning
                    shape = 'circle';
                    position = 'aboveBar';
                    text = 'OB';
                    tooltip = 'Overbought: RSI crossed above 70';
                    break;
                    
                case 'overbought_exit':
                    color = '#ff9800'; // Orange for recovery from overbought
                    shape = 'arrowDown';
                    position = 'aboveBar';
                    text = 'OB Exit';
                    tooltip = 'Overbought Exit: RSI crossed below 70';
                    break;
                    
                case 'oversold':
                    color = '#26a69a'; // Green for potential buy
                    shape = 'circle';
                    position = 'belowBar';
                    text = 'OS';
                    tooltip = 'Oversold: RSI crossed below 30';
                    break;
                    
                case 'oversold_exit':
                    color = '#4caf50'; // Lighter green for recovery from oversold
                    shape = 'arrowUp';
                    position = 'belowBar';
                    text = 'OS Exit';
                    tooltip = 'Oversold Exit: RSI crossed above 30';
                    break;
                    
                default:
                    color = '#9e9e9e'; // Default gray
                    shape = 'square';
                    position = 'inBar';
                    text = 'RSI';
                    tooltip = 'RSI Level Cross';
            }
            
            return {
                time: crossover.time,
                position: position,
                color: color,
                shape: shape,
                text: text,
                tooltip: tooltip,
                id: `rsi-${crossover.type}-${crossover.time}`
            };
        });
    }
    
    /**
     * Calculate Golden Cross and Death Cross events from SMA data
     * @param {Array} sma50Data - SMA 50 data points with time and value
     * @param {Array} sma200Data - SMA 200 data points with time and value
     * @returns {Array} Array of golden/death cross events
     */
    static calculateGoldenDeathCrosses(sma50Data, sma200Data) {
        if (!sma50Data || !sma200Data || sma50Data.length === 0 || sma200Data.length === 0) {
            console.warn('Insufficient SMA data for golden/death cross detection');
            return [];
        }
        
        console.log(`Calculating Golden/Death crosses with ${sma50Data.length} SMA50 points and ${sma200Data.length} SMA200 points`);
        
        const crossovers = [];
        
        // Sort data by time
        const sortedSma50Data = [...sma50Data].sort((a, b) => a.time - b.time);
        const sortedSma200Data = [...sma200Data].sort((a, b) => a.time - b.time);
        
        // Create a map of SMA 200 values by time for quick lookups
        const sma200ByTime = new Map();
        sortedSma200Data.forEach(point => {
            sma200ByTime.set(point.time, point.value);
        });
        
        console.log('Sample SMA data:', {
            sma50Sample: sortedSma50Data[0],
            sma200Sample: sortedSma200Data[0]
        });
        
        // Loop through SMA50 data to detect crossovers with SMA200
        for (let i = 1; i < sortedSma50Data.length; i++) { // Start at 1 to have previous values
            const currentTime = sortedSma50Data[i].time;
            const currentSma50 = sortedSma50Data[i].value;
            const prevTime = sortedSma50Data[i-1].time;
            const prevSma50 = sortedSma50Data[i-1].value;
            
            // Get SMA200 values for current and previous time points
            const currentSma200 = sma200ByTime.get(currentTime);
            const prevSma200 = sma200ByTime.get(prevTime);
            
            // Skip if we don't have SMA200 values for comparison
            if (currentSma200 === undefined || prevSma200 === undefined) {
                continue;
            }
            
            // Golden Cross: SMA50 crosses above SMA200
            if (prevSma50 <= prevSma200 && currentSma50 > currentSma200) {
                crossovers.push({
                    time: currentTime,
                    type: 'golden',
                    sma50Value: currentSma50,
                    sma200Value: currentSma200
                });
                console.log(`Golden Cross detected at ${new Date(currentTime * 1000).toISOString()} - SMA50=${currentSma50.toFixed(2)}, SMA200=${currentSma200.toFixed(2)}`);
            }
            // Death Cross: SMA50 crosses below SMA200
            else if (prevSma50 >= prevSma200 && currentSma50 < currentSma200) {
                crossovers.push({
                    time: currentTime,
                    type: 'death',
                    sma50Value: currentSma50,
                    sma200Value: currentSma200
                });
                console.log(`Death Cross detected at ${new Date(currentTime * 1000).toISOString()} - SMA50=${currentSma50.toFixed(2)}, SMA200=${currentSma200.toFixed(2)}`);
            }
        }
        
        console.log(`Golden/Death cross detection completed: ${crossovers.length} crossovers found`);
        if (crossovers.length > 0) {
            console.log('First few golden/death crosses:');
            crossovers.slice(0, 3).forEach((crossover, i) => {
                console.log(`  Cross #${i+1}: ${crossover.type} at ${new Date(crossover.time * 1000).toISOString()}`);
            });
        }
        
        return crossovers;
    }

    /**
     * Create series markers from Golden/Death cross events for candlestick charts
     * @param {Array} crossovers - Array of golden/death cross events with time and type
     * @returns {Array} Array of marker objects for Lightweight Charts
     */
    static createGoldenDeathCrossMarkers(crossovers) {
        if (!crossovers || crossovers.length === 0) {
            console.log('No golden/death crosses to create markers from');
            return [];
        }
        
        console.log(`Creating Golden/Death cross markers for ${crossovers.length} events`);
        console.log('First crossover for marker creation:', JSON.stringify(crossovers[0]));
        
        // Format markers according to the Lightweight Charts documentation
        return crossovers.map(crossover => {
            let color, shape, position, text, tooltip;
            
            // Configure marker appearance based on crossover type
            if (crossover.type === 'golden') {
                color = '#FFD700'; // Gold color for Golden Cross
                shape = 'arrowUp';
                position = 'belowBar';
                text = 'GC';
                tooltip = 'Golden Cross: SMA50 crossed above SMA200';
            } else if (crossover.type === 'death') {
                color = '#FF4444'; // Red color for Death Cross
                shape = 'arrowDown';
                position = 'aboveBar';
                text = 'DC';
                tooltip = 'Death Cross: SMA50 crossed below SMA200';
            } else {
                // Default styling for unknown crossover types
                color = '#888888';
                shape = 'circle';
                position = 'inBar';
                text = 'X';
                tooltip = 'SMA Crossover';
            }
            
            return {
                time: crossover.time,
                position: position,
                color: color,
                shape: shape,
                text: text,
                tooltip: tooltip,
                id: `sma-${crossover.type}-${crossover.time}`
            };
        });
    }
}
