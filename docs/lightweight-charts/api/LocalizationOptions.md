# API: Localizationoptions

*Source: docs\api\interfaces\LocalizationOptions.html*

Version: 5.0

On this page

Represents options for formatting dates, times, and prices according to a locale.

## Extends[​](LocalizationOptions.html#extends "Direct link to Extends")

  * [`LocalizationOptionsBase`](LocalizationOptionsBase.md)

## Extended by[​](LocalizationOptions.html#extended-by "Direct link to Extended by")

  * [`PriceChartLocalizationOptions`](PriceChartLocalizationOptions.md)

## Type parameters[​](LocalizationOptions.html#type-parameters "Direct link to Type parameters")

• **HorzScaleItem**

## Properties[​](LocalizationOptions.html#properties "Direct link to Properties")

### timeFormatter?[​](LocalizationOptions.html#timeformatter "Direct link to timeFormatter?")

> `optional` **timeFormatter** : [`TimeFormatterFn`](../type-aliases/TimeFormatterFn.md)<`HorzScaleItem`>

Override formatting of the time scale crosshair label.

#### Default Value[​](LocalizationOptions.html#default-value "Direct link to Default Value")

`undefined`

* * *

### dateFormat[​](LocalizationOptions.html#dateformat "Direct link to dateFormat")

> **dateFormat** : `string`

Date formatting string.

Can contain `yyyy`, `yy`, `MMMM`, `MMM`, `MM` and `dd` literals which will be replaced with corresponding date's value.

Ignored if [timeFormatter](LocalizationOptions.html#timeformatter) has been specified.

#### Default Value[​](LocalizationOptions.html#default-value-1 "Direct link to Default Value")

`'dd MMM \'yy'`

* * *

### locale[​](LocalizationOptions.html#locale "Direct link to locale")

> **locale** : `string`

Current locale used to format dates. Uses the browser's language settings by default.

#### See[​](LocalizationOptions.html#see "Direct link to See")

<https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl#Locale_identification_and_negotiation>

#### Default Value[​](LocalizationOptions.html#default-value-2 "Direct link to Default Value")

`navigator.language`

#### Inherited from[​](LocalizationOptions.html#inherited-from "Direct link to Inherited from")

[`LocalizationOptionsBase`](LocalizationOptionsBase.md) . [`locale`](LocalizationOptionsBase.html#locale)

* * *

### priceFormatter?[​](LocalizationOptions.html#priceformatter "Direct link to priceFormatter?")

> `optional` **priceFormatter** : [`PriceFormatterFn`](../type-aliases/PriceFormatterFn.md)

Override formatting of the price scale tick marks, labels and crosshair labels. Can be used for cases that can't be covered with built-in price formats.

#### See[​](LocalizationOptions.html#see-1 "Direct link to See")

[PriceFormatCustom](PriceFormatCustom.md)

#### Default Value[​](LocalizationOptions.html#default-value-3 "Direct link to Default Value")

`undefined`

#### Inherited from[​](LocalizationOptions.html#inherited-from-1 "Direct link to Inherited from")

[`LocalizationOptionsBase`](LocalizationOptionsBase.md) . [`priceFormatter`](LocalizationOptionsBase.html#priceformatter)

* * *

### percentageFormatter?[​](LocalizationOptions.html#percentageformatter "Direct link to percentageFormatter?")

> `optional` **percentageFormatter** : [`PercentageFormatterFn`](../type-aliases/PercentageFormatterFn.md)

Override formatting of the percentage scale tick marks, labels and crosshair labels. Can be used for cases that can't be covered with built-in percentage format.

#### Default Value[​](LocalizationOptions.html#default-value-4 "Direct link to Default Value")

`undefined`

#### Inherited from[​](LocalizationOptions.html#inherited-from-2 "Direct link to Inherited from")

[`LocalizationOptionsBase`](LocalizationOptionsBase.md) . [`percentageFormatter`](LocalizationOptionsBase.html#percentageformatter)
