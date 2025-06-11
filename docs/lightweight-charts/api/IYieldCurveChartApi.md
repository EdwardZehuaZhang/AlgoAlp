# API: Iyieldcurvechartapi

*Source: docs\api\interfaces\IYieldCurveChartApi.html*

Version: 5.0

On this page

The main interface of a single yield curve chart.

## Extends[​](IYieldCurveChartApi.html#extends "Direct link to Extends")

  * `Omit` <[`IChartApiBase`](IChartApiBase.md)<`number`>, `"addSeries"`>

## Methods[​](IYieldCurveChartApi.html#methods "Direct link to Methods")

### remove()[​](IYieldCurveChartApi.html#remove "Direct link to remove\(\)")

> **remove**(): `void`

Removes the chart object including all DOM elements. This is an irreversible operation, you cannot do anything with the chart after removing it.

#### Returns[​](IYieldCurveChartApi.html#returns "Direct link to Returns")

`void`

#### Inherited from[​](IYieldCurveChartApi.html#inherited-from "Direct link to Inherited from")

`Omit.remove`

* * *

### resize()[​](IYieldCurveChartApi.html#resize "Direct link to resize\(\)")

> **resize**(`width`, `height`, `forceRepaint`?): `void`

Sets fixed size of the chart. By default chart takes up 100% of its container.

If chart has the `autoSize` option enabled, and the ResizeObserver is available then the width and height values will be ignored.

#### Parameters[​](IYieldCurveChartApi.html#parameters "Direct link to Parameters")

• **width** : `number`

Target width of the chart.

• **height** : `number`

Target height of the chart.

• **forceRepaint?** : `boolean`

True to initiate resize immediately. One could need this to get screenshot immediately after resize.

#### Returns[​](IYieldCurveChartApi.html#returns-1 "Direct link to Returns")

`void`

#### Inherited from[​](IYieldCurveChartApi.html#inherited-from-1 "Direct link to Inherited from")

`Omit.resize`

* * *

### addCustomSeries()[​](IYieldCurveChartApi.html#addcustomseries "Direct link to addCustomSeries\(\)")

> **addCustomSeries** <`TData`, `TOptions`, `TPartialOptions`>(`customPaneView`, `customOptions`?, `paneIndex`?): [`ISeriesApi`](ISeriesApi.md)<`"Custom"`, `number`, [`WhitespaceData`](WhitespaceData.md)<`number`> | `TData`, `TOptions`, `TPartialOptions`>

Creates a custom series with specified parameters.

A custom series is a generic series which can be extended with a custom renderer to implement chart types which the library doesn't support by default.

#### Type parameters[​](IYieldCurveChartApi.html#type-parameters "Direct link to Type parameters")

• **TData** _extends_ [`CustomData`](CustomData.md)<`number`>

• **TOptions** _extends_ [`CustomSeriesOptions`](../type-aliases/CustomSeriesOptions.md)

• **TPartialOptions** _extends_ [`DeepPartial`](../type-aliases/DeepPartial.md)<`TOptions` & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> = [`DeepPartial`](../type-aliases/DeepPartial.md)<`TOptions` & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)>

#### Parameters[​](IYieldCurveChartApi.html#parameters-1 "Direct link to Parameters")

• **customPaneView** : [`ICustomSeriesPaneView`](ICustomSeriesPaneView.md)<`number`, `TData`, `TOptions`>

A custom series pane view which implements the custom renderer.

• **customOptions?** : [`DeepPartial`](../type-aliases/DeepPartial.md)<`TOptions` & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)>

Customization parameters of the series being created.
    
    
    const series = chart.addCustomSeries(myCustomPaneView);  
    

• **paneIndex?** : `number`

#### Returns[​](IYieldCurveChartApi.html#returns-2 "Direct link to Returns")

[`ISeriesApi`](ISeriesApi.md)<`"Custom"`, `number`, [`WhitespaceData`](WhitespaceData.md)<`number`> | `TData`, `TOptions`, `TPartialOptions`>

#### Inherited from[​](IYieldCurveChartApi.html#inherited-from-2 "Direct link to Inherited from")

`Omit.addCustomSeries`

* * *

### removeSeries()[​](IYieldCurveChartApi.html#removeseries "Direct link to removeSeries\(\)")

> **removeSeries**(`seriesApi`): `void`

