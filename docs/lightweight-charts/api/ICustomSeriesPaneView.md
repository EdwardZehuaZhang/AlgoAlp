# API: Icustomseriespaneview

*Source: docs\api\interfaces\ICustomSeriesPaneView.html*

Version: 5.0

On this page

This interface represents the view for the custom series

## Type parameters[​](ICustomSeriesPaneView.html#type-parameters "Direct link to Type parameters")

• **HorzScaleItem** = [`Time`](../type-aliases/Time.md)

• **TData** _extends_ [`CustomData`](CustomData.md)<`HorzScaleItem`> = [`CustomData`](CustomData.md)<`HorzScaleItem`>

• **TSeriesOptions** _extends_ [`CustomSeriesOptions`](../type-aliases/CustomSeriesOptions.md) = [`CustomSeriesOptions`](../type-aliases/CustomSeriesOptions.md)

## Methods[​](ICustomSeriesPaneView.html#methods "Direct link to Methods")

### renderer()[​](ICustomSeriesPaneView.html#renderer "Direct link to renderer\(\)")

> **renderer**(): [`ICustomSeriesPaneRenderer`](ICustomSeriesPaneRenderer.md)

This method returns a renderer - special object to draw data for the series on the main chart pane.

#### Returns[​](ICustomSeriesPaneView.html#returns "Direct link to Returns")

[`ICustomSeriesPaneRenderer`](ICustomSeriesPaneRenderer.md)

an renderer object to be used for drawing.

* * *

### update()[​](ICustomSeriesPaneView.html#update "Direct link to update\(\)")

> **update**(`data`, `seriesOptions`): `void`

This method will be called with the latest data for the renderer to use during the next paint.

#### Parameters[​](ICustomSeriesPaneView.html#parameters "Direct link to Parameters")

• **data** : [`PaneRendererCustomData`](PaneRendererCustomData.md)<`HorzScaleItem`, `TData`>

• **seriesOptions** : `TSeriesOptions`

#### Returns[​](ICustomSeriesPaneView.html#returns-1 "Direct link to Returns")

`void`

* * *

### priceValueBuilder()[​](ICustomSeriesPaneView.html#pricevaluebuilder "Direct link to priceValueBuilder\(\)")

> **priceValueBuilder**(`plotRow`): [`CustomSeriesPricePlotValues`](../type-aliases/CustomSeriesPricePlotValues.md)

A function for interpreting the custom series data and returning an array of numbers representing the price values for the item. These price values are used by the chart to determine the auto-scaling (to ensure the items are in view) and the crosshair and price line positions. The last value in the array will be used as the current value. You shouldn't need to have more than 3 values in this array since the library only needs a largest, smallest, and current value.

#### Parameters[​](ICustomSeriesPaneView.html#parameters-1 "Direct link to Parameters")

• **plotRow** : `TData`

#### Returns[​](ICustomSeriesPaneView.html#returns-2 "Direct link to Returns")

[`CustomSeriesPricePlotValues`](../type-aliases/CustomSeriesPricePlotValues.md)

* * *

### isWhitespace()[​](ICustomSeriesPaneView.html#iswhitespace "Direct link to isWhitespace\(\)")

> **isWhitespace**(`data`): `data is CustomSeriesWhitespaceData<HorzScaleItem>`

A function for testing whether a data point should be considered fully specified, or if it should be considered as whitespace. Should return `true` if is whitespace.

#### Parameters[​](ICustomSeriesPaneView.html#parameters-2 "Direct link to Parameters")

• **data** : `TData` | [`CustomSeriesWhitespaceData`](CustomSeriesWhitespaceData.md)<`HorzScaleItem`>

data point to be tested

#### Returns[​](ICustomSeriesPaneView.html#returns-3 "Direct link to Returns")

`data is CustomSeriesWhitespaceData<HorzScaleItem>`

* * *

### defaultOptions()[​](ICustomSeriesPaneView.html#defaultoptions "Direct link to defaultOptions\(\)")

> **defaultOptions**(): `TSeriesOptions`

Default options

#### Returns[​](ICustomSeriesPaneView.html#returns-4 "Direct link to Returns")

`TSeriesOptions`

* * *

### destroy()?[​](ICustomSeriesPaneView.html#destroy "Direct link to destroy\(\)?")

> `optional` **destroy**(): `void`

This method will be evoked when the series has been removed from the chart. This method should be used to clean up any objects, references, and other items that could potentially cause memory leaks.

This method should contain all the necessary code to clean up the object before it is removed from memory. This includes removing any event listeners or timers that are attached to the object, removing any references to other objects, and resetting any values or properties that were modified during the lifetime of the object.

#### Returns[​](ICustomSeriesPaneView.html#returns-5 "Direct link to Returns")

`void`
