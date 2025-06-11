# API: Ipaneapi

*Source: docs\api\interfaces\IPaneApi.html*

Version: 5.0

On this page

Represents the interface for interacting with a pane in a lightweight chart.

## Type parameters[​](IPaneApi.html#type-parameters "Direct link to Type parameters")

• **HorzScaleItem**

## Methods[​](IPaneApi.html#methods "Direct link to Methods")

### getHeight()[​](IPaneApi.html#getheight "Direct link to getHeight\(\)")

> **getHeight**(): `number`

Retrieves the height of the pane in pixels.

#### Returns[​](IPaneApi.html#returns "Direct link to Returns")

`number`

The height of the pane in pixels.

* * *

### setHeight()[​](IPaneApi.html#setheight "Direct link to setHeight\(\)")

> **setHeight**(`height`): `void`

Sets the height of the pane.

#### Parameters[​](IPaneApi.html#parameters "Direct link to Parameters")

• **height** : `number`

The number of pixels to set as the height of the pane.

#### Returns[​](IPaneApi.html#returns-1 "Direct link to Returns")

`void`

* * *

### moveTo()[​](IPaneApi.html#moveto "Direct link to moveTo\(\)")

> **moveTo**(`paneIndex`): `void`

Moves the pane to a new position.

#### Parameters[​](IPaneApi.html#parameters-1 "Direct link to Parameters")

• **paneIndex** : `number`

The target index of the pane. Should be a number between 0 and the total number of panes - 1.

#### Returns[​](IPaneApi.html#returns-2 "Direct link to Returns")

`void`

* * *

### paneIndex()[​](IPaneApi.html#paneindex "Direct link to paneIndex\(\)")

> **paneIndex**(): `number`

Retrieves the index of the pane.

#### Returns[​](IPaneApi.html#returns-3 "Direct link to Returns")

`number`

The index of the pane. It is a number between 0 and the total number of panes - 1.

* * *

### getSeries()[​](IPaneApi.html#getseries "Direct link to getSeries\(\)")

> **getSeries**(): [`ISeriesApi`](ISeriesApi.md)<keyof [`SeriesOptionsMap`](SeriesOptionsMap.md), `HorzScaleItem`, [`AreaData`](AreaData.md)<`HorzScaleItem`> | [`WhitespaceData`](WhitespaceData.md)<`HorzScaleItem`> | [`BarData`](BarData.md)<`HorzScaleItem`> | [`CandlestickData`](CandlestickData.md)<`HorzScaleItem`> | [`BaselineData`](BaselineData.md)<`HorzScaleItem`> | [`LineData`](LineData.md)<`HorzScaleItem`> | [`HistogramData`](HistogramData.md)<`HorzScaleItem`> | [`CustomData`](CustomData.md)<`HorzScaleItem`> | [`CustomSeriesWhitespaceData`](CustomSeriesWhitespaceData.md)<`HorzScaleItem`>, [`CustomSeriesOptions`](../type-aliases/CustomSeriesOptions.md) | [`AreaSeriesOptions`](../type-aliases/AreaSeriesOptions.md) | [`BarSeriesOptions`](../type-aliases/BarSeriesOptions.md) | [`CandlestickSeriesOptions`](../type-aliases/CandlestickSeriesOptions.md) | [`BaselineSeriesOptions`](../type-aliases/BaselineSeriesOptions.md) | [`LineSeriesOptions`](../type-aliases/LineSeriesOptions.md) | [`HistogramSeriesOptions`](../type-aliases/HistogramSeriesOptions.md), [`DeepPartial`](../type-aliases/DeepPartial.md) <[`AreaStyleOptions`](AreaStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`BarStyleOptions`](BarStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`CandlestickStyleOptions`](CandlestickStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`BaselineStyleOptions`](BaselineStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`LineStyleOptions`](LineStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`HistogramStyleOptions`](HistogramStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`CustomStyleOptions`](CustomStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)>>[]

Retrieves the array of series for the current pane.

#### Returns[​](IPaneApi.html#returns-4 "Direct link to Returns")

