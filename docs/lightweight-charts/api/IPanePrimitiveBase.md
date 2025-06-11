# API: Ipaneprimitivebase

*Source: docs\api\interfaces\IPanePrimitiveBase.html*

Version: 5.0

On this page

Base interface for series primitives. It must be implemented to add some external graphics to series

## Type parameters[​](IPanePrimitiveBase.html#type-parameters "Direct link to Type parameters")

• **TPaneAttachedParameters** = `unknown`

## Methods[​](IPanePrimitiveBase.html#methods "Direct link to Methods")

### updateAllViews()?[​](IPanePrimitiveBase.html#updateallviews "Direct link to updateAllViews\(\)?")

> `optional` **updateAllViews**(): `void`

This method is called when viewport has been changed, so primitive have to recalculate / invalidate its data

#### Returns[​](IPanePrimitiveBase.html#returns "Direct link to Returns")

`void`

* * *

### paneViews()?[​](IPanePrimitiveBase.html#paneviews "Direct link to paneViews\(\)?")

> `optional` **paneViews**(): readonly [`IPanePrimitivePaneView`](IPanePrimitivePaneView.md)[]

Returns array of objects representing primitive in the main area of the chart

#### Returns[​](IPanePrimitiveBase.html#returns-1 "Direct link to Returns")

readonly [`IPanePrimitivePaneView`](IPanePrimitivePaneView.md)[]

array of objects; each of then must implement IPrimitivePaneView interface

For performance reasons, the lightweight library uses internal caches based on references to arrays So, this method must return new array if set of views has changed and should try to return the same array if nothing changed

* * *

### attached()?[​](IPanePrimitiveBase.html#attached "Direct link to attached\(\)?")

> `optional` **attached**(`param`): `void`

Attached Lifecycle hook.

#### Parameters[​](IPanePrimitiveBase.html#parameters "Direct link to Parameters")

• **param** : `TPaneAttachedParameters`

An object containing useful references for the attached primitive to use.

#### Returns[​](IPanePrimitiveBase.html#returns-2 "Direct link to Returns")

`void`

void

* * *

### detached()?[​](IPanePrimitiveBase.html#detached "Direct link to detached\(\)?")

> `optional` **detached**(): `void`

Detached Lifecycle hook.

#### Returns[​](IPanePrimitiveBase.html#returns-3 "Direct link to Returns")

`void`

void

* * *

### hitTest()?[​](IPanePrimitiveBase.html#hittest "Direct link to hitTest\(\)?")

> `optional` **hitTest**(`x`, `y`): [`PrimitiveHoveredItem`](PrimitiveHoveredItem.md)

Hit test method which will be called by the library when the cursor is moved. Use this to register object ids being hovered for use within the crosshairMoved and click events emitted by the chart. Additionally, the hit test result can specify a preferred cursor type to display for the main chart pane. This method should return the top most hit for this primitive if more than one object is being intersected.

#### Parameters[​](IPanePrimitiveBase.html#parameters-1 "Direct link to Parameters")

• **x** : `number`

x Coordinate of mouse event

• **y** : `number`

y Coordinate of mouse event

#### Returns[​](IPanePrimitiveBase.html#returns-4 "Direct link to Returns")

[`PrimitiveHoveredItem`](PrimitiveHoveredItem.md)
