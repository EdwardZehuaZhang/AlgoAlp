# API: Createoptionschart

*Source: docs\api\functions\createOptionsChart.html*

Version: 5.0

On this page

> **createOptionsChart**(`container`, `options`?): [`IChartApiBase`](../interfaces/IChartApiBase.md)<`number`>

Creates an 'options' chart with price values on the horizontal scale.

This function is used to create a specialized chart type where the horizontal scale represents price values instead of time. It's particularly useful for visualizing option chains, price distributions, or any data where price is the primary x-axis metric.

## Parameters[​](createOptionsChart.html#parameters "Direct link to Parameters")

• **container** : `string` | `HTMLElement`

The DOM element or its id where the chart will be rendered.

• **options?** : [`DeepPartial`](../type-aliases/DeepPartial.md) <[`PriceChartOptions`](../interfaces/PriceChartOptions.md)>

Optional configuration options for the price chart.

## Returns[​](createOptionsChart.html#returns "Direct link to Returns")

[`IChartApiBase`](../interfaces/IChartApiBase.md)<`number`>

An instance of IChartApiBase configured for price-based horizontal scaling.
