// Unified utility exports - Re-exporting from modular files
// This file maintains backwards compatibility with existing code

import { DataUtils } from './utils/dataUtils.js';
import { IndicatorUtils } from './utils/indicatorUtils.js';
import { TimeUtils } from './utils/timeUtils.js';
import { MarkerUtils } from './utils/markerUtils.js';

// Create a unified DataUtils class that combines all the utilities
// for backward compatibility
export { DataUtils, IndicatorUtils, TimeUtils, MarkerUtils };

// Also export a combined Utils object that includes all functions
export const Utils = {
    // Data Utils
    parseCSV: DataUtils.parseCSV,
    filterMarketHours: DataUtils.filterMarketHours,
    transformPolygonData: DataUtils.transformPolygonData,
    
    // Indicator Utils
    calculateSMA: IndicatorUtils.calculateSMA,
    calculateEMA: IndicatorUtils.calculateEMA,
    calculateMACDComplete: IndicatorUtils.calculateMACDComplete,
    calculateMACDHistogram: IndicatorUtils.calculateMACDHistogram,
    calculateRSI: IndicatorUtils.calculateRSI,
    calculateBarColors: IndicatorUtils.calculateBarColors,
    
    // Time Utils
    isDaylightSavingTime: TimeUtils.isDaylightSavingTime,
    formatTimestamp: TimeUtils.formatTimestamp,
    getMarketSessions: TimeUtils.getMarketSessions,
    
    // Marker Utils
    calculateMACDCrossovers: MarkerUtils.calculateMACDCrossovers,
    createMACDCrossoverMarkers: MarkerUtils.createMACDCrossoverMarkers,
    createCrossoverMarkers: MarkerUtils.createCrossoverMarkers,
    calculateVolumeProfile: MarkerUtils.calculateVolumeProfile
};
