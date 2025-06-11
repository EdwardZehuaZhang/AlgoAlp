# API: Mouseeventparams

*Source: docs\api\interfaces\MouseEventParams.html*

Version: 5.0

On this page

Represents a mouse event.

## Type parameters[​](MouseEventParams.html#type-parameters "Direct link to Type parameters")

• **HorzScaleItem** = [`Time`](../type-aliases/Time.md)

## Properties[​](MouseEventParams.html#properties "Direct link to Properties")

### time?[​](MouseEventParams.html#time "Direct link to time?")

> `optional` **time** : `HorzScaleItem`

Time of the data at the location of the mouse event.

The value will be `undefined` if the location of the event in the chart is outside the range of available data.

* * *

### logical?[​](MouseEventParams.html#logical "Direct link to logical?")

> `optional` **logical** : [`Logical`](../type-aliases/Logical.md)

Logical index

* * *

### point?[​](MouseEventParams.html#point "Direct link to point?")

> `optional` **point** : [`Point`](Point.md)

Location of the event in the chart.

The value will be `undefined` if the event is fired outside the chart, for example a mouse leave event.

* * *

### paneIndex?[​](MouseEventParams.html#paneindex "Direct link to paneIndex?")

> `optional` **paneIndex** : `number`

The index of the Pane

* * *

### seriesData[​](MouseEventParams.html#seriesdata "Direct link to seriesData")

> **seriesData** : `Map` <[`ISeriesApi`](ISeriesApi.md)<keyof [`SeriesOptionsMap`](SeriesOptionsMap.md), `HorzScaleItem`, [`AreaData`](AreaData.md)<`HorzScaleItem`> | [`WhitespaceData`](WhitespaceData.md)<`HorzScaleItem`> | [`BarData`](BarData.md)<`HorzScaleItem`> | [`CandlestickData`](CandlestickData.md)<`HorzScaleItem`> | [`BaselineData`](BaselineData.md)<`HorzScaleItem`> | [`LineData`](LineData.md)<`HorzScaleItem`> | [`HistogramData`](HistogramData.md)<`HorzScaleItem`> | [`CustomData`](CustomData.md)<`HorzScaleItem`> | [`CustomSeriesWhitespaceData`](CustomSeriesWhitespaceData.md)<`HorzScaleItem`>, [`CustomSeriesOptions`](../type-aliases/CustomSeriesOptions.md) | [`AreaSeriesOptions`](../type-aliases/AreaSeriesOptions.md) | [`BarSeriesOptions`](../type-aliases/BarSeriesOptions.md) | [`CandlestickSeriesOptions`](../type-aliases/CandlestickSeriesOptions.md) | [`BaselineSeriesOptions`](../type-aliases/BaselineSeriesOptions.md) | [`LineSeriesOptions`](../type-aliases/LineSeriesOptions.md) | [`HistogramSeriesOptions`](../type-aliases/HistogramSeriesOptions.md), [`DeepPartial`](../type-aliases/DeepPartial.md) <[`AreaStyleOptions`](AreaStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`BarStyleOptions`](BarStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`CandlestickStyleOptions`](CandlestickStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`BaselineStyleOptions`](BaselineStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`LineStyleOptions`](LineStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`HistogramStyleOptions`](HistogramStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`CustomStyleOptions`](CustomStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)>>, [`BarData`](BarData.md)<`HorzScaleItem`> | [`LineData`](LineData.md)<`HorzScaleItem`> | [`HistogramData`](HistogramData.md)<`HorzScaleItem`> | [`CustomData`](CustomData.md)<`HorzScaleItem`>>

Data of all series at the location of the event in the chart.

Keys of the map are [ISeriesApi](ISeriesApi.md) instances. Values are prices. Values of the map are original data items

* * *

### hoveredSeries?[​](MouseEventParams.html#hoveredseries "Direct link to hoveredSeries?")

> `optional` **hoveredSeries** : [`ISeriesApi`](ISeriesApi.md)<keyof [`SeriesOptionsMap`](SeriesOptionsMap.md), `HorzScaleItem`, [`AreaData`](AreaData.md)<`HorzScaleItem`> | [`WhitespaceData`](WhitespaceData.md)<`HorzScaleItem`> | [`BarData`](BarData.md)<`HorzScaleItem`> | [`CandlestickData`](CandlestickData.md)<`HorzScaleItem`> | [`BaselineData`](BaselineData.md)<`HorzScaleItem`> | [`LineData`](LineData.md)<`HorzScaleItem`> | [`HistogramData`](HistogramData.md)<`HorzScaleItem`> | [`CustomData`](CustomData.md)<`HorzScaleItem`> | [`CustomSeriesWhitespaceData`](CustomSeriesWhitespaceData.md)<`HorzScaleItem`>, [`CustomSeriesOptions`](../type-aliases/CustomSeriesOptions.md) | [`AreaSeriesOptions`](../type-aliases/AreaSeriesOptions.md) | [`BarSeriesOptions`](../type-aliases/BarSeriesOptions.md) | [`CandlestickSeriesOptions`](../type-aliases/CandlestickSeriesOptions.md) | [`BaselineSeriesOptions`](../type-aliases/BaselineSeriesOptions.md) | [`LineSeriesOptions`](../type-aliases/LineSeriesOptions.md) | [`HistogramSeriesOptions`](../type-aliases/HistogramSeriesOptions.md), [`DeepPartial`](../type-aliases/DeepPartial.md) <[`AreaStyleOptions`](AreaStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`BarStyleOptions`](BarStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`CandlestickStyleOptions`](CandlestickStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`BaselineStyleOptions`](BaselineStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`LineStyleOptions`](LineStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`HistogramStyleOptions`](HistogramStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)> | [`DeepPartial`](../type-aliases/DeepPartial.md) <[`CustomStyleOptions`](CustomStyleOptions.md) & [`SeriesOptionsCommon`](SeriesOptionsCommon.md)>>

The [ISeriesApi](ISeriesApi.md) for the series at the point of the mouse event.

* * *

### hoveredObjectId?[​](MouseEventParams.html#hoveredobjectid "Direct link to hoveredObjectId?")

> `optional` **hoveredObjectId** : `unknown`

The ID of the object at the point of the mouse event.

* * *

### sourceEvent?[​](MouseEventParams.html#sourceevent "Direct link to sourceEvent?")

> `optional` **sourceEvent** : [`TouchMouseEventData`](TouchMouseEventData.md)

The underlying source mouse or touch event data, if available
