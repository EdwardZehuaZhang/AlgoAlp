# API: Iseriesmarkerspluginapi

*Source: docs\api\interfaces\ISeriesMarkersPluginApi.html*

Version: 5.0

On this page

Interface for a series markers plugin

## Extends[​](ISeriesMarkersPluginApi.html#extends "Direct link to Extends")

  * [`ISeriesPrimitiveWrapper`](ISeriesPrimitiveWrapper.md)<`HorzScaleItem`>

## Type parameters[​](ISeriesMarkersPluginApi.html#type-parameters "Direct link to Type parameters")

• **HorzScaleItem**

## Properties[​](ISeriesMarkersPluginApi.html#properties "Direct link to Properties")

### setMarkers()[​](ISeriesMarkersPluginApi.html#setmarkers "Direct link to setMarkers\(\)")

> **setMarkers** : (`markers`) => `void`

Set markers to the series.

#### Parameters[​](ISeriesMarkersPluginApi.html#parameters "Direct link to Parameters")

• **markers** : [`SeriesMarker`](../type-aliases/SeriesMarker.md)<`HorzScaleItem`>[]

An array of markers to be displayed on the series.

#### Returns[​](ISeriesMarkersPluginApi.html#returns "Direct link to Returns")

`void`

* * *

### markers()[​](ISeriesMarkersPluginApi.html#markers "Direct link to markers\(\)")

> **markers** : () => readonly [`SeriesMarker`](../type-aliases/SeriesMarker.md)<`HorzScaleItem`>[]

Returns current markers.

#### Returns[​](ISeriesMarkersPluginApi.html#returns-1 "Direct link to Returns")

readonly [`SeriesMarker`](../type-aliases/SeriesMarker.md)<`HorzScaleItem`>[]

* * *

### detach()[​](ISeriesMarkersPluginApi.html#detach "Direct link to detach\(\)")

> **detach** : () => `void`

Detaches the plugin from the series.

#### Returns[​](ISeriesMarkersPluginApi.html#returns-2 "Direct link to Returns")

`void`

#### Overrides[​](ISeriesMarkersPluginApi.html#overrides "Direct link to Overrides")

[`ISeriesPrimitiveWrapper`](ISeriesPrimitiveWrapper.md) . [`detach`](ISeriesPrimitiveWrapper.html#detach)

* * *

### getSeries()[​](ISeriesMarkersPluginApi.html#getseries "Direct link to getSeries\(\)")

> **getSeries** : () => [`ISeriesApi`](ISeriesApi.md)<keyof [`SeriesOptionsMap`](SeriesOptionsMap.md), `HorzScaleItem`, [`AreaData`](AreaData.md)<`HorzScaleItem`> | [`WhitespaceData`](WhitespaceData.md)<`HorzScaleItem`> | [`BarData`](BarData.md)<`HorzScaleItem`> | [`CandlestickData`](CandlestickData.md)<`HorzScaleItem`> | [`BaselineData`](BaselineData.md)<`HorzScaleItem`> | [`LineData`](LineData.md)<`HorzScaleItem`> | [`HistogramData`](HistogramData.md)<`HorzScaleItem`> | [`CustomData`](CustomData.md)<`HorzScaleItem`> | [`CustomSeriesWhitespaceData`](CustomSeriesWhitespaceData.md)<`HorzScaleItem`>, [`CustomSeriesOptions`](../type-aliases/CustomSeriesOptions.md) | [`AreaSeriesOptions`](../type-aliases/AreaSeriesOptions.md) | [`BarSeriesOptions`](../type-aliases/BarSeriesOptions.md) | [`CandlestickSeriesOptions`](../type-aliases/CandlestickSeriesOptions.md) | [`BaselineSeriesOptions`](../type-aliases/BaselineSeriesOptions.md) | [`LineSeriesOptions`](../type-aliases/LineSeriesOptions.md) | [`HistogramSeriesOptions`](../type-aliases/HistogramSeriesOptions.md), [`DeepPartial`](../type-aliases/DeepPartial.md) <[`AreaStyleOptions`](AreaStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`BarStyleOptions`](BarStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`CandlestickStyleOptions`](CandlestickStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`BaselineStyleOptions`](BaselineStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`LineStyleOptions`](LineStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`HistogramStyleOptions`](HistogramStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`CustomStyleOptions`](CustomStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)>>

Returns the current series.

#### Returns[​](ISeriesMarkersPluginApi.html#returns-3 "Direct link to Returns")

[`ISeriesApi`](ISeriesApi.md)<keyof [`SeriesOptionsMap`](SeriesOptionsMap.md), `HorzScaleItem`, [`AreaData`](AreaData.md)<`HorzScaleItem`> | [`WhitespaceData`](WhitespaceData.md)<`HorzScaleItem`> | [`BarData`](BarData.md)<`HorzScaleItem`> | [`CandlestickData`](CandlestickData.md)<`HorzScaleItem`> | [`BaselineData`](BaselineData.md)<`HorzScaleItem`> | [`LineData`](LineData.md)<`HorzScaleItem`> | [`HistogramData`](HistogramData.md)<`HorzScaleItem`> | [`CustomData`](CustomData.md)<`HorzScaleItem`> | [`CustomSeriesWhitespaceData`](CustomSeriesWhitespaceData.md)<`HorzScaleItem`>, [`CustomSeriesOptions`](../type-aliases/CustomSeriesOptions.md) | [`AreaSeriesOptions`](../type-aliases/AreaSeriesOptions.md) | [`BarSeriesOptions`](../type-aliases/BarSeriesOptions.md) | [`CandlestickSeriesOptions`](../type-aliases/CandlestickSeriesOptions.md) | [`BaselineSeriesOptions`](../type-aliases/BaselineSeriesOptions.md) | [`LineSeriesOptions`](../type-aliases/LineSeriesOptions.md) | [`HistogramSeriesOptions`](../type-aliases/HistogramSeriesOptions.md), [`DeepPartial`](../type-aliases/DeepPartial.md) <[`AreaStyleOptions`](AreaStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`BarStyleOptions`](BarStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`CandlestickStyleOptions`](CandlestickStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`BaselineStyleOptions`](BaselineStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`LineStyleOptions`](LineStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`HistogramStyleOptions`](HistogramStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`CustomStyleOptions`](CustomStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)>>

#### Inherited from[​](ISeriesMarkersPluginApi.html#inherited-from "Direct link to Inherited from")

[`ISeriesPrimitiveWrapper`](ISeriesPrimitiveWrapper.md) . [`getSeries`](ISeriesPrimitiveWrapper.html#getseries)

* * *

### applyOptions()?[​](ISeriesMarkersPluginApi.html#applyoptions "Direct link to applyOptions\(\)?")

> `optional` **applyOptions** : (`options`) => `void`

Applies options to the primitive.

#### Parameters[​](ISeriesMarkersPluginApi.html#parameters-1 "Direct link to Parameters")

• **options** : [`DeepPartial`](../type-aliases/DeepPartial.md)<`unknown`>

Options to apply. The options are deeply merged with the current options.

#### Returns[​](ISeriesMarkersPluginApi.html#returns-4 "Direct link to Returns")

`void`

#### Inherited from[​](ISeriesMarkersPluginApi.html#inherited-from-1 "Direct link to Inherited from")

[`ISeriesPrimitiveWrapper`](ISeriesPrimitiveWrapper.md) . [`applyOptions`](ISeriesPrimitiveWrapper.html#applyoptions)
