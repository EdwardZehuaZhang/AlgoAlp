# API: Createyieldcurvechart

*Source: docs\api\functions\createYieldCurveChart.html*

Version: 5.0

On this page

> **createYieldCurveChart**(`container`, `options`?): [`IYieldCurveChartApi`](../interfaces/IYieldCurveChartApi.md)

Creates a yield curve chart with the specified options.

A yield curve chart differs from the default chart type in the following ways:

  * Horizontal scale is linearly spaced, and defined in monthly time duration units
  * Whitespace is ignored for the crosshair and grid lines

## Parameters[​](createYieldCurveChart.html#parameters "Direct link to Parameters")

• **container** : `string` | `HTMLElement`

ID of HTML element or element itself

• **options?** : [`DeepPartial`](../type-aliases/DeepPartial.md) <[`YieldCurveChartOptions`](../interfaces/YieldCurveChartOptions.md)>

The yield chart options.

## Returns[​](createYieldCurveChart.html#returns "Direct link to Returns")

[`IYieldCurveChartApi`](../interfaces/IYieldCurveChartApi.md)

An interface to the created chart
