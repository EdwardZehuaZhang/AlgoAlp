# API: Horzscaleoptions

*Source: docs\api\interfaces\HorzScaleOptions.html*

Version: 5.0

On this page

Options for the time scale; the horizontal scale at the bottom of the chart that displays the time of data.

## Extended by[​](HorzScaleOptions.html#extended-by "Direct link to Extended by")

  * [`TimeScaleOptions`](TimeScaleOptions.md)

## Properties[​](HorzScaleOptions.html#properties "Direct link to Properties")

### rightOffset[​](HorzScaleOptions.html#rightoffset "Direct link to rightOffset")

> **rightOffset** : `number`

The margin space in bars from the right side of the chart.

#### Default Value[​](HorzScaleOptions.html#default-value "Direct link to Default Value")

`0`

* * *

### barSpacing[​](HorzScaleOptions.html#barspacing "Direct link to barSpacing")

> **barSpacing** : `number`

The space between bars in pixels.

#### Default Value[​](HorzScaleOptions.html#default-value-1 "Direct link to Default Value")

`6`

* * *

### minBarSpacing[​](HorzScaleOptions.html#minbarspacing "Direct link to minBarSpacing")

> **minBarSpacing** : `number`

The minimum space between bars in pixels.

#### Default Value[​](HorzScaleOptions.html#default-value-2 "Direct link to Default Value")

`0.5`

* * *

### maxBarSpacing[​](HorzScaleOptions.html#maxbarspacing "Direct link to maxBarSpacing")

> **maxBarSpacing** : `number`

The maximum space between bars in pixels.

Has no effect if value is set to `0`.

#### Default Value[​](HorzScaleOptions.html#default-value-3 "Direct link to Default Value")

`0`

* * *

### fixLeftEdge[​](HorzScaleOptions.html#fixleftedge "Direct link to fixLeftEdge")

> **fixLeftEdge** : `boolean`

Prevent scrolling to the left of the first bar.

#### Default Value[​](HorzScaleOptions.html#default-value-4 "Direct link to Default Value")

`false`

* * *

### fixRightEdge[​](HorzScaleOptions.html#fixrightedge "Direct link to fixRightEdge")

> **fixRightEdge** : `boolean`

Prevent scrolling to the right of the most recent bar.

#### Default Value[​](HorzScaleOptions.html#default-value-5 "Direct link to Default Value")

`false`

* * *

### lockVisibleTimeRangeOnResize[​](HorzScaleOptions.html#lockvisibletimerangeonresize "Direct link to lockVisibleTimeRangeOnResize")

> **lockVisibleTimeRangeOnResize** : `boolean`

Prevent changing the visible time range during chart resizing.

#### Default Value[​](HorzScaleOptions.html#default-value-6 "Direct link to Default Value")

`false`

* * *

### rightBarStaysOnScroll[​](HorzScaleOptions.html#rightbarstaysonscroll "Direct link to rightBarStaysOnScroll")

> **rightBarStaysOnScroll** : `boolean`

Prevent the hovered bar from moving when scrolling.

#### Default Value[​](HorzScaleOptions.html#default-value-7 "Direct link to Default Value")

`false`

* * *

### borderVisible[​](HorzScaleOptions.html#bordervisible "Direct link to borderVisible")

> **borderVisible** : `boolean`

Show the time scale border.

#### Default Value[​](HorzScaleOptions.html#default-value-8 "Direct link to Default Value")

`true`

* * *

### borderColor[​](HorzScaleOptions.html#bordercolor "Direct link to borderColor")

> **borderColor** : `string`

The time scale border color.

#### Default Value[​](HorzScaleOptions.html#default-value-9 "Direct link to Default Value")

`'#2B2B43'`

* * *

### visible[​](HorzScaleOptions.html#visible "Direct link to visible")

> **visible** : `boolean`

Show the time scale.

#### Default Value[​](HorzScaleOptions.html#default-value-10 "Direct link to Default Value")

`true`

* * *

### timeVisible[​](HorzScaleOptions.html#timevisible "Direct link to timeVisible")

> **timeVisible** : `boolean`

