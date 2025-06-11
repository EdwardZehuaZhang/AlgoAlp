# API: Pricescaleoptions

*Source: docs\api\interfaces\PriceScaleOptions.html*

Version: 5.0

On this page

Structure that describes price scale options

## Properties[​](PriceScaleOptions.html#properties "Direct link to Properties")

### autoScale[​](PriceScaleOptions.html#autoscale "Direct link to autoScale")

> **autoScale** : `boolean`

Autoscaling is a feature that automatically adjusts a price scale to fit the visible range of data. Note that overlay price scales are always auto-scaled.

#### Default Value[​](PriceScaleOptions.html#default-value "Direct link to Default Value")

`true`

* * *

### mode[​](PriceScaleOptions.html#mode "Direct link to mode")

> **mode** : [`PriceScaleMode`](../enumerations/PriceScaleMode.md)

Price scale mode.

#### Default Value[​](PriceScaleOptions.html#default-value-1 "Direct link to Default Value")
    
    
    {@link PriceScaleMode.Normal}  
    

* * *

### invertScale[​](PriceScaleOptions.html#invertscale "Direct link to invertScale")

> **invertScale** : `boolean`

Invert the price scale, so that a upwards trend is shown as a downwards trend and vice versa. Affects both the price scale and the data on the chart.

#### Default Value[​](PriceScaleOptions.html#default-value-2 "Direct link to Default Value")

`false`

* * *

### alignLabels[​](PriceScaleOptions.html#alignlabels "Direct link to alignLabels")

> **alignLabels** : `boolean`

Align price scale labels to prevent them from overlapping.

#### Default Value[​](PriceScaleOptions.html#default-value-3 "Direct link to Default Value")

`true`

* * *

### scaleMargins[​](PriceScaleOptions.html#scalemargins "Direct link to scaleMargins")

> **scaleMargins** : [`PriceScaleMargins`](PriceScaleMargins.md)

Price scale margins.

#### Default Value[​](PriceScaleOptions.html#default-value-4 "Direct link to Default Value")

`{ bottom: 0.1, top: 0.2 }`

#### Example[​](PriceScaleOptions.html#example "Direct link to Example")
    
    
    chart.priceScale('right').applyOptions({  
        scaleMargins: {  
            top: 0.8,  
            bottom: 0,  
        },  
    });  
    

* * *

### borderVisible[​](PriceScaleOptions.html#bordervisible "Direct link to borderVisible")

> **borderVisible** : `boolean`

Set true to draw a border between the price scale and the chart area.

#### Default Value[​](PriceScaleOptions.html#default-value-5 "Direct link to Default Value")

`true`

* * *

### borderColor[​](PriceScaleOptions.html#bordercolor "Direct link to borderColor")

> **borderColor** : `string`

Price scale border color.

#### Default Value[​](PriceScaleOptions.html#default-value-6 "Direct link to Default Value")

`'#2B2B43'`

* * *

### textColor?[​](PriceScaleOptions.html#textcolor "Direct link to textColor?")

> `optional` **textColor** : `string`

Price scale text color. If not provided [LayoutOptions.textColor](LayoutOptions.html#textcolor) is used.

#### Default Value[​](PriceScaleOptions.html#default-value-7 "Direct link to Default Value")

`undefined`

* * *

### entireTextOnly[​](PriceScaleOptions.html#entiretextonly "Direct link to entireTextOnly")

> **entireTextOnly** : `boolean`

Show top and bottom corner labels only if entire text is visible.

#### Default Value[​](PriceScaleOptions.html#default-value-8 "Direct link to Default Value")

`false`

* * *

### visible[​](PriceScaleOptions.html#visible "Direct link to visible")

> **visible** : `boolean`

Indicates if this price scale visible. Ignored by overlay price scales.

#### Default Value[​](PriceScaleOptions.html#default-value-9 "Direct link to Default Value")

`true` for the right price scale and `false` for the left. For the yield curve chart, the default is for the left scale to be visible.

* * *

### ticksVisible[​](PriceScaleOptions.html#ticksvisible "Direct link to ticksVisible")

> **ticksVisible** : `boolean`

Draw small horizontal line on price axis labels.

#### Default Value[​](PriceScaleOptions.html#default-value-10 "Direct link to Default Value")

`false`

* * *

### minimumWidth[​](PriceScaleOptions.html#minimumwidth "Direct link to minimumWidth")

> **minimumWidth** : `number`

Define a minimum width for the price scale. Note: This value will be exceeded if the price scale needs more space to display it's contents.

Setting a minimum width could be useful for ensuring that multiple charts positioned in a vertical stack each have an identical price scale width, or for plugins which require a bit more space within the price scale pane.

#### Default Value[​](PriceScaleOptions.html#default-value-11 "Direct link to Default Value")
    
    
    0  
    
