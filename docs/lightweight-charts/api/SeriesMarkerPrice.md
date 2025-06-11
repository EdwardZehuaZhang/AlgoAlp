# API: Seriesmarkerprice

*Source: docs\api\interfaces\SeriesMarkerPrice.html*

Version: 5.0

On this page

Represents a series marker.

## Extends[​](SeriesMarkerPrice.html#extends "Direct link to Extends")

  * [`SeriesMarkerBase`](SeriesMarkerBase.md)<`TimeType`>

## Type parameters[​](SeriesMarkerPrice.html#type-parameters "Direct link to Type parameters")

• **TimeType**

## Properties[​](SeriesMarkerPrice.html#properties "Direct link to Properties")

### time[​](SeriesMarkerPrice.html#time "Direct link to time")

> **time** : `TimeType`

The time of the marker.

#### Inherited from[​](SeriesMarkerPrice.html#inherited-from "Direct link to Inherited from")

[`SeriesMarkerBase`](SeriesMarkerBase.md) . [`time`](SeriesMarkerBase.html#time)

* * *

### shape[​](SeriesMarkerPrice.html#shape "Direct link to shape")

> **shape** : [`SeriesMarkerShape`](../type-aliases/SeriesMarkerShape.md)

The shape of the marker.

#### Inherited from[​](SeriesMarkerPrice.html#inherited-from-1 "Direct link to Inherited from")

[`SeriesMarkerBase`](SeriesMarkerBase.md) . [`shape`](SeriesMarkerBase.html#shape)

* * *

### color[​](SeriesMarkerPrice.html#color "Direct link to color")

> **color** : `string`

The color of the marker.

#### Inherited from[​](SeriesMarkerPrice.html#inherited-from-2 "Direct link to Inherited from")

[`SeriesMarkerBase`](SeriesMarkerBase.md) . [`color`](SeriesMarkerBase.html#color)

* * *

### id?[​](SeriesMarkerPrice.html#id "Direct link to id?")

> `optional` **id** : `string`

The ID of the marker.

#### Inherited from[​](SeriesMarkerPrice.html#inherited-from-3 "Direct link to Inherited from")

[`SeriesMarkerBase`](SeriesMarkerBase.md) . [`id`](SeriesMarkerBase.html#id)

* * *

### text?[​](SeriesMarkerPrice.html#text "Direct link to text?")

> `optional` **text** : `string`

The optional text of the marker.

#### Inherited from[​](SeriesMarkerPrice.html#inherited-from-4 "Direct link to Inherited from")

[`SeriesMarkerBase`](SeriesMarkerBase.md) . [`text`](SeriesMarkerBase.html#text)

* * *

### size?[​](SeriesMarkerPrice.html#size "Direct link to size?")

> `optional` **size** : `number`

The optional size of the marker.

#### Default Value[​](SeriesMarkerPrice.html#default-value "Direct link to Default Value")

`1`

#### Inherited from[​](SeriesMarkerPrice.html#inherited-from-5 "Direct link to Inherited from")

[`SeriesMarkerBase`](SeriesMarkerBase.md) . [`size`](SeriesMarkerBase.html#size)

* * *

### position[​](SeriesMarkerPrice.html#position "Direct link to position")

> **position** : [`SeriesMarkerPricePosition`](../type-aliases/SeriesMarkerPricePosition.md)

The position of the marker.

#### Overrides[​](SeriesMarkerPrice.html#overrides "Direct link to Overrides")

[`SeriesMarkerBase`](SeriesMarkerBase.md) . [`position`](SeriesMarkerBase.html#position)

* * *

### price[​](SeriesMarkerPrice.html#price "Direct link to price")

> **price** : `number`

The price value for exact Y-axis positioning.

Required when using [SeriesMarkerPricePosition](../type-aliases/SeriesMarkerPricePosition.md) position type.

#### Overrides[​](SeriesMarkerPrice.html#overrides-1 "Direct link to Overrides")

[`SeriesMarkerBase`](SeriesMarkerBase.md) . [`price`](SeriesMarkerBase.html#price)
