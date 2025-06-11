# API: Ihorzscalebehavior

*Source: docs\api\interfaces\IHorzScaleBehavior.html*

Version: 5.0

On this page

Class interface for Horizontal scale behavior

## Type parameters[​](IHorzScaleBehavior.html#type-parameters "Direct link to Type parameters")

• **HorzScaleItem**

## Methods[​](IHorzScaleBehavior.html#methods "Direct link to Methods")

### options()[​](IHorzScaleBehavior.html#options "Direct link to options\(\)")

> **options**(): [`ChartOptionsImpl`](ChartOptionsImpl.md)<`HorzScaleItem`>

Structure describing options of the chart.

#### Returns[​](IHorzScaleBehavior.html#returns "Direct link to Returns")

[`ChartOptionsImpl`](ChartOptionsImpl.md)<`HorzScaleItem`>

ChartOptionsBase

* * *

### setOptions()[​](IHorzScaleBehavior.html#setoptions "Direct link to setOptions\(\)")

> **setOptions**(`options`): `void`

Set the chart options. Note that this is different to `applyOptions` since the provided options will overwrite the current options instead of merging with the current options.

#### Parameters[​](IHorzScaleBehavior.html#parameters "Direct link to Parameters")

• **options** : [`ChartOptionsImpl`](ChartOptionsImpl.md)<`HorzScaleItem`>

Chart options to be set

#### Returns[​](IHorzScaleBehavior.html#returns-1 "Direct link to Returns")

`void`

void

* * *

### preprocessData()[​](IHorzScaleBehavior.html#preprocessdata "Direct link to preprocessData\(\)")

> **preprocessData**(`data`): `void`

Method to preprocess the data.

#### Parameters[​](IHorzScaleBehavior.html#parameters-1 "Direct link to Parameters")

• **data** : [`DataItem`](../type-aliases/DataItem.md)<`HorzScaleItem`> | [`DataItem`](../type-aliases/DataItem.md)<`HorzScaleItem`>[]

Data items for the series

#### Returns[​](IHorzScaleBehavior.html#returns-2 "Direct link to Returns")

`void`

void

* * *

### convertHorzItemToInternal()[​](IHorzScaleBehavior.html#converthorzitemtointernal "Direct link to convertHorzItemToInternal\(\)")

> **convertHorzItemToInternal**(`item`): `object`

Convert horizontal scale item into an internal horizontal scale item.

#### Parameters[​](IHorzScaleBehavior.html#parameters-2 "Direct link to Parameters")

• **item** : `HorzScaleItem`

item to be converted

#### Returns[​](IHorzScaleBehavior.html#returns-3 "Direct link to Returns")

`object`

InternalHorzScaleItem

##### [species][​](IHorzScaleBehavior.html#species "Direct link to \[species\]")

> **[species]** : `"InternalHorzScaleItem"`

The 'name' or species of the nominal.

* * *

### createConverterToInternalObj()[​](IHorzScaleBehavior.html#createconvertertointernalobj "Direct link to createConverterToInternalObj\(\)")

> **createConverterToInternalObj**(`data`): [`HorzScaleItemConverterToInternalObj`](../type-aliases/HorzScaleItemConverterToInternalObj.md)<`HorzScaleItem`>

Creates and returns a converter for changing series data into internal horizontal scale items.

#### Parameters[​](IHorzScaleBehavior.html#parameters-3 "Direct link to Parameters")

• **data** : ([`AreaData`](AreaData.md)<`HorzScaleItem`> | [`WhitespaceData`](WhitespaceData.md)<`HorzScaleItem`> | [`BarData`](BarData.md)<`HorzScaleItem`> | [`CandlestickData`](CandlestickData.md)<`HorzScaleItem`> | [`BaselineData`](BaselineData.md)<`HorzScaleItem`> | [`LineData`](LineData.md)<`HorzScaleItem`> | [`HistogramData`](HistogramData.md)<`HorzScaleItem`> | [`CustomData`](CustomData.md)<`HorzScaleItem`> | [`CustomSeriesWhitespaceData`](CustomSeriesWhitespaceData.md)<`HorzScaleItem`>)[]

series data

#### Returns[​](IHorzScaleBehavior.html#returns-4 "Direct link to Returns")

[`HorzScaleItemConverterToInternalObj`](../type-aliases/HorzScaleItemConverterToInternalObj.md)<`HorzScaleItem`>

HorzScaleItemConverterToInternalObj

* * *

### key()[​](IHorzScaleBehavior.html#key "Direct link to key\(\)")

> **key**(`internalItem`): [`InternalHorzScaleItemKey`](../type-aliases/InternalHorzScaleItemKey.md)

Returns the key for the specified horizontal scale item.

#### Parameters[​](IHorzScaleBehavior.html#parameters-4 "Direct link to Parameters")

• **internalItem** : `HorzScaleItem` | `object`

horizontal scale item for which the key should be returned

