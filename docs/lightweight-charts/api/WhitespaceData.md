# API: Whitespacedata

*Source: docs\api\interfaces\WhitespaceData.html*

Version: 5.0

On this page

Represents a whitespace data item, which is a data point without a value.

## Example[​](WhitespaceData.html#example "Direct link to Example")
    
    
    const data = [  
        { time: '2018-12-03', value: 27.02 },  
        { time: '2018-12-04' }, // whitespace  
        { time: '2018-12-05' }, // whitespace  
        { time: '2018-12-06' }, // whitespace  
        { time: '2018-12-07' }, // whitespace  
        { time: '2018-12-08', value: 23.92 },  
        { time: '2018-12-13', value: 30.74 },  
    ];  
    

## Extended by[​](WhitespaceData.html#extended-by "Direct link to Extended by")

  * [`OhlcData`](OhlcData.md)
  * [`SingleValueData`](SingleValueData.md)

## Type parameters[​](WhitespaceData.html#type-parameters "Direct link to Type parameters")

• **HorzScaleItem** = [`Time`](../type-aliases/Time.md)

## Properties[​](WhitespaceData.html#properties "Direct link to Properties")

### time[​](WhitespaceData.html#time "Direct link to time")

> **time** : `HorzScaleItem`

The time of the data.

* * *

### customValues?[​](WhitespaceData.html#customvalues "Direct link to customValues?")

> `optional` **customValues** : `Record`<`string`, `unknown`>

Additional custom values which will be ignored by the library, but could be used by plugins.
