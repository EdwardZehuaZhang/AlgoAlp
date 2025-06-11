# API: Iseriesprimitivebase

*Source: docs\api\interfaces\ISeriesPrimitiveBase.html*

Version: 5.0

On this page

Base interface for series primitives. It must be implemented to add some external graphics to series

## Type parameters[​](ISeriesPrimitiveBase.html#type-parameters "Direct link to Type parameters")

• **TSeriesAttachedParameters** = `unknown`

## Methods[​](ISeriesPrimitiveBase.html#methods "Direct link to Methods")

### updateAllViews()?[​](ISeriesPrimitiveBase.html#updateallviews "Direct link to updateAllViews\(\)?")

> `optional` **updateAllViews**(): `void`

This method is called when viewport has been changed, so primitive have to recalculate / invalidate its data

#### Returns[​](ISeriesPrimitiveBase.html#returns "Direct link to Returns")

`void`

* * *

### priceAxisViews()?[​](ISeriesPrimitiveBase.html#priceaxisviews "Direct link to priceAxisViews\(\)?")

> `optional` **priceAxisViews**(): readonly [`ISeriesPrimitiveAxisView`](ISeriesPrimitiveAxisView.md)[]

Returns array of labels to be drawn on the price axis used by the series

#### Returns[​](ISeriesPrimitiveBase.html#returns-1 "Direct link to Returns")

readonly [`ISeriesPrimitiveAxisView`](ISeriesPrimitiveAxisView.md)[]

array of objects; each of then must implement ISeriesPrimitiveAxisView interface

For performance reasons, the lightweight library uses internal caches based on references to arrays So, this method must return new array if set of views has changed and should try to return the same array if nothing changed

* * *

### timeAxisViews()?[​](ISeriesPrimitiveBase.html#timeaxisviews "Direct link to timeAxisViews\(\)?")

> `optional` **timeAxisViews**(): readonly [`ISeriesPrimitiveAxisView`](ISeriesPrimitiveAxisView.md)[]

Returns array of labels to be drawn on the time axis

#### Returns[​](ISeriesPrimitiveBase.html#returns-2 "Direct link to Returns")

readonly [`ISeriesPrimitiveAxisView`](ISeriesPrimitiveAxisView.md)[]

array of objects; each of then must implement ISeriesPrimitiveAxisView interface

For performance reasons, the lightweight library uses internal caches based on references to arrays So, this method must return new array if set of views has changed and should try to return the same array if nothing changed

* * *

### paneViews()?[​](ISeriesPrimitiveBase.html#paneviews "Direct link to paneViews\(\)?")

> `optional` **paneViews**(): readonly [`IPrimitivePaneView`](IPrimitivePaneView.md)[]

Returns array of objects representing primitive in the main area of the chart

#### Returns[​](ISeriesPrimitiveBase.html#returns-3 "Direct link to Returns")

readonly [`IPrimitivePaneView`](IPrimitivePaneView.md)[]

array of objects; each of then must implement ISeriesPrimitivePaneView interface

For performance reasons, the lightweight library uses internal caches based on references to arrays So, this method must return new array if set of views has changed and should try to return the same array if nothing changed

* * *

### priceAxisPaneViews()?[​](ISeriesPrimitiveBase.html#priceaxispaneviews "Direct link to priceAxisPaneViews\(\)?")

> `optional` **priceAxisPaneViews**(): readonly [`IPrimitivePaneView`](IPrimitivePaneView.md)[]

Returns array of objects representing primitive in the price axis area of the chart

#### Returns[​](ISeriesPrimitiveBase.html#returns-4 "Direct link to Returns")

readonly [`IPrimitivePaneView`](IPrimitivePaneView.md)[]

array of objects; each of then must implement ISeriesPrimitivePaneView interface

For performance reasons, the lightweight library uses internal caches based on references to arrays So, this method must return new array if set of views has changed and should try to return the same array if nothing changed

* * *

### timeAxisPaneViews()?[​](ISeriesPrimitiveBase.html#timeaxispaneviews "Direct link to timeAxisPaneViews\(\)?")

> `optional` **timeAxisPaneViews**(): readonly [`IPrimitivePaneView`](IPrimitivePaneView.md)[]

Returns array of objects representing primitive in the time axis area of the chart

#### Returns[​](ISeriesPrimitiveBase.html#returns-5 "Direct link to Returns")

readonly [`IPrimitivePaneView`](IPrimitivePaneView.md)[]

array of objects; each of then must implement ISeriesPrimitivePaneView interface

For performance reasons, the lightweight library uses internal caches based on references to arrays So, this method must return new array if set of views has changed and should try to return the same array if nothing changed

* * *

### autoscaleInfo()?[​](ISeriesPrimitiveBase.html#autoscaleinfo "Direct link to autoscaleInfo\(\)?")

> `optional` **autoscaleInfo**(`startTimePoint`, `endTimePoint`): [`AutoscaleInfo`](AutoscaleInfo.md)

Return autoscaleInfo which will be merged with the series base autoscaleInfo. You can use this to expand the autoscale range to include visual elements drawn outside of the series' current visible price range.

**Important** : Please note that this method will be evoked very often during scrolling and zooming of the chart, thus it is recommended that this method is either simple to execute, or makes use of optimisations such as caching to ensure that the chart remains responsive.

#### Parameters[​](ISeriesPrimitiveBase.html#parameters "Direct link to Parameters")

• **startTimePoint** : [`Logical`](../type-aliases/Logical.md)

start time point for the current visible range

• **endTimePoint** : [`Logical`](../type-aliases/Logical.md)

end time point for the current visible range

#### Returns[​](ISeriesPrimitiveBase.html#returns-6 "Direct link to Returns")

[`AutoscaleInfo`](AutoscaleInfo.md)

AutoscaleInfo

* * *

### attached()?[​](ISeriesPrimitiveBase.html#attached "Direct link to attached\(\)?")

> `optional` **attached**(`param`): `void`

Attached Lifecycle hook.

#### Parameters[​](ISeriesPrimitiveBase.html#parameters-1 "Direct link to Parameters")

• **param** : `TSeriesAttachedParameters`

An object containing useful references for the attached primitive to use.

#### Returns[​](ISeriesPrimitiveBase.html#returns-7 "Direct link to Returns")

`void`

void

* * *

### detached()?[​](ISeriesPrimitiveBase.html#detached "Direct link to detached\(\)?")

> `optional` **detached**(): `void`

Detached Lifecycle hook.

#### Returns[​](ISeriesPrimitiveBase.html#returns-8 "Direct link to Returns")

`void`

void

* * *

### hitTest()?[​](ISeriesPrimitiveBase.html#hittest "Direct link to hitTest\(\)?")

> `optional` **hitTest**(`x`, `y`): [`PrimitiveHoveredItem`](PrimitiveHoveredItem.md)

Hit test method which will be called by the library when the cursor is moved. Use this to register object ids being hovered for use within the crosshairMoved and click events emitted by the chart. Additionally, the hit test result can specify a preferred cursor type to display for the main chart pane. This method should return the top most hit for this primitive if more than one object is being intersected.

#### Parameters[​](ISeriesPrimitiveBase.html#parameters-2 "Direct link to Parameters")

• **x** : `number`

x Coordinate of mouse event

• **y** : `number`

y Coordinate of mouse event

#### Returns[​](ISeriesPrimitiveBase.html#returns-9 "Direct link to Returns")

[`PrimitiveHoveredItem`](PrimitiveHoveredItem.md)
