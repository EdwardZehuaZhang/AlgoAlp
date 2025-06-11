# API: Areadata

*Source: docs\api\interfaces\AreaData.html*

Version: 5.0

On this page

Structure describing a single item of data for area series

## Extends[​](AreaData.html#extends "Direct link to Extends")

  * [`SingleValueData`](SingleValueData.md)<`HorzScaleItem`>

## Type parameters[​](AreaData.html#type-parameters "Direct link to Type parameters")

• **HorzScaleItem** = [`Time`](../type-aliases/Time.md)

## Properties[​](AreaData.html#properties "Direct link to Properties")

### lineColor?[​](AreaData.html#linecolor "Direct link to lineColor?")

> `optional` **lineColor** : `string`

Optional line color value for certain data item. If missed, color from options is used

* * *

### topColor?[​](AreaData.html#topcolor "Direct link to topColor?")

> `optional` **topColor** : `string`

Optional top color value for certain data item. If missed, color from options is used

* * *

### bottomColor?[​](AreaData.html#bottomcolor "Direct link to bottomColor?")

> `optional` **bottomColor** : `string`

Optional bottom color value for certain data item. If missed, color from options is used

* * *

### time[​](AreaData.html#time "Direct link to time")

> **time** : `HorzScaleItem`

The time of the data.

#### Inherited from[​](AreaData.html#inherited-from "Direct link to Inherited from")

[`SingleValueData`](SingleValueData.md) . [`time`](SingleValueData.html#time)

* * *

### value[​](AreaData.html#value "Direct link to value")

> **value** : `number`

Price value of the data.

#### Inherited from[​](AreaData.html#inherited-from-1 "Direct link to Inherited from")

[`SingleValueData`](SingleValueData.md) . [`value`](SingleValueData.html#value)

* * *

### customValues?[​](AreaData.html#customvalues "Direct link to customValues?")

> `optional` **customValues** : `Record`<`string`, `unknown`>

Additional custom values which will be ignored by the library, but could be used by plugins.

#### Inherited from[​](AreaData.html#inherited-from-2 "Direct link to Inherited from")

[`SingleValueData`](SingleValueData.md) . [`customValues`](SingleValueData.html#customvalues)
