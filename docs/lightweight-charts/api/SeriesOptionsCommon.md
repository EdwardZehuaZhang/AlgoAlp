# API: Seriesoptionscommon

*Source: docs\api\interfaces\SeriesOptionsCommon.html*

Version: 5.0

On this page

Represents options common for all types of series

## Properties[​](SeriesOptionsCommon.html#properties "Direct link to Properties")

### lastValueVisible[​](SeriesOptionsCommon.html#lastvaluevisible "Direct link to lastValueVisible")

> **lastValueVisible** : `boolean`

Visibility of the label with the latest visible price on the price scale.

#### Default Value[​](SeriesOptionsCommon.html#default-value "Direct link to Default Value")

`true`, `false` for yield curve charts

* * *

### title[​](SeriesOptionsCommon.html#title "Direct link to title")

> **title** : `string`

You can name series when adding it to a chart. This name will be displayed on the label next to the last value label.

#### Default Value[​](SeriesOptionsCommon.html#default-value-1 "Direct link to Default Value")

`''`

* * *

### priceScaleId?[​](SeriesOptionsCommon.html#pricescaleid "Direct link to priceScaleId?")

> `optional` **priceScaleId** : `string`

Target price scale to bind new series to.

#### Default Value[​](SeriesOptionsCommon.html#default-value-2 "Direct link to Default Value")

`'right'` if right scale is visible and `'left'` otherwise

* * *

### visible[​](SeriesOptionsCommon.html#visible "Direct link to visible")

> **visible** : `boolean`

Visibility of the series. If the series is hidden, everything including price lines, baseline, price labels and markers, will also be hidden. Please note that hiding a series is not equivalent to deleting it, since hiding does not affect the timeline at all, unlike deleting where the timeline can be changed (some points can be deleted).

#### Default Value[​](SeriesOptionsCommon.html#default-value-3 "Direct link to Default Value")

`true`

* * *

### priceLineVisible[​](SeriesOptionsCommon.html#pricelinevisible "Direct link to priceLineVisible")

> **priceLineVisible** : `boolean`

Show the price line. Price line is a horizontal line indicating the last price of the series.

#### Default Value[​](SeriesOptionsCommon.html#default-value-4 "Direct link to Default Value")

`true`, `false` for yield curve charts

* * *

### priceLineSource[​](SeriesOptionsCommon.html#pricelinesource "Direct link to priceLineSource")

> **priceLineSource** : [`PriceLineSource`](../enumerations/PriceLineSource.md)

The source to use for the value of the price line.

#### Default Value[​](SeriesOptionsCommon.html#default-value-5 "Direct link to Default Value")
    
    
    {@link PriceLineSource.LastBar}  
    

* * *

### priceLineWidth[​](SeriesOptionsCommon.html#pricelinewidth "Direct link to priceLineWidth")

> **priceLineWidth** : [`LineWidth`](../type-aliases/LineWidth.md)

Width of the price line.

#### Default Value[​](SeriesOptionsCommon.html#default-value-6 "Direct link to Default Value")

`1`

* * *

### priceLineColor[​](SeriesOptionsCommon.html#pricelinecolor "Direct link to priceLineColor")

> **priceLineColor** : `string`

Color of the price line. By default, its color is set by the last bar color (or by line color on Line and Area charts).

#### Default Value[​](SeriesOptionsCommon.html#default-value-7 "Direct link to Default Value")

`''`

* * *

### priceLineStyle[​](SeriesOptionsCommon.html#pricelinestyle "Direct link to priceLineStyle")

> **priceLineStyle** : [`LineStyle`](../enumerations/LineStyle.md)

Price line style.

#### Default Value[​](SeriesOptionsCommon.html#default-value-8 "Direct link to Default Value")
    
    
    {@link LineStyle.Dashed}  
    

* * *

### priceFormat[​](SeriesOptionsCommon.html#priceformat "Direct link to priceFormat")

> **priceFormat** : [`PriceFormat`](../type-aliases/PriceFormat.md)

Price format.

#### Default Value[​](SeriesOptionsCommon.html#default-value-9 "Direct link to Default Value")

`{ type: 'price', precision: 2, minMove: 0.01 }`

* * *

### baseLineVisible[​](SeriesOptionsCommon.html#baselinevisible "Direct link to baseLineVisible")

> **baseLineVisible** : `boolean`

Visibility of base line. Suitable for percentage and `IndexedTo100` scales.

#### Default Value[​](SeriesOptionsCommon.html#default-value-10 "Direct link to Default Value")

`true`

* * *

### baseLineColor[​](SeriesOptionsCommon.html#baselinecolor "Direct link to baseLineColor")

> **baseLineColor** : `string`

Color of the base line in `IndexedTo100` mode.

#### Default Value[​](SeriesOptionsCommon.html#default-value-11 "Direct link to Default Value")

`'#B2B5BE'`

* * *

### baseLineWidth[​](SeriesOptionsCommon.html#baselinewidth "Direct link to baseLineWidth")

> **baseLineWidth** : [`LineWidth`](../type-aliases/LineWidth.md)

Base line width. Suitable for percentage and `IndexedTo10` scales.

#### Default Value[​](SeriesOptionsCommon.html#default-value-12 "Direct link to Default Value")

`1`

* * *

### baseLineStyle[​](SeriesOptionsCommon.html#baselinestyle "Direct link to baseLineStyle")

> **baseLineStyle** : [`LineStyle`](../enumerations/LineStyle.md)

Base line style. Suitable for percentage and indexedTo100 scales.

#### Default Value[​](SeriesOptionsCommon.html#default-value-13 "Direct link to Default Value")
    
    
    {@link LineStyle.Solid}  
    

* * *

### autoscaleInfoProvider?[​](SeriesOptionsCommon.html#autoscaleinfoprovider "Direct link to autoscaleInfoProvider?")

> `optional` **autoscaleInfoProvider** : [`AutoscaleInfoProvider`](../type-aliases/AutoscaleInfoProvider.md)

Override the default [AutoscaleInfo](AutoscaleInfo.md) provider. By default, the chart scales data automatically based on visible data range. However, for some reasons one could require overriding this behavior.

#### Default Value[​](SeriesOptionsCommon.html#default-value-14 "Direct link to Default Value")

`undefined`

#### Examples[​](SeriesOptionsCommon.html#examples "Direct link to Examples")
    
    
    const firstSeries = chart.addSeries(LineSeries, {  
        autoscaleInfoProvider: () => ({  
            priceRange: {  
                minValue: 0,  
                maxValue: 100,  
            },  
        }),  
    });  
    
    
    
    const firstSeries = chart.addSeries(LineSeries, {  
        autoscaleInfoProvider: () => ({  
            priceRange: {  
                minValue: 0,  
                maxValue: 100,  
            },  
            margins: {  
                above: 10,  
                below: 10,  
            },  
        }),  
    });  
    
    
    
    const firstSeries = chart.addSeries(LineSeries, {  
        autoscaleInfoProvider: original => {  
            const res = original();  
            if (res !== null) {  
                res.priceRange.minValue -= 10;  
                res.priceRange.maxValue += 10;  
            }  
            return res;  
        },  
    });  
    
