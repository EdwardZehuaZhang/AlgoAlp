# API: Priceformatbuiltin

*Source: docs\api\interfaces\PriceFormatBuiltIn.html*

Version: 5.0

On this page

Represents series value formatting options. The precision and minMove properties allow wide customization of formatting.

## Examples[​](PriceFormatBuiltIn.html#examples "Direct link to Examples")
    
    
    `minMove=0.01`, `precision` is not specified - prices will change like 1.13, 1.14, 1.15 etc.  
    
    
    
    `minMove=0.01`, `precision=3` - prices will change like 1.130, 1.140, 1.150 etc.  
    
    
    
    `minMove=0.05`, `precision` is not specified - prices will change like 1.10, 1.15, 1.20 etc.  
    

## Properties[​](PriceFormatBuiltIn.html#properties "Direct link to Properties")

### type[​](PriceFormatBuiltIn.html#type "Direct link to type")

> **type** : `"percent"` | `"price"` | `"volume"`

Built-in price formats:

  * `'price'` is the most common choice; it allows customization of precision and rounding of prices.
  * `'volume'` uses abbreviation for formatting prices like `1.2K` or `12.67M`.
  * `'percent'` uses `%` sign at the end of prices.

* * *

### precision[​](PriceFormatBuiltIn.html#precision "Direct link to precision")

> **precision** : `number`

Number of digits after the decimal point. If it is not set, then its value is calculated automatically based on minMove.

#### Default Value[​](PriceFormatBuiltIn.html#default-value "Direct link to Default Value")

`2` if both [minMove](PriceFormatBuiltIn.html#minmove) and [precision](PriceFormatBuiltIn.html#precision) are not provided, calculated automatically based on [minMove](PriceFormatBuiltIn.html#minmove) otherwise.

* * *

### minMove[​](PriceFormatBuiltIn.html#minmove "Direct link to minMove")

> **minMove** : `number`

The minimum possible step size for price value movement. This value shouldn't have more decimal digits than the precision.

#### Default Value[​](PriceFormatBuiltIn.html#default-value-1 "Direct link to Default Value")

`0.01`
