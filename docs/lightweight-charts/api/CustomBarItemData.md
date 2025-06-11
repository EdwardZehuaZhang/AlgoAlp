# API: Custombaritemdata

*Source: docs\api\interfaces\CustomBarItemData.html*

Version: 5.0

On this page

Renderer data for an item within the custom series.

## Type parameters[​](CustomBarItemData.html#type-parameters "Direct link to Type parameters")

• **HorzScaleItem**

• **TData** _extends_ [`CustomData`](CustomData.md)<`HorzScaleItem`> = [`CustomData`](CustomData.md)<`HorzScaleItem`>

## Properties[​](CustomBarItemData.html#properties "Direct link to Properties")

### x[​](CustomBarItemData.html#x "Direct link to x")

> **x** : `number`

Horizontal coordinate for the item. Measured from the left edge of the pane in pixels.

* * *

### time[​](CustomBarItemData.html#time "Direct link to time")

> **time** : `number`

Time scale index for the item. This isn't the timestamp but rather the logical index.

* * *

### originalData[​](CustomBarItemData.html#originaldata "Direct link to originalData")

> **originalData** : `TData`

Original data for the item.

* * *

### barColor[​](CustomBarItemData.html#barcolor "Direct link to barColor")

> **barColor** : `string`

Color assigned for the item, typically used for price line and price scale label.
