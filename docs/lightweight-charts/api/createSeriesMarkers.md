# API: Createseriesmarkers

*Source: docs\api\functions\createSeriesMarkers.html*

Version: 5.0

On this page

> **createSeriesMarkers** <`HorzScaleItem`>(`series`, `markers`?): [`ISeriesMarkersPluginApi`](../interfaces/ISeriesMarkersPluginApi.md)<`HorzScaleItem`>

A function to create a series markers primitive.

## Type parameters[​](createSeriesMarkers.html#type-parameters "Direct link to Type parameters")

• **HorzScaleItem**

## Parameters[​](createSeriesMarkers.html#parameters "Direct link to Parameters")

• **series** : [`ISeriesApi`](../interfaces/ISeriesApi.md)<keyof [`SeriesOptionsMap`](../interfaces/SeriesOptionsMap.md), `HorzScaleItem`, [`AreaData`](../interfaces/AreaData.md)<`HorzScaleItem`> | [`WhitespaceData`](../interfaces/WhitespaceData.md)<`HorzScaleItem`> | [`BarData`](../interfaces/BarData.md)<`HorzScaleItem`> | [`CandlestickData`](../interfaces/CandlestickData.md)<`HorzScaleItem`> | [`BaselineData`](../interfaces/BaselineData.md)<`HorzScaleItem`> | [`LineData`](../interfaces/LineData.md)<`HorzScaleItem`> | [`HistogramData`](../interfaces/HistogramData.md)<`HorzScaleItem`> | [`CustomData`](../interfaces/CustomData.md)<`HorzScaleItem`> | [`CustomSeriesWhitespaceData`](../interfaces/CustomSeriesWhitespaceData.md)<`HorzScaleItem`>, [`CustomSeriesOptions`](../type-aliases/CustomSeriesOptions.md) | [`AreaSeriesOptions`](../type-aliases/AreaSeriesOptions.md) | [`BarSeriesOptions`](../type-aliases/BarSeriesOptions.md) | [`CandlestickSeriesOptions`](../type-aliases/CandlestickSeriesOptions.md) | [`BaselineSeriesOptions`](../type-aliases/BaselineSeriesOptions.md) | [`LineSeriesOptions`](../type-aliases/LineSeriesOptions.md) | [`HistogramSeriesOptions`](../type-aliases/HistogramSeriesOptions.md), [`DeepPartial`](../type-aliases/DeepPartial.md) <[`AreaStyleOptions`](../interfaces/AreaStyleOptions.md) & [`SeriesOptionsCommon`](../interfaces/SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`BarStyleOptions`](../interfaces/BarStyleOptions.md) & [`SeriesOptionsCommon`](../interfaces/SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`CandlestickStyleOptions`](../interfaces/CandlestickStyleOptions.md) & [`SeriesOptionsCommon`](../interfaces/SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`BaselineStyleOptions`](../interfaces/BaselineStyleOptions.md) & [`SeriesOptionsCommon`](../interfaces/SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`LineStyleOptions`](../interfaces/LineStyleOptions.md) & [`SeriesOptionsCommon`](../interfaces/SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`HistogramStyleOptions`](../interfaces/HistogramStyleOptions.md) & [`SeriesOptionsCommon`](../interfaces/SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`CustomStyleOptions`](../interfaces/CustomStyleOptions.md) & [`SeriesOptionsCommon`](../interfaces/SeriesOptionsCommon.md)>>

The series to which the primitive will be attached.

• **markers?** : [`SeriesMarker`](../type-aliases/SeriesMarker.md)<`HorzScaleItem`>[]

An array of markers to be displayed on the series.

## Returns[​](createSeriesMarkers.html#returns "Direct link to Returns")

[`ISeriesMarkersPluginApi`](../interfaces/ISeriesMarkersPluginApi.md)<`HorzScaleItem`>

## Example[​](createSeriesMarkers.html#example "Direct link to Example")
    
    
    import { createSeriesMarkers } from 'lightweight-charts';  
      
        const seriesMarkers = createSeriesMarkers(  
            series,  
            [  
                {  
                    color: 'green',  
                    position: 'inBar',  
                    shape: 'arrowDown',  
                    time: 1556880900,  
                },  
            ]  
        );  
     // and then you can modify the markers  
     // set it to empty array to remove all markers  
     seriesMarkers.setMarkers([]);  
      
     // `seriesMarkers.markers()` returns current markers  
    
