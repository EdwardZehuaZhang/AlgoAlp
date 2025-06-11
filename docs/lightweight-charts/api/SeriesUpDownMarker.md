# API: Seriesupdownmarker

*Source: docs\api\interfaces\SeriesUpDownMarker.html*

Version: 5.0

On this page

Represents a marker drawn above or below a data point to indicate a price change update.

## Type parameters[​](SeriesUpDownMarker.html#type-parameters "Direct link to Type parameters")

• **T** = [`Time`](../type-aliases/Time.md)

The type of the time value, defaults to Time.

## Properties[​](SeriesUpDownMarker.html#properties "Direct link to Properties")

### time[​](SeriesUpDownMarker.html#time "Direct link to time")

> **time** : `T`

The point on the horizontal scale.

* * *

### value[​](SeriesUpDownMarker.html#value "Direct link to value")

> **value** : `number`

The price value for the data point.

* * *

### sign[​](SeriesUpDownMarker.html#sign "Direct link to sign")

> **sign** : [`MarkerSign`](../enumerations/MarkerSign.md)

The direction of the price change.
