# API: Iseriesupdownmarkerpluginapi

*Source: docs\api\interfaces\ISeriesUpDownMarkerPluginApi.html*

Version: 5.0

On this page

UpDownMarkersPrimitive Plugin for showing the direction of price changes on the chart. This plugin can only be used with Line and Area series types.

  1. Manual control:

  * Use the `setMarkers` method to manually add markers to the chart. This will replace any existing markers.
  * Use `clearMarkers` to remove all markers.

  2. Automatic updates:

Use `setData` and `update` from this primitive instead of the those on the series to let the primitive handle the creation of price change markers automatically.

  * Use `setData` to initialize or replace all data points.
  * Use `update` to modify individual data points. This will automatically create markers for price changes on existing data points.
  * The `updateVisibilityDuration` option controls how long markers remain visible.

## Extends[​](ISeriesUpDownMarkerPluginApi.html#extends "Direct link to Extends")

  * [`ISeriesPrimitiveWrapper`](ISeriesPrimitiveWrapper.md)<`HorzScaleItem`>

## Type parameters[​](ISeriesUpDownMarkerPluginApi.html#type-parameters "Direct link to Type parameters")

• **HorzScaleItem**

• **TData** _extends_ [`SeriesDataItemTypeMap`](SeriesDataItemTypeMap.md)<`HorzScaleItem`>[[`UpDownMarkersSupportedSeriesTypes`](../type-aliases/UpDownMarkersSupportedSeriesTypes.md)] = [`SeriesDataItemTypeMap`](SeriesDataItemTypeMap.md)<`HorzScaleItem`>[`"Line"`]

## Properties[​](ISeriesUpDownMarkerPluginApi.html#properties "Direct link to Properties")

### detach()[​](ISeriesUpDownMarkerPluginApi.html#detach "Direct link to detach\(\)")

> **detach** : () => `void`

Detaches the plugin from the series.

#### Returns[​](ISeriesUpDownMarkerPluginApi.html#returns "Direct link to Returns")

`void`

#### Inherited from[​](ISeriesUpDownMarkerPluginApi.html#inherited-from "Direct link to Inherited from")

