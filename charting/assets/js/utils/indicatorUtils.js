// Technical indicators and calculation utilities

export class IndicatorUtils {
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
                // Not enough data for SMA calculation
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
     * Calculate Exponential Moving Average (EMA)
     * @param {Array} data - Array of data points with close values
     * @param {number} period - EMA period
     * @returns {Array} Array of EMA values
     */
    static calculateEMA(data, period) {
        if (!data || data.length === 0 || period <= 0) {
            return [];
        }
        
        const ema = [];
        const multiplier = 2 / (period + 1);
        
        // Start with first close price as initial EMA
        ema[0] = data[0].close;
        
        for (let i = 1; i < data.length; i++) {
            ema[i] = ((data[i].close - ema[i-1]) * multiplier) + ema[i-1];
        }
        
        return ema;
    }
    
    /**
     * Calculate complete MACD data for Lightweight Charts
     * @param {Array} data - Array of data points with close values
     * @param {number} fastPeriod - Fast EMA period (default: 12)
     * @param {number} slowPeriod - Slow EMA period (default: 26)
     * @param {number} signalPeriod - Signal line EMA period (default: 9)
     * @returns {Object} Object containing histogram, macdLine, and signalLine arrays
     */


static calculateMACDComplete(data, fastPeriod = 12, slowPeriod = 26, signalPeriod = 9) {
    if (!data || data.length === 0) {
        return {
            histogram: [],
            macdLine: [],
            signalLine: []
        };
    }
    
    console.log(`Calculating complete MACD with periods: Fast=${fastPeriod}, Slow=${slowPeriod}, Signal=${signalPeriod}`);
    console.log(`Input data length: ${data.length} points`);
    
    // CALCULATION PHASE - Use all data points
    // Calculate EMAs
    const fastEMA = this.calculateEMA(data, fastPeriod);
    const slowEMA = this.calculateEMA(data, slowPeriod);
    
    console.log(`Fast EMA calculated: ${fastEMA.filter(x => x !== undefined).length} valid points`);
    console.log(`Slow EMA calculated: ${slowEMA.filter(x => x !== undefined).length} valid points`);
    
    // Calculate MACD line (Fast EMA - Slow EMA)
    const macdValues = [];
    const allMacdLineData = [];
    
    let validMACDCount = 0;
    for (let i = 0; i < data.length; i++) {
        if (fastEMA[i] !== undefined && slowEMA[i] !== undefined) {
            const macdValue = fastEMA[i] - slowEMA[i];
            macdValues.push(macdValue);
            allMacdLineData.push({
                time: data[i].time,
                value: macdValue,
                originalTime: data[i].originalTime || data[i].time
            });
            validMACDCount++;
        } else {
            macdValues.push(undefined);
        }
    }
    
    console.log(`MACD line calculated: ${validMACDCount} valid points`);
    
    // Create temporary data array for signal EMA calculation with ALL MACD values
    const macdData = macdValues.map((value, index) => ({
        close: value,
        time: data[index].time,
        originalTime: data[index].originalTime || data[index].time
    })).filter(item => item.close !== undefined);
    
    // Calculate Signal line (EMA of MACD)
    const signalEMAValues = this.calculateEMA(macdData, signalPeriod);
    
    // Map signal values back to original indices
    const signalValues = new Array(data.length).fill(undefined);
    let signalIdx = 0;
    for (let i = 0; i < data.length; i++) {
        if (fastEMA[i] !== undefined && slowEMA[i] !== undefined) {
            if (signalIdx < signalEMAValues.length) {
                signalValues[i] = signalEMAValues[signalIdx];
                signalIdx++;
            }
        }
    }
    
    // PREPARATION PHASE - Create all data points
    const allSignalLineData = [];
    const allHistogramData = [];
    
    for (let i = 0; i < data.length; i++) {
        if (macdValues[i] !== undefined && signalValues[i] !== undefined) {
            // Signal line data
            allSignalLineData.push({
                time: data[i].time,
                value: signalValues[i],
                originalTime: data[i].originalTime || data[i].time
            });
            
            // Histogram data (MACD - Signal)
            const histogram = macdValues[i] - signalValues[i];
            allHistogramData.push({
                time: data[i].time,
                value: histogram,
                color: histogram >= 0 ? '#26a69a' : '#ef5350', // Green for positive, red for negative
                originalTime: data[i].originalTime || data[i].time
            });
        }
    }
    
    // FILTERING PHASE - Filter data points to desired timeframe
    const isWithinTimeframe = (timestamp) => {
        const date = new Date(timestamp * 1000);
        const hours = date.getHours();
        
        // Adjust this condition based on your specific timeframe requirements
        // For example, for market hours (9:30 AM - 4:00 PM):
        return hours >= 21 || hours < 4;  // For your specific use case
    };
    
    // Apply filtering to output data
    const macdLineData = allMacdLineData.filter(item => isWithinTimeframe(item.time));
    const signalLineData = allSignalLineData.filter(item => isWithinTimeframe(item.time));
    const histogramData = allHistogramData.filter(item => isWithinTimeframe(item.time));
    
    console.log(`All MACD data points: ${allMacdLineData.length}`);
    console.log(`Filtered MACD data points: ${macdLineData.length}`);
    console.log(`Filtered signal line data points: ${signalLineData.length}`);
    console.log(`Filtered histogram data points: ${histogramData.length}`);
    
    return {
        histogram: histogramData,
        macdLine: macdLineData,
        signalLine: signalLineData
    };
}
    /**
     * Calculate MACD Histogram data for Lightweight Charts (backward compatibility)
     * @param {Array} data - Array of data points with close values
     * @param {number} fastPeriod - Fast EMA period (default: 12)
     * @param {number} slowPeriod - Slow EMA period (default: 26)
     * @param {number} signalPeriod - Signal line EMA period (default: 9)
     * @returns {Array} Array of histogram data points for chart
     */
static calculateMACDComplete(data, fastPeriod = 12, slowPeriod = 26, signalPeriod = 9) {
    if (!data || data.length === 0) {
        return {
            histogram: [],
            macdLine: [],
            signalLine: []
        };
    }
    
    console.log(`Calculating complete MACD with periods: Fast=${fastPeriod}, Slow=${slowPeriod}, Signal=${signalPeriod}`);
    
    // CALCULATION PHASE - Use all data points
    // Calculate EMAs
    const fastEMA = this.calculateEMA(data, fastPeriod);
    const slowEMA = this.calculateEMA(data, slowPeriod);
    
    // Calculate MACD line (Fast EMA - Slow EMA)
    const macdValues = [];
    const allMacdLineData = [];
    
    for (let i = 0; i < data.length; i++) {
        if (fastEMA[i] !== undefined && slowEMA[i] !== undefined) {
            const macdValue = fastEMA[i] - slowEMA[i];
            macdValues.push(macdValue);
            
            // Shift time by subtracting 4 hours (4 * 60 * 60 seconds)
            const adjustedTime = data[i].time - (4 * 60 * 60);
            
            allMacdLineData.push({
                time: adjustedTime,
                value: macdValue,
                originalTime: data[i].time
            });
        } else {
            macdValues.push(undefined);
        }
    }
    
    // Create temporary data array for signal EMA calculation
    const macdData = macdValues.map((value, index) => ({
        close: value,
        time: data[index].time, // Keep original time for calculation
        originalTime: data[index].time
    })).filter(item => item.close !== undefined);
    
    // Calculate Signal line (EMA of MACD)
    const signalEMAValues = this.calculateEMA(macdData, signalPeriod);
    
    // Map signal values back to original indices
    const signalValues = new Array(data.length).fill(undefined);
    let signalIdx = 0;
    for (let i = 0; i < data.length; i++) {
        if (fastEMA[i] !== undefined && slowEMA[i] !== undefined) {
            if (signalIdx < signalEMAValues.length) {
                signalValues[i] = signalEMAValues[signalIdx];
                signalIdx++;
            }
        }
    }
    
    // Format signal line data and calculate histogram with adjusted timestamps
    const allSignalLineData = [];
    const allHistogramData = [];
    
    for (let i = 0; i < data.length; i++) {
        if (macdValues[i] !== undefined && signalValues[i] !== undefined) {
            // Shift time by subtracting 4 hours (4 * 60 * 60 seconds)
            const adjustedTime = data[i].time - (4 * 60 * 60);
            
            // Signal line data
            allSignalLineData.push({
                time: adjustedTime,
                value: signalValues[i],
                originalTime: data[i].time
            });
            
            // Histogram data (MACD - Signal)
            const histogram = macdValues[i] - signalValues[i];
            allHistogramData.push({
                time: adjustedTime,
                value: histogram,
                color: histogram >= 0 ? '#26a69a' : '#ef5350', // Green for positive, red for negative
                originalTime: data[i].time
            });
        }
    }
    
    // FILTERING PHASE - Filter data points to desired timeframe
    const isWithinTimeframe = (timestamp) => {
        const date = new Date(timestamp * 1000);
        const hours = date.getHours();
        return hours >= 17 || hours < 4;  // Keep the same filtering
    };
    
    // Apply filtering to output data with adjusted timestamps
    const macdLineData = allMacdLineData.filter(item => isWithinTimeframe(item.time));
    const signalLineData = allSignalLineData.filter(item => isWithinTimeframe(item.time));
    const histogramData = allHistogramData.filter(item => isWithinTimeframe(item.time));
    
    console.log(`All MACD data points: ${allMacdLineData.length}`);
    console.log(`Filtered MACD data points: ${macdLineData.length}`);
    
    return {
        histogram: histogramData,
        macdLine: macdLineData,
        signalLine: signalLineData
    };
}

