# API: Createchartex

*Source: docs\api\functions\createChartEx.html*

Version: 5.0

On this page

> **createChartEx** <`HorzScaleItem`, `THorzScaleBehavior`>(`container`, `horzScaleBehavior`, `options`?): [`IChartApiBase`](../interfaces/IChartApiBase.md)<`HorzScaleItem`>

This function is the main entry point of the Lightweight Charting Library. If you are using time values for the horizontal scale then it is recommended that you rather use the [createChart](createChart.md) function.

## Type parameters[​](createChartEx.html#type-parameters "Direct link to Type parameters")

• **HorzScaleItem**

type of points on the horizontal scale

• **THorzScaleBehavior** _extends_ [`IHorzScaleBehavior`](../interfaces/IHorzScaleBehavior.md)<`HorzScaleItem`>

type of horizontal axis strategy that encapsulate all the specific behaviors of the horizontal scale type

## Parameters[​](createChartEx.html#parameters "Direct link to Parameters")

• **container** : `string` | `HTMLElement`

ID of HTML element or element itself

• **horzScaleBehavior** : `THorzScaleBehavior`

Horizontal scale behavior

• **options?** : [`DeepPartial`](../type-aliases/DeepPartial.md)<`ReturnType`<`THorzScaleBehavior`[`"options"`]>>

Any subset of options to be applied at start.

## Returns[​](createChartEx.html#returns "Direct link to Returns")

[`IChartApiBase`](../interfaces/IChartApiBase.md)<`HorzScaleItem`>

An interface to the created chart
