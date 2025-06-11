# API: Priceformatcustom

*Source: docs\api\interfaces\PriceFormatCustom.html*

Version: 5.0

On this page

Represents series value formatting options.

## Properties[​](PriceFormatCustom.html#properties "Direct link to Properties")

### type[​](PriceFormatCustom.html#type "Direct link to type")

> **type** : `"custom"`

The custom price format.

* * *

### formatter[​](PriceFormatCustom.html#formatter "Direct link to formatter")

> **formatter** : [`PriceFormatterFn`](../type-aliases/PriceFormatterFn.md)

Override price formatting behaviour. Can be used for cases that can't be covered with built-in price formats.

* * *

### minMove[​](PriceFormatCustom.html#minmove "Direct link to minMove")

> **minMove** : `number`

The minimum possible step size for price value movement.

#### Default Value[​](PriceFormatCustom.html#default-value "Direct link to Default Value")

`0.01`
