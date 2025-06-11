# API: Pricechartlocalizationoptions

*Source: docs\api\interfaces\PriceChartLocalizationOptions.html*

Version: 5.0

On this page

Extends LocalizationOptions for price-based charts. Includes settings specific to formatting price values on the horizontal scale.

## Extends[​](PriceChartLocalizationOptions.html#extends "Direct link to Extends")

  * [`LocalizationOptions`](LocalizationOptions.md) <[`HorzScalePriceItem`](../type-aliases/HorzScalePriceItem.md)>

## Properties[​](PriceChartLocalizationOptions.html#properties "Direct link to Properties")

### timeFormatter?[​](PriceChartLocalizationOptions.html#timeformatter "Direct link to timeFormatter?")

> `optional` **timeFormatter** : [`TimeFormatterFn`](../type-aliases/TimeFormatterFn.md)<`number`>

Override formatting of the time scale crosshair label.

#### Default Value[​](PriceChartLocalizationOptions.html#default-value "Direct link to Default Value")

`undefined`

#### Inherited from[​](PriceChartLocalizationOptions.html#inherited-from "Direct link to Inherited from")

[`LocalizationOptions`](LocalizationOptions.md) . [`timeFormatter`](LocalizationOptions.html#timeformatter)

* * *

### dateFormat[​](PriceChartLocalizationOptions.html#dateformat "Direct link to dateFormat")

> **dateFormat** : `string`

Date formatting string.

Can contain `yyyy`, `yy`, `MMMM`, `MMM`, `MM` and `dd` literals which will be replaced with corresponding date's value.

Ignored if [timeFormatter](LocalizationOptions.html#timeformatter) has been specified.

#### Default Value[​](PriceChartLocalizationOptions.html#default-value-1 "Direct link to Default Value")

`'dd MMM \'yy'`

#### Inherited from[​](PriceChartLocalizationOptions.html#inherited-from-1 "Direct link to Inherited from")

[`LocalizationOptions`](LocalizationOptions.md) . [`dateFormat`](LocalizationOptions.html#dateformat)

* * *

### locale[​](PriceChartLocalizationOptions.html#locale "Direct link to locale")

> **locale** : `string`

Current locale used to format dates. Uses the browser's language settings by default.

#### See[​](PriceChartLocalizationOptions.html#see "Direct link to See")

<https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl#Locale_identification_and_negotiation>

#### Default Value[​](PriceChartLocalizationOptions.html#default-value-2 "Direct link to Default Value")

`navigator.language`

#### Inherited from[​](PriceChartLocalizationOptions.html#inherited-from-2 "Direct link to Inherited from")

[`LocalizationOptions`](LocalizationOptions.md) . [`locale`](LocalizationOptions.html#locale)

* * *

### priceFormatter?[​](PriceChartLocalizationOptions.html#priceformatter "Direct link to priceFormatter?")

> `optional` **priceFormatter** : [`PriceFormatterFn`](../type-aliases/PriceFormatterFn.md)

Override formatting of the price scale tick marks, labels and crosshair labels. Can be used for cases that can't be covered with built-in price formats.

#### See[​](PriceChartLocalizationOptions.html#see-1 "Direct link to See")

[PriceFormatCustom](PriceFormatCustom.md)

#### Default Value[​](PriceChartLocalizationOptions.html#default-value-3 "Direct link to Default Value")

`undefined`

#### Inherited from[​](PriceChartLocalizationOptions.html#inherited-from-3 "Direct link to Inherited from")

[`LocalizationOptions`](LocalizationOptions.md) . [`priceFormatter`](LocalizationOptions.html#priceformatter)

* * *

### percentageFormatter?[​](PriceChartLocalizationOptions.html#percentageformatter "Direct link to percentageFormatter?")

> `optional` **percentageFormatter** : [`PercentageFormatterFn`](../type-aliases/PercentageFormatterFn.md)

Override formatting of the percentage scale tick marks, labels and crosshair labels. Can be used for cases that can't be covered with built-in percentage format.

#### Default Value[​](PriceChartLocalizationOptions.html#default-value-4 "Direct link to Default Value")

`undefined`

#### Inherited from[​](PriceChartLocalizationOptions.html#inherited-from-4 "Direct link to Inherited from")

[`LocalizationOptions`](LocalizationOptions.md) . [`percentageFormatter`](LocalizationOptions.html#percentageformatter)

* * *

### precision[​](PriceChartLocalizationOptions.html#precision "Direct link to precision")

> **precision** : `number`

The number of decimal places to display for price values on the horizontal scale.
