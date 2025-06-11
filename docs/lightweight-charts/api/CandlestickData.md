# API: Candlestickdata

*Source: docs\api\interfaces\CandlestickData.html*

Version: 5.0

On this page

Structure describing a single item of data for candlestick series

## Extends[​](CandlestickData.html#extends "Direct link to Extends")

  * [`OhlcData`](OhlcData.md)<`HorzScaleItem`>

## Type parameters[​](CandlestickData.html#type-parameters "Direct link to Type parameters")

• **HorzScaleItem** = [`Time`](../type-aliases/Time.md)

## Properties[​](CandlestickData.html#properties "Direct link to Properties")

### color?[​](CandlestickData.html#color "Direct link to color?")

> `optional` **color** : `string`

Optional color value for certain data item. If missed, color from options is used

* * *

### borderColor?[​](CandlestickData.html#bordercolor "Direct link to borderColor?")

> `optional` **borderColor** : `string`

Optional border color value for certain data item. If missed, color from options is used

* * *

### wickColor?[​](CandlestickData.html#wickcolor "Direct link to wickColor?")

> `optional` **wickColor** : `string`

Optional wick color value for certain data item. If missed, color from options is used

* * *

### time[​](CandlestickData.html#time "Direct link to time")

> **time** : `HorzScaleItem`

The bar time.

#### Inherited from[​](CandlestickData.html#inherited-from "Direct link to Inherited from")

[`OhlcData`](OhlcData.md) . [`time`](OhlcData.html#time)

* * *

### open[​](CandlestickData.html#open "Direct link to open")

> **open** : `number`

The open price.

#### Inherited from[​](CandlestickData.html#inherited-from-1 "Direct link to Inherited from")

[`OhlcData`](OhlcData.md) . [`open`](OhlcData.html#open)

* * *

### high[​](CandlestickData.html#high "Direct link to high")

> **high** : `number`

The high price.

#### Inherited from[​](CandlestickData.html#inherited-from-2 "Direct link to Inherited from")

[`OhlcData`](OhlcData.md) . [`high`](OhlcData.html#high)

* * *

### low[​](CandlestickData.html#low "Direct link to low")

> **low** : `number`

The low price.

#### Inherited from[​](CandlestickData.html#inherited-from-3 "Direct link to Inherited from")

[`OhlcData`](OhlcData.md) . [`low`](OhlcData.html#low)

* * *

### close[​](CandlestickData.html#close "Direct link to close")

> **close** : `number`

The close price.

#### Inherited from[​](CandlestickData.html#inherited-from-4 "Direct link to Inherited from")

[`OhlcData`](OhlcData.md) . [`close`](OhlcData.html#close)

* * *

### customValues?[​](CandlestickData.html#customvalues "Direct link to customValues?")

> `optional` **customValues** : `Record`<`string`, `unknown`>

Additional custom values which will be ignored by the library, but could be used by plugins.

#### Inherited from[​](CandlestickData.html#inherited-from-5 "Direct link to Inherited from")

[`OhlcData`](OhlcData.md) . [`customValues`](OhlcData.html#customvalues)
