# API: Ichartapibase

*Source: docs\api\interfaces\IChartApiBase.html*

Version: 5.0

On this page

The main interface of a single chart.

## Extended by[​](IChartApiBase.html#extended-by "Direct link to Extended by")

  * [`IChartApi`](IChartApi.md)

## Type parameters[​](IChartApiBase.html#type-parameters "Direct link to Type parameters")

• **HorzScaleItem** = [`Time`](../type-aliases/Time.md)

## Methods[​](IChartApiBase.html#methods "Direct link to Methods")

### remove()[​](IChartApiBase.html#remove "Direct link to remove\(\)")

> **remove**(): `void`

Removes the chart object including all DOM elements. This is an irreversible operation, you cannot do anything with the chart after removing it.

#### Returns[​](IChartApiBase.html#returns "Direct link to Returns")

`void`

* * *

### resize()[​](IChartApiBase.html#resize "Direct link to resize\(\)")

> **resize**(`width`, `height`, `forceRepaint`?): `void`

Sets fixed size of the chart. By default chart takes up 100% of its container.

If chart has the `autoSize` option enabled, and the ResizeObserver is available then the width and height values will be ignored.

#### Parameters[​](IChartApiBase.html#parameters "Direct link to Parameters")

• **width** : `number`

Target width of the chart.

• **height** : `number`

Target height of the chart.

• **forceRepaint?** : `boolean`

True to initiate resize immediately. One could need this to get screenshot immediately after resize.

#### Returns[​](IChartApiBase.html#returns-1 "Direct link to Returns")

`void`

* * *

### addCustomSeries()[​](IChartApiBase.html#addcustomseries "Direct link to addCustomSeries\(\)")

> **addCustomSeries** <`TData`, `TOptions`, `TPartialOptions`>(`customPaneView`, `customOptions`?, `paneIndex`?): [`ISeriesApi`](ISeriesApi.md)<`"Custom"`, `HorzScaleItem`, `TData` | [`WhitespaceData`](WhitespaceData.md)<`HorzScaleItem`>, `TOptions`, `TPartialOptions`>

Creates a custom series with specified parameters.

A custom series is a generic series which can be extended with a custom renderer to implement chart types which the library doesn't support by default.

#### Type parameters[​](IChartApiBase.html#type-parameters-1 "Direct link to Type parameters")

• **TData** _extends_ [`CustomData`](CustomData.md)<`HorzScaleItem`>

• **TOptions** _extends_ [`CustomSeriesOptions`](../type-aliases/CustomSeriesOptions.md)

• **TPartialOptions** _extends_ [`DeepPartial`](../type-aliases/DeepPartial.md)<`TOptions` & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> = [`DeepPartial`](../type-aliases/DeepPartial.md)<`TOptions` & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)>

#### Parameters[​](IChartApiBase.html#parameters-1 "Direct link to Parameters")

• **customPaneView** : [`ICustomSeriesPaneView`](ICustomSeriesPaneView.md)<`HorzScaleItem`, `TData`, `TOptions`>

A custom series pane view which implements the custom renderer.

• **customOptions?** : [`DeepPartial`](../type-aliases/DeepPartial.md)<`TOptions` & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)>

Customization parameters of the series being created.
    
    
    const series = chart.addCustomSeries(myCustomPaneView);  
    

• **paneIndex?** : `number`

#### Returns[​](IChartApiBase.html#returns-2 "Direct link to Returns")

[`ISeriesApi`](ISeriesApi.md)<`"Custom"`, `HorzScaleItem`, `TData` | [`WhitespaceData`](WhitespaceData.md)<`HorzScaleItem`>, `TOptions`, `TPartialOptions`>

* * *

### addSeries()[​](IChartApiBase.html#addseries "Direct link to addSeries\(\)")

> **addSeries** <`T`>(`definition`, `options`?, `paneIndex`?): [`ISeriesApi`](ISeriesApi.md)<`T`, `HorzScaleItem`, [`SeriesDataItemTypeMap`](SeriesDataItemTypeMap.md)<`HorzScaleItem`>[`T`], [`SeriesOptionsMap`](SeriesOptionsMap.md)[`T`], [`SeriesPartialOptionsMap`](SeriesPartialOptionsMap.md)[`T`]>

Creates a series with specified parameters.

#### Type parameters[​](IChartApiBase.html#type-parameters-2 "Direct link to Type parameters")

• **T** _extends_ keyof [`SeriesOptionsMap`](SeriesOptionsMap.md)

