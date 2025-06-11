# API: Updownmarkerspluginoptions

*Source: docs\api\interfaces\UpDownMarkersPluginOptions.html*

Version: 5.0

On this page

Configuration options for the UpDownMarkers plugin.

## Properties[​](UpDownMarkersPluginOptions.html#properties "Direct link to Properties")

### positiveColor[​](UpDownMarkersPluginOptions.html#positivecolor "Direct link to positiveColor")

> **positiveColor** : `string`

The color used for markers indicating a positive price change. This color will be applied to markers shown above data points where the price has increased.

* * *

### negativeColor[​](UpDownMarkersPluginOptions.html#negativecolor "Direct link to negativeColor")

> **negativeColor** : `string`

The color used for markers indicating a negative price change. This color will be applied to markers shown below data points where the price has decreased.

* * *

### updateVisibilityDuration[​](UpDownMarkersPluginOptions.html#updatevisibilityduration "Direct link to updateVisibilityDuration")

> **updateVisibilityDuration** : `number`

The duration (in milliseconds) for which update markers remain visible on the chart. After this duration, the markers will automatically disappear. Set to 0 for markers to remain indefinitely until the next update.
