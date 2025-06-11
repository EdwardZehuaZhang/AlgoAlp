# API: Primitivehovereditem

*Source: docs\api\interfaces\PrimitiveHoveredItem.html*

Version: 5.0

On this page

Data representing the currently hovered object from the Hit test.

## Properties[​](PrimitiveHoveredItem.html#properties "Direct link to Properties")

### cursorStyle?[​](PrimitiveHoveredItem.html#cursorstyle "Direct link to cursorStyle?")

> `optional` **cursorStyle** : `string`

CSS cursor style as defined here: [MDN: CSS Cursor](https://developer.mozilla.org/en-US/docs/Web/CSS/cursor) or `undefined` if you want the library to use the default cursor style instead.

* * *

### externalId[​](PrimitiveHoveredItem.html#externalid "Direct link to externalId")

> **externalId** : `string`

Hovered objects external ID. Can be used to identify the source item within a mouse subscriber event.

* * *

### zOrder[​](PrimitiveHoveredItem.html#zorder "Direct link to zOrder")

> **zOrder** : [`PrimitivePaneViewZOrder`](../type-aliases/PrimitivePaneViewZOrder.md)

The zOrder of the hovered item.

* * *

### isBackground?[​](PrimitiveHoveredItem.html#isbackground "Direct link to isBackground?")

> `optional` **isBackground** : `boolean`

Set to true if the object is rendered using `drawBackground` instead of `draw`.
