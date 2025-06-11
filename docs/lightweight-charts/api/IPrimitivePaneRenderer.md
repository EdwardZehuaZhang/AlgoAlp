# API: Iprimitivepanerenderer

*Source: docs\api\interfaces\IPrimitivePaneRenderer.html*

Version: 5.0

On this page

This interface represents rendering some element on the canvas

## Methods[​](IPrimitivePaneRenderer.html#methods "Direct link to Methods")

### draw()[​](IPrimitivePaneRenderer.html#draw "Direct link to draw\(\)")

> **draw**(`target`): `void`

Method to draw main content of the element

#### Parameters[​](IPrimitivePaneRenderer.html#parameters "Direct link to Parameters")

• **target** : `CanvasRenderingTarget2D`

canvas context to draw on, refer to FancyCanvas library for more details about this class

#### Returns[​](IPrimitivePaneRenderer.html#returns "Direct link to Returns")

`void`

* * *

### drawBackground()?[​](IPrimitivePaneRenderer.html#drawbackground "Direct link to drawBackground\(\)?")

> `optional` **drawBackground**(`target`): `void`

Optional method to draw the background. Some elements could implement this method to draw on the background of the chart. Usually this is some kind of watermarks or time areas highlighting.

#### Parameters[​](IPrimitivePaneRenderer.html#parameters-1 "Direct link to Parameters")

• **target** : `CanvasRenderingTarget2D`

canvas context to draw on, refer FancyCanvas library for more details about this class

#### Returns[​](IPrimitivePaneRenderer.html#returns-1 "Direct link to Returns")

`void`
