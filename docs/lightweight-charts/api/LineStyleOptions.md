# API: Linestyleoptions

*Source: docs\api\interfaces\LineStyleOptions.html*

Version: 5.0

On this page

Represents style options for a line series.

## Properties[​](LineStyleOptions.html#properties "Direct link to Properties")

### color[​](LineStyleOptions.html#color "Direct link to color")

> **color** : `string`

Line color.

#### Default Value[​](LineStyleOptions.html#default-value "Direct link to Default Value")

`'#2196f3'`

* * *

### lineStyle[​](LineStyleOptions.html#linestyle "Direct link to lineStyle")

> **lineStyle** : [`LineStyle`](../enumerations/LineStyle.md)

Line style.

#### Default Value[​](LineStyleOptions.html#default-value-1 "Direct link to Default Value")
    
    
    {@link LineStyle.Solid}  
    

* * *

### lineWidth[​](LineStyleOptions.html#linewidth "Direct link to lineWidth")

> **lineWidth** : [`LineWidth`](../type-aliases/LineWidth.md)

Line width in pixels.

#### Default Value[​](LineStyleOptions.html#default-value-2 "Direct link to Default Value")

`3`

* * *

### lineType[​](LineStyleOptions.html#linetype "Direct link to lineType")

> **lineType** : [`LineType`](../enumerations/LineType.md)

Line type.

#### Default Value[​](LineStyleOptions.html#default-value-3 "Direct link to Default Value")
    
    
    {@link LineType.Simple}  
    

* * *

### lineVisible[​](LineStyleOptions.html#linevisible "Direct link to lineVisible")

> **lineVisible** : `boolean`

Show series line.

#### Default Value[​](LineStyleOptions.html#default-value-4 "Direct link to Default Value")

`true`

* * *

### pointMarkersVisible[​](LineStyleOptions.html#pointmarkersvisible "Direct link to pointMarkersVisible")

> **pointMarkersVisible** : `boolean`

Show circle markers on each point.

#### Default Value[​](LineStyleOptions.html#default-value-5 "Direct link to Default Value")

`false`

* * *

### pointMarkersRadius?[​](LineStyleOptions.html#pointmarkersradius "Direct link to pointMarkersRadius?")

> `optional` **pointMarkersRadius** : `number`

Circle markers radius in pixels.

#### Default Value[​](LineStyleOptions.html#default-value-6 "Direct link to Default Value")

`undefined`

* * *

### crosshairMarkerVisible[​](LineStyleOptions.html#crosshairmarkervisible "Direct link to crosshairMarkerVisible")

> **crosshairMarkerVisible** : `boolean`

Show the crosshair marker.

#### Default Value[​](LineStyleOptions.html#default-value-7 "Direct link to Default Value")

`true`

* * *

### crosshairMarkerRadius[​](LineStyleOptions.html#crosshairmarkerradius "Direct link to crosshairMarkerRadius")

> **crosshairMarkerRadius** : `number`

Crosshair marker radius in pixels.

#### Default Value[​](LineStyleOptions.html#default-value-8 "Direct link to Default Value")

`4`

* * *

### crosshairMarkerBorderColor[​](LineStyleOptions.html#crosshairmarkerbordercolor "Direct link to crosshairMarkerBorderColor")

> **crosshairMarkerBorderColor** : `string`

Crosshair marker border color. An empty string falls back to the color of the series under the crosshair.

#### Default Value[​](LineStyleOptions.html#default-value-9 "Direct link to Default Value")

`''`

* * *

### crosshairMarkerBackgroundColor[​](LineStyleOptions.html#crosshairmarkerbackgroundcolor "Direct link to crosshairMarkerBackgroundColor")

> **crosshairMarkerBackgroundColor** : `string`

The crosshair marker background color. An empty string falls back to the color of the series under the crosshair.

#### Default Value[​](LineStyleOptions.html#default-value-10 "Direct link to Default Value")

`''`

* * *

### crosshairMarkerBorderWidth[​](LineStyleOptions.html#crosshairmarkerborderwidth "Direct link to crosshairMarkerBorderWidth")

> **crosshairMarkerBorderWidth** : `number`

Crosshair marker border width in pixels.

#### Default Value[​](LineStyleOptions.html#default-value-11 "Direct link to Default Value")

`2`

* * *

### lastPriceAnimation[​](LineStyleOptions.html#lastpriceanimation "Direct link to lastPriceAnimation")

> **lastPriceAnimation** : [`LastPriceAnimationMode`](../enumerations/LastPriceAnimationMode.md)

Last price animation mode.

#### Default Value[​](LineStyleOptions.html#default-value-12 "Direct link to Default Value")
    
    
    {@link LastPriceAnimationMode.Disabled}  
    
