# API: Customdata

*Source: docs\api\interfaces\CustomData.html*

Version: 5.0

On this page

Base structure describing a single item of data for a custom series.

This type allows for any properties to be defined within the interface. It is recommended that you extend this interface with the required data structure.

## Extends[​](CustomData.html#extends "Direct link to Extends")

  * [`CustomSeriesWhitespaceData`](CustomSeriesWhitespaceData.md)<`HorzScaleItem`>

## Type parameters[​](CustomData.html#type-parameters "Direct link to Type parameters")

• **HorzScaleItem** = [`Time`](../type-aliases/Time.md)

## Properties[​](CustomData.html#properties "Direct link to Properties")

### color?[​](CustomData.html#color "Direct link to color?")

> `optional` **color** : `string`

If defined then this color will be used for the price line and price scale line for this specific data item of the custom series.

* * *

### time[​](CustomData.html#time "Direct link to time")

> **time** : `HorzScaleItem`

The time of the data.

#### Inherited from[​](CustomData.html#inherited-from "Direct link to Inherited from")

[`CustomSeriesWhitespaceData`](CustomSeriesWhitespaceData.md) . [`time`](CustomSeriesWhitespaceData.html#time)

* * *

### customValues?[​](CustomData.html#customvalues "Direct link to customValues?")

> `optional` **customValues** : `Record`<`string`, `unknown`>

Additional custom values which will be ignored by the library, but could be used by plugins.

#### Inherited from[​](CustomData.html#inherited-from-1 "Direct link to Inherited from")

[`CustomSeriesWhitespaceData`](CustomSeriesWhitespaceData.md) . [`customValues`](CustomSeriesWhitespaceData.html#customvalues)
