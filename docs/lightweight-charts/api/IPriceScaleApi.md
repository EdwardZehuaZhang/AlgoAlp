# API: Ipricescaleapi

*Source: docs\api\interfaces\IPriceScaleApi.html*

Version: 5.0

On this page

Interface to control chart's price scale

## Methods[​](IPriceScaleApi.html#methods "Direct link to Methods")

### applyOptions()[​](IPriceScaleApi.html#applyoptions "Direct link to applyOptions\(\)")

> **applyOptions**(`options`): `void`

Applies new options to the price scale

#### Parameters[​](IPriceScaleApi.html#parameters "Direct link to Parameters")

• **options** : [`DeepPartial`](../type-aliases/DeepPartial.md) <[`PriceScaleOptions`](PriceScaleOptions.md)>

Any subset of options.

#### Returns[​](IPriceScaleApi.html#returns "Direct link to Returns")

`void`

* * *

### options()[​](IPriceScaleApi.html#options "Direct link to options\(\)")

> **options**(): `Readonly` <[`PriceScaleOptions`](PriceScaleOptions.md)>

Returns currently applied options of the price scale

#### Returns[​](IPriceScaleApi.html#returns-1 "Direct link to Returns")

`Readonly` <[`PriceScaleOptions`](PriceScaleOptions.md)>

Full set of currently applied options, including defaults

* * *

### width()[​](IPriceScaleApi.html#width "Direct link to width\(\)")

> **width**(): `number`

Returns a width of the price scale if it's visible or 0 if invisible.

#### Returns[​](IPriceScaleApi.html#returns-2 "Direct link to Returns")

`number`