      /**
     * Calculate Relative Strength Index (RSI)
     * @param {Array} data - Array of price data points (should already be filtered for market hours)
     * @param {number} period - RSI period (default: 14)
     * @returns {Array} Array of RSI data points
     */
    static calculateRSI(data, period = 14) {
        if (!data || data.length <= period) {
            console.warn(`Not enough data points for ${period}-period RSI calculation (need > ${period}, have ${data?.length || 0})`);
            return [];
        }
        
        console.log(`Calculating ${period}-period RSI for ${data.length} data points`);
        
        const rsiData = [];
        const gains = [];
        const losses = [];
        
        // Calculate price changes
        for (let i = 1; i < data.length; i++) {
            const change = data[i].close - data[i-1].close;
            gains.push(change > 0 ? change : 0);
            losses.push(change < 0 ? Math.abs(change) : 0);
        }
        
        // Calculate first average gain and loss
        let avgGain = gains.slice(0, period).reduce((sum, gain) => sum + gain, 0) / period;
        let avgLoss = losses.slice(0, period).reduce((sum, loss) => sum + loss, 0) / period;
        
        // Calculate initial RSI
        let rs = avgGain / (avgLoss === 0 ? 0.001 : avgLoss); // Avoid division by zero
        let rsi = 100 - (100 / (1 + rs));
        
        rsiData.push({
            time: data[period].time,
            value: rsi
        });
        
        // Calculate subsequent RSI values using the smoothing method
        for (let i = period + 1; i < data.length; i++) {
            const currentGain = gains[i - 1];
            const currentLoss = losses[i - 1];
            
            // Update average gain and loss using smoothing formula
            avgGain = ((avgGain * (period - 1)) + currentGain) / period;
            avgLoss = ((avgLoss * (period - 1)) + currentLoss) / period;
            
            // Calculate RS and RSI
            rs = avgGain / (avgLoss === 0 ? 0.001 : avgLoss);
            rsi = 100 - (100 / (1 + rs));
            
            rsiData.push({
                time: data[i].time,
                value: rsi
            });
        }
        
        return rsiData;
    }
    
