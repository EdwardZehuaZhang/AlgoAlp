# API: Createupdownmarkers

*Source: docs\api\functions\createUpDownMarkers.html*

Version: 5.0

On this page

> **createUpDownMarkers** <`T`>(`series`, `options`?): [`ISeriesUpDownMarkerPluginApi`](../interfaces/ISeriesUpDownMarkerPluginApi.md)<`T`>

Creates and attaches the Series Up Down Markers Plugin.

## Type parameters[​](createUpDownMarkers.html#type-parameters "Direct link to Type parameters")

• **T**

## Parameters[​](createUpDownMarkers.html#parameters "Direct link to Parameters")

• **series** : [`ISeriesApi`](../interfaces/ISeriesApi.md)<keyof [`SeriesOptionsMap`](../interfaces/SeriesOptionsMap.md), `T`, [`AreaData`](../interfaces/AreaData.md)<`T`> | [`WhitespaceData`](../interfaces/WhitespaceData.md)<`T`> | [`BarData`](../interfaces/BarData.md)<`T`> | [`CandlestickData`](../interfaces/CandlestickData.md)<`T`> | [`BaselineData`](../interfaces/BaselineData.md)<`T`> | [`LineData`](../interfaces/LineData.md)<`T`> | [`HistogramData`](../interfaces/HistogramData.md)<`T`> | [`CustomData`](../interfaces/CustomData.md)<`T`> | [`CustomSeriesWhitespaceData`](../interfaces/CustomSeriesWhitespaceData.md)<`T`>, [`CustomSeriesOptions`](../type-aliases/CustomSeriesOptions.md) | [`AreaSeriesOptions`](../type-aliases/AreaSeriesOptions.md) | [`BarSeriesOptions`](../type-aliases/BarSeriesOptions.md) | [`CandlestickSeriesOptions`](../type-aliases/CandlestickSeriesOptions.md) | [`BaselineSeriesOptions`](../type-aliases/BaselineSeriesOptions.md) | [`LineSeriesOptions`](../type-aliases/LineSeriesOptions.md) | [`HistogramSeriesOptions`](../type-aliases/HistogramSeriesOptions.md), [`DeepPartial`](../type-aliases/DeepPartial.md) <[`AreaStyleOptions`](../interfaces/AreaStyleOptions.md) & [`SeriesOptionsCommon`](../interfaces/SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`BarStyleOptions`](../interfaces/BarStyleOptions.md) & [`SeriesOptionsCommon`](../interfaces/SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`CandlestickStyleOptions`](../interfaces/CandlestickStyleOptions.md) & [`SeriesOptionsCommon`](../interfaces/SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`BaselineStyleOptions`](../interfaces/BaselineStyleOptions.md) & [`SeriesOptionsCommon`](../interfaces/SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`LineStyleOptions`](../interfaces/LineStyleOptions.md) & [`SeriesOptionsCommon`](../interfaces/SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`HistogramStyleOptions`](../interfaces/HistogramStyleOptions.md) & [`SeriesOptionsCommon`](../interfaces/SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`CustomStyleOptions`](../interfaces/CustomStyleOptions.md) & [`SeriesOptionsCommon`](../interfaces/SeriesOptionsCommon.md)>>

Series to which attach the Up Down Markers Plugin

• **options?** : `Partial` <[`UpDownMarkersPluginOptions`](../interfaces/UpDownMarkersPluginOptions.md)>

options for the Up Down Markers Plugin

## Returns[​](createUpDownMarkers.html#returns "Direct link to Returns")

[`ISeriesUpDownMarkerPluginApi`](../interfaces/ISeriesUpDownMarkerPluginApi.md)<`T`>

Api for Series Up Down Marker Plugin. [ISeriesUpDownMarkerPluginApi](../interfaces/ISeriesUpDownMarkerPluginApi.md)

## Example[​](createUpDownMarkers.html#example "Direct link to Example")
    
    
    import { createUpDownMarkers, createChart, LineSeries } from 'lightweight-charts';  
      
    const chart = createChart('container');  
    const lineSeries = chart.addSeries(LineSeries);  
    const upDownMarkers = createUpDownMarkers(lineSeries, {  
        positiveColor: '#22AB94',  
        negativeColor: '#F7525F',  
        updateVisibilityDuration: 5000,  
    });  
    // to add some data  
    upDownMarkers.setData(  
        [  
            { time: '2020-02-02', value: 12.34 },  
            //... more line series data  
        ]  
    );  
    // ... Update some values  
    upDownMarkers.update({ time: '2020-02-02', value: 13.54 }, true);  
    // to remove plugin from the series  
    upDownMarkers.detach();  
    