Removes a series of any type. This is an irreversible operation, you cannot do anything with the series after removing it.

#### Parameters[​](IYieldCurveChartApi.html#parameters-2 "Direct link to Parameters")

• **seriesApi** : [`ISeriesApi`](ISeriesApi.md)<keyof [`SeriesOptionsMap`](SeriesOptionsMap.md), `number`, [`WhitespaceData`](WhitespaceData.md)<`number`> | [`LineData`](LineData.md)<`number`> | [`CustomData`](CustomData.md)<`number`> | [`AreaData`](AreaData.md)<`number`> | [`BarData`](BarData.md)<`number`> | [`CandlestickData`](CandlestickData.md)<`number`> | [`BaselineData`](BaselineData.md)<`number`> | [`HistogramData`](HistogramData.md)<`number`> | [`CustomSeriesWhitespaceData`](CustomSeriesWhitespaceData.md)<`number`>, [`CustomSeriesOptions`](../type-aliases/CustomSeriesOptions.md) | [`AreaSeriesOptions`](../type-aliases/AreaSeriesOptions.md) | [`BarSeriesOptions`](../type-aliases/BarSeriesOptions.md) | [`CandlestickSeriesOptions`](../type-aliases/CandlestickSeriesOptions.md) | [`BaselineSeriesOptions`](../type-aliases/BaselineSeriesOptions.md) | [`LineSeriesOptions`](../type-aliases/LineSeriesOptions.md) | [`HistogramSeriesOptions`](../type-aliases/HistogramSeriesOptions.md), [`DeepPartial`](../type-aliases/DeepPartial.md) <[`AreaStyleOptions`](AreaStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`BarStyleOptions`](BarStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`CandlestickStyleOptions`](CandlestickStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`BaselineStyleOptions`](BaselineStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`LineStyleOptions`](LineStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`HistogramStyleOptions`](HistogramStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`CustomStyleOptions`](CustomStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)>>

#### Returns[​](IYieldCurveChartApi.html#returns-3 "Direct link to Returns")

`void`

#### Inherited from[​](IYieldCurveChartApi.html#inherited-from-3 "Direct link to Inherited from")

`Omit.removeSeries`

#### Example[​](IYieldCurveChartApi.html#example "Direct link to Example")
    
    
    chart.removeSeries(series);  
    

* * *

### subscribeClick()[​](IYieldCurveChartApi.html#subscribeclick "Direct link to subscribeClick\(\)")

> **subscribeClick**(`handler`): `void`

Subscribe to the chart click event.

#### Parameters[​](IYieldCurveChartApi.html#parameters-3 "Direct link to Parameters")

• **handler** : [`MouseEventHandler`](../type-aliases/MouseEventHandler.md)<`number`>

Handler to be called on mouse click.

#### Returns[​](IYieldCurveChartApi.html#returns-4 "Direct link to Returns")

`void`

#### Inherited from[​](IYieldCurveChartApi.html#inherited-from-4 "Direct link to Inherited from")

`Omit.subscribeClick`

#### Example[​](IYieldCurveChartApi.html#example-1 "Direct link to Example")
    
    
    function myClickHandler(param) {  
        if (!param.point) {  
            return;  
        }  
      
        console.log(`Click at ${param.point.x}, ${param.point.y}. The time is ${param.time}.`);  
    }  
      
    chart.subscribeClick(myClickHandler);  
    

* * *

### unsubscribeClick()[​](IYieldCurveChartApi.html#unsubscribeclick "Direct link to unsubscribeClick\(\)")

> **unsubscribeClick**(`handler`): `void`

