# API: Crosshairlineoptions

*Source: docs\api\interfaces\CrosshairLineOptions.html*

Version: 5.0

On this page

Structure describing a crosshair line (vertical or horizontal)

## Properties[​](CrosshairLineOptions.html#properties "Direct link to Properties")

### color[​](CrosshairLineOptions.html#color "Direct link to color")

> **color** : `string`

Crosshair line color.

#### Default Value[​](CrosshairLineOptions.html#default-value "Direct link to Default Value")

`'#758696'`

* * *

### width[​](CrosshairLineOptions.html#width "Direct link to width")

> **width** : [`LineWidth`](../type-aliases/LineWidth.md)

Crosshair line width.

#### Default Value[​](CrosshairLineOptions.html#default-value-1 "Direct link to Default Value")

`1`

* * *

### style[​](CrosshairLineOptions.html#style "Direct link to style")

> **style** : [`LineStyle`](../enumerations/LineStyle.md)

Crosshair line style.

#### Default Value[​](CrosshairLineOptions.html#default-value-2 "Direct link to Default Value")
    
    
    {@link LineStyle.LargeDashed}  
    

* * *

### visible[​](CrosshairLineOptions.html#visible "Direct link to visible")

> **visible** : `boolean`

Display the crosshair line.

Note that disabling crosshair lines does not disable crosshair marker on Line and Area series. It can be disabled by using `crosshairMarkerVisible` option of a relevant series.

#### See[​](CrosshairLineOptions.html#see "Direct link to See")

  * [LineStyleOptions.crosshairMarkerVisible](LineStyleOptions.html#crosshairmarkervisible)
  * [AreaStyleOptions.crosshairMarkerVisible](AreaStyleOptions.html#crosshairmarkervisible)
  * [BaselineStyleOptions.crosshairMarkerVisible](BaselineStyleOptions.html#crosshairmarkervisible)

#### Default Value[​](CrosshairLineOptions.html#default-value-3 "Direct link to Default Value")

`true`

* * *

### labelVisible[​](CrosshairLineOptions.html#labelvisible "Direct link to labelVisible")

> **labelVisible** : `boolean`

Display the crosshair label on the relevant scale.

#### Default Value[​](CrosshairLineOptions.html#default-value-4 "Direct link to Default Value")

`true`

* * *

### labelBackgroundColor[​](CrosshairLineOptions.html#labelbackgroundcolor "Direct link to labelBackgroundColor")

> **labelBackgroundColor** : `string`

Crosshair label background color.

#### Default Value[​](CrosshairLineOptions.html#default-value-5 "Direct link to Default Value")

`'#4c525e'`
