# API: Singlevaluedata

*Source: docs\api\interfaces\SingleValueData.html*

Version: 5.0

On this page

A base interface for a data point of single-value series.

## Extends[​](SingleValueData.html#extends "Direct link to Extends")

  * [`WhitespaceData`](WhitespaceData.md)<`HorzScaleItem`>

## Extended by[​](SingleValueData.html#extended-by "Direct link to Extended by")

  * [`AreaData`](AreaData.md)
  * [`BaselineData`](BaselineData.md)
  * [`HistogramData`](HistogramData.md)
  * [`LineData`](LineData.md)

## Type parameters[​](SingleValueData.html#type-parameters "Direct link to Type parameters")

• **HorzScaleItem** = [`Time`](../type-aliases/Time.md)

## Properties[​](SingleValueData.html#properties "Direct link to Properties")

### time[​](SingleValueData.html#time "Direct link to time")

> **time** : `HorzScaleItem`

The time of the data.

#### Overrides[​](SingleValueData.html#overrides "Direct link to Overrides")

[`WhitespaceData`](WhitespaceData.md) . [`time`](WhitespaceData.html#time)

* * *

### value[​](SingleValueData.html#value "Direct link to value")

> **value** : `number`

Price value of the data.

* * *

### customValues?[​](SingleValueData.html#customvalues "Direct link to customValues?")

> `optional` **customValues** : `Record`<`string`, `unknown`>

Additional custom values which will be ignored by the library, but could be used by plugins.

#### Inherited from[​](SingleValueData.html#inherited-from "Direct link to Inherited from")

[`WhitespaceData`](WhitespaceData.md) . [`customValues`](WhitespaceData.html#customvalues)
