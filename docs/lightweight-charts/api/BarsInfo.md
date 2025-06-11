# API: Barsinfo

*Source: docs\api\interfaces\BarsInfo.html*

Version: 5.0

On this page

Represents a range of bars and the number of bars outside the range.

## Extends[​](BarsInfo.html#extends "Direct link to Extends")

  * `Partial` <[`IRange`](IRange.md)<`HorzScaleItem`>>

## Type parameters[​](BarsInfo.html#type-parameters "Direct link to Type parameters")

• **HorzScaleItem**

## Properties[​](BarsInfo.html#properties "Direct link to Properties")

### barsBefore[​](BarsInfo.html#barsbefore "Direct link to barsBefore")

> **barsBefore** : `number`

The number of bars before the start of the range. Positive value means that there are some bars before (out of logical range from the left) the [IRange.from](IRange.html#from) logical index in the series. Negative value means that the first series' bar is inside the passed logical range, and between the first series' bar and the [IRange.from](IRange.html#from) logical index are some bars.

* * *

### barsAfter[​](BarsInfo.html#barsafter "Direct link to barsAfter")

> **barsAfter** : `number`

The number of bars after the end of the range. Positive value in the `barsAfter` field means that there are some bars after (out of logical range from the right) the [IRange.to](IRange.html#to) logical index in the series. Negative value means that the last series' bar is inside the passed logical range, and between the last series' bar and the [IRange.to](IRange.html#to) logical index are some bars.

* * *

### from?[​](BarsInfo.html#from "Direct link to from?")

> `optional` **from** : `HorzScaleItem`

The from value. The start of the range.

#### Inherited from[​](BarsInfo.html#inherited-from "Direct link to Inherited from")

`Partial.from`

* * *

### to?[​](BarsInfo.html#to "Direct link to to?")

> `optional` **to** : `HorzScaleItem`

The to value. The end of the range.

#### Inherited from[​](BarsInfo.html#inherited-from-1 "Direct link to Inherited from")

`Partial.to`
