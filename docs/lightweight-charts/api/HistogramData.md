# API: Histogramdata

*Source: docs\api\interfaces\HistogramData.html*

Version: 5.0

On this page

Structure describing a single item of data for histogram series

## Extends[​](HistogramData.html#extends "Direct link to Extends")

  * [`SingleValueData`](SingleValueData.md)<`HorzScaleItem`>

## Type parameters[​](HistogramData.html#type-parameters "Direct link to Type parameters")

• **HorzScaleItem** = [`Time`](../type-aliases/Time.md)

## Properties[​](HistogramData.html#properties "Direct link to Properties")

### color?[​](HistogramData.html#color "Direct link to color?")

> `optional` **color** : `string`

Optional color value for certain data item. If missed, color from options is used

* * *

### time[​](HistogramData.html#time "Direct link to time")

> **time** : `HorzScaleItem`

The time of the data.

#### Inherited from[​](HistogramData.html#inherited-from "Direct link to Inherited from")

[`SingleValueData`](SingleValueData.md) . [`time`](SingleValueData.html#time)

* * *

### value[​](HistogramData.html#value "Direct link to value")

> **value** : `number`

Price value of the data.

#### Inherited from[​](HistogramData.html#inherited-from-1 "Direct link to Inherited from")

[`SingleValueData`](SingleValueData.md) . [`value`](SingleValueData.html#value)

* * *

### customValues?[​](HistogramData.html#customvalues "Direct link to customValues?")

> `optional` **customValues** : `Record`<`string`, `unknown`>

Additional custom values which will be ignored by the library, but could be used by plugins.

#### Inherited from[​](HistogramData.html#inherited-from-2 "Direct link to Inherited from")

[`SingleValueData`](SingleValueData.md) . [`customValues`](SingleValueData.html#customvalues)
