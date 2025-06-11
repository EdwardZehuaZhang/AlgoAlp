# API: Customserieswhitespacedata

*Source: docs\api\interfaces\CustomSeriesWhitespaceData.html*

Version: 5.0

On this page

Represents a whitespace data item, which is a data point without a value.

## Extended by[​](CustomSeriesWhitespaceData.html#extended-by "Direct link to Extended by")

  * [`CustomData`](CustomData.md)

## Type parameters[​](CustomSeriesWhitespaceData.html#type-parameters "Direct link to Type parameters")

• **HorzScaleItem**

## Properties[​](CustomSeriesWhitespaceData.html#properties "Direct link to Properties")

### time[​](CustomSeriesWhitespaceData.html#time "Direct link to time")

> **time** : `HorzScaleItem`

The time of the data.

* * *

### customValues?[​](CustomSeriesWhitespaceData.html#customvalues "Direct link to customValues?")

> `optional` **customValues** : `Record`<`string`, `unknown`>

Additional custom values which will be ignored by the library, but could be used by plugins.
