# API: Chartoptionsbase

*Source: docs\api\interfaces\ChartOptionsBase.html*

Version: 5.0

On this page

Represents common chart options

## Extended by[​](ChartOptionsBase.html#extended-by "Direct link to Extended by")

  * [`ChartOptionsImpl`](ChartOptionsImpl.md)

## Properties[​](ChartOptionsBase.html#properties "Direct link to Properties")

### width[​](ChartOptionsBase.html#width "Direct link to width")

> **width** : `number`

Width of the chart in pixels

#### Default Value[​](ChartOptionsBase.html#default-value "Direct link to Default Value")

If `0` (default) or none value provided, then a size of the widget will be calculated based its container's size.

* * *

### height[​](ChartOptionsBase.html#height "Direct link to height")

> **height** : `number`

Height of the chart in pixels

#### Default Value[​](ChartOptionsBase.html#default-value-1 "Direct link to Default Value")

If `0` (default) or none value provided, then a size of the widget will be calculated based its container's size.

* * *

### autoSize[​](ChartOptionsBase.html#autosize "Direct link to autoSize")

> **autoSize** : `boolean`

Setting this flag to `true` will make the chart watch the chart container's size and automatically resize the chart to fit its container whenever the size changes.

This feature requires [`ResizeObserver`](https://developer.mozilla.org/en-US/docs/Web/API/ResizeObserver) class to be available in the global scope. Note that calling code is responsible for providing a polyfill if required. If the global scope does not have `ResizeObserver`, a warning will appear and the flag will be ignored.

Please pay attention that `autoSize` option and explicit sizes options `width` and `height` don't conflict with one another. If you specify `autoSize` flag, then `width` and `height` options will be ignored unless `ResizeObserver` has failed. If it fails then the values will be used as fallback.

The flag `autoSize` could also be set with and unset with `applyOptions` function.
    
    
    const chart = LightweightCharts.createChart(document.body, {  
        autoSize: true,  
    });  
    

* * *

### layout[​](ChartOptionsBase.html#layout "Direct link to layout")

> **layout** : [`LayoutOptions`](LayoutOptions.md)

Layout options

* * *

### leftPriceScale[​](ChartOptionsBase.html#leftpricescale "Direct link to leftPriceScale")

> **leftPriceScale** : [`PriceScaleOptions`](PriceScaleOptions.md)

Left price scale options

* * *

### rightPriceScale[​](ChartOptionsBase.html#rightpricescale "Direct link to rightPriceScale")

> **rightPriceScale** : [`PriceScaleOptions`](PriceScaleOptions.md)

Right price scale options

* * *

### overlayPriceScales[​](ChartOptionsBase.html#overlaypricescales "Direct link to overlayPriceScales")

> **overlayPriceScales** : [`OverlayPriceScaleOptions`](../type-aliases/OverlayPriceScaleOptions.md)

Overlay price scale options

* * *

### timeScale[​](ChartOptionsBase.html#timescale "Direct link to timeScale")

> **timeScale** : [`HorzScaleOptions`](HorzScaleOptions.md)

Time scale options

* * *

### crosshair[​](ChartOptionsBase.html#crosshair "Direct link to crosshair")

> **crosshair** : [`CrosshairOptions`](CrosshairOptions.md)

The crosshair shows the intersection of the price and time scale values at any point on the chart.

* * *

### grid[​](ChartOptionsBase.html#grid "Direct link to grid")

> **grid** : [`GridOptions`](GridOptions.md)

A grid is represented in the chart background as a vertical and horizontal lines drawn at the levels of visible marks of price and the time scales.

* * *

### handleScroll[​](ChartOptionsBase.html#handlescroll "Direct link to handleScroll")

> **handleScroll** : `boolean` | [`HandleScrollOptions`](HandleScrollOptions.md)

Scroll options, or a boolean flag that enables/disables scrolling

* * *

### handleScale[​](ChartOptionsBase.html#handlescale "Direct link to handleScale")

> **handleScale** : `boolean` | [`HandleScaleOptions`](HandleScaleOptions.md)

Scale options, or a boolean flag that enables/disables scaling

* * *

### kineticScroll[​](ChartOptionsBase.html#kineticscroll "Direct link to kineticScroll")

> **kineticScroll** : [`KineticScrollOptions`](KineticScrollOptions.md)

Kinetic scroll options

* * *

### trackingMode[​](ChartOptionsBase.html#trackingmode "Direct link to trackingMode")

> **trackingMode** : [`TrackingModeOptions`](TrackingModeOptions.md)

Represent options for the tracking mode's behavior.

Mobile users will not have the ability to see the values/dates like they do on desktop. To see it, they should enter the tracking mode. The tracking mode will deactivate the scrolling and make it possible to check values and dates.

* * *

### localization[​](ChartOptionsBase.html#localization "Direct link to localization")

> **localization** : [`LocalizationOptionsBase`](LocalizationOptionsBase.md)

Basic localization options
