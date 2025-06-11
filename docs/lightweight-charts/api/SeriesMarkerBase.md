# API: Seriesmarkerbase

*Source: docs\api\interfaces\SeriesMarkerBase.html*

Version: 5.0

On this page

Represents a series marker.

## Extended by[​](SeriesMarkerBase.html#extended-by "Direct link to Extended by")

  * [`SeriesMarkerBar`](SeriesMarkerBar.md)
  * [`SeriesMarkerPrice`](SeriesMarkerPrice.md)

## Type parameters[​](SeriesMarkerBase.html#type-parameters "Direct link to Type parameters")

• **TimeType**

## Properties[​](SeriesMarkerBase.html#properties "Direct link to Properties")

### time[​](SeriesMarkerBase.html#time "Direct link to time")

> **time** : `TimeType`

The time of the marker.

* * *

### position[​](SeriesMarkerBase.html#position "Direct link to position")

> **position** : [`SeriesMarkerPosition`](../type-aliases/SeriesMarkerPosition.md)

The position of the marker.

* * *

### shape[​](SeriesMarkerBase.html#shape "Direct link to shape")

> **shape** : [`SeriesMarkerShape`](../type-aliases/SeriesMarkerShape.md)

The shape of the marker.

* * *

### color[​](SeriesMarkerBase.html#color "Direct link to color")

> **color** : `string`

The color of the marker.

* * *

### id?[​](SeriesMarkerBase.html#id "Direct link to id?")

> `optional` **id** : `string`

The ID of the marker.

* * *

### text?[​](SeriesMarkerBase.html#text "Direct link to text?")

> `optional` **text** : `string`

The optional text of the marker.

* * *

### size?[​](SeriesMarkerBase.html#size "Direct link to size?")

> `optional` **size** : `number`

The optional size of the marker.

#### Default Value[​](SeriesMarkerBase.html#default-value "Direct link to Default Value")

`1`

* * *

### price?[​](SeriesMarkerBase.html#price "Direct link to price?")

> `optional` **price** : `number`

The price value for exact Y-axis positioning.

Required when using [SeriesMarkerPricePosition](../type-aliases/SeriesMarkerPricePosition.md) position type.
