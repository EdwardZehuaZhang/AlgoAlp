# API: Timescaleoptions

*Source: docs\api\interfaces\TimeScaleOptions.html*

Version: 5.0

On this page

Extended time scale options for time-based horizontal scale

## Extends[​](TimeScaleOptions.html#extends "Direct link to Extends")

  * [`HorzScaleOptions`](HorzScaleOptions.md)

## Properties[​](TimeScaleOptions.html#properties "Direct link to Properties")

### rightOffset[​](TimeScaleOptions.html#rightoffset "Direct link to rightOffset")

> **rightOffset** : `number`

The margin space in bars from the right side of the chart.

#### Default Value[​](TimeScaleOptions.html#default-value "Direct link to Default Value")

`0`

#### Inherited from[​](TimeScaleOptions.html#inherited-from "Direct link to Inherited from")

[`HorzScaleOptions`](HorzScaleOptions.md) . [`rightOffset`](HorzScaleOptions.html#rightoffset)

* * *

### barSpacing[​](TimeScaleOptions.html#barspacing "Direct link to barSpacing")

> **barSpacing** : `number`

The space between bars in pixels.

#### Default Value[​](TimeScaleOptions.html#default-value-1 "Direct link to Default Value")

`6`

#### Inherited from[​](TimeScaleOptions.html#inherited-from-1 "Direct link to Inherited from")

[`HorzScaleOptions`](HorzScaleOptions.md) . [`barSpacing`](HorzScaleOptions.html#barspacing)

* * *

### minBarSpacing[​](TimeScaleOptions.html#minbarspacing "Direct link to minBarSpacing")

> **minBarSpacing** : `number`

The minimum space between bars in pixels.

#### Default Value[​](TimeScaleOptions.html#default-value-2 "Direct link to Default Value")

`0.5`

#### Inherited from[​](TimeScaleOptions.html#inherited-from-2 "Direct link to Inherited from")

[`HorzScaleOptions`](HorzScaleOptions.md) . [`minBarSpacing`](HorzScaleOptions.html#minbarspacing)

* * *

### maxBarSpacing[​](TimeScaleOptions.html#maxbarspacing "Direct link to maxBarSpacing")

> **maxBarSpacing** : `number`

The maximum space between bars in pixels.

Has no effect if value is set to `0`.

#### Default Value[​](TimeScaleOptions.html#default-value-3 "Direct link to Default Value")

`0`

#### Inherited from[​](TimeScaleOptions.html#inherited-from-3 "Direct link to Inherited from")

[`HorzScaleOptions`](HorzScaleOptions.md) . [`maxBarSpacing`](HorzScaleOptions.html#maxbarspacing)

* * *

### fixLeftEdge[​](TimeScaleOptions.html#fixleftedge "Direct link to fixLeftEdge")

> **fixLeftEdge** : `boolean`

Prevent scrolling to the left of the first bar.

#### Default Value[​](TimeScaleOptions.html#default-value-4 "Direct link to Default Value")

`false`

#### Inherited from[​](TimeScaleOptions.html#inherited-from-4 "Direct link to Inherited from")

[`HorzScaleOptions`](HorzScaleOptions.md) . [`fixLeftEdge`](HorzScaleOptions.html#fixleftedge)

* * *

### fixRightEdge[​](TimeScaleOptions.html#fixrightedge "Direct link to fixRightEdge")

> **fixRightEdge** : `boolean`

Prevent scrolling to the right of the most recent bar.

#### Default Value[​](TimeScaleOptions.html#default-value-5 "Direct link to Default Value")

`false`

#### Inherited from[​](TimeScaleOptions.html#inherited-from-5 "Direct link to Inherited from")

[`HorzScaleOptions`](HorzScaleOptions.md) . [`fixRightEdge`](HorzScaleOptions.html#fixrightedge)

* * *

### lockVisibleTimeRangeOnResize[​](TimeScaleOptions.html#lockvisibletimerangeonresize "Direct link to lockVisibleTimeRangeOnResize")

> **lockVisibleTimeRangeOnResize** : `boolean`

Prevent changing the visible time range during chart resizing.

#### Default Value[​](TimeScaleOptions.html#default-value-6 "Direct link to Default Value")

`false`

#### Inherited from[​](TimeScaleOptions.html#inherited-from-6 "Direct link to Inherited from")

[`HorzScaleOptions`](HorzScaleOptions.md) . [`lockVisibleTimeRangeOnResize`](HorzScaleOptions.html#lockvisibletimerangeonresize)

* * *

### rightBarStaysOnScroll[​](TimeScaleOptions.html#rightbarstaysonscroll "Direct link to rightBarStaysOnScroll")

> **rightBarStaysOnScroll** : `boolean`

Prevent the hovered bar from moving when scrolling.

#### Default Value[​](TimeScaleOptions.html#default-value-7 "Direct link to Default Value")

`false`

#### Inherited from[​](TimeScaleOptions.html#inherited-from-7 "Direct link to Inherited from")

[`HorzScaleOptions`](HorzScaleOptions.md) . [`rightBarStaysOnScroll`](HorzScaleOptions.html#rightbarstaysonscroll)

* * *

### borderVisible[​](TimeScaleOptions.html#bordervisible "Direct link to borderVisible")

> **borderVisible** : `boolean`

Show the time scale border.

#### Default Value[​](TimeScaleOptions.html#default-value-8 "Direct link to Default Value")

`true`

#### Inherited from[​](TimeScaleOptions.html#inherited-from-8 "Direct link to Inherited from")

[`HorzScaleOptions`](HorzScaleOptions.md) . [`borderVisible`](HorzScaleOptions.html#bordervisible)

* * *

### borderColor[​](TimeScaleOptions.html#bordercolor "Direct link to borderColor")

> **borderColor** : `string`

The time scale border color.

#### Default Value[​](TimeScaleOptions.html#default-value-9 "Direct link to Default Value")

`'#2B2B43'`

#### Inherited from[​](TimeScaleOptions.html#inherited-from-9 "Direct link to Inherited from")

[`HorzScaleOptions`](HorzScaleOptions.md) . [`borderColor`](HorzScaleOptions.html#bordercolor)

* * *

### visible[​](TimeScaleOptions.html#visible "Direct link to visible")

> **visible** : `boolean`

Show the time scale.

#### Default Value[​](TimeScaleOptions.html#default-value-10 "Direct link to Default Value")

`true`

#### Inherited from[​](TimeScaleOptions.html#inherited-from-10 "Direct link to Inherited from")

[`HorzScaleOptions`](HorzScaleOptions.md) . [`visible`](HorzScaleOptions.html#visible)

* * *

### timeVisible[​](TimeScaleOptions.html#timevisible "Direct link to timeVisible")

> **timeVisible** : `boolean`

Show the time, not just the date, in the time scale and vertical crosshair label.

#### Default Value[​](TimeScaleOptions.html#default-value-11 "Direct link to Default Value")

`false`

#### Inherited from[​](TimeScaleOptions.html#inherited-from-11 "Direct link to Inherited from")

[`HorzScaleOptions`](HorzScaleOptions.md) . [`timeVisible`](HorzScaleOptions.html#timevisible)

* * *

### secondsVisible[​](TimeScaleOptions.html#secondsvisible "Direct link to secondsVisible")

> **secondsVisible** : `boolean`

Show seconds in the time scale and vertical crosshair label in `hh:mm:ss` format for intraday data.

#### Default Value[​](TimeScaleOptions.html#default-value-12 "Direct link to Default Value")

`true`

#### Inherited from[​](TimeScaleOptions.html#inherited-from-12 "Direct link to Inherited from")

[`HorzScaleOptions`](HorzScaleOptions.md) . [`secondsVisible`](HorzScaleOptions.html#secondsvisible)

* * *

### shiftVisibleRangeOnNewBar[​](TimeScaleOptions.html#shiftvisiblerangeonnewbar "Direct link to shiftVisibleRangeOnNewBar")

> **shiftVisibleRangeOnNewBar** : `boolean`

Shift the visible range to the right (into the future) by the number of new bars when new data is added.

Note that this only applies when the last bar is visible.

#### Default Value[​](TimeScaleOptions.html#default-value-13 "Direct link to Default Value")

`true`

#### Inherited from[​](TimeScaleOptions.html#inherited-from-13 "Direct link to Inherited from")

[`HorzScaleOptions`](HorzScaleOptions.md) . [`shiftVisibleRangeOnNewBar`](HorzScaleOptions.html#shiftvisiblerangeonnewbar)

* * *

### allowShiftVisibleRangeOnWhitespaceReplacement[​](TimeScaleOptions.html#allowshiftvisiblerangeonwhitespacereplacement "Direct link to allowShiftVisibleRangeOnWhitespaceReplacement")

> **allowShiftVisibleRangeOnWhitespaceReplacement** : `boolean`

Allow the visible range to be shifted to the right when a new bar is added which is replacing an existing whitespace time point on the chart.

Note that this only applies when the last bar is visible & `shiftVisibleRangeOnNewBar` is enabled.

#### Default Value[​](TimeScaleOptions.html#default-value-14 "Direct link to Default Value")

`false`

#### Inherited from[​](TimeScaleOptions.html#inherited-from-14 "Direct link to Inherited from")

[`HorzScaleOptions`](HorzScaleOptions.md) . [`allowShiftVisibleRangeOnWhitespaceReplacement`](HorzScaleOptions.html#allowshiftvisiblerangeonwhitespacereplacement)

* * *

### ticksVisible[​](TimeScaleOptions.html#ticksvisible "Direct link to ticksVisible")

> **ticksVisible** : `boolean`

Draw small vertical line on time axis labels.

#### Default Value[​](TimeScaleOptions.html#default-value-15 "Direct link to Default Value")

`false`

#### Inherited from[​](TimeScaleOptions.html#inherited-from-15 "Direct link to Inherited from")

[`HorzScaleOptions`](HorzScaleOptions.md) . [`ticksVisible`](HorzScaleOptions.html#ticksvisible)

* * *

### tickMarkMaxCharacterLength?[​](TimeScaleOptions.html#tickmarkmaxcharacterlength "Direct link to tickMarkMaxCharacterLength?")

> `optional` **tickMarkMaxCharacterLength** : `number`

Maximum tick mark label length. Used to override the default 8 character maximum length.

#### Default Value[​](TimeScaleOptions.html#default-value-16 "Direct link to Default Value")

`undefined`

#### Inherited from[​](TimeScaleOptions.html#inherited-from-16 "Direct link to Inherited from")

[`HorzScaleOptions`](HorzScaleOptions.md) . [`tickMarkMaxCharacterLength`](HorzScaleOptions.html#tickmarkmaxcharacterlength)

* * *

### uniformDistribution[​](TimeScaleOptions.html#uniformdistribution "Direct link to uniformDistribution")

> **uniformDistribution** : `boolean`

Changes horizontal scale marks generation. With this flag equal to `true`, marks of the same weight are either all drawn or none are drawn at all.

#### Inherited from[​](TimeScaleOptions.html#inherited-from-17 "Direct link to Inherited from")

[`HorzScaleOptions`](HorzScaleOptions.md) . [`uniformDistribution`](HorzScaleOptions.html#uniformdistribution)

* * *

### minimumHeight[​](TimeScaleOptions.html#minimumheight "Direct link to minimumHeight")

> **minimumHeight** : `number`

Define a minimum height for the time scale. Note: This value will be exceeded if the time scale needs more space to display it's contents.

Setting a minimum height could be useful for ensuring that multiple charts positioned in a horizontal stack each have an identical time scale height, or for plugins which require a bit more space within the time scale pane.

#### Default Value[​](TimeScaleOptions.html#default-value-17 "Direct link to Default Value")
    
    
    0  
    

#### Inherited from[​](TimeScaleOptions.html#inherited-from-18 "Direct link to Inherited from")

[`HorzScaleOptions`](HorzScaleOptions.md) . [`minimumHeight`](HorzScaleOptions.html#minimumheight)

* * *

### allowBoldLabels[​](TimeScaleOptions.html#allowboldlabels "Direct link to allowBoldLabels")

> **allowBoldLabels** : `boolean`

Allow major time scale labels to be rendered in a bolder font weight.

#### Default Value[​](TimeScaleOptions.html#default-value-18 "Direct link to Default Value")
    
    
    true  
    

#### Inherited from[​](TimeScaleOptions.html#inherited-from-19 "Direct link to Inherited from")

[`HorzScaleOptions`](HorzScaleOptions.md) . [`allowBoldLabels`](HorzScaleOptions.html#allowboldlabels)

* * *

### ignoreWhitespaceIndices[​](TimeScaleOptions.html#ignorewhitespaceindices "Direct link to ignoreWhitespaceIndices")

> **ignoreWhitespaceIndices** : `boolean`

Ignore time scale points containing only whitespace (for all series) when drawing grid lines, tick marks, and snapping the crosshair to time scale points.

For the yield curve chart type it defaults to `true`.

#### Default Value[​](TimeScaleOptions.html#default-value-19 "Direct link to Default Value")
    
    
    false  
    

#### Inherited from[​](TimeScaleOptions.html#inherited-from-20 "Direct link to Inherited from")

[`HorzScaleOptions`](HorzScaleOptions.md) . [`ignoreWhitespaceIndices`](HorzScaleOptions.html#ignorewhitespaceindices)

* * *

### tickMarkFormatter?[​](TimeScaleOptions.html#tickmarkformatter "Direct link to tickMarkFormatter?")

> `optional` **tickMarkFormatter** : [`TickMarkFormatter`](../type-aliases/TickMarkFormatter.md)

Tick marks formatter can be used to customize tick marks labels on the time axis.

#### Default Value[​](TimeScaleOptions.html#default-value-20 "Direct link to Default Value")

`undefined`
