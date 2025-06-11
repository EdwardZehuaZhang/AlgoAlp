# API: Ohlcdata

*Source: docs\api\interfaces\OhlcData.html*

Version: 5.0

On this page

Represents a bar with a [Time](../type-aliases/Time.md) and open, high, low, and close prices.

## Extends[​](OhlcData.html#extends "Direct link to Extends")

  * [`WhitespaceData`](WhitespaceData.md)<`HorzScaleItem`>

## Extended by[​](OhlcData.html#extended-by "Direct link to Extended by")

  * [`BarData`](BarData.md)
  * [`CandlestickData`](CandlestickData.md)

## Type parameters[​](OhlcData.html#type-parameters "Direct link to Type parameters")

• **HorzScaleItem** = [`Time`](../type-aliases/Time.md)

## Properties[​](OhlcData.html#properties "Direct link to Properties")

### time[​](OhlcData.html#time "Direct link to time")

> **time** : `HorzScaleItem`

The bar time.

#### Overrides[​](OhlcData.html#overrides "Direct link to Overrides")

[`WhitespaceData`](WhitespaceData.md) . [`time`](WhitespaceData.html#time)

* * *

### open[​](OhlcData.html#open "Direct link to open")

> **open** : `number`

The open price.

* * *

### high[​](OhlcData.html#high "Direct link to high")

> **high** : `number`

The high price.

* * *

### low[​](OhlcData.html#low "Direct link to low")

> **low** : `number`

The low price.

* * *

### close[​](OhlcData.html#close "Direct link to close")

> **close** : `number`

The close price.

* * *

### customValues?[​](OhlcData.html#customvalues "Direct link to customValues?")

> `optional` **customValues** : `Record`<`string`, `unknown`>

Additional custom values which will be ignored by the library, but could be used by plugins.

#### Inherited from[​](OhlcData.html#inherited-from "Direct link to Inherited from")

[`WhitespaceData`](WhitespaceData.md) . [`customValues`](WhitespaceData.html#customvalues)