#### Returns[​](IHorzScaleBehavior.html#returns-5 "Direct link to Returns")

[`InternalHorzScaleItemKey`](../type-aliases/InternalHorzScaleItemKey.md)

InternalHorzScaleItemKey

* * *

### cacheKey()[​](IHorzScaleBehavior.html#cachekey "Direct link to cacheKey\(\)")

> **cacheKey**(`internalItem`): `number`

Returns the cache key for the specified horizontal scale item.

#### Parameters[​](IHorzScaleBehavior.html#parameters-5 "Direct link to Parameters")

• **internalItem**

horizontal scale item for which the cache key should be returned

• **internalItem.[species]** : `"InternalHorzScaleItem"`

The 'name' or species of the nominal.

#### Returns[​](IHorzScaleBehavior.html#returns-6 "Direct link to Returns")

`number`

number

* * *

### updateFormatter()[​](IHorzScaleBehavior.html#updateformatter "Direct link to updateFormatter\(\)")

> **updateFormatter**(`options`): `void`

Update the formatter with the localization options.

#### Parameters[​](IHorzScaleBehavior.html#parameters-6 "Direct link to Parameters")

• **options** : [`LocalizationOptions`](LocalizationOptions.md)<`HorzScaleItem`>

Localization options

#### Returns[​](IHorzScaleBehavior.html#returns-7 "Direct link to Returns")

`void`

void

* * *

### formatHorzItem()[​](IHorzScaleBehavior.html#formathorzitem "Direct link to formatHorzItem\(\)")

> **formatHorzItem**(`item`): `string`

Format the horizontal scale item into a display string.

#### Parameters[​](IHorzScaleBehavior.html#parameters-7 "Direct link to Parameters")

• **item**

horizontal scale item to be formatted as a string

• **item.[species]** : `"InternalHorzScaleItem"`

The 'name' or species of the nominal.

#### Returns[​](IHorzScaleBehavior.html#returns-8 "Direct link to Returns")

`string`

string

* * *

### formatTickmark()[​](IHorzScaleBehavior.html#formattickmark "Direct link to formatTickmark\(\)")

> **formatTickmark**(`item`, `localizationOptions`): `string`

Format the horizontal scale tickmark into a display string.

#### Parameters[​](IHorzScaleBehavior.html#parameters-8 "Direct link to Parameters")

• **item** : [`TickMark`](TickMark.md)

tickmark item

• **localizationOptions** : [`LocalizationOptions`](LocalizationOptions.md)<`HorzScaleItem`>

Localization options

#### Returns[​](IHorzScaleBehavior.html#returns-9 "Direct link to Returns")

`string`

string

* * *

### maxTickMarkWeight()[​](IHorzScaleBehavior.html#maxtickmarkweight "Direct link to maxTickMarkWeight\(\)")

> **maxTickMarkWeight**(`marks`): [`TickMarkWeightValue`](../type-aliases/TickMarkWeightValue.md)

Returns the maximum tickmark weight value for the specified tickmarks on the time scale.

#### Parameters[​](IHorzScaleBehavior.html#parameters-9 "Direct link to Parameters")

• **marks** : [`TimeMark`](TimeMark.md)[]

Timescale tick marks

#### Returns[​](IHorzScaleBehavior.html#returns-10 "Direct link to Returns")

[`TickMarkWeightValue`](../type-aliases/TickMarkWeightValue.md)

TickMarkWeightValue

* * *

### fillWeightsForPoints()[​](IHorzScaleBehavior.html#fillweightsforpoints "Direct link to fillWeightsForPoints\(\)")

> **fillWeightsForPoints**(`sortedTimePoints`, `startIndex`): `void`

Fill the weights for the sorted time scale points.

#### Parameters[​](IHorzScaleBehavior.html#parameters-10 "Direct link to Parameters")

• **sortedTimePoints** : readonly [`Mutable`](../type-aliases/Mutable.md) <[`TimeScalePoint`](TimeScalePoint.md)>[]

sorted time scale points

• **startIndex** : `number`

starting index

#### Returns[​](IHorzScaleBehavior.html#returns-11 "Direct link to Returns")

`void`

void

* * *

### shouldResetTickmarkLabels()?[​](IHorzScaleBehavior.html#shouldresettickmarklabels "Direct link to shouldResetTickmarkLabels\(\)?")

> `optional` **shouldResetTickmarkLabels**(`tickMarks`): `boolean`

If returns true, then the tick mark formatter will be called for all the visible tick marks even if the formatter has previously been called for a specific tick mark. This allows you to change the formatting on all the tick marks.

#### Parameters[​](IHorzScaleBehavior.html#parameters-11 "Direct link to Parameters")

• **tickMarks** : readonly [`TickMark`](TickMark.md)[]

array of tick marks

#### Returns[​](IHorzScaleBehavior.html#returns-12 "Direct link to Returns")

`boolean`

boolean
