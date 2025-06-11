# API: Icustomseriespanerenderer

*Source: docs\api\interfaces\ICustomSeriesPaneRenderer.html*

Version: 5.0

On this page

Renderer for the custom series. This paints on the main chart pane.

## Methods[​](ICustomSeriesPaneRenderer.html#methods "Direct link to Methods")

### draw()[​](ICustomSeriesPaneRenderer.html#draw "Direct link to draw\(\)")

> **draw**(`target`, `priceConverter`, `isHovered`, `hitTestData`?): `void`

Draw function for the renderer.

#### Parameters[​](ICustomSeriesPaneRenderer.html#parameters "Direct link to Parameters")

• **target** : `CanvasRenderingTarget2D`

canvas context to draw on, refer to FancyCanvas library for more details about this class.

• **priceConverter** : [`PriceToCoordinateConverter`](../type-aliases/PriceToCoordinateConverter.md)

converter function for changing prices into vertical coordinate values.

• **isHovered** : `boolean`

Whether the series is hovered.

• **hitTestData?** : `unknown`

Optional hit test data for the series.

#### Returns[​](ICustomSeriesPaneRenderer.html#returns "Direct link to Returns")

`void`