    /**
     * Calculate dynamic bar colors based on SMA crossovers and price action
     * @param {Array} data - Array of bar data points with OHLC values
     * @param {Array} sma50Data - Array of 50-period SMA data points
     * @param {Array} sma200Data - Array of 200-period SMA data points
     * @returns {Object} Object containing coloredData array and crossovers array
     */
    static calculateBarColors(data, sma50Data, sma200Data) {
        if (!data || data.length === 0 || !sma50Data || !sma200Data) {
            return {
                coloredData: [],
                crossovers: []
            };
        }
        
        console.log(`Calculating bar colors for ${data.length} data points`);
        
        const coloredData = [];
        const crossovers = []; // Track crossover events for markers
        let isBullish = null; // Track market state (null = uninitialized, true = bullish, false = bearish)
        
        // Color constants
        const GOLD_COLOR = '#FFD700';    // Gold for bullish bars above SMAs
        const RED_COLOR = '#8B0000';     // Maroon for bearish bars below SMAs  
        const GRAY_COLOR = '#808080';    // Gray for indecision/weak trends
        
        for (let i = 0; i < data.length; i++) {
            const currentTime = data[i].time;
            const currentBar = { ...data[i] };
            
            // Find corresponding SMA values for the current bar
            let sma50Value = null;
            let sma200Value = null;
            
            for (let j = 0; j < sma50Data.length; j++) {
                if (Math.abs(sma50Data[j].time - currentTime) < 1) {
                    sma50Value = sma50Data[j].value;
                    break;
                }
            }
            
            for (let j = 0; j < sma200Data.length; j++) {
                if (Math.abs(sma200Data[j].time - currentTime) < 1) {
                    sma200Value = sma200Data[j].value;
                    break;
                }
            }
            
            // Skip if we don't have SMA values
            if (sma50Value === null || sma200Value === null) {
                currentBar.color = GRAY_COLOR;
                coloredData.push(currentBar);
                continue;
            }
            
            // Detect crossovers (Golden Cross / Death Cross)
            if (i > 0) {
                // Get previous SMA values for crossover detection
                let prevSma50Value = null;
                let prevSma200Value = null;
                const prevTime = data[i-1].time;
                
                for (let j = 0; j < sma50Data.length; j++) {
                    if (Math.abs(sma50Data[j].time - prevTime) < 1) {
                        prevSma50Value = sma50Data[j].value;
                        break;
                    }
                }
                
                for (let j = 0; j < sma200Data.length; j++) {
                    if (Math.abs(sma200Data[j].time - prevTime) < 1) {
                        prevSma200Value = sma200Data[j].value;
                        break;
                    }
                }
                
                // Check for crossovers if we have previous values
                if (prevSma50Value !== null && prevSma200Value !== null) {
                    // Golden Cross: 50 SMA crosses above 200 SMA
                    if (prevSma50Value <= prevSma200Value && sma50Value > sma200Value) {
                        isBullish = true;
                        crossovers.push({
                            time: currentTime,
                            type: 'golden'
                        });
                        console.log(`Golden Cross detected at ${new Date(currentTime * 1000).toISOString()}`);
                    }
                    // Death Cross: 50 SMA crosses below 200 SMA
                    else if (prevSma50Value >= prevSma200Value && sma50Value < sma200Value) {
                        isBullish = false;
                        crossovers.push({
                            time: currentTime,
                            type: 'death'
                        });
                        console.log(`Death Cross detected at ${new Date(currentTime * 1000).toISOString()}`);
                    }
                }
            }
              // Assign color based on market state and price action
            // Following the exact logic provided:
            // 1. If bullish market (after golden cross):
            //    - Yellow/Gold if price is above both SMAs
            //    - Gray otherwise
            // 2. If bearish market (after death cross):
            //    - Red/Maroon if price is below both SMAs
            //    - Gray otherwise
            // 3. Default to standard coloring if market state not yet determined
            
            let barColor = GRAY_COLOR; // Default to gray
            
            if (isBullish === true) { // Explicitly true, market is in bullish state after golden cross
                if (currentBar.close > sma50Value && currentBar.close > sma200Value) {
                    barColor = GOLD_COLOR; // Bullish and price above both SMAs
                } else {
                    barColor = GRAY_COLOR; // Bullish but price not above both SMAs
                }
            } else if (isBullish === false) { // Explicitly false, market is in bearish state after death cross
                if (currentBar.close < sma50Value && currentBar.close < sma200Value) {
                    barColor = RED_COLOR; // Bearish and price below both SMAs
                } else {
                    barColor = GRAY_COLOR; // Bearish but price not below both SMAs
                }
            } else {
                // No market state determined yet (no crossovers detected)
                // Use standard green/red coloring based on candle direction
                barColor = currentBar.close >= currentBar.open ? '#00BB00' : '#FF6666';
            }
            
            currentBar.color = barColor;
            coloredData.push(currentBar);
        }
        
        console.log(`Bar coloring completed: ${coloredData.length} bars colored`);
        console.log(`Crossovers detected: ${crossovers.length} events`);
        return {
            coloredData: coloredData,
            crossovers: crossovers
        };
    }
}