[`ISeriesPrimitiveWrapper`](ISeriesPrimitiveWrapper.md) . [`detach`](ISeriesPrimitiveWrapper.html#detach)

* * *

### getSeries()[​](ISeriesUpDownMarkerPluginApi.html#getseries "Direct link to getSeries\(\)")

> **getSeries** : () => [`ISeriesApi`](ISeriesApi.md)<keyof [`SeriesOptionsMap`](SeriesOptionsMap.md), `HorzScaleItem`, [`WhitespaceData`](WhitespaceData.md)<`HorzScaleItem`> | [`LineData`](LineData.md)<`HorzScaleItem`> | [`AreaData`](AreaData.md)<`HorzScaleItem`> | [`BarData`](BarData.md)<`HorzScaleItem`> | [`CandlestickData`](CandlestickData.md)<`HorzScaleItem`> | [`BaselineData`](BaselineData.md)<`HorzScaleItem`> | [`HistogramData`](HistogramData.md)<`HorzScaleItem`> | [`CustomData`](CustomData.md)<`HorzScaleItem`> | [`CustomSeriesWhitespaceData`](CustomSeriesWhitespaceData.md)<`HorzScaleItem`>, [`CustomSeriesOptions`](../type-aliases/CustomSeriesOptions.md) | [`AreaSeriesOptions`](../type-aliases/AreaSeriesOptions.md) | [`BarSeriesOptions`](../type-aliases/BarSeriesOptions.md) | [`CandlestickSeriesOptions`](../type-aliases/CandlestickSeriesOptions.md) | [`BaselineSeriesOptions`](../type-aliases/BaselineSeriesOptions.md) | [`LineSeriesOptions`](../type-aliases/LineSeriesOptions.md) | [`HistogramSeriesOptions`](../type-aliases/HistogramSeriesOptions.md), [`DeepPartial`](../type-aliases/DeepPartial.md) <[`AreaStyleOptions`](AreaStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`BarStyleOptions`](BarStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`CandlestickStyleOptions`](CandlestickStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`BaselineStyleOptions`](BaselineStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`LineStyleOptions`](LineStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`HistogramStyleOptions`](HistogramStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`CustomStyleOptions`](CustomStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)>>

Returns the current series.

#### Returns[​](ISeriesUpDownMarkerPluginApi.html#returns-1 "Direct link to Returns")

[`ISeriesApi`](ISeriesApi.md)<keyof [`SeriesOptionsMap`](SeriesOptionsMap.md), `HorzScaleItem`, [`WhitespaceData`](WhitespaceData.md)<`HorzScaleItem`> | [`LineData`](LineData.md)<`HorzScaleItem`> | [`AreaData`](AreaData.md)<`HorzScaleItem`> | [`BarData`](BarData.md)<`HorzScaleItem`> | [`CandlestickData`](CandlestickData.md)<`HorzScaleItem`> | [`BaselineData`](BaselineData.md)<`HorzScaleItem`> | [`HistogramData`](HistogramData.md)<`HorzScaleItem`> | [`CustomData`](CustomData.md)<`HorzScaleItem`> | [`CustomSeriesWhitespaceData`](CustomSeriesWhitespaceData.md)<`HorzScaleItem`>, [`CustomSeriesOptions`](../type-aliases/CustomSeriesOptions.md) | [`AreaSeriesOptions`](../type-aliases/AreaSeriesOptions.md) | [`BarSeriesOptions`](../type-aliases/BarSeriesOptions.md) | [`CandlestickSeriesOptions`](../type-aliases/CandlestickSeriesOptions.md) | [`BaselineSeriesOptions`](../type-aliases/BaselineSeriesOptions.md) | [`LineSeriesOptions`](../type-aliases/LineSeriesOptions.md) | [`HistogramSeriesOptions`](../type-aliases/HistogramSeriesOptions.md), [`DeepPartial`](../type-aliases/DeepPartial.md) <[`AreaStyleOptions`](AreaStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`BarStyleOptions`](BarStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`CandlestickStyleOptions`](CandlestickStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`BaselineStyleOptions`](BaselineStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`LineStyleOptions`](LineStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`HistogramStyleOptions`](HistogramStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`CustomStyleOptions`](CustomStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)>>

#### Inherited from[​](ISeriesUpDownMarkerPluginApi.html#inherited-from-1 "Direct link to Inherited from")

[`ISeriesPrimitiveWrapper`](ISeriesPrimitiveWrapper.md) . [`getSeries`](ISeriesPrimitiveWrapper.html#getseries)

* * *

### applyOptions()[​](ISeriesUpDownMarkerPluginApi.html#applyoptions "Direct link to applyOptions\(\)")

> **applyOptions** : (`options`) => `void`

Applies new options to the plugin.

#### Parameters[​](ISeriesUpDownMarkerPluginApi.html#parameters "Direct link to Parameters")

• **options** : `Partial` <[`UpDownMarkersPluginOptions`](UpDownMarkersPluginOptions.md)>

Partial options to apply.

#### Returns[​](ISeriesUpDownMarkerPluginApi.html#returns-2 "Direct link to Returns")

`void`

#### Overrides[​](ISeriesUpDownMarkerPluginApi.html#overrides "Direct link to Overrides")

[`ISeriesPrimitiveWrapper`](ISeriesPrimitiveWrapper.md) . [`applyOptions`](ISeriesPrimitiveWrapper.html#applyoptions)

* * *

### setData()[​](ISeriesUpDownMarkerPluginApi.html#setdata "Direct link to setData\(\)")

> **setData** : (`data`) => `void`

Sets the data for the series and manages data points for marker updates.

#### Parameters[​](ISeriesUpDownMarkerPluginApi.html#parameters-1 "Direct link to Parameters")

• **data** : `TData`[]

Array of data points to set.

#### Returns[​](ISeriesUpDownMarkerPluginApi.html#returns-3 "Direct link to Returns")

`void`

* * *

### update()[​](ISeriesUpDownMarkerPluginApi.html#update "Direct link to update\(\)")

> **update** : (`data`, `historicalUpdate`?) => `void`

Updates a single data point and manages marker updates for existing data points.

#### Parameters[​](ISeriesUpDownMarkerPluginApi.html#parameters-2 "Direct link to Parameters")

• **data** : `TData`

The data point to update.

• **historicalUpdate?** : `boolean`

Optional flag for historical updates.

#### Returns[​](ISeriesUpDownMarkerPluginApi.html#returns-4 "Direct link to Returns")

`void`

* * *

### markers()[​](ISeriesUpDownMarkerPluginApi.html#markers "Direct link to markers\(\)")

> **markers** : () => readonly [`SeriesUpDownMarker`](SeriesUpDownMarker.md)<`HorzScaleItem`>[]

Retrieves the current markers on the chart.

#### Returns[​](ISeriesUpDownMarkerPluginApi.html#returns-5 "Direct link to Returns")

readonly [`SeriesUpDownMarker`](SeriesUpDownMarker.md)<`HorzScaleItem`>[]

* * *

### setMarkers()[​](ISeriesUpDownMarkerPluginApi.html#setmarkers "Direct link to setMarkers\(\)")

> **setMarkers** : (`markers`) => `void`

Manually sets markers on the chart.

#### Parameters[​](ISeriesUpDownMarkerPluginApi.html#parameters-3 "Direct link to Parameters")

• **markers** : [`SeriesUpDownMarker`](SeriesUpDownMarker.md)<`HorzScaleItem`>[]

Array of SeriesUpDownMarker to set.

#### Returns[​](ISeriesUpDownMarkerPluginApi.html#returns-6 "Direct link to Returns")

`void`

* * *

### clearMarkers()[​](ISeriesUpDownMarkerPluginApi.html#clearmarkers "Direct link to clearMarkers\(\)")

> **clearMarkers** : () => `void`

Clears all markers from the chart.

#### Returns[​](ISeriesUpDownMarkerPluginApi.html#returns-7 "Direct link to Returns")

`void`
