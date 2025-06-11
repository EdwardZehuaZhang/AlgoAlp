# API: Yieldcurvechartoptions

*Source: docs\api\interfaces\YieldCurveChartOptions.html*

Version: 5.0

On this page

Extended chart options that include yield curve specific options. This interface combines the standard chart options with yield curve options.

## Extends[​](YieldCurveChartOptions.html#extends "Direct link to Extends")

  * [`ChartOptionsImpl`](ChartOptionsImpl.md)<`number`>

## Properties[​](YieldCurveChartOptions.html#properties "Direct link to Properties")

### width[​](YieldCurveChartOptions.html#width "Direct link to width")

> **width** : `number`

Width of the chart in pixels

#### Default Value[​](YieldCurveChartOptions.html#default-value "Direct link to Default Value")

If `0` (default) or none value provided, then a size of the widget will be calculated based its container's size.

#### Inherited from[​](YieldCurveChartOptions.html#inherited-from "Direct link to Inherited from")

[`ChartOptionsImpl`](ChartOptionsImpl.md) . [`width`](ChartOptionsImpl.html#width)

* * *

### height[​](YieldCurveChartOptions.html#height "Direct link to height")

> **height** : `number`

Height of the chart in pixels

#### Default Value[​](YieldCurveChartOptions.html#default-value-1 "Direct link to Default Value")

If `0` (default) or none value provided, then a size of the widget will be calculated based its container's size.

#### Inherited from[​](YieldCurveChartOptions.html#inherited-from-1 "Direct link to Inherited from")

[`ChartOptionsImpl`](ChartOptionsImpl.md) . [`height`](ChartOptionsImpl.html#height)

* * *

### autoSize[​](YieldCurveChartOptions.html#autosize "Direct link to autoSize")

> **autoSize** : `boolean`

Setting this flag to `true` will make the chart watch the chart container's size and automatically resize the chart to fit its container whenever the size changes.

This feature requires [`ResizeObserver`](https://developer.mozilla.org/en-US/docs/Web/API/ResizeObserver) class to be available in the global scope. Note that calling code is responsible for providing a polyfill if required. If the global scope does not have `ResizeObserver`, a warning will appear and the flag will be ignored.

Please pay attention that `autoSize` option and explicit sizes options `width` and `height` don't conflict with one another. If you specify `autoSize` flag, then `width` and `height` options will be ignored unless `ResizeObserver` has failed. If it fails then the values will be used as fallback.

The flag `autoSize` could also be set with and unset with `applyOptions` function.
    
    
    const chart = LightweightCharts.createChart(document.body, {  
        autoSize: true,  
    });  
    

#### Inherited from[​](YieldCurveChartOptions.html#inherited-from-2 "Direct link to Inherited from")

[`ChartOptionsImpl`](ChartOptionsImpl.md) . [`autoSize`](ChartOptionsImpl.html#autosize)

* * *

### layout[​](YieldCurveChartOptions.html#layout "Direct link to layout")

> **layout** : [`LayoutOptions`](LayoutOptions.md)

Layout options

#### Inherited from[​](YieldCurveChartOptions.html#inherited-from-3 "Direct link to Inherited from")

[`ChartOptionsImpl`](ChartOptionsImpl.md) . [`layout`](ChartOptionsImpl.html#layout)

* * *

### leftPriceScale[​](YieldCurveChartOptions.html#leftpricescale "Direct link to leftPriceScale")

> **leftPriceScale** : [`PriceScaleOptions`](PriceScaleOptions.md)

Left price scale options

#### Inherited from[​](YieldCurveChartOptions.html#inherited-from-4 "Direct link to Inherited from")

[`ChartOptionsImpl`](ChartOptionsImpl.md) . [`leftPriceScale`](ChartOptionsImpl.html#leftpricescale)

* * *

### rightPriceScale[​](YieldCurveChartOptions.html#rightpricescale "Direct link to rightPriceScale")

> **rightPriceScale** : [`PriceScaleOptions`](PriceScaleOptions.md)

Right price scale options

#### Inherited from[​](YieldCurveChartOptions.html#inherited-from-5 "Direct link to Inherited from")

[`ChartOptionsImpl`](ChartOptionsImpl.md) . [`rightPriceScale`](ChartOptionsImpl.html#rightpricescale)

* * *

### overlayPriceScales[​](YieldCurveChartOptions.html#overlaypricescales "Direct link to overlayPriceScales")

> **overlayPriceScales** : [`OverlayPriceScaleOptions`](../type-aliases/OverlayPriceScaleOptions.md)

Overlay price scale options

#### Inherited from[​](YieldCurveChartOptions.html#inherited-from-6 "Direct link to Inherited from")

[`ChartOptionsImpl`](ChartOptionsImpl.md) . [`overlayPriceScales`](ChartOptionsImpl.html#overlaypricescales)

* * *

### timeScale[​](YieldCurveChartOptions.html#timescale "Direct link to timeScale")

> **timeScale** : [`HorzScaleOptions`](HorzScaleOptions.md)

Time scale options

#### Inherited from[​](YieldCurveChartOptions.html#inherited-from-7 "Direct link to Inherited from")

[`ChartOptionsImpl`](ChartOptionsImpl.md) . [`timeScale`](ChartOptionsImpl.html#timescale)

* * *

### crosshair[​](YieldCurveChartOptions.html#crosshair "Direct link to crosshair")

> **crosshair** : [`CrosshairOptions`](CrosshairOptions.md)

The crosshair shows the intersection of the price and time scale values at any point on the chart.

#### Inherited from[​](YieldCurveChartOptions.html#inherited-from-8 "Direct link to Inherited from")

[`ChartOptionsImpl`](ChartOptionsImpl.md) . [`crosshair`](ChartOptionsImpl.html#crosshair)

* * *

### grid[​](YieldCurveChartOptions.html#grid "Direct link to grid")

> **grid** : [`GridOptions`](GridOptions.md)

A grid is represented in the chart background as a vertical and horizontal lines drawn at the levels of visible marks of price and the time scales.

#### Inherited from[​](YieldCurveChartOptions.html#inherited-from-9 "Direct link to Inherited from")

[`ChartOptionsImpl`](ChartOptionsImpl.md) . [`grid`](ChartOptionsImpl.html#grid)

* * *

### handleScroll[​](YieldCurveChartOptions.html#handlescroll "Direct link to handleScroll")

> **handleScroll** : `boolean` | [`HandleScrollOptions`](HandleScrollOptions.md)

Scroll options, or a boolean flag that enables/disables scrolling

#### Inherited from[​](YieldCurveChartOptions.html#inherited-from-10 "Direct link to Inherited from")

[`ChartOptionsImpl`](ChartOptionsImpl.md) . [`handleScroll`](ChartOptionsImpl.html#handlescroll)

* * *

### handleScale[​](YieldCurveChartOptions.html#handlescale "Direct link to handleScale")

> **handleScale** : `boolean` | [`HandleScaleOptions`](HandleScaleOptions.md)

Scale options, or a boolean flag that enables/disables scaling

#### Inherited from[​](YieldCurveChartOptions.html#inherited-from-11 "Direct link to Inherited from")

[`ChartOptionsImpl`](ChartOptionsImpl.md) . [`handleScale`](ChartOptionsImpl.html#handlescale)

* * *

### kineticScroll[​](YieldCurveChartOptions.html#kineticscroll "Direct link to kineticScroll")

> **kineticScroll** : [`KineticScrollOptions`](KineticScrollOptions.md)

Kinetic scroll options

#### Inherited from[​](YieldCurveChartOptions.html#inherited-from-12 "Direct link to Inherited from")

[`ChartOptionsImpl`](ChartOptionsImpl.md) . [`kineticScroll`](ChartOptionsImpl.html#kineticscroll)

* * *

### trackingMode[​](YieldCurveChartOptions.html#trackingmode "Direct link to trackingMode")

> **trackingMode** : [`TrackingModeOptions`](TrackingModeOptions.md)

Represent options for the tracking mode's behavior.

Mobile users will not have the ability to see the values/dates like they do on desktop. To see it, they should enter the tracking mode. The tracking mode will deactivate the scrolling and make it possible to check values and dates.

#### Inherited from[​](YieldCurveChartOptions.html#inherited-from-13 "Direct link to Inherited from")

[`ChartOptionsImpl`](ChartOptionsImpl.md) . [`trackingMode`](ChartOptionsImpl.html#trackingmode)

* * *

### localization[​](YieldCurveChartOptions.html#localization "Direct link to localization")

> **localization** : [`LocalizationOptions`](LocalizationOptions.md)<`number`>

Localization options.

#### Inherited from[​](YieldCurveChartOptions.html#inherited-from-14 "Direct link to Inherited from")

[`ChartOptionsImpl`](ChartOptionsImpl.md) . [`localization`](ChartOptionsImpl.html#localization)

* * *

### yieldCurve[​](YieldCurveChartOptions.html#yieldcurve "Direct link to yieldCurve")

> **yieldCurve** : [`YieldCurveOptions`](YieldCurveOptions.md)

Yield curve specific options. This object contains all the settings related to how the yield curve is displayed and behaves.
