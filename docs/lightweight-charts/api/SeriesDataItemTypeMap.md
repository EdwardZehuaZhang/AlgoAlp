# API: Seriesdataitemtypemap

*Source: docs\api\interfaces\SeriesDataItemTypeMap.html*

Version: 5.0

On this page

Represents the type of data that a series contains.

For example a bar series contains [BarData](BarData.md) or [WhitespaceData](WhitespaceData.md).

## Type parameters[​](SeriesDataItemTypeMap.html#type-parameters "Direct link to Type parameters")

• **HorzScaleItem** = [`Time`](../type-aliases/Time.md)

## Properties[​](SeriesDataItemTypeMap.html#properties "Direct link to Properties")

### Bar[​](SeriesDataItemTypeMap.html#bar "Direct link to Bar")

> **Bar** : [`WhitespaceData`](WhitespaceData.md)<`HorzScaleItem`> | [`BarData`](BarData.md)<`HorzScaleItem`>

The types of bar series data.

* * *

### Candlestick[​](SeriesDataItemTypeMap.html#candlestick "Direct link to Candlestick")

> **Candlestick** : [`WhitespaceData`](WhitespaceData.md)<`HorzScaleItem`> | [`CandlestickData`](CandlestickData.md)<`HorzScaleItem`>

The types of candlestick series data.

* * *

### Area[​](SeriesDataItemTypeMap.html#area "Direct link to Area")

> **Area** : [`AreaData`](AreaData.md)<`HorzScaleItem`> | [`WhitespaceData`](WhitespaceData.md)<`HorzScaleItem`>

The types of area series data.

* * *

### Baseline[​](SeriesDataItemTypeMap.html#baseline "Direct link to Baseline")

> **Baseline** : [`WhitespaceData`](WhitespaceData.md)<`HorzScaleItem`> | [`BaselineData`](BaselineData.md)<`HorzScaleItem`>

The types of baseline series data.

* * *

### Line[​](SeriesDataItemTypeMap.html#line "Direct link to Line")

> **Line** : [`WhitespaceData`](WhitespaceData.md)<`HorzScaleItem`> | [`LineData`](LineData.md)<`HorzScaleItem`>

The types of line series data.

* * *

### Histogram[​](SeriesDataItemTypeMap.html#histogram "Direct link to Histogram")

> **Histogram** : [`WhitespaceData`](WhitespaceData.md)<`HorzScaleItem`> | [`HistogramData`](HistogramData.md)<`HorzScaleItem`>

The types of histogram series data.

* * *

### Custom[​](SeriesDataItemTypeMap.html#custom "Direct link to Custom")

> **Custom** : [`CustomData`](CustomData.md)<`HorzScaleItem`> | [`CustomSeriesWhitespaceData`](CustomSeriesWhitespaceData.md)<`HorzScaleItem`>

The base types of an custom series data.