#### Parameters[​](IChartApiBase.html#parameters-2 "Direct link to Parameters")

• **definition** : [`SeriesDefinition`](SeriesDefinition.md)<`T`>

A series definition.

• **options?** : [`SeriesPartialOptionsMap`](SeriesPartialOptionsMap.md)[`T`]

Customization parameters of the series being created.

• **paneIndex?** : `number`

An index of the pane where the series should be created.
    
    
    const series = chart.addSeries(LineSeries, { lineWidth: 2 });  
    

#### Returns[​](IChartApiBase.html#returns-3 "Direct link to Returns")

[`ISeriesApi`](ISeriesApi.md)<`T`, `HorzScaleItem`, [`SeriesDataItemTypeMap`](SeriesDataItemTypeMap.md)<`HorzScaleItem`>[`T`], [`SeriesOptionsMap`](SeriesOptionsMap.md)[`T`], [`SeriesPartialOptionsMap`](SeriesPartialOptionsMap.md)[`T`]>

* * *

### removeSeries()[​](IChartApiBase.html#removeseries "Direct link to removeSeries\(\)")

> **removeSeries**(`seriesApi`): `void`

Removes a series of any type. This is an irreversible operation, you cannot do anything with the series after removing it.

#### Parameters[​](IChartApiBase.html#parameters-3 "Direct link to Parameters")

• **seriesApi** : [`ISeriesApi`](ISeriesApi.md)<keyof [`SeriesOptionsMap`](SeriesOptionsMap.md), `HorzScaleItem`, [`CustomData`](CustomData.md)<`HorzScaleItem`> | [`WhitespaceData`](WhitespaceData.md)<`HorzScaleItem`> | [`AreaData`](AreaData.md)<`HorzScaleItem`> | [`BarData`](BarData.md)<`HorzScaleItem`> | [`CandlestickData`](CandlestickData.md)<`HorzScaleItem`> | [`BaselineData`](BaselineData.md)<`HorzScaleItem`> | [`LineData`](LineData.md)<`HorzScaleItem`> | [`HistogramData`](HistogramData.md)<`HorzScaleItem`> | [`CustomSeriesWhitespaceData`](CustomSeriesWhitespaceData.md)<`HorzScaleItem`>, [`CustomSeriesOptions`](../type-aliases/CustomSeriesOptions.md) | [`AreaSeriesOptions`](../type-aliases/AreaSeriesOptions.md) | [`BarSeriesOptions`](../type-aliases/BarSeriesOptions.md) | [`CandlestickSeriesOptions`](../type-aliases/CandlestickSeriesOptions.md) | [`BaselineSeriesOptions`](../type-aliases/BaselineSeriesOptions.md) | [`LineSeriesOptions`](../type-aliases/LineSeriesOptions.md) | [`HistogramSeriesOptions`](../type-aliases/HistogramSeriesOptions.md), [`DeepPartial`](../type-aliases/DeepPartial.md) <[`AreaStyleOptions`](AreaStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`BarStyleOptions`](BarStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`CandlestickStyleOptions`](CandlestickStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`BaselineStyleOptions`](BaselineStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`LineStyleOptions`](LineStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`HistogramStyleOptions`](HistogramStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`CustomStyleOptions`](CustomStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)>>

#### Returns[​](IChartApiBase.html#returns-4 "Direct link to Returns")

`void`

#### Example[​](IChartApiBase.html#example "Direct link to Example")
    
    
    chart.removeSeries(series);  
    

* * *

### subscribeClick()[​](IChartApiBase.html#subscribeclick "Direct link to subscribeClick\(\)")

> **subscribeClick**(`handler`): `void`

Subscribe to the chart click event.

#### Parameters[​](IChartApiBase.html#parameters-4 "Direct link to Parameters")

• **handler** : [`MouseEventHandler`](../type-aliases/MouseEventHandler.md)<`HorzScaleItem`>

Handler to be called on mouse click.

#### Returns[​](IChartApiBase.html#returns-5 "Direct link to Returns")

`void`

#### Example[​](IChartApiBase.html#example-1 "Direct link to Example")
    
    
    function myClickHandler(param) {  
        if (!param.point) {  
            return;  
        }  
      
        console.log(`Click at ${param.point.x}, ${param.point.y}. The time is ${param.time}.`);  
    }  
      
    chart.subscribeClick(myClickHandler);  
    

* * *

### unsubscribeClick()[​](IChartApiBase.html#unsubscribeclick "Direct link to unsubscribeClick\(\)")

