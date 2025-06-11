# API: Seriesattachedparameter

*Source: docs\api\interfaces\SeriesAttachedParameter.html*

Version: 5.0

On this page

Object containing references to the chart and series instances, and a requestUpdate method for triggering a refresh of the chart.

## Type parameters[​](SeriesAttachedParameter.html#type-parameters "Direct link to Type parameters")

• **HorzScaleItem** = [`Time`](../type-aliases/Time.md)

• **TSeriesType** _extends_ [`SeriesType`](../type-aliases/SeriesType.md) = keyof [`SeriesOptionsMap`](SeriesOptionsMap.md)

## Properties[​](SeriesAttachedParameter.html#properties "Direct link to Properties")

### chart[​](SeriesAttachedParameter.html#chart "Direct link to chart")

> **chart** : [`IChartApiBase`](IChartApiBase.md)<`HorzScaleItem`>

Chart instance.

* * *

### series[​](SeriesAttachedParameter.html#series "Direct link to series")

> **series** : [`ISeriesApi`](ISeriesApi.md)<`TSeriesType`, `HorzScaleItem`, [`SeriesDataItemTypeMap`](SeriesDataItemTypeMap.md)<`HorzScaleItem`>[`TSeriesType`], [`SeriesOptionsMap`](SeriesOptionsMap.md)[`TSeriesType`], [`SeriesPartialOptionsMap`](SeriesPartialOptionsMap.md)[`TSeriesType`]>

Series to which the Primitive is attached.

* * *

### requestUpdate()[​](SeriesAttachedParameter.html#requestupdate "Direct link to requestUpdate\(\)")

> **requestUpdate** : () => `void`

Request an update (redraw the chart)

#### Returns[​](SeriesAttachedParameter.html#returns "Direct link to Returns")

`void`

* * *

### horzScaleBehavior[​](SeriesAttachedParameter.html#horzscalebehavior "Direct link to horzScaleBehavior")

> **horzScaleBehavior** : [`IHorzScaleBehavior`](IHorzScaleBehavior.md)<`HorzScaleItem`>

Horizontal Scale Behaviour for the chart.
