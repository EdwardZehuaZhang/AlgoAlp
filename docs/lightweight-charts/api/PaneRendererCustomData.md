# API: Panerenderercustomdata

*Source: docs\api\interfaces\PaneRendererCustomData.html*

Version: 5.0

On this page

Data provide to the custom series pane view which can be used within the renderer for drawing the series data.

## Type parameters[​](PaneRendererCustomData.html#type-parameters "Direct link to Type parameters")

• **HorzScaleItem**

• **TData** _extends_ [`CustomData`](CustomData.md)<`HorzScaleItem`>

## Properties[​](PaneRendererCustomData.html#properties "Direct link to Properties")

### bars[​](PaneRendererCustomData.html#bars "Direct link to bars")

> **bars** : readonly [`CustomBarItemData`](CustomBarItemData.md)<`HorzScaleItem`, `TData`>[]

List of all the series' items and their x coordinates.

* * *

### barSpacing[​](PaneRendererCustomData.html#barspacing "Direct link to barSpacing")

> **barSpacing** : `number`

Spacing between consecutive bars.

* * *

### visibleRange[​](PaneRendererCustomData.html#visiblerange "Direct link to visibleRange")

> **visibleRange** : [`IRange`](IRange.md)<`number`>

The current visible range of items on the chart.
