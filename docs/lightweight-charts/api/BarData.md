# API: Bardata

*Source: docs\api\interfaces\BarData.html*

Version: 5.0

On this page

Structure describing a single item of data for bar series

## Extends[​](BarData.html#extends "Direct link to Extends")

  * [`OhlcData`](OhlcData.md)<`HorzScaleItem`>

## Type parameters[​](BarData.html#type-parameters "Direct link to Type parameters")

• **HorzScaleItem** = [`Time`](../type-aliases/Time.md)

## Properties[​](BarData.html#properties "Direct link to Properties")

### color?[​](BarData.html#color "Direct link to color?")

> `optional` **color** : `string`

Optional color value for certain data item. If missed, color from options is used

* * *

### time[​](BarData.html#time "Direct link to time")

> **time** : `HorzScaleItem`

The bar time.

#### Inherited from[​](BarData.html#inherited-from "Direct link to Inherited from")

[`OhlcData`](OhlcData.md) . [`time`](OhlcData.html#time)

* * *

### open[​](BarData.html#open "Direct link to open")

> **open** : `number`

The open price.

#### Inherited from[​](BarData.html#inherited-from-1 "Direct link to Inherited from")

[`OhlcData`](OhlcData.md) . [`open`](OhlcData.html#open)

* * *

### high[​](BarData.html#high "Direct link to high")

> **high** : `number`

The high price.

#### Inherited from[​](BarData.html#inherited-from-2 "Direct link to Inherited from")

[`OhlcData`](OhlcData.md) . [`high`](OhlcData.html#high)

* * *

### low[​](BarData.html#low "Direct link to low")

> **low** : `number`

The low price.

#### Inherited from[​](BarData.html#inherited-from-3 "Direct link to Inherited from")

[`OhlcData`](OhlcData.md) . [`low`](OhlcData.html#low)

* * *

### close[​](BarData.html#close "Direct link to close")

> **close** : `number`

The close price.

#### Inherited from[​](BarData.html#inherited-from-4 "Direct link to Inherited from")

[`OhlcData`](OhlcData.md) . [`close`](OhlcData.html#close)

* * *

### customValues?[​](BarData.html#customvalues "Direct link to customValues?")

> `optional` **customValues** : `Record`<`string`, `unknown`>

Additional custom values which will be ignored by the library, but could be used by plugins.

#### Inherited from[​](BarData.html#inherited-from-5 "Direct link to Inherited from")

[`OhlcData`](OhlcData.md) . [`customValues`](OhlcData.html#customvalues)