Show the time, not just the date, in the time scale and vertical crosshair label.

#### Default Value[​](HorzScaleOptions.html#default-value-11 "Direct link to Default Value")

`false`

* * *

### secondsVisible[​](HorzScaleOptions.html#secondsvisible "Direct link to secondsVisible")

> **secondsVisible** : `boolean`

Show seconds in the time scale and vertical crosshair label in `hh:mm:ss` format for intraday data.

#### Default Value[​](HorzScaleOptions.html#default-value-12 "Direct link to Default Value")

`true`

* * *

### shiftVisibleRangeOnNewBar[​](HorzScaleOptions.html#shiftvisiblerangeonnewbar "Direct link to shiftVisibleRangeOnNewBar")

> **shiftVisibleRangeOnNewBar** : `boolean`

Shift the visible range to the right (into the future) by the number of new bars when new data is added.

Note that this only applies when the last bar is visible.

#### Default Value[​](HorzScaleOptions.html#default-value-13 "Direct link to Default Value")

`true`

* * *

### allowShiftVisibleRangeOnWhitespaceReplacement[​](HorzScaleOptions.html#allowshiftvisiblerangeonwhitespacereplacement "Direct link to allowShiftVisibleRangeOnWhitespaceReplacement")

> **allowShiftVisibleRangeOnWhitespaceReplacement** : `boolean`

Allow the visible range to be shifted to the right when a new bar is added which is replacing an existing whitespace time point on the chart.

Note that this only applies when the last bar is visible & `shiftVisibleRangeOnNewBar` is enabled.

#### Default Value[​](HorzScaleOptions.html#default-value-14 "Direct link to Default Value")

`false`

* * *

### ticksVisible[​](HorzScaleOptions.html#ticksvisible "Direct link to ticksVisible")

> **ticksVisible** : `boolean`

Draw small vertical line on time axis labels.

#### Default Value[​](HorzScaleOptions.html#default-value-15 "Direct link to Default Value")

`false`

* * *

### tickMarkMaxCharacterLength?[​](HorzScaleOptions.html#tickmarkmaxcharacterlength "Direct link to tickMarkMaxCharacterLength?")

> `optional` **tickMarkMaxCharacterLength** : `number`

Maximum tick mark label length. Used to override the default 8 character maximum length.

#### Default Value[​](HorzScaleOptions.html#default-value-16 "Direct link to Default Value")

`undefined`

* * *

### uniformDistribution[​](HorzScaleOptions.html#uniformdistribution "Direct link to uniformDistribution")

> **uniformDistribution** : `boolean`

Changes horizontal scale marks generation. With this flag equal to `true`, marks of the same weight are either all drawn or none are drawn at all.

* * *

### minimumHeight[​](HorzScaleOptions.html#minimumheight "Direct link to minimumHeight")

> **minimumHeight** : `number`

Define a minimum height for the time scale. Note: This value will be exceeded if the time scale needs more space to display it's contents.

Setting a minimum height could be useful for ensuring that multiple charts positioned in a horizontal stack each have an identical time scale height, or for plugins which require a bit more space within the time scale pane.

#### Default Value[​](HorzScaleOptions.html#default-value-17 "Direct link to Default Value")
    
    
    0  
    

* * *

### allowBoldLabels[​](HorzScaleOptions.html#allowboldlabels "Direct link to allowBoldLabels")

> **allowBoldLabels** : `boolean`

Allow major time scale labels to be rendered in a bolder font weight.

#### Default Value[​](HorzScaleOptions.html#default-value-18 "Direct link to Default Value")
    
    
    true  
    

* * *

### ignoreWhitespaceIndices[​](HorzScaleOptions.html#ignorewhitespaceindices "Direct link to ignoreWhitespaceIndices")

> **ignoreWhitespaceIndices** : `boolean`

Ignore time scale points containing only whitespace (for all series) when drawing grid lines, tick marks, and snapping the crosshair to time scale points.

For the yield curve chart type it defaults to `true`.

#### Default Value[​](HorzScaleOptions.html#default-value-19 "Direct link to Default Value")
    
    
    false  
    
