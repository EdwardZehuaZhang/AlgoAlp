# API: Baselinestyleoptions

*Source: docs\api\interfaces\BaselineStyleOptions.html*

Version: 5.0

On this page

Represents style options for a baseline series.

## Properties[​](BaselineStyleOptions.html#properties "Direct link to Properties")

### baseValue[​](BaselineStyleOptions.html#basevalue "Direct link to baseValue")

> **baseValue** : [`BaseValuePrice`](BaseValuePrice.md)

Base value of the series.

#### Default Value[​](BaselineStyleOptions.html#default-value "Direct link to Default Value")

`{ type: 'price', price: 0 }`

* * *

### relativeGradient[​](BaselineStyleOptions.html#relativegradient "Direct link to relativeGradient")

> **relativeGradient** : `boolean`

Gradient is relative to the base value and the currently visible range. If it is false, the gradient is relative to the top and bottom of the chart.

#### Default Value[​](BaselineStyleOptions.html#default-value-1 "Direct link to Default Value")

`false`

* * *

### topFillColor1[​](BaselineStyleOptions.html#topfillcolor1 "Direct link to topFillColor1")

> **topFillColor1** : `string`

The first color of the top area.

#### Default Value[​](BaselineStyleOptions.html#default-value-2 "Direct link to Default Value")

`'rgba(38, 166, 154, 0.28)'`

* * *

### topFillColor2[​](BaselineStyleOptions.html#topfillcolor2 "Direct link to topFillColor2")

> **topFillColor2** : `string`

The second color of the top area.

#### Default Value[​](BaselineStyleOptions.html#default-value-3 "Direct link to Default Value")

`'rgba(38, 166, 154, 0.05)'`

* * *

### topLineColor[​](BaselineStyleOptions.html#toplinecolor "Direct link to topLineColor")

> **topLineColor** : `string`

The line color of the top area.

#### Default Value[​](BaselineStyleOptions.html#default-value-4 "Direct link to Default Value")

`'rgba(38, 166, 154, 1)'`

* * *

### bottomFillColor1[​](BaselineStyleOptions.html#bottomfillcolor1 "Direct link to bottomFillColor1")

> **bottomFillColor1** : `string`

The first color of the bottom area.

#### Default Value[​](BaselineStyleOptions.html#default-value-5 "Direct link to Default Value")

`'rgba(239, 83, 80, 0.05)'`

* * *

### bottomFillColor2[​](BaselineStyleOptions.html#bottomfillcolor2 "Direct link to bottomFillColor2")

> **bottomFillColor2** : `string`

The second color of the bottom area.

#### Default Value[​](BaselineStyleOptions.html#default-value-6 "Direct link to Default Value")

`'rgba(239, 83, 80, 0.28)'`

* * *

### bottomLineColor[​](BaselineStyleOptions.html#bottomlinecolor "Direct link to bottomLineColor")

> **bottomLineColor** : `string`

The line color of the bottom area.

#### Default Value[​](BaselineStyleOptions.html#default-value-7 "Direct link to Default Value")

`'rgba(239, 83, 80, 1)'`

* * *

### lineWidth[​](BaselineStyleOptions.html#linewidth "Direct link to lineWidth")

> **lineWidth** : [`LineWidth`](../type-aliases/LineWidth.md)

Line width.

#### Default Value[​](BaselineStyleOptions.html#default-value-8 "Direct link to Default Value")

`3`

* * *

### lineStyle[​](BaselineStyleOptions.html#linestyle "Direct link to lineStyle")

> **lineStyle** : [`LineStyle`](../enumerations/LineStyle.md)

Line style.

#### Default Value[​](BaselineStyleOptions.html#default-value-9 "Direct link to Default Value")
    
    
    {@link LineStyle.Solid}  
    

* * *

### lineType[​](BaselineStyleOptions.html#linetype "Direct link to lineType")

> **lineType** : [`LineType`](../enumerations/LineType.md)

Line type.

#### Default Value[​](BaselineStyleOptions.html#default-value-10 "Direct link to Default Value")
    
    
    {@link LineType.Simple}  
    

* * *

### lineVisible[​](BaselineStyleOptions.html#linevisible "Direct link to lineVisible")

> **lineVisible** : `boolean`

Show series line.

#### Default Value[​](BaselineStyleOptions.html#default-value-11 "Direct link to Default Value")

`true`

* * *

### pointMarkersVisible[​](BaselineStyleOptions.html#pointmarkersvisible "Direct link to pointMarkersVisible")

> **pointMarkersVisible** : `boolean`

Show circle markers on each point.

#### Default Value[​](BaselineStyleOptions.html#default-value-12 "Direct link to Default Value")

`false`

* * *

### pointMarkersRadius?[​](BaselineStyleOptions.html#pointmarkersradius "Direct link to pointMarkersRadius?")

> `optional` **pointMarkersRadius** : `number`

Circle markers radius in pixels.

#### Default Value[​](BaselineStyleOptions.html#default-value-13 "Direct link to Default Value")

`undefined`

* * *

### crosshairMarkerVisible[​](BaselineStyleOptions.html#crosshairmarkervisible "Direct link to crosshairMarkerVisible")

> **crosshairMarkerVisible** : `boolean`

Show the crosshair marker.

#### Default Value[​](BaselineStyleOptions.html#default-value-14 "Direct link to Default Value")

`true`

* * *

### crosshairMarkerRadius[​](BaselineStyleOptions.html#crosshairmarkerradius "Direct link to crosshairMarkerRadius")

> **crosshairMarkerRadius** : `number`

Crosshair marker radius in pixels.

#### Default Value[​](BaselineStyleOptions.html#default-value-15 "Direct link to Default Value")

`4`

* * *

### crosshairMarkerBorderColor[​](BaselineStyleOptions.html#crosshairmarkerbordercolor "Direct link to crosshairMarkerBorderColor")

> **crosshairMarkerBorderColor** : `string`

Crosshair marker border color. An empty string falls back to the color of the series under the crosshair.

#### Default Value[​](BaselineStyleOptions.html#default-value-16 "Direct link to Default Value")

`''`

* * *

### crosshairMarkerBackgroundColor[​](BaselineStyleOptions.html#crosshairmarkerbackgroundcolor "Direct link to crosshairMarkerBackgroundColor")

> **crosshairMarkerBackgroundColor** : `string`

The crosshair marker background color. An empty string falls back to the color of the series under the crosshair.

#### Default Value[​](BaselineStyleOptions.html#default-value-17 "Direct link to Default Value")

`''`

* * *

### crosshairMarkerBorderWidth[​](BaselineStyleOptions.html#crosshairmarkerborderwidth "Direct link to crosshairMarkerBorderWidth")

> **crosshairMarkerBorderWidth** : `number`

Crosshair marker border width in pixels.

#### Default Value[​](BaselineStyleOptions.html#default-value-18 "Direct link to Default Value")

`2`

* * *

### lastPriceAnimation[​](BaselineStyleOptions.html#lastpriceanimation "Direct link to lastPriceAnimation")

> **lastPriceAnimation** : [`LastPriceAnimationMode`](../enumerations/LastPriceAnimationMode.md)

Last price animation mode.

#### Default Value[​](BaselineStyleOptions.html#default-value-19 "Direct link to Default Value")
    
    
    {@link LastPriceAnimationMode.Disabled}  
    