[`ISeriesApi`](ISeriesApi.md)<keyof [`SeriesOptionsMap`](SeriesOptionsMap.md), `HorzScaleItem`, [`AreaData`](AreaData.md)<`HorzScaleItem`> | [`WhitespaceData`](WhitespaceData.md)<`HorzScaleItem`> | [`BarData`](BarData.md)<`HorzScaleItem`> | [`CandlestickData`](CandlestickData.md)<`HorzScaleItem`> | [`BaselineData`](BaselineData.md)<`HorzScaleItem`> | [`LineData`](LineData.md)<`HorzScaleItem`> | [`HistogramData`](HistogramData.md)<`HorzScaleItem`> | [`CustomData`](CustomData.md)<`HorzScaleItem`> | [`CustomSeriesWhitespaceData`](CustomSeriesWhitespaceData.md)<`HorzScaleItem`>, [`CustomSeriesOptions`](../type-aliases/CustomSeriesOptions.md) | [`AreaSeriesOptions`](../type-aliases/AreaSeriesOptions.md) | [`BarSeriesOptions`](../type-aliases/BarSeriesOptions.md) | [`CandlestickSeriesOptions`](../type-aliases/CandlestickSeriesOptions.md) | [`BaselineSeriesOptions`](../type-aliases/BaselineSeriesOptions.md) | [`LineSeriesOptions`](../type-aliases/LineSeriesOptions.md) | [`HistogramSeriesOptions`](../type-aliases/HistogramSeriesOptions.md), [`DeepPartial`](../type-aliases/DeepPartial.md) <[`AreaStyleOptions`](AreaStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`BarStyleOptions`](BarStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`CandlestickStyleOptions`](CandlestickStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`BaselineStyleOptions`](BaselineStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`LineStyleOptions`](LineStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`HistogramStyleOptions`](HistogramStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`CustomStyleOptions`](CustomStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)>>[]

An array of series.

* * *

### getHTMLElement()[​](IPaneApi.html#gethtmlelement "Direct link to getHTMLElement\(\)")

> **getHTMLElement**(): `HTMLElement`

Retrieves the HTML element of the pane.

#### Returns[​](IPaneApi.html#returns-5 "Direct link to Returns")

`HTMLElement`

The HTML element of the pane.

* * *

### attachPrimitive()[​](IPaneApi.html#attachprimitive "Direct link to attachPrimitive\(\)")

> **attachPrimitive**(`primitive`): `void`

Attaches additional drawing primitive to the pane

#### Parameters[​](IPaneApi.html#parameters-2 "Direct link to Parameters")

• **primitive** : [`IPanePrimitive`](../type-aliases/IPanePrimitive.md)<`HorzScaleItem`>

any implementation of IPanePrimitive interface

#### Returns[​](IPaneApi.html#returns-6 "Direct link to Returns")

`void`

* * *

### detachPrimitive()[​](IPaneApi.html#detachprimitive "Direct link to detachPrimitive\(\)")

> **detachPrimitive**(`primitive`): `void`

Detaches additional drawing primitive from the pane

#### Parameters[​](IPaneApi.html#parameters-3 "Direct link to Parameters")

• **primitive** : [`IPanePrimitive`](../type-aliases/IPanePrimitive.md)<`HorzScaleItem`>

implementation of IPanePrimitive interface attached before Does nothing if specified primitive was not attached

#### Returns[​](IPaneApi.html#returns-7 "Direct link to Returns")

`void`

* * *

### priceScale()[​](IPaneApi.html#pricescale "Direct link to priceScale\(\)")

> **priceScale**(`priceScaleId`): [`IPriceScaleApi`](IPriceScaleApi.md)

Returns the price scale with the given id.

#### Parameters[​](IPaneApi.html#parameters-4 "Direct link to Parameters")

• **priceScaleId** : `string`

ID of the price scale to find

#### Returns[​](IPaneApi.html#returns-8 "Direct link to Returns")

[`IPriceScaleApi`](IPriceScaleApi.md)

#### Throws[​](IPaneApi.html#throws "Direct link to Throws")

If the price scale with the given id is not found in this pane
