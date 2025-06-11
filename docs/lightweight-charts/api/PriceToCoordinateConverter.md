# API: Pricetocoordinateconverter

*Source: docs\api\type-aliases\PriceToCoordinateConverter.html*

Version: 5.0

On this page

> **PriceToCoordinateConverter** : (`price`) => [`Coordinate`](Coordinate.md) | `null`

Converter function for changing prices into vertical coordinate values.

This is provided as a convenience function since the series original data will most likely be defined in price values, and the renderer needs to draw with coordinates. This returns the same values as directly using the series' priceToCoordinate method.

## Parameters[​](PriceToCoordinateConverter.html#parameters "Direct link to Parameters")

• **price** : `number`

## Returns[​](PriceToCoordinateConverter.html#returns "Direct link to Returns")

[`Coordinate`](Coordinate.md) | `null`
