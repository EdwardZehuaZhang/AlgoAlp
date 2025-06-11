# API: Baselinedata

*Source: docs\api\interfaces\BaselineData.html*

Version: 5.0

On this page

Structure describing a single item of data for baseline series

## Extends[​](BaselineData.html#extends "Direct link to Extends")

  * [`SingleValueData`](SingleValueData.md)<`HorzScaleItem`>

## Type parameters[​](BaselineData.html#type-parameters "Direct link to Type parameters")

• **HorzScaleItem** = [`Time`](../type-aliases/Time.md)

## Properties[​](BaselineData.html#properties "Direct link to Properties")

### topFillColor1?[​](BaselineData.html#topfillcolor1 "Direct link to topFillColor1?")

> `optional` **topFillColor1** : `string`

Optional top area top fill color value for certain data item. If missed, color from options is used

* * *

### topFillColor2?[​](BaselineData.html#topfillcolor2 "Direct link to topFillColor2?")

> `optional` **topFillColor2** : `string`

Optional top area bottom fill color value for certain data item. If missed, color from options is used

* * *

### topLineColor?[​](BaselineData.html#toplinecolor "Direct link to topLineColor?")

> `optional` **topLineColor** : `string`

Optional top area line color value for certain data item. If missed, color from options is used

* * *

### bottomFillColor1?[​](BaselineData.html#bottomfillcolor1 "Direct link to bottomFillColor1?")

> `optional` **bottomFillColor1** : `string`

Optional bottom area top fill color value for certain data item. If missed, color from options is used

* * *

### bottomFillColor2?[​](BaselineData.html#bottomfillcolor2 "Direct link to bottomFillColor2?")

> `optional` **bottomFillColor2** : `string`

Optional bottom area bottom fill color value for certain data item. If missed, color from options is used

* * *

### bottomLineColor?[​](BaselineData.html#bottomlinecolor "Direct link to bottomLineColor?")

> `optional` **bottomLineColor** : `string`

Optional bottom area line color value for certain data item. If missed, color from options is used

* * *

### time[​](BaselineData.html#time "Direct link to time")

> **time** : `HorzScaleItem`

The time of the data.

#### Inherited from[​](BaselineData.html#inherited-from "Direct link to Inherited from")

[`SingleValueData`](SingleValueData.md) . [`time`](SingleValueData.html#time)

* * *

### value[​](BaselineData.html#value "Direct link to value")

> **value** : `number`

Price value of the data.

#### Inherited from[​](BaselineData.html#inherited-from-1 "Direct link to Inherited from")

[`SingleValueData`](SingleValueData.md) . [`value`](SingleValueData.html#value)

* * *

### customValues?[​](BaselineData.html#customvalues "Direct link to customValues?")

> `optional` **customValues** : `Record`<`string`, `unknown`>

Additional custom values which will be ignored by the library, but could be used by plugins.

#### Inherited from[​](BaselineData.html#inherited-from-2 "Direct link to Inherited from")

[`SingleValueData`](SingleValueData.md) . [`customValues`](SingleValueData.html#customvalues)
