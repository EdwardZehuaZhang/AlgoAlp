# API: Seriesmarkerbar

*Source: docs\api\interfaces\SeriesMarkerBar.html*

Version: 5.0

On this page

Represents a series marker.

## Extends[​](SeriesMarkerBar.html#extends "Direct link to Extends")

  * [`SeriesMarkerBase`](SeriesMarkerBase.md)<`TimeType`>

## Type parameters[​](SeriesMarkerBar.html#type-parameters "Direct link to Type parameters")

• **TimeType**

## Properties[​](SeriesMarkerBar.html#properties "Direct link to Properties")

### position[​](SeriesMarkerBar.html#position "Direct link to position")

> **position** : [`SeriesMarkerBarPosition`](../type-aliases/SeriesMarkerBarPosition.md)

The position of the marker.

#### Overrides[​](SeriesMarkerBar.html#overrides "Direct link to Overrides")

[`SeriesMarkerBase`](SeriesMarkerBase.md) . [`position`](SeriesMarkerBase.html#position)

* * *

### time[​](SeriesMarkerBar.html#time "Direct link to time")

> **time** : `TimeType`

The time of the marker.

#### Inherited from[​](SeriesMarkerBar.html#inherited-from "Direct link to Inherited from")

[`SeriesMarkerBase`](SeriesMarkerBase.md) . [`time`](SeriesMarkerBase.html#time)

* * *

### shape[​](SeriesMarkerBar.html#shape "Direct link to shape")

> **shape** : [`SeriesMarkerShape`](../type-aliases/SeriesMarkerShape.md)

The shape of the marker.

#### Inherited from[​](SeriesMarkerBar.html#inherited-from-1 "Direct link to Inherited from")

[`SeriesMarkerBase`](SeriesMarkerBase.md) . [`shape`](SeriesMarkerBase.html#shape)

* * *

### color[​](SeriesMarkerBar.html#color "Direct link to color")

> **color** : `string`

The color of the marker.

#### Inherited from[​](SeriesMarkerBar.html#inherited-from-2 "Direct link to Inherited from")

[`SeriesMarkerBase`](SeriesMarkerBase.md) . [`color`](SeriesMarkerBase.html#color)

* * *

### id?[​](SeriesMarkerBar.html#id "Direct link to id?")

> `optional` **id** : `string`

The ID of the marker.

#### Inherited from[​](SeriesMarkerBar.html#inherited-from-3 "Direct link to Inherited from")

[`SeriesMarkerBase`](SeriesMarkerBase.md) . [`id`](SeriesMarkerBase.html#id)

* * *

### text?[​](SeriesMarkerBar.html#text "Direct link to text?")

> `optional` **text** : `string`

The optional text of the marker.

#### Inherited from[​](SeriesMarkerBar.html#inherited-from-4 "Direct link to Inherited from")

[`SeriesMarkerBase`](SeriesMarkerBase.md) . [`text`](SeriesMarkerBase.html#text)

* * *

### size?[​](SeriesMarkerBar.html#size "Direct link to size?")

> `optional` **size** : `number`

The optional size of the marker.

#### Default Value[​](SeriesMarkerBar.html#default-value "Direct link to Default Value")

`1`

#### Inherited from[​](SeriesMarkerBar.html#inherited-from-5 "Direct link to Inherited from")

[`SeriesMarkerBase`](SeriesMarkerBase.md) . [`size`](SeriesMarkerBase.html#size)

* * *

### price?[​](SeriesMarkerBar.html#price "Direct link to price?")

> `optional` **price** : `number`

The price value for exact Y-axis positioning.

Required when using [SeriesMarkerPricePosition](../type-aliases/SeriesMarkerPricePosition.md) position type.

#### Inherited from[​](SeriesMarkerBar.html#inherited-from-6 "Direct link to Inherited from")

[`SeriesMarkerBase`](SeriesMarkerBase.md) . [`price`](SeriesMarkerBase.html#price)
