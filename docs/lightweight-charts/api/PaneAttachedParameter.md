# API: Paneattachedparameter

*Source: docs\api\interfaces\PaneAttachedParameter.html*

Version: 5.0

On this page

Object containing references to the chart instance, and a requestUpdate method for triggering a refresh of the chart.

## Type parameters[​](PaneAttachedParameter.html#type-parameters "Direct link to Type parameters")

• **HorzScaleItem** = [`Time`](../type-aliases/Time.md)

## Properties[​](PaneAttachedParameter.html#properties "Direct link to Properties")

### chart[​](PaneAttachedParameter.html#chart "Direct link to chart")

> **chart** : [`IChartApiBase`](IChartApiBase.md)<`HorzScaleItem`>

Chart instance.

* * *

### requestUpdate()[​](PaneAttachedParameter.html#requestupdate "Direct link to requestUpdate\(\)")

> **requestUpdate** : () => `void`

Request an update (redraw the chart)

#### Returns[​](PaneAttachedParameter.html#returns "Direct link to Returns")

`void`