Unsubscribe a handler that was previously subscribed using [subscribeClick](IChartApiBase.html#subscribeclick).

#### Parameters[​](IYieldCurveChartApi.html#parameters-4 "Direct link to Parameters")

• **handler** : [`MouseEventHandler`](../type-aliases/MouseEventHandler.md)<`number`>

Previously subscribed handler

#### Returns[​](IYieldCurveChartApi.html#returns-5 "Direct link to Returns")

`void`

#### Inherited from[​](IYieldCurveChartApi.html#inherited-from-5 "Direct link to Inherited from")

`Omit.unsubscribeClick`

#### Example[​](IYieldCurveChartApi.html#example-2 "Direct link to Example")
    
    
    chart.unsubscribeClick(myClickHandler);  
    

* * *

### subscribeDblClick()[​](IYieldCurveChartApi.html#subscribedblclick "Direct link to subscribeDblClick\(\)")

> **subscribeDblClick**(`handler`): `void`

Subscribe to the chart double-click event.

#### Parameters[​](IYieldCurveChartApi.html#parameters-5 "Direct link to Parameters")

• **handler** : [`MouseEventHandler`](../type-aliases/MouseEventHandler.md)<`number`>

Handler to be called on mouse double-click.

#### Returns[​](IYieldCurveChartApi.html#returns-6 "Direct link to Returns")

`void`

#### Inherited from[​](IYieldCurveChartApi.html#inherited-from-6 "Direct link to Inherited from")

`Omit.subscribeDblClick`

#### Example[​](IYieldCurveChartApi.html#example-3 "Direct link to Example")
    
    
    function myDblClickHandler(param) {  
        if (!param.point) {  
            return;  
        }  
      
        console.log(`Double Click at ${param.point.x}, ${param.point.y}. The time is ${param.time}.`);  
    }  
      
    chart.subscribeDblClick(myDblClickHandler);  
    

* * *

### unsubscribeDblClick()[​](IYieldCurveChartApi.html#unsubscribedblclick "Direct link to unsubscribeDblClick\(\)")

> **unsubscribeDblClick**(`handler`): `void`

Unsubscribe a handler that was previously subscribed using [subscribeDblClick](IChartApiBase.html#subscribedblclick).

#### Parameters[​](IYieldCurveChartApi.html#parameters-6 "Direct link to Parameters")

• **handler** : [`MouseEventHandler`](../type-aliases/MouseEventHandler.md)<`number`>

Previously subscribed handler

#### Returns[​](IYieldCurveChartApi.html#returns-7 "Direct link to Returns")

`void`

#### Inherited from[​](IYieldCurveChartApi.html#inherited-from-7 "Direct link to Inherited from")

`Omit.unsubscribeDblClick`

#### Example[​](IYieldCurveChartApi.html#example-4 "Direct link to Example")
    
    
    chart.unsubscribeDblClick(myDblClickHandler);  
    

* * *

### subscribeCrosshairMove()[​](IYieldCurveChartApi.html#subscribecrosshairmove "Direct link to subscribeCrosshairMove\(\)")

> **subscribeCrosshairMove**(`handler`): `void`

Subscribe to the crosshair move event.

#### Parameters[​](IYieldCurveChartApi.html#parameters-7 "Direct link to Parameters")

• **handler** : [`MouseEventHandler`](../type-aliases/MouseEventHandler.md)<`number`>

Handler to be called on crosshair move.

#### Returns[​](IYieldCurveChartApi.html#returns-8 "Direct link to Returns")

`void`

#### Inherited from[​](IYieldCurveChartApi.html#inherited-from-8 "Direct link to Inherited from")

`Omit.subscribeCrosshairMove`

#### Example[​](IYieldCurveChartApi.html#example-5 "Direct link to Example")
    
    
    function myCrosshairMoveHandler(param) {  
        if (!param.point) {  
            return;  
        }  
      
        console.log(`Crosshair moved to ${param.point.x}, ${param.point.y}. The time is ${param.time}.`);  
    }  
      
    chart.subscribeCrosshairMove(myCrosshairMoveHandler);  
    

* * *

### unsubscribeCrosshairMove()[​](IYieldCurveChartApi.html#unsubscribecrosshairmove "Direct link to unsubscribeCrosshairMove\(\)")

> **unsubscribeCrosshairMove**(`handler`): `void`

Unsubscribe a handler that was previously subscribed using [subscribeCrosshairMove](IChartApiBase.html#subscribecrosshairmove).

#### Parameters[​](IYieldCurveChartApi.html#parameters-8 "Direct link to Parameters")

• **handler** : [`MouseEventHandler`](../type-aliases/MouseEventHandler.md)<`number`>

Previously subscribed handler

#### Returns[​](IYieldCurveChartApi.html#returns-9 "Direct link to Returns")

`void`

#### Inherited from[​](IYieldCurveChartApi.html#inherited-from-9 "Direct link to Inherited from")

`Omit.unsubscribeCrosshairMove`

#### Example[​](IYieldCurveChartApi.html#example-6 "Direct link to Example")
    
    
    chart.unsubscribeCrosshairMove(myCrosshairMoveHandler);  
    

* * *

### priceScale()[​](IYieldCurveChartApi.html#pricescale "Direct link to priceScale\(\)")

> **priceScale**(`priceScaleId`, `paneIndex`?): [`IPriceScaleApi`](IPriceScaleApi.md)

Returns API to manipulate a price scale.

#### Parameters[​](IYieldCurveChartApi.html#parameters-9 "Direct link to Parameters")

• **priceScaleId** : `string`

ID of the price scale.

• **paneIndex?** : `number`

Index of the pane (default: 0)

#### Returns[​](IYieldCurveChartApi.html#returns-10 "Direct link to Returns")

[`IPriceScaleApi`](IPriceScaleApi.md)

Price scale API.

#### Inherited from[​](IYieldCurveChartApi.html#inherited-from-10 "Direct link to Inherited from")

`Omit.priceScale`

* * *

### timeScale()[​](IYieldCurveChartApi.html#timescale "Direct link to timeScale\(\)")

> **timeScale**(): [`ITimeScaleApi`](ITimeScaleApi.md)<`number`>

Returns API to manipulate the time scale

#### Returns[​](IYieldCurveChartApi.html#returns-11 "Direct link to Returns")

[`ITimeScaleApi`](ITimeScaleApi.md)<`number`>

Target API

#### Inherited from[​](IYieldCurveChartApi.html#inherited-from-11 "Direct link to Inherited from")

`Omit.timeScale`

* * *

### applyOptions()[​](IYieldCurveChartApi.html#applyoptions "Direct link to applyOptions\(\)")

> **applyOptions**(`options`): `void`

Applies new options to the chart

#### Parameters[​](IYieldCurveChartApi.html#parameters-10 "Direct link to Parameters")

• **options** : [`DeepPartial`](../type-aliases/DeepPartial.md) <[`ChartOptionsImpl`](ChartOptionsImpl.md)<`number`>>

Any subset of options.

#### Returns[​](IYieldCurveChartApi.html#returns-12 "Direct link to Returns")

`void`

#### Inherited from[​](IYieldCurveChartApi.html#inherited-from-12 "Direct link to Inherited from")

`Omit.applyOptions`

* * *

### options()[​](IYieldCurveChartApi.html#options "Direct link to options\(\)")

> **options**(): `Readonly` <[`ChartOptionsImpl`](ChartOptionsImpl.md)<`number`>>

Returns currently applied options

#### Returns[​](IYieldCurveChartApi.html#returns-13 "Direct link to Returns")

`Readonly` <[`ChartOptionsImpl`](ChartOptionsImpl.md)<`number`>>

Full set of currently applied options, including defaults

#### Inherited from[​](IYieldCurveChartApi.html#inherited-from-13 "Direct link to Inherited from")

`Omit.options`

* * *

### takeScreenshot()[​](IYieldCurveChartApi.html#takescreenshot "Direct link to takeScreenshot\(\)")

> **takeScreenshot**(): `HTMLCanvasElement`

Make a screenshot of the chart with all the elements excluding crosshair.

#### Returns[​](IYieldCurveChartApi.html#returns-14 "Direct link to Returns")

`HTMLCanvasElement`

A canvas with the chart drawn on. Any `Canvas` methods like `toDataURL()` or `toBlob()` can be used to serialize the result.

#### Inherited from[​](IYieldCurveChartApi.html#inherited-from-14 "Direct link to Inherited from")

`Omit.takeScreenshot`

* * *

### panes()[​](IYieldCurveChartApi.html#panes "Direct link to panes\(\)")

> **panes**(): [`IPaneApi`](IPaneApi.md)<`number`>[]

Returns array of panes' API

#### Returns[​](IYieldCurveChartApi.html#returns-15 "Direct link to Returns")

[`IPaneApi`](IPaneApi.md)<`number`>[]

array of pane's Api

#### Inherited from[​](IYieldCurveChartApi.html#inherited-from-15 "Direct link to Inherited from")

`Omit.panes`

* * *

### removePane()[​](IYieldCurveChartApi.html#removepane "Direct link to removePane\(\)")

> **removePane**(`index`): `void`

Removes a pane with index

#### Parameters[​](IYieldCurveChartApi.html#parameters-11 "Direct link to Parameters")

• **index** : `number`

the pane to be removed

#### Returns[​](IYieldCurveChartApi.html#returns-16 "Direct link to Returns")

`void`

#### Inherited from[​](IYieldCurveChartApi.html#inherited-from-16 "Direct link to Inherited from")

`Omit.removePane`

* * *

### swapPanes()[​](IYieldCurveChartApi.html#swappanes "Direct link to swapPanes\(\)")

> **swapPanes**(`first`, `second`): `void`

swap the position of two panes.

#### Parameters[​](IYieldCurveChartApi.html#parameters-12 "Direct link to Parameters")

• **first** : `number`

the first index

• **second** : `number`

the second index

#### Returns[​](IYieldCurveChartApi.html#returns-17 "Direct link to Returns")

`void`

#### Inherited from[​](IYieldCurveChartApi.html#inherited-from-17 "Direct link to Inherited from")

`Omit.swapPanes`

* * *

### autoSizeActive()[​](IYieldCurveChartApi.html#autosizeactive "Direct link to autoSizeActive\(\)")

> **autoSizeActive**(): `boolean`

Returns the active state of the `autoSize` option. This can be used to check whether the chart is handling resizing automatically with a `ResizeObserver`.

#### Returns[​](IYieldCurveChartApi.html#returns-18 "Direct link to Returns")

`boolean`

Whether the `autoSize` option is enabled and the active.

#### Inherited from[​](IYieldCurveChartApi.html#inherited-from-18 "Direct link to Inherited from")

`Omit.autoSizeActive`

* * *

### chartElement()[​](IYieldCurveChartApi.html#chartelement "Direct link to chartElement\(\)")

> **chartElement**(): `HTMLDivElement`

Returns the generated div element containing the chart. This can be used for adding your own additional event listeners, or for measuring the elements dimensions and position within the document.

#### Returns[​](IYieldCurveChartApi.html#returns-19 "Direct link to Returns")

`HTMLDivElement`

generated div element containing the chart.

#### Inherited from[​](IYieldCurveChartApi.html#inherited-from-19 "Direct link to Inherited from")

`Omit.chartElement`

* * *

### setCrosshairPosition()[​](IYieldCurveChartApi.html#setcrosshairposition "Direct link to setCrosshairPosition\(\)")

> **setCrosshairPosition**(`price`, `horizontalPosition`, `seriesApi`): `void`

Set the crosshair position within the chart.

Usually the crosshair position is set automatically by the user's actions. However in some cases you may want to set it explicitly.

For example if you want to synchronise the crosshairs of two separate charts.

#### Parameters[​](IYieldCurveChartApi.html#parameters-13 "Direct link to Parameters")

• **price** : `number`

The price (vertical coordinate) of the new crosshair position.

• **horizontalPosition** : `number`

The horizontal coordinate (time by default) of the new crosshair position.

• **seriesApi** : [`ISeriesApi`](ISeriesApi.md)<keyof [`SeriesOptionsMap`](SeriesOptionsMap.md), `number`, [`WhitespaceData`](WhitespaceData.md)<`number`> | [`LineData`](LineData.md)<`number`> | [`CustomData`](CustomData.md)<`number`> | [`AreaData`](AreaData.md)<`number`> | [`BarData`](BarData.md)<`number`> | [`CandlestickData`](CandlestickData.md)<`number`> | [`BaselineData`](BaselineData.md)<`number`> | [`HistogramData`](HistogramData.md)<`number`> | [`CustomSeriesWhitespaceData`](CustomSeriesWhitespaceData.md)<`number`>, [`CustomSeriesOptions`](../type-aliases/CustomSeriesOptions.md) | [`AreaSeriesOptions`](../type-aliases/AreaSeriesOptions.md) | [`BarSeriesOptions`](../type-aliases/BarSeriesOptions.md) | [`CandlestickSeriesOptions`](../type-aliases/CandlestickSeriesOptions.md) | [`BaselineSeriesOptions`](../type-aliases/BaselineSeriesOptions.md) | [`LineSeriesOptions`](../type-aliases/LineSeriesOptions.md) | [`HistogramSeriesOptions`](../type-aliases/HistogramSeriesOptions.md), [`DeepPartial`](../type-aliases/DeepPartial.md) <[`AreaStyleOptions`](AreaStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`BarStyleOptions`](BarStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`CandlestickStyleOptions`](CandlestickStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`BaselineStyleOptions`](BaselineStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`LineStyleOptions`](LineStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`HistogramStyleOptions`](HistogramStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`CustomStyleOptions`](CustomStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)>>

#### Returns[​](IYieldCurveChartApi.html#returns-20 "Direct link to Returns")

`void`

#### Inherited from[​](IYieldCurveChartApi.html#inherited-from-20 "Direct link to Inherited from")

`Omit.setCrosshairPosition`

* * *

### clearCrosshairPosition()[​](IYieldCurveChartApi.html#clearcrosshairposition "Direct link to clearCrosshairPosition\(\)")

> **clearCrosshairPosition**(): `void`

Clear the crosshair position within the chart.

#### Returns[​](IYieldCurveChartApi.html#returns-21 "Direct link to Returns")

`void`

#### Inherited from[​](IYieldCurveChartApi.html#inherited-from-21 "Direct link to Inherited from")

`Omit.clearCrosshairPosition`

* * *

### paneSize()[​](IYieldCurveChartApi.html#panesize "Direct link to paneSize\(\)")

> **paneSize**(`paneIndex`?): [`PaneSize`](PaneSize.md)

Returns the dimensions of the chart pane (the plot surface which excludes time and price scales). This would typically only be useful for plugin development.

#### Parameters[​](IYieldCurveChartApi.html#parameters-14 "Direct link to Parameters")

• **paneIndex?** : `number`

The index of the pane

#### Returns[​](IYieldCurveChartApi.html#returns-22 "Direct link to Returns")

[`PaneSize`](PaneSize.md)

Dimensions of the chart pane

#### Inherited from[​](IYieldCurveChartApi.html#inherited-from-22 "Direct link to Inherited from")

`Omit.paneSize`

#### Default Value[​](IYieldCurveChartApi.html#default-value "Direct link to Default Value")

`0`

* * *

### horzBehaviour()[​](IYieldCurveChartApi.html#horzbehaviour "Direct link to horzBehaviour\(\)")

> **horzBehaviour**(): [`IHorzScaleBehavior`](IHorzScaleBehavior.md)<`number`>

Returns the horizontal scale behaviour.

#### Returns[​](IYieldCurveChartApi.html#returns-23 "Direct link to Returns")

[`IHorzScaleBehavior`](IHorzScaleBehavior.md)<`number`>

#### Inherited from[​](IYieldCurveChartApi.html#inherited-from-23 "Direct link to Inherited from")

`Omit.horzBehaviour`

* * *

### addSeries()[​](IYieldCurveChartApi.html#addseries "Direct link to addSeries\(\)")

> **addSeries** <`T`>(`definition`, `options`?, `paneIndex`?): [`ISeriesApi`](ISeriesApi.md)<`T`, `number`, [`WhitespaceData`](WhitespaceData.md)<`number`> | [`LineData`](LineData.md)<`number`>, [`SeriesOptionsMap`](SeriesOptionsMap.md)[`T`], [`SeriesPartialOptionsMap`](SeriesPartialOptionsMap.md)[`T`]>

Creates a series with specified parameters.

Note that the Yield Curve chart only supports the Area and Line series types.

#### Type parameters[​](IYieldCurveChartApi.html#type-parameters-1 "Direct link to Type parameters")

• **T** _extends_ [`YieldCurveSeriesType`](../type-aliases/YieldCurveSeriesType.md)

#### Parameters[​](IYieldCurveChartApi.html#parameters-15 "Direct link to Parameters")

• **definition** : [`SeriesDefinition`](SeriesDefinition.md)<`T`>

A series definition for either AreaSeries or LineSeries.

• **options?** : [`SeriesPartialOptionsMap`](SeriesPartialOptionsMap.md)[`T`]

Customization parameters of the series being created.

• **paneIndex?** : `number`

An index of the pane where the series should be created.
    
    
    const series = chart.addSeries(LineSeries, { lineWidth: 2 });  
    

#### Returns[​](IYieldCurveChartApi.html#returns-24 "Direct link to Returns")

[`ISeriesApi`](ISeriesApi.md)<`T`, `number`, [`WhitespaceData`](WhitespaceData.md)<`number`> | [`LineData`](LineData.md)<`number`>, [`SeriesOptionsMap`](SeriesOptionsMap.md)[`T`], [`SeriesPartialOptionsMap`](SeriesPartialOptionsMap.md)[`T`]>
