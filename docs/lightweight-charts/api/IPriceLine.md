# API: Ipriceline

*Source: docs\api\interfaces\IPriceLine.html*

Version: 5.0

On this page

Represents the interface for interacting with price lines.

## Methods[​](IPriceLine.html#methods "Direct link to Methods")

### applyOptions()[​](IPriceLine.html#applyoptions "Direct link to applyOptions\(\)")

> **applyOptions**(`options`): `void`

Apply options to the price line.

#### Parameters[​](IPriceLine.html#parameters "Direct link to Parameters")

• **options** : `Partial` <[`PriceLineOptions`](PriceLineOptions.md)>

Any subset of options.

#### Returns[​](IPriceLine.html#returns "Direct link to Returns")

`void`

#### Example[​](IPriceLine.html#example "Direct link to Example")
    
    
    priceLine.applyOptions({  
        price: 90.0,  
        color: 'red',  
        lineWidth: 3,  
        lineStyle: LightweightCharts.LineStyle.Dashed,  
        axisLabelVisible: false,  
        title: 'P/L 600',  
    });  
    

* * *

### options()[​](IPriceLine.html#options "Direct link to options\(\)")

> **options**(): `Readonly` <[`PriceLineOptions`](PriceLineOptions.md)>

Get the currently applied options.

#### Returns[​](IPriceLine.html#returns-1 "Direct link to Returns")

`Readonly` <[`PriceLineOptions`](PriceLineOptions.md)>
