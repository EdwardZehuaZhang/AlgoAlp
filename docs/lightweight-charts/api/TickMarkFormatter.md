# API: Tickmarkformatter

*Source: docs\api\type-aliases\TickMarkFormatter.html*

Version: 5.0

On this page

> **TickMarkFormatter** : (`time`, `tickMarkType`, `locale`) => `string` | `null`

The `TickMarkFormatter` is used to customize tick mark labels on the time scale.

This function should return `time` as a string formatted according to `tickMarkType` type (year, month, etc) and `locale`.

Note that the returned string should be the shortest possible value and should have no more than 8 characters. Otherwise, the tick marks will overlap each other.

If the formatter function returns `null` then the default tick mark formatter will be used as a fallback.

## Example[​](TickMarkFormatter.html#example "Direct link to Example")
    
    
    const customFormatter = (time, tickMarkType, locale) => {  
        // your code here  
    };  
    

## Parameters[​](TickMarkFormatter.html#parameters "Direct link to Parameters")

• **time** : [`Time`](Time.md)

• **tickMarkType** : [`TickMarkType`](../enumerations/TickMarkType.md)

• **locale** : `string`

## Returns[​](TickMarkFormatter.html#returns "Direct link to Returns")

`string` | `null`