> **unsubscribeClick**(`handler`): `void`

Unsubscribe a handler that was previously subscribed using [subscribeClick](IChartApiBase.html#subscribeclick).

#### Parameters[​](IChartApiBase.html#parameters-5 "Direct link to Parameters")

• **handler** : [`MouseEventHandler`](../type-aliases/MouseEventHandler.md)<`HorzScaleItem`>

Previously subscribed handler

#### Returns[​](IChartApiBase.html#returns-6 "Direct link to Returns")

`void`

#### Example[​](IChartApiBase.html#example-2 "Direct link to Example")
    
    
    chart.unsubscribeClick(myClickHandler);  
    

* * *

### subscribeDblClick()[​](IChartApiBase.html#subscribedblclick "Direct link to subscribeDblClick\(\)")

> **subscribeDblClick**(`handler`): `void`

Subscribe to the chart double-click event.

#### Parameters[​](IChartApiBase.html#parameters-6 "Direct link to Parameters")

• **handler** : [`MouseEventHandler`](../type-aliases/MouseEventHandler.md)<`HorzScaleItem`>

Handler to be called on mouse double-click.

#### Returns[​](IChartApiBase.html#returns-7 "Direct link to Returns")

`void`

#### Example[​](IChartApiBase.html#example-3 "Direct link to Example")
    
    
    function myDblClickHandler(param) {  
        if (!param.point) {  
            return;  
        }  
      
        console.log(`Double Click at ${param.point.x}, ${param.point.y}. The time is ${param.time}.`);  
    }  
      
    chart.subscribeDblClick(myDblClickHandler);  
    

* * *

### unsubscribeDblClick()[​](IChartApiBase.html#unsubscribedblclick "Direct link to unsubscribeDblClick\(\)")

> **unsubscribeDblClick**(`handler`): `void`

Unsubscribe a handler that was previously subscribed using [subscribeDblClick](IChartApiBase.html#subscribedblclick).

#### Parameters[​](IChartApiBase.html#parameters-7 "Direct link to Parameters")

• **handler** : [`MouseEventHandler`](../type-aliases/MouseEventHandler.md)<`HorzScaleItem`>

Previously subscribed handler

#### Returns[​](IChartApiBase.html#returns-8 "Direct link to Returns")

`void`

#### Example[​](IChartApiBase.html#example-4 "Direct link to Example")
    
    
    chart.unsubscribeDblClick(myDblClickHandler);  
    

* * *

### subscribeCrosshairMove()[​](IChartApiBase.html#subscribecrosshairmove "Direct link to subscribeCrosshairMove\(\)")

> **subscribeCrosshairMove**(`handler`): `void`

Subscribe to the crosshair move event.

#### Parameters[​](IChartApiBase.html#parameters-8 "Direct link to Parameters")

• **handler** : [`MouseEventHandler`](../type-aliases/MouseEventHandler.md)<`HorzScaleItem`>

Handler to be called on crosshair move.

#### Returns[​](IChartApiBase.html#returns-9 "Direct link to Returns")

`void`

#### Example[​](IChartApiBase.html#example-5 "Direct link to Example")
    
    
    function myCrosshairMoveHandler(param) {  
        if (!param.point) {  
            return;  
        }  
      
        console.log(`Crosshair moved to ${param.point.x}, ${param.point.y}. The time is ${param.time}.`);  
    }  
      
    chart.subscribeCrosshairMove(myCrosshairMoveHandler);  
    

* * *

### unsubscribeCrosshairMove()[​](IChartApiBase.html#unsubscribecrosshairmove "Direct link to unsubscribeCrosshairMove\(\)")

> **unsubscribeCrosshairMove**(`handler`): `void`

Unsubscribe a handler that was previously subscribed using [subscribeCrosshairMove](IChartApiBase.html#subscribecrosshairmove).

#### Parameters[​](IChartApiBase.html#parameters-9 "Direct link to Parameters")

• **handler** : [`MouseEventHandler`](../type-aliases/MouseEventHandler.md)<`HorzScaleItem`>

Previously subscribed handler

#### Returns[​](IChartApiBase.html#returns-10 "Direct link to Returns")

`void`

#### Example[​](IChartApiBase.html#example-6 "Direct link to Example")
    
    
    chart.unsubscribeCrosshairMove(myCrosshairMoveHandler);  
    

* * *

### priceScale()[​](IChartApiBase.html#pricescale "Direct link to priceScale\(\)")

> **priceScale**(`priceScaleId`, `paneIndex`?): [`IPriceScaleApi`](IPriceScaleApi.md)

Returns API to manipulate a price scale.

#### Parameters[​](IChartApiBase.html#parameters-10 "Direct link to Parameters")

• **priceScaleId** : `string`

ID of the price scale.

• **paneIndex?** : `number`

Index of the pane (default: 0)

#### Returns[​](IChartApiBase.html#returns-11 "Direct link to Returns")

[`IPriceScaleApi`](IPriceScaleApi.md)

Price scale API.

* * *

### timeScale()[​](IChartApiBase.html#timescale "Direct link to timeScale\(\)")

> **timeScale**(): [`ITimeScaleApi`](ITimeScaleApi.md)<`HorzScaleItem`>

Returns API to manipulate the time scale

#### Returns[​](IChartApiBase.html#returns-12 "Direct link to Returns")

[`ITimeScaleApi`](ITimeScaleApi.md)<`HorzScaleItem`>

Target API

* * *

### applyOptions()[​](IChartApiBase.html#applyoptions "Direct link to applyOptions\(\)")

> **applyOptions**(`options`): `void`

Applies new options to the chart

#### Parameters[​](IChartApiBase.html#parameters-11 "Direct link to Parameters")

• **options** : [`DeepPartial`](../type-aliases/DeepPartial.md) <[`ChartOptionsImpl`](ChartOptionsImpl.md)<`HorzScaleItem`>>

Any subset of options.

#### Returns[​](IChartApiBase.html#returns-13 "Direct link to Returns")

`void`

* * *

### options()[​](IChartApiBase.html#options "Direct link to options\(\)")

> **options**(): `Readonly` <[`ChartOptionsImpl`](ChartOptionsImpl.md)<`HorzScaleItem`>>

Returns currently applied options

#### Returns[​](IChartApiBase.html#returns-14 "Direct link to Returns")

`Readonly` <[`ChartOptionsImpl`](ChartOptionsImpl.md)<`HorzScaleItem`>>

Full set of currently applied options, including defaults

* * *

### takeScreenshot()[​](IChartApiBase.html#takescreenshot "Direct link to takeScreenshot\(\)")

> **takeScreenshot**(): `HTMLCanvasElement`

Make a screenshot of the chart with all the elements excluding crosshair.

#### Returns[​](IChartApiBase.html#returns-15 "Direct link to Returns")

`HTMLCanvasElement`

A canvas with the chart drawn on. Any `Canvas` methods like `toDataURL()` or `toBlob()` can be used to serialize the result.

* * *

### panes()[​](IChartApiBase.html#panes "Direct link to panes\(\)")

> **panes**(): [`IPaneApi`](IPaneApi.md)<`HorzScaleItem`>[]

Returns array of panes' API

#### Returns[​](IChartApiBase.html#returns-16 "Direct link to Returns")

[`IPaneApi`](IPaneApi.md)<`HorzScaleItem`>[]

array of pane's Api

* * *

### removePane()[​](IChartApiBase.html#removepane "Direct link to removePane\(\)")

> **removePane**(`index`): `void`

Removes a pane with index

#### Parameters[​](IChartApiBase.html#parameters-12 "Direct link to Parameters")

• **index** : `number`

the pane to be removed

#### Returns[​](IChartApiBase.html#returns-17 "Direct link to Returns")

`void`

* * *

### swapPanes()[​](IChartApiBase.html#swappanes "Direct link to swapPanes\(\)")

> **swapPanes**(`first`, `second`): `void`

swap the position of two panes.

#### Parameters[​](IChartApiBase.html#parameters-13 "Direct link to Parameters")

• **first** : `number`

the first index

• **second** : `number`

the second index

#### Returns[​](IChartApiBase.html#returns-18 "Direct link to Returns")

`void`

* * *

### autoSizeActive()[​](IChartApiBase.html#autosizeactive "Direct link to autoSizeActive\(\)")

> **autoSizeActive**(): `boolean`

Returns the active state of the `autoSize` option. This can be used to check whether the chart is handling resizing automatically with a `ResizeObserver`.

#### Returns[​](IChartApiBase.html#returns-19 "Direct link to Returns")

`boolean`

Whether the `autoSize` option is enabled and the active.

* * *

### chartElement()[​](IChartApiBase.html#chartelement "Direct link to chartElement\(\)")

> **chartElement**(): `HTMLDivElement`

Returns the generated div element containing the chart. This can be used for adding your own additional event listeners, or for measuring the elements dimensions and position within the document.

#### Returns[​](IChartApiBase.html#returns-20 "Direct link to Returns")

`HTMLDivElement`

generated div element containing the chart.

* * *

### setCrosshairPosition()[​](IChartApiBase.html#setcrosshairposition "Direct link to setCrosshairPosition\(\)")

> **setCrosshairPosition**(`price`, `horizontalPosition`, `seriesApi`): `void`

Set the crosshair position within the chart.

Usually the crosshair position is set automatically by the user's actions. However in some cases you may want to set it explicitly.

For example if you want to synchronise the crosshairs of two separate charts.

#### Parameters[​](IChartApiBase.html#parameters-14 "Direct link to Parameters")

• **price** : `number`

The price (vertical coordinate) of the new crosshair position.

• **horizontalPosition** : `HorzScaleItem`

The horizontal coordinate (time by default) of the new crosshair position.

• **seriesApi** : [`ISeriesApi`](ISeriesApi.md)<keyof [`SeriesOptionsMap`](SeriesOptionsMap.md), `HorzScaleItem`, [`CustomData`](CustomData.md)<`HorzScaleItem`> | [`WhitespaceData`](WhitespaceData.md)<`HorzScaleItem`> | [`AreaData`](AreaData.md)<`HorzScaleItem`> | [`BarData`](BarData.md)<`HorzScaleItem`> | [`CandlestickData`](CandlestickData.md)<`HorzScaleItem`> | [`BaselineData`](BaselineData.md)<`HorzScaleItem`> | [`LineData`](LineData.md)<`HorzScaleItem`> | [`HistogramData`](HistogramData.md)<`HorzScaleItem`> | [`CustomSeriesWhitespaceData`](CustomSeriesWhitespaceData.md)<`HorzScaleItem`>, [`CustomSeriesOptions`](../type-aliases/CustomSeriesOptions.md) | [`AreaSeriesOptions`](../type-aliases/AreaSeriesOptions.md) | [`BarSeriesOptions`](../type-aliases/BarSeriesOptions.md) | [`CandlestickSeriesOptions`](../type-aliases/CandlestickSeriesOptions.md) | [`BaselineSeriesOptions`](../type-aliases/BaselineSeriesOptions.md) | [`LineSeriesOptions`](../type-aliases/LineSeriesOptions.md) | [`HistogramSeriesOptions`](../type-aliases/HistogramSeriesOptions.md), [`DeepPartial`](../type-aliases/DeepPartial.md) <[`AreaStyleOptions`](AreaStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`BarStyleOptions`](BarStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`CandlestickStyleOptions`](CandlestickStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`BaselineStyleOptions`](BaselineStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`LineStyleOptions`](LineStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`HistogramStyleOptions`](HistogramStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`CustomStyleOptions`](CustomStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)>>

#### Returns[​](IChartApiBase.html#returns-21 "Direct link to Returns")

`void`

* * *

### clearCrosshairPosition()[​](IChartApiBase.html#clearcrosshairposition "Direct link to clearCrosshairPosition\(\)")

> **clearCrosshairPosition**(): `void`

Clear the crosshair position within the chart.

#### Returns[​](IChartApiBase.html#returns-22 "Direct link to Returns")

`void`

* * *

### paneSize()[​](IChartApiBase.html#panesize "Direct link to paneSize\(\)")

> **paneSize**(`paneIndex`?): [`PaneSize`](PaneSize.md)

Returns the dimensions of the chart pane (the plot surface which excludes time and price scales). This would typically only be useful for plugin development.

#### Parameters[​](IChartApiBase.html#parameters-15 "Direct link to Parameters")

• **paneIndex?** : `number`

The index of the pane

#### Returns[​](IChartApiBase.html#returns-23 "Direct link to Returns")

[`PaneSize`](PaneSize.md)

Dimensions of the chart pane

#### Default Value[​](IChartApiBase.html#default-value "Direct link to Default Value")

`0`

* * *

### horzBehaviour()[​](IChartApiBase.html#horzbehaviour "Direct link to horzBehaviour\(\)")

> **horzBehaviour**(): [`IHorzScaleBehavior`](IHorzScaleBehavior.md)<`HorzScaleItem`>

Returns the horizontal scale behaviour.

#### Returns[​](IChartApiBase.html#returns-24 "Direct link to Returns")

[`IHorzScaleBehavior`](IHorzScaleBehavior.md)<`HorzScaleItem`>
