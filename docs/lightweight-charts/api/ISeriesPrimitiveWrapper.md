# API: Iseriesprimitivewrapper

*Source: docs\api\interfaces\ISeriesPrimitiveWrapper.html*

Version: 5.0

On this page

Interface for a series primitive.

## Extended by[​](ISeriesPrimitiveWrapper.html#extended-by "Direct link to Extended by")

  * [`ISeriesMarkersPluginApi`](ISeriesMarkersPluginApi.md)
  * [`ISeriesUpDownMarkerPluginApi`](ISeriesUpDownMarkerPluginApi.md)

## Type parameters[​](ISeriesPrimitiveWrapper.html#type-parameters "Direct link to Type parameters")

• **T**

• **Options** = `unknown`

## Properties[​](ISeriesPrimitiveWrapper.html#properties "Direct link to Properties")

### detach()[​](ISeriesPrimitiveWrapper.html#detach "Direct link to detach\(\)")

> **detach** : () => `void`

Detaches the plugin from the series.

#### Returns[​](ISeriesPrimitiveWrapper.html#returns "Direct link to Returns")

`void`

* * *

### getSeries()[​](ISeriesPrimitiveWrapper.html#getseries "Direct link to getSeries\(\)")

> **getSeries** : () => [`ISeriesApi`](ISeriesApi.md)<keyof [`SeriesOptionsMap`](SeriesOptionsMap.md), `T`, [`AreaData`](AreaData.md)<`T`> | [`WhitespaceData`](WhitespaceData.md)<`T`> | [`BarData`](BarData.md)<`T`> | [`CandlestickData`](CandlestickData.md)<`T`> | [`BaselineData`](BaselineData.md)<`T`> | [`LineData`](LineData.md)<`T`> | [`HistogramData`](HistogramData.md)<`T`> | [`CustomData`](CustomData.md)<`T`> | [`CustomSeriesWhitespaceData`](CustomSeriesWhitespaceData.md)<`T`>, [`CustomSeriesOptions`](../type-aliases/CustomSeriesOptions.md) | [`AreaSeriesOptions`](../type-aliases/AreaSeriesOptions.md) | [`BarSeriesOptions`](../type-aliases/BarSeriesOptions.md) | [`CandlestickSeriesOptions`](../type-aliases/CandlestickSeriesOptions.md) | [`BaselineSeriesOptions`](../type-aliases/BaselineSeriesOptions.md) | [`LineSeriesOptions`](../type-aliases/LineSeriesOptions.md) | [`HistogramSeriesOptions`](../type-aliases/HistogramSeriesOptions.md), [`DeepPartial`](../type-aliases/DeepPartial.md) <[`AreaStyleOptions`](AreaStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`BarStyleOptions`](BarStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`CandlestickStyleOptions`](CandlestickStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`BaselineStyleOptions`](BaselineStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`LineStyleOptions`](LineStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`HistogramStyleOptions`](HistogramStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`CustomStyleOptions`](CustomStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)>>

Returns the current series.

#### Returns[​](ISeriesPrimitiveWrapper.html#returns-1 "Direct link to Returns")

[`ISeriesApi`](ISeriesApi.md)<keyof [`SeriesOptionsMap`](SeriesOptionsMap.md), `T`, [`AreaData`](AreaData.md)<`T`> | [`WhitespaceData`](WhitespaceData.md)<`T`> | [`BarData`](BarData.md)<`T`> | [`CandlestickData`](CandlestickData.md)<`T`> | [`BaselineData`](BaselineData.md)<`T`> | [`LineData`](LineData.md)<`T`> | [`HistogramData`](HistogramData.md)<`T`> | [`CustomData`](CustomData.md)<`T`> | [`CustomSeriesWhitespaceData`](CustomSeriesWhitespaceData.md)<`T`>, [`CustomSeriesOptions`](../type-aliases/CustomSeriesOptions.md) | [`AreaSeriesOptions`](../type-aliases/AreaSeriesOptions.md) | [`BarSeriesOptions`](../type-aliases/BarSeriesOptions.md) | [`CandlestickSeriesOptions`](../type-aliases/CandlestickSeriesOptions.md) | [`BaselineSeriesOptions`](../type-aliases/BaselineSeriesOptions.md) | [`LineSeriesOptions`](../type-aliases/LineSeriesOptions.md) | [`HistogramSeriesOptions`](../type-aliases/HistogramSeriesOptions.md), [`DeepPartial`](../type-aliases/DeepPartial.md) <[`AreaStyleOptions`](AreaStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`BarStyleOptions`](BarStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`CandlestickStyleOptions`](CandlestickStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`BaselineStyleOptions`](BaselineStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`LineStyleOptions`](LineStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`HistogramStyleOptions`](HistogramStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`CustomStyleOptions`](CustomStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)>>

* * *

### applyOptions()?[​](ISeriesPrimitiveWrapper.html#applyoptions "Direct link to applyOptions\(\)?")

> `optional` **applyOptions** : (`options`) => `void`

Applies options to the primitive.

#### Parameters[​](ISeriesPrimitiveWrapper.html#parameters "Direct link to Parameters")

• **options** : [`DeepPartial`](../type-aliases/DeepPartial.md)<`Options`>

Options to apply. The options are deeply merged with the current options.

#### Returns[​](ISeriesPrimitiveWrapper.html#returns-2 "Direct link to Returns")

`void`
