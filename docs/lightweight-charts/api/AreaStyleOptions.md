# API: Areastyleoptions

*Source: docs\api\interfaces\AreaStyleOptions.html*

Version: 5.0

On this page

Represents style options for an area series.

## Properties[​](AreaStyleOptions.html#properties "Direct link to Properties")

### topColor[​](AreaStyleOptions.html#topcolor "Direct link to topColor")

> **topColor** : `string`

Color of the top part of the area.

#### Default Value[​](AreaStyleOptions.html#default-value "Direct link to Default Value")

`'rgba( 46, 220, 135, 0.4)'`

* * *

### bottomColor[​](AreaStyleOptions.html#bottomcolor "Direct link to bottomColor")

> **bottomColor** : `string`

Color of the bottom part of the area.

#### Default Value[​](AreaStyleOptions.html#default-value-1 "Direct link to Default Value")

`'rgba( 40, 221, 100, 0)'`

* * *

### relativeGradient[​](AreaStyleOptions.html#relativegradient "Direct link to relativeGradient")

> **relativeGradient** : `boolean`

Gradient is relative to the base value and the currently visible range. If it is false, the gradient is relative to the top and bottom of the chart.

#### Default Value[​](AreaStyleOptions.html#default-value-2 "Direct link to Default Value")

`false`

* * *

### invertFilledArea[​](AreaStyleOptions.html#invertfilledarea "Direct link to invertFilledArea")

> **invertFilledArea** : `boolean`

Invert the filled area. Fills the area above the line if set to true.

#### Default Value[​](AreaStyleOptions.html#default-value-3 "Direct link to Default Value")

`false`

* * *

### lineColor[​](AreaStyleOptions.html#linecolor "Direct link to lineColor")

> **lineColor** : `string`

Line color.

#### Default Value[​](AreaStyleOptions.html#default-value-4 "Direct link to Default Value")

`'#33D778'`

* * *

### lineStyle[​](AreaStyleOptions.html#linestyle "Direct link to lineStyle")

> **lineStyle** : [`LineStyle`](../enumerations/LineStyle.md)

Line style.

#### Default Value[​](AreaStyleOptions.html#default-value-5 "Direct link to Default Value")
    
    
    {@link LineStyle.Solid}  
    

* * *

### lineWidth[​](AreaStyleOptions.html#linewidth "Direct link to lineWidth")

> **lineWidth** : [`LineWidth`](../type-aliases/LineWidth.md)

Line width in pixels.

#### Default Value[​](AreaStyleOptions.html#default-value-6 "Direct link to Default Value")

`3`

* * *

### lineType[​](AreaStyleOptions.html#linetype "Direct link to lineType")

> **lineType** : [`LineType`](../enumerations/LineType.md)

Line type.

#### Default Value[​](AreaStyleOptions.html#default-value-7 "Direct link to Default Value")
    
    
    {@link LineType.Simple}  
    

* * *

### lineVisible[​](AreaStyleOptions.html#linevisible "Direct link to lineVisible")

> **lineVisible** : `boolean`

Show series line.

#### Default Value[​](AreaStyleOptions.html#default-value-8 "Direct link to Default Value")

`true`

* * *

### pointMarkersVisible[​](AreaStyleOptions.html#pointmarkersvisible "Direct link to pointMarkersVisible")

> **pointMarkersVisible** : `boolean`

Show circle markers on each point.

#### Default Value[​](AreaStyleOptions.html#default-value-9 "Direct link to Default Value")

`false`

* * *

### pointMarkersRadius?[​](AreaStyleOptions.html#pointmarkersradius "Direct link to pointMarkersRadius?")

> `optional` **pointMarkersRadius** : `number`

Circle markers radius in pixels.

#### Default Value[​](AreaStyleOptions.html#default-value-10 "Direct link to Default Value")

`undefined`

* * *

### crosshairMarkerVisible[​](AreaStyleOptions.html#crosshairmarkervisible "Direct link to crosshairMarkerVisible")

> **crosshairMarkerVisible** : `boolean`

Show the crosshair marker.

#### Default Value[​](AreaStyleOptions.html#default-value-11 "Direct link to Default Value")

`true`

* * *

### crosshairMarkerRadius[​](AreaStyleOptions.html#crosshairmarkerradius "Direct link to crosshairMarkerRadius")

> **crosshairMarkerRadius** : `number`

Crosshair marker radius in pixels.

#### Default Value[​](AreaStyleOptions.html#default-value-12 "Direct link to Default Value")

`4`

* * *

### crosshairMarkerBorderColor[​](AreaStyleOptions.html#crosshairmarkerbordercolor "Direct link to crosshairMarkerBorderColor")

> **crosshairMarkerBorderColor** : `string`

Crosshair marker border color. An empty string falls back to the color of the series under the crosshair.

#### Default Value[​](AreaStyleOptions.html#default-value-13 "Direct link to Default Value")

`''`

* * *

### crosshairMarkerBackgroundColor[​](AreaStyleOptions.html#crosshairmarkerbackgroundcolor "Direct link to crosshairMarkerBackgroundColor")

> **crosshairMarkerBackgroundColor** : `string`

The crosshair marker background color. An empty string falls back to the color of the series under the crosshair.

#### Default Value[​](AreaStyleOptions.html#default-value-14 "Direct link to Default Value")

`''`

* * *

### crosshairMarkerBorderWidth[​](AreaStyleOptions.html#crosshairmarkerborderwidth "Direct link to crosshairMarkerBorderWidth")

> **crosshairMarkerBorderWidth** : `number`

Crosshair marker border width in pixels.

#### Default Value[​](AreaStyleOptions.html#default-value-15 "Direct link to Default Value")

`2`

* * *

### lastPriceAnimation[​](AreaStyleOptions.html#lastpriceanimation "Direct link to lastPriceAnimation")

> **lastPriceAnimation** : [`LastPriceAnimationMode`](../enumerations/LastPriceAnimationMode.md)

Last price animation mode.

#### Default Value[​](AreaStyleOptions.html#default-value-16 "Direct link to Default Value")
    
    
    {@link LastPriceAnimationMode.Disabled}  
    
