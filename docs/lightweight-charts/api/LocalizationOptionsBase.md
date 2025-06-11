# API: Localizationoptionsbase

*Source: docs\api\interfaces\LocalizationOptionsBase.html*

Version: 5.0

On this page

Represents basic localization options

## Extended by[​](LocalizationOptionsBase.html#extended-by "Direct link to Extended by")

  * [`LocalizationOptions`](LocalizationOptions.md)

## Properties[​](LocalizationOptionsBase.html#properties "Direct link to Properties")

### locale[​](LocalizationOptionsBase.html#locale "Direct link to locale")

> **locale** : `string`

Current locale used to format dates. Uses the browser's language settings by default.

#### See[​](LocalizationOptionsBase.html#see "Direct link to See")

<https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl#Locale_identification_and_negotiation>

#### Default Value[​](LocalizationOptionsBase.html#default-value "Direct link to Default Value")

`navigator.language`

* * *

### priceFormatter?[​](LocalizationOptionsBase.html#priceformatter "Direct link to priceFormatter?")

> `optional` **priceFormatter** : [`PriceFormatterFn`](../type-aliases/PriceFormatterFn.md)

Override formatting of the price scale tick marks, labels and crosshair labels. Can be used for cases that can't be covered with built-in price formats.

#### See[​](LocalizationOptionsBase.html#see-1 "Direct link to See")

[PriceFormatCustom](PriceFormatCustom.md)

#### Default Value[​](LocalizationOptionsBase.html#default-value-1 "Direct link to Default Value")

`undefined`

* * *

### percentageFormatter?[​](LocalizationOptionsBase.html#percentageformatter "Direct link to percentageFormatter?")

> `optional` **percentageFormatter** : [`PercentageFormatterFn`](../type-aliases/PercentageFormatterFn.md)

Override formatting of the percentage scale tick marks, labels and crosshair labels. Can be used for cases that can't be covered with built-in percentage format.

#### Default Value[​](LocalizationOptionsBase.html#default-value-2 "Direct link to Default Value")

`undefined`
