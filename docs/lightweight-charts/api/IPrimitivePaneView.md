# API: Iprimitivepaneview

*Source: docs\api\interfaces\IPrimitivePaneView.html*

Version: 5.0

On this page

This interface represents the primitive for one of the pane of the chart (main chart area, time scale, price scale).

## Methods[​](IPrimitivePaneView.html#methods "Direct link to Methods")

### zOrder()?[​](IPrimitivePaneView.html#zorder "Direct link to zOrder\(\)?")

> `optional` **zOrder**(): [`PrimitivePaneViewZOrder`](../type-aliases/PrimitivePaneViewZOrder.md)

Defines where in the visual layer stack the renderer should be executed. Default is `'normal'`.

#### Returns[​](IPrimitivePaneView.html#returns "Direct link to Returns")

[`PrimitivePaneViewZOrder`](../type-aliases/PrimitivePaneViewZOrder.md)

the desired position in the visual layer stack.

#### See[​](IPrimitivePaneView.html#see "Direct link to See")

[PrimitivePaneViewZOrder](../type-aliases/PrimitivePaneViewZOrder.md)

* * *

### renderer()[​](IPrimitivePaneView.html#renderer "Direct link to renderer\(\)")

> **renderer**(): [`IPrimitivePaneRenderer`](IPrimitivePaneRenderer.md)

This method returns a renderer - special object to draw data

#### Returns[​](IPrimitivePaneView.html#returns-1 "Direct link to Returns")

[`IPrimitivePaneRenderer`](IPrimitivePaneRenderer.md)

an renderer object to be used for drawing, or `null` if we have nothing to draw.
