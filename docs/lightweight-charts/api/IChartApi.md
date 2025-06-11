# API: Ichartapi

*Source: docs\api\interfaces\IChartApi.html*

Version: 5.0

On this page

The main interface of a single chart using time for horizontal scale.

## Extends[​](IChartApi.html#extends "Direct link to Extends")

  * [`IChartApiBase`](IChartApiBase.md) <[`Time`](../type-aliases/Time.md)>

## Methods[​](IChartApi.html#methods "Direct link to Methods")

### applyOptions()[​](IChartApi.html#applyoptions "Direct link to applyOptions\(\)")

> **applyOptions**(`options`): `void`

Applies new options to the chart

#### Parameters[​](IChartApi.html#parameters "Direct link to Parameters")

• **options** : [`DeepPartial`](../type-aliases/DeepPartial.md) <[`TimeChartOptions`](TimeChartOptions.md)>

Any subset of options.

#### Returns[​](IChartApi.html#returns "Direct link to Returns")

`void`

#### Overrides[​](IChartApi.html#overrides "Direct link to Overrides")

[`IChartApiBase`](IChartApiBase.md) . [`applyOptions`](IChartApiBase.html#applyoptions)

* * *

### remove()[​](IChartApi.html#remove "Direct link to remove\(\)")

> **remove**(): `void`

Removes the chart object including all DOM elements. This is an irreversible operation, you cannot do anything with the chart after removing it.

#### Returns[​](IChartApi.html#returns-1 "Direct link to Returns")

`void`

#### Inherited from[​](IChartApi.html#inherited-from "Direct link to Inherited from")

[`IChartApiBase`](IChartApiBase.md) . [`remove`](IChartApiBase.html#remove)

* * *

### resize()[​](IChartApi.html#resize "Direct link to resize\(\)")

> **resize**(`width`, `height`, `forceRepaint`?): `void`

Sets fixed size of the chart. By default chart takes up 100% of its container.

If chart has the `autoSize` option enabled, and the ResizeObserver is available then the width and height values will be ignored.

#### Parameters[​](IChartApi.html#parameters-1 "Direct link to Parameters")

• **width** : `number`

Target width of the chart.

• **height** : `number`

Target height of the chart.

• **forceRepaint?** : `boolean`

True to initiate resize immediately. One could need this to get screenshot immediately after resize.

#### Returns[​](IChartApi.html#returns-2 "Direct link to Returns")

`void`

#### Inherited from[​](IChartApi.html#inherited-from-1 "Direct link to Inherited from")

[`IChartApiBase`](IChartApiBase.md) . [`resize`](IChartApiBase.html#resize)

* * *

### addCustomSeries()[​](IChartApi.html#addcustomseries "Direct link to addCustomSeries\(\)")

> **addCustomSeries** <`TData`, `TOptions`, `TPartialOptions`>(`customPaneView`, `customOptions`?, `paneIndex`?): [`ISeriesApi`](ISeriesApi.md)<`"Custom"`, [`Time`](../type-aliases/Time.md), `TData` | [`WhitespaceData`](WhitespaceData.md) <[`Time`](../type-aliases/Time.md)>, `TOptions`, `TPartialOptions`>

Creates a custom series with specified parameters.

A custom series is a generic series which can be extended with a custom renderer to implement chart types which the library doesn't support by default.

#### Type parameters[​](IChartApi.html#type-parameters "Direct link to Type parameters")

• **TData** _extends_ [`CustomData`](CustomData.md) <[`Time`](../type-aliases/Time.md)>

• **TOptions** _extends_ [`CustomSeriesOptions`](../type-aliases/CustomSeriesOptions.md)

• **TPartialOptions** _extends_ [`DeepPartial`](../type-aliases/DeepPartial.md)<`TOptions` & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> = [`DeepPartial`](../type-aliases/DeepPartial.md)<`TOptions` & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)>

#### Parameters[​](IChartApi.html#parameters-2 "Direct link to Parameters")

• **customPaneView** : [`ICustomSeriesPaneView`](ICustomSeriesPaneView.md) <[`Time`](../type-aliases/Time.md), `TData`, `TOptions`>

A custom series pane view which implements the custom renderer.

• **customOptions?** : [`DeepPartial`](../type-aliases/DeepPartial.md)<`TOptions` & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)>

Customization parameters of the series being created.
    
    
    const series = chart.addCustomSeries(myCustomPaneView);  
    

• **paneIndex?** : `number`

#### Returns[​](IChartApi.html#returns-3 "Direct link to Returns")

[`ISeriesApi`](ISeriesApi.md)<`"Custom"`, [`Time`](../type-aliases/Time.md), `TData` | [`WhitespaceData`](WhitespaceData.md) <[`Time`](../type-aliases/Time.md)>, `TOptions`, `TPartialOptions`>

#### Inherited from[​](IChartApi.html#inherited-from-2 "Direct link to Inherited from")

[`IChartApiBase`](IChartApiBase.md) . [`addCustomSeries`](IChartApiBase.html#addcustomseries)

* * *

### addSeries()[​](IChartApi.html#addseries "Direct link to addSeries\(\)")

> **addSeries** <`T`>(`definition`, `options`?, `paneIndex`?): [`ISeriesApi`](ISeriesApi.md)<`T`, [`Time`](../type-aliases/Time.md), [`SeriesDataItemTypeMap`](SeriesDataItemTypeMap.md) <[`Time`](../type-aliases/Time.md)>[`T`], [`SeriesOptionsMap`](SeriesOptionsMap.md)[`T`], [`SeriesPartialOptionsMap`](SeriesPartialOptionsMap.md)[`T`]>

Creates a series with specified parameters.

#### Type parameters[​](IChartApi.html#type-parameters-1 "Direct link to Type parameters")

• **T** _extends_ keyof [`SeriesOptionsMap`](SeriesOptionsMap.md)

#### Parameters[​](IChartApi.html#parameters-3 "Direct link to Parameters")

• **definition** : [`SeriesDefinition`](SeriesDefinition.md)<`T`>

A series definition.

• **options?** : [`SeriesPartialOptionsMap`](SeriesPartialOptionsMap.md)[`T`]

Customization parameters of the series being created.

• **paneIndex?** : `number`

An index of the pane where the series should be created.
    
    
    const series = chart.addSeries(LineSeries, { lineWidth: 2 });  
    

#### Returns[​](IChartApi.html#returns-4 "Direct link to Returns")

[`ISeriesApi`](ISeriesApi.md)<`T`, [`Time`](../type-aliases/Time.md), [`SeriesDataItemTypeMap`](SeriesDataItemTypeMap.md) <[`Time`](../type-aliases/Time.md)>[`T`], [`SeriesOptionsMap`](SeriesOptionsMap.md)[`T`], [`SeriesPartialOptionsMap`](SeriesPartialOptionsMap.md)[`T`]>

#### Inherited from[​](IChartApi.html#inherited-from-3 "Direct link to Inherited from")

[`IChartApiBase`](IChartApiBase.md) . [`addSeries`](IChartApiBase.html#addseries)

* * *

### removeSeries()[​](IChartApi.html#removeseries "Direct link to removeSeries\(\)")

> **removeSeries**(`seriesApi`): `void`

Removes a series of any type. This is an irreversible operation, you cannot do anything with the series after removing it.

#### Parameters[​](IChartApi.html#parameters-4 "Direct link to Parameters")

• **seriesApi** : [`ISeriesApi`](ISeriesApi.md)<keyof [`SeriesOptionsMap`](SeriesOptionsMap.md), [`Time`](../type-aliases/Time.md), [`CustomData`](CustomData.md) <[`Time`](../type-aliases/Time.md)> | [`WhitespaceData`](WhitespaceData.md) <[`Time`](../type-aliases/Time.md)> | [`AreaData`](AreaData.md) <[`Time`](../type-aliases/Time.md)> | [`BarData`](BarData.md) <[`Time`](../type-aliases/Time.md)> | [`CandlestickData`](CandlestickData.md) <[`Time`](../type-aliases/Time.md)> | [`BaselineData`](BaselineData.md) <[`Time`](../type-aliases/Time.md)> | [`LineData`](LineData.md) <[`Time`](../type-aliases/Time.md)> | [`HistogramData`](HistogramData.md) <[`Time`](../type-aliases/Time.md)> | [`CustomSeriesWhitespaceData`](CustomSeriesWhitespaceData.md) <[`Time`](../type-aliases/Time.md)>, [`CustomSeriesOptions`](../type-aliases/CustomSeriesOptions.md) | [`AreaSeriesOptions`](../type-aliases/AreaSeriesOptions.md) | [`BarSeriesOptions`](../type-aliases/BarSeriesOptions.md) | [`CandlestickSeriesOptions`](../type-aliases/CandlestickSeriesOptions.md) | [`BaselineSeriesOptions`](../type-aliases/BaselineSeriesOptions.md) | [`LineSeriesOptions`](../type-aliases/LineSeriesOptions.md) | [`HistogramSeriesOptions`](../type-aliases/HistogramSeriesOptions.md), [`DeepPartial`](../type-aliases/DeepPartial.md) <[`AreaStyleOptions`](AreaStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`BarStyleOptions`](BarStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`CandlestickStyleOptions`](CandlestickStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`BaselineStyleOptions`](BaselineStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`LineStyleOptions`](LineStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`HistogramStyleOptions`](HistogramStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`CustomStyleOptions`](CustomStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)>>

#### Returns[​](IChartApi.html#returns-5 "Direct link to Returns")

`void`

#### Inherited from[​](IChartApi.html#inherited-from-4 "Direct link to Inherited from")

[`IChartApiBase`](IChartApiBase.md) . [`removeSeries`](IChartApiBase.html#removeseries)

#### Example[​](IChartApi.html#example "Direct link to Example")
    
    
    chart.removeSeries(series);  
    

* * *

### subscribeClick()[​](IChartApi.html#subscribeclick "Direct link to subscribeClick\(\)")

> **subscribeClick**(`handler`): `void`

Subscribe to the chart click event.

#### Parameters[​](IChartApi.html#parameters-5 "Direct link to Parameters")

• **handler** : [`MouseEventHandler`](../type-aliases/MouseEventHandler.md) <[`Time`](../type-aliases/Time.md)>

Handler to be called on mouse click.

#### Returns[​](IChartApi.html#returns-6 "Direct link to Returns")

`void`

#### Inherited from[​](IChartApi.html#inherited-from-5 "Direct link to Inherited from")

[`IChartApiBase`](IChartApiBase.md) . [`subscribeClick`](IChartApiBase.html#subscribeclick)

#### Example[​](IChartApi.html#example-1 "Direct link to Example")
    
    
    function myClickHandler(param) {  
        if (!param.point) {  
            return;  
        }  
      
        console.log(`Click at ${param.point.x}, ${param.point.y}. The time is ${param.time}.`);  
    }  
      
    chart.subscribeClick(myClickHandler);  
    

* * *

### unsubscribeClick()[​](IChartApi.html#unsubscribeclick "Direct link to unsubscribeClick\(\)")

> **unsubscribeClick**(`handler`): `void`

Unsubscribe a handler that was previously subscribed using [subscribeClick](IChartApiBase.html#subscribeclick).

#### Parameters[​](IChartApi.html#parameters-6 "Direct link to Parameters")

• **handler** : [`MouseEventHandler`](../type-aliases/MouseEventHandler.md) <[`Time`](../type-aliases/Time.md)>

Previously subscribed handler

#### Returns[​](IChartApi.html#returns-7 "Direct link to Returns")

`void`

#### Inherited from[​](IChartApi.html#inherited-from-6 "Direct link to Inherited from")

[`IChartApiBase`](IChartApiBase.md) . [`unsubscribeClick`](IChartApiBase.html#unsubscribeclick)

#### Example[​](IChartApi.html#example-2 "Direct link to Example")
    
    
    chart.unsubscribeClick(myClickHandler);  
    

* * *

### subscribeDblClick()[​](IChartApi.html#subscribedblclick "Direct link to subscribeDblClick\(\)")

> **subscribeDblClick**(`handler`): `void`

Subscribe to the chart double-click event.

#### Parameters[​](IChartApi.html#parameters-7 "Direct link to Parameters")

• **handler** : [`MouseEventHandler`](../type-aliases/MouseEventHandler.md) <[`Time`](../type-aliases/Time.md)>

Handler to be called on mouse double-click.

#### Returns[​](IChartApi.html#returns-8 "Direct link to Returns")

`void`

#### Inherited from[​](IChartApi.html#inherited-from-7 "Direct link to Inherited from")

[`IChartApiBase`](IChartApiBase.md) . [`subscribeDblClick`](IChartApiBase.html#subscribedblclick)

#### Example[​](IChartApi.html#example-3 "Direct link to Example")
    
    
    function myDblClickHandler(param) {  
        if (!param.point) {  
            return;  
        }  
      
        console.log(`Double Click at ${param.point.x}, ${param.point.y}. The time is ${param.time}.`);  
    }  
      
    chart.subscribeDblClick(myDblClickHandler);  
    

* * *

### unsubscribeDblClick()[​](IChartApi.html#unsubscribedblclick "Direct link to unsubscribeDblClick\(\)")

> **unsubscribeDblClick**(`handler`): `void`

Unsubscribe a handler that was previously subscribed using [subscribeDblClick](IChartApiBase.html#subscribedblclick).

#### Parameters[​](IChartApi.html#parameters-8 "Direct link to Parameters")

• **handler** : [`MouseEventHandler`](../type-aliases/MouseEventHandler.md) <[`Time`](../type-aliases/Time.md)>

Previously subscribed handler

#### Returns[​](IChartApi.html#returns-9 "Direct link to Returns")

`void`

#### Inherited from[​](IChartApi.html#inherited-from-8 "Direct link to Inherited from")

[`IChartApiBase`](IChartApiBase.md) . [`unsubscribeDblClick`](IChartApiBase.html#unsubscribedblclick)

#### Example[​](IChartApi.html#example-4 "Direct link to Example")
    
    
    chart.unsubscribeDblClick(myDblClickHandler);  
    

* * *

### subscribeCrosshairMove()[​](IChartApi.html#subscribecrosshairmove "Direct link to subscribeCrosshairMove\(\)")

> **subscribeCrosshairMove**(`handler`): `void`

Subscribe to the crosshair move event.

#### Parameters[​](IChartApi.html#parameters-9 "Direct link to Parameters")

• **handler** : [`MouseEventHandler`](../type-aliases/MouseEventHandler.md) <[`Time`](../type-aliases/Time.md)>

Handler to be called on crosshair move.

#### Returns[​](IChartApi.html#returns-10 "Direct link to Returns")

`void`

#### Inherited from[​](IChartApi.html#inherited-from-9 "Direct link to Inherited from")

[`IChartApiBase`](IChartApiBase.md) . [`subscribeCrosshairMove`](IChartApiBase.html#subscribecrosshairmove)

#### Example[​](IChartApi.html#example-5 "Direct link to Example")
    
    
    function myCrosshairMoveHandler(param) {  
        if (!param.point) {  
            return;  
        }  
      
        console.log(`Crosshair moved to ${param.point.x}, ${param.point.y}. The time is ${param.time}.`);  
    }  
      
    chart.subscribeCrosshairMove(myCrosshairMoveHandler);  
    

* * *

### unsubscribeCrosshairMove()[​](IChartApi.html#unsubscribecrosshairmove "Direct link to unsubscribeCrosshairMove\(\)")

> **unsubscribeCrosshairMove**(`handler`): `void`

Unsubscribe a handler that was previously subscribed using [subscribeCrosshairMove](IChartApiBase.html#subscribecrosshairmove).

#### Parameters[​](IChartApi.html#parameters-10 "Direct link to Parameters")

• **handler** : [`MouseEventHandler`](../type-aliases/MouseEventHandler.md) <[`Time`](../type-aliases/Time.md)>

Previously subscribed handler

#### Returns[​](IChartApi.html#returns-11 "Direct link to Returns")

`void`

#### Inherited from[​](IChartApi.html#inherited-from-10 "Direct link to Inherited from")

[`IChartApiBase`](IChartApiBase.md) . [`unsubscribeCrosshairMove`](IChartApiBase.html#unsubscribecrosshairmove)

#### Example[​](IChartApi.html#example-6 "Direct link to Example")
    
    
    chart.unsubscribeCrosshairMove(myCrosshairMoveHandler);  
    

* * *

### priceScale()[​](IChartApi.html#pricescale "Direct link to priceScale\(\)")

> **priceScale**(`priceScaleId`, `paneIndex`?): [`IPriceScaleApi`](IPriceScaleApi.md)

Returns API to manipulate a price scale.

#### Parameters[​](IChartApi.html#parameters-11 "Direct link to Parameters")

• **priceScaleId** : `string`

ID of the price scale.

• **paneIndex?** : `number`

Index of the pane (default: 0)

#### Returns[​](IChartApi.html#returns-12 "Direct link to Returns")

[`IPriceScaleApi`](IPriceScaleApi.md)

Price scale API.

#### Inherited from[​](IChartApi.html#inherited-from-11 "Direct link to Inherited from")

[`IChartApiBase`](IChartApiBase.md) . [`priceScale`](IChartApiBase.html#pricescale)

* * *

### timeScale()[​](IChartApi.html#timescale "Direct link to timeScale\(\)")

> **timeScale**(): [`ITimeScaleApi`](ITimeScaleApi.md) <[`Time`](../type-aliases/Time.md)>

Returns API to manipulate the time scale

#### Returns[​](IChartApi.html#returns-13 "Direct link to Returns")

[`ITimeScaleApi`](ITimeScaleApi.md) <[`Time`](../type-aliases/Time.md)>

Target API

#### Inherited from[​](IChartApi.html#inherited-from-12 "Direct link to Inherited from")

[`IChartApiBase`](IChartApiBase.md) . [`timeScale`](IChartApiBase.html#timescale)

* * *

### options()[​](IChartApi.html#options "Direct link to options\(\)")

> **options**(): `Readonly` <[`ChartOptionsImpl`](ChartOptionsImpl.md) <[`Time`](../type-aliases/Time.md)>>

Returns currently applied options

#### Returns[​](IChartApi.html#returns-14 "Direct link to Returns")

`Readonly` <[`ChartOptionsImpl`](ChartOptionsImpl.md) <[`Time`](../type-aliases/Time.md)>>

Full set of currently applied options, including defaults

#### Inherited from[​](IChartApi.html#inherited-from-13 "Direct link to Inherited from")

[`IChartApiBase`](IChartApiBase.md) . [`options`](IChartApiBase.html#options)

* * *

### takeScreenshot()[​](IChartApi.html#takescreenshot "Direct link to takeScreenshot\(\)")

> **takeScreenshot**(): `HTMLCanvasElement`

Make a screenshot of the chart with all the elements excluding crosshair.

#### Returns[​](IChartApi.html#returns-15 "Direct link to Returns")

`HTMLCanvasElement`

A canvas with the chart drawn on. Any `Canvas` methods like `toDataURL()` or `toBlob()` can be used to serialize the result.

#### Inherited from[​](IChartApi.html#inherited-from-14 "Direct link to Inherited from")

[`IChartApiBase`](IChartApiBase.md) . [`takeScreenshot`](IChartApiBase.html#takescreenshot)

* * *

### panes()[​](IChartApi.html#panes "Direct link to panes\(\)")

> **panes**(): [`IPaneApi`](IPaneApi.md) <[`Time`](../type-aliases/Time.md)>[]

Returns array of panes' API

#### Returns[​](IChartApi.html#returns-16 "Direct link to Returns")

[`IPaneApi`](IPaneApi.md) <[`Time`](../type-aliases/Time.md)>[]

array of pane's Api

#### Inherited from[​](IChartApi.html#inherited-from-15 "Direct link to Inherited from")

[`IChartApiBase`](IChartApiBase.md) . [`panes`](IChartApiBase.html#panes)

* * *

### removePane()[​](IChartApi.html#removepane "Direct link to removePane\(\)")

> **removePane**(`index`): `void`

Removes a pane with index

#### Parameters[​](IChartApi.html#parameters-12 "Direct link to Parameters")

• **index** : `number`

the pane to be removed

#### Returns[​](IChartApi.html#returns-17 "Direct link to Returns")

`void`

#### Inherited from[​](IChartApi.html#inherited-from-16 "Direct link to Inherited from")

[`IChartApiBase`](IChartApiBase.md) . [`removePane`](IChartApiBase.html#removepane)

* * *

### swapPanes()[​](IChartApi.html#swappanes "Direct link to swapPanes\(\)")

> **swapPanes**(`first`, `second`): `void`

swap the position of two panes.

#### Parameters[​](IChartApi.html#parameters-13 "Direct link to Parameters")

• **first** : `number`

the first index

• **second** : `number`

the second index

#### Returns[​](IChartApi.html#returns-18 "Direct link to Returns")

`void`

#### Inherited from[​](IChartApi.html#inherited-from-17 "Direct link to Inherited from")

[`IChartApiBase`](IChartApiBase.md) . [`swapPanes`](IChartApiBase.html#swappanes)

* * *

### autoSizeActive()[​](IChartApi.html#autosizeactive "Direct link to autoSizeActive\(\)")

> **autoSizeActive**(): `boolean`

Returns the active state of the `autoSize` option. This can be used to check whether the chart is handling resizing automatically with a `ResizeObserver`.

#### Returns[​](IChartApi.html#returns-19 "Direct link to Returns")

`boolean`

Whether the `autoSize` option is enabled and the active.

#### Inherited from[​](IChartApi.html#inherited-from-18 "Direct link to Inherited from")

[`IChartApiBase`](IChartApiBase.md) . [`autoSizeActive`](IChartApiBase.html#autosizeactive)

* * *

### chartElement()[​](IChartApi.html#chartelement "Direct link to chartElement\(\)")

> **chartElement**(): `HTMLDivElement`

Returns the generated div element containing the chart. This can be used for adding your own additional event listeners, or for measuring the elements dimensions and position within the document.

#### Returns[​](IChartApi.html#returns-20 "Direct link to Returns")

`HTMLDivElement`

generated div element containing the chart.

#### Inherited from[​](IChartApi.html#inherited-from-19 "Direct link to Inherited from")

[`IChartApiBase`](IChartApiBase.md) . [`chartElement`](IChartApiBase.html#chartelement)

* * *

### setCrosshairPosition()[​](IChartApi.html#setcrosshairposition "Direct link to setCrosshairPosition\(\)")

> **setCrosshairPosition**(`price`, `horizontalPosition`, `seriesApi`): `void`

Set the crosshair position within the chart.

Usually the crosshair position is set automatically by the user's actions. However in some cases you may want to set it explicitly.

For example if you want to synchronise the crosshairs of two separate charts.

#### Parameters[​](IChartApi.html#parameters-14 "Direct link to Parameters")

• **price** : `number`

The price (vertical coordinate) of the new crosshair position.

• **horizontalPosition** : [`Time`](../type-aliases/Time.md)

The horizontal coordinate (time by default) of the new crosshair position.

• **seriesApi** : [`ISeriesApi`](ISeriesApi.md)<keyof [`SeriesOptionsMap`](SeriesOptionsMap.md), [`Time`](../type-aliases/Time.md), [`CustomData`](CustomData.md) <[`Time`](../type-aliases/Time.md)> | [`WhitespaceData`](WhitespaceData.md) <[`Time`](../type-aliases/Time.md)> | [`AreaData`](AreaData.md) <[`Time`](../type-aliases/Time.md)> | [`BarData`](BarData.md) <[`Time`](../type-aliases/Time.md)> | [`CandlestickData`](CandlestickData.md) <[`Time`](../type-aliases/Time.md)> | [`BaselineData`](BaselineData.md) <[`Time`](../type-aliases/Time.md)> | [`LineData`](LineData.md) <[`Time`](../type-aliases/Time.md)> | [`HistogramData`](HistogramData.md) <[`Time`](../type-aliases/Time.md)> | [`CustomSeriesWhitespaceData`](CustomSeriesWhitespaceData.md) <[`Time`](../type-aliases/Time.md)>, [`CustomSeriesOptions`](../type-aliases/CustomSeriesOptions.md) | [`AreaSeriesOptions`](../type-aliases/AreaSeriesOptions.md) | [`BarSeriesOptions`](../type-aliases/BarSeriesOptions.md) | [`CandlestickSeriesOptions`](../type-aliases/CandlestickSeriesOptions.md) | [`BaselineSeriesOptions`](../type-aliases/BaselineSeriesOptions.md) | [`LineSeriesOptions`](../type-aliases/LineSeriesOptions.md) | [`HistogramSeriesOptions`](../type-aliases/HistogramSeriesOptions.md), [`DeepPartial`](../type-aliases/DeepPartial.md) <[`AreaStyleOptions`](AreaStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`BarStyleOptions`](BarStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`CandlestickStyleOptions`](CandlestickStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`BaselineStyleOptions`](BaselineStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`LineStyleOptions`](LineStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`HistogramStyleOptions`](HistogramStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`CustomStyleOptions`](CustomStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)>>

#### Returns[​](IChartApi.html#returns-21 "Direct link to Returns")

`void`

#### Inherited from[​](IChartApi.html#inherited-from-20 "Direct link to Inherited from")

[`IChartApiBase`](IChartApiBase.md) . [`setCrosshairPosition`](IChartApiBase.html#setcrosshairposition)

* * *

### clearCrosshairPosition()[​](IChartApi.html#clearcrosshairposition "Direct link to clearCrosshairPosition\(\)")

> **clearCrosshairPosition**(): `void`

Clear the crosshair position within the chart.

#### Returns[​](IChartApi.html#returns-22 "Direct link to Returns")

`void`

#### Inherited from[​](IChartApi.html#inherited-from-21 "Direct link to Inherited from")

[`IChartApiBase`](IChartApiBase.md) . [`clearCrosshairPosition`](IChartApiBase.html#clearcrosshairposition)

* * *

### paneSize()[​](IChartApi.html#panesize "Direct link to paneSize\(\)")

> **paneSize**(`paneIndex`?): [`PaneSize`](PaneSize.md)

Returns the dimensions of the chart pane (the plot surface which excludes time and price scales). This would typically only be useful for plugin development.

#### Parameters[​](IChartApi.html#parameters-15 "Direct link to Parameters")

• **paneIndex?** : `number`

The index of the pane

#### Returns[​](IChartApi.html#returns-23 "Direct link to Returns")

[`PaneSize`](PaneSize.md)

Dimensions of the chart pane

#### Inherited from[​](IChartApi.html#inherited-from-22 "Direct link to Inherited from")

[`IChartApiBase`](IChartApiBase.md) . [`paneSize`](IChartApiBase.html#panesize)

#### Default Value[​](IChartApi.html#default-value "Direct link to Default Value")

`0`

* * *

### horzBehaviour()[​](IChartApi.html#horzbehaviour "Direct link to horzBehaviour\(\)")

> **horzBehaviour**(): [`IHorzScaleBehavior`](IHorzScaleBehavior.md) <[`Time`](../type-aliases/Time.md)>

Returns the horizontal scale behaviour.

#### Returns[​](IChartApi.html#returns-24 "Direct link to Returns")

[`IHorzScaleBehavior`](IHorzScaleBehavior.md) <[`Time`](../type-aliases/Time.md)>

#### Inherited from[​](IChartApi.html#inherited-from-23 "Direct link to Inherited from")

[`IChartApiBase`](IChartApiBase.md) . [`horzBehaviour`](IChartApiBase.html#horzbehaviour)
