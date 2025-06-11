# API: Itimescaleapi

*Source: docs\api\interfaces\ITimeScaleApi.html*

Version: 5.0

On this page

Interface to chart time scale

## Type parameters[​](ITimeScaleApi.html#type-parameters "Direct link to Type parameters")

• **HorzScaleItem**

## Methods[​](ITimeScaleApi.html#methods "Direct link to Methods")

### scrollPosition()[​](ITimeScaleApi.html#scrollposition "Direct link to scrollPosition\(\)")

> **scrollPosition**(): `number`

Return the distance from the right edge of the time scale to the lastest bar of the series measured in bars.

#### Returns[​](ITimeScaleApi.html#returns "Direct link to Returns")

`number`

* * *

### scrollToPosition()[​](ITimeScaleApi.html#scrolltoposition "Direct link to scrollToPosition\(\)")

> **scrollToPosition**(`position`, `animated`): `void`

Scrolls the chart to the specified position.

#### Parameters[​](ITimeScaleApi.html#parameters "Direct link to Parameters")

• **position** : `number`

Target data position

• **animated** : `boolean`

Setting this to true makes the chart scrolling smooth and adds animation

#### Returns[​](ITimeScaleApi.html#returns-1 "Direct link to Returns")

`void`

* * *

### scrollToRealTime()[​](ITimeScaleApi.html#scrolltorealtime "Direct link to scrollToRealTime\(\)")

> **scrollToRealTime**(): `void`

Restores default scroll position of the chart. This process is always animated.

#### Returns[​](ITimeScaleApi.html#returns-2 "Direct link to Returns")

`void`

* * *

### getVisibleRange()[​](ITimeScaleApi.html#getvisiblerange "Direct link to getVisibleRange\(\)")

> **getVisibleRange**(): [`IRange`](IRange.md)<`HorzScaleItem`>

Returns current visible time range of the chart.

Note that this method cannot extrapolate time and will use the only currently existent data. To get complete information about current visible range, please use [getVisibleLogicalRange](ITimeScaleApi.html#getvisiblelogicalrange) and [ISeriesApi.barsInLogicalRange](ISeriesApi.html#barsinlogicalrange).

#### Returns[​](ITimeScaleApi.html#returns-3 "Direct link to Returns")

[`IRange`](IRange.md)<`HorzScaleItem`>

Visible range or null if the chart has no data at all.

* * *

### setVisibleRange()[​](ITimeScaleApi.html#setvisiblerange "Direct link to setVisibleRange\(\)")

> **setVisibleRange**(`range`): `void`

Sets visible range of data.

Note that this method cannot extrapolate time and will use the only currently existent data. Thus, for example, if currently a chart doesn't have data prior `2018-01-01` date and you set visible range with `from` date `2016-01-01`, it will be automatically adjusted to `2018-01-01` (and the same for `to` date).

But if you can approximate indexes on your own - you could use [setVisibleLogicalRange](ITimeScaleApi.html#setvisiblelogicalrange) instead.

#### Parameters[​](ITimeScaleApi.html#parameters-1 "Direct link to Parameters")

• **range** : [`IRange`](IRange.md)<`HorzScaleItem`>

Target visible range of data.

#### Returns[​](ITimeScaleApi.html#returns-4 "Direct link to Returns")

`void`

#### Example[​](ITimeScaleApi.html#example "Direct link to Example")
    
    
    chart.timeScale().setVisibleRange({  
        from: (new Date(Date.UTC(2018, 0, 1, 0, 0, 0, 0))).getTime() / 1000,  
        to: (new Date(Date.UTC(2018, 1, 1, 0, 0, 0, 0))).getTime() / 1000,  
    });  
    

* * *

### getVisibleLogicalRange()[​](ITimeScaleApi.html#getvisiblelogicalrange "Direct link to getVisibleLogicalRange\(\)")

> **getVisibleLogicalRange**(): [`LogicalRange`](../type-aliases/LogicalRange.md)

Returns the current visible [logical range](../../time-scale.html#logical-range) of the chart as an object with the first and last time points of the logical range, or returns `null` if the chart has no data.

#### Returns[​](ITimeScaleApi.html#returns-5 "Direct link to Returns")

[`LogicalRange`](../type-aliases/LogicalRange.md)

Visible range or null if the chart has no data at all.

* * *

### setVisibleLogicalRange()[​](ITimeScaleApi.html#setvisiblelogicalrange "Direct link to setVisibleLogicalRange\(\)")

> **setVisibleLogicalRange**(`range`): `void`

Sets visible [logical range](../../time-scale.html#logical-range) of data.

#### Parameters[​](ITimeScaleApi.html#parameters-2 "Direct link to Parameters")

• **range** : [`IRange`](IRange.md)<`number`>

Target visible logical range of data.

#### Returns[​](ITimeScaleApi.html#returns-6 "Direct link to Returns")

`void`

#### Example[​](ITimeScaleApi.html#example-1 "Direct link to Example")
    
    
    chart.timeScale().setVisibleLogicalRange({ from: 0, to: 10 });  
    

* * *

### resetTimeScale()[​](ITimeScaleApi.html#resettimescale "Direct link to resetTimeScale\(\)")

> **resetTimeScale**(): `void`

Restores default zoom level and scroll position of the time scale.

#### Returns[​](ITimeScaleApi.html#returns-7 "Direct link to Returns")

`void`

* * *

### fitContent()[​](ITimeScaleApi.html#fitcontent "Direct link to fitContent\(\)")

> **fitContent**(): `void`

Automatically calculates the visible range to fit all data from all series.

#### Returns[​](ITimeScaleApi.html#returns-8 "Direct link to Returns")

`void`

* * *

### logicalToCoordinate()[​](ITimeScaleApi.html#logicaltocoordinate "Direct link to logicalToCoordinate\(\)")

> **logicalToCoordinate**(`logical`): [`Coordinate`](../type-aliases/Coordinate.md)

Converts a logical index to local x coordinate.

#### Parameters[​](ITimeScaleApi.html#parameters-3 "Direct link to Parameters")

• **logical** : [`Logical`](../type-aliases/Logical.md)

Logical index needs to be converted

#### Returns[​](ITimeScaleApi.html#returns-9 "Direct link to Returns")

[`Coordinate`](../type-aliases/Coordinate.md)

x coordinate of that time or `null` if the chart doesn't have data

* * *

### coordinateToLogical()[​](ITimeScaleApi.html#coordinatetological "Direct link to coordinateToLogical\(\)")

> **coordinateToLogical**(`x`): [`Logical`](../type-aliases/Logical.md)

Converts a coordinate to logical index.

#### Parameters[​](ITimeScaleApi.html#parameters-4 "Direct link to Parameters")

• **x** : `number`

Coordinate needs to be converted

#### Returns[​](ITimeScaleApi.html#returns-10 "Direct link to Returns")

[`Logical`](../type-aliases/Logical.md)

Logical index that is located on that coordinate or `null` if the chart doesn't have data

* * *

### timeToIndex()[​](ITimeScaleApi.html#timetoindex "Direct link to timeToIndex\(\)")

> **timeToIndex**(`time`, `findNearest`?): [`TimePointIndex`](../type-aliases/TimePointIndex.md)

Converts a time to local x coordinate.

#### Parameters[​](ITimeScaleApi.html#parameters-5 "Direct link to Parameters")

• **time** : `HorzScaleItem`

Time needs to be converted

• **findNearest?** : `boolean`

#### Returns[​](ITimeScaleApi.html#returns-11 "Direct link to Returns")

[`TimePointIndex`](../type-aliases/TimePointIndex.md)

X coordinate of that time or `null` if no time found on time scale

* * *

### timeToCoordinate()[​](ITimeScaleApi.html#timetocoordinate "Direct link to timeToCoordinate\(\)")

> **timeToCoordinate**(`time`): [`Coordinate`](../type-aliases/Coordinate.md)

Converts a time to local x coordinate.

#### Parameters[​](ITimeScaleApi.html#parameters-6 "Direct link to Parameters")

• **time** : `HorzScaleItem`

Time needs to be converted

#### Returns[​](ITimeScaleApi.html#returns-12 "Direct link to Returns")

[`Coordinate`](../type-aliases/Coordinate.md)

X coordinate of that time or `null` if no time found on time scale

* * *

### coordinateToTime()[​](ITimeScaleApi.html#coordinatetotime "Direct link to coordinateToTime\(\)")

> **coordinateToTime**(`x`): `HorzScaleItem`

Converts a coordinate to time.

#### Parameters[​](ITimeScaleApi.html#parameters-7 "Direct link to Parameters")

• **x** : `number`

Coordinate needs to be converted.

#### Returns[​](ITimeScaleApi.html#returns-13 "Direct link to Returns")

`HorzScaleItem`

Time of a bar that is located on that coordinate or `null` if there are no bars found on that coordinate.

* * *

### width()[​](ITimeScaleApi.html#width "Direct link to width\(\)")

> **width**(): `number`

Returns a width of the time scale.

#### Returns[​](ITimeScaleApi.html#returns-14 "Direct link to Returns")

`number`

* * *

### height()[​](ITimeScaleApi.html#height "Direct link to height\(\)")

> **height**(): `number`

Returns a height of the time scale.

#### Returns[​](ITimeScaleApi.html#returns-15 "Direct link to Returns")

`number`

* * *

### subscribeVisibleTimeRangeChange()[​](ITimeScaleApi.html#subscribevisibletimerangechange "Direct link to subscribeVisibleTimeRangeChange\(\)")

> **subscribeVisibleTimeRangeChange**(`handler`): `void`

Subscribe to the visible time range change events.

The argument passed to the handler function is an object with `from` and `to` properties of type [Time](../type-aliases/Time.md), or `null` if there is no visible data.

#### Parameters[​](ITimeScaleApi.html#parameters-8 "Direct link to Parameters")

• **handler** : [`TimeRangeChangeEventHandler`](../type-aliases/TimeRangeChangeEventHandler.md)<`HorzScaleItem`>

Handler (function) to be called when the visible indexes change.

#### Returns[​](ITimeScaleApi.html#returns-16 "Direct link to Returns")

`void`

#### Example[​](ITimeScaleApi.html#example-2 "Direct link to Example")
    
    
    function myVisibleTimeRangeChangeHandler(newVisibleTimeRange) {  
        if (newVisibleTimeRange === null) {  
            // handle null  
        }  
      
        // handle new logical range  
    }  
      
    chart.timeScale().subscribeVisibleTimeRangeChange(myVisibleTimeRangeChangeHandler);  
    

* * *

### unsubscribeVisibleTimeRangeChange()[​](ITimeScaleApi.html#unsubscribevisibletimerangechange "Direct link to unsubscribeVisibleTimeRangeChange\(\)")

> **unsubscribeVisibleTimeRangeChange**(`handler`): `void`

Unsubscribe a handler that was previously subscribed using [subscribeVisibleTimeRangeChange](ITimeScaleApi.html#subscribevisibletimerangechange).

#### Parameters[​](ITimeScaleApi.html#parameters-9 "Direct link to Parameters")

• **handler** : [`TimeRangeChangeEventHandler`](../type-aliases/TimeRangeChangeEventHandler.md)<`HorzScaleItem`>

Previously subscribed handler

#### Returns[​](ITimeScaleApi.html#returns-17 "Direct link to Returns")

`void`

#### Example[​](ITimeScaleApi.html#example-3 "Direct link to Example")
    
    
    chart.timeScale().unsubscribeVisibleTimeRangeChange(myVisibleTimeRangeChangeHandler);  
    

* * *

### subscribeVisibleLogicalRangeChange()[​](ITimeScaleApi.html#subscribevisiblelogicalrangechange "Direct link to subscribeVisibleLogicalRangeChange\(\)")

> **subscribeVisibleLogicalRangeChange**(`handler`): `void`

Subscribe to the visible logical range change events.

The argument passed to the handler function is an object with `from` and `to` properties of type `number`, or `null` if there is no visible data.

#### Parameters[​](ITimeScaleApi.html#parameters-10 "Direct link to Parameters")

• **handler** : [`LogicalRangeChangeEventHandler`](../type-aliases/LogicalRangeChangeEventHandler.md)

Handler (function) to be called when the visible indexes change.

#### Returns[​](ITimeScaleApi.html#returns-18 "Direct link to Returns")

`void`

#### Example[​](ITimeScaleApi.html#example-4 "Direct link to Example")
    
    
    function myVisibleLogicalRangeChangeHandler(newVisibleLogicalRange) {  
        if (newVisibleLogicalRange === null) {  
            // handle null  
        }  
      
        // handle new logical range  
    }  
      
    chart.timeScale().subscribeVisibleLogicalRangeChange(myVisibleLogicalRangeChangeHandler);  
    

* * *

### unsubscribeVisibleLogicalRangeChange()[​](ITimeScaleApi.html#unsubscribevisiblelogicalrangechange "Direct link to unsubscribeVisibleLogicalRangeChange\(\)")

> **unsubscribeVisibleLogicalRangeChange**(`handler`): `void`

Unsubscribe a handler that was previously subscribed using [subscribeVisibleLogicalRangeChange](ITimeScaleApi.html#subscribevisiblelogicalrangechange).

#### Parameters[​](ITimeScaleApi.html#parameters-11 "Direct link to Parameters")

• **handler** : [`LogicalRangeChangeEventHandler`](../type-aliases/LogicalRangeChangeEventHandler.md)

Previously subscribed handler

#### Returns[​](ITimeScaleApi.html#returns-19 "Direct link to Returns")

`void`

#### Example[​](ITimeScaleApi.html#example-5 "Direct link to Example")
    
    
    chart.timeScale().unsubscribeVisibleLogicalRangeChange(myVisibleLogicalRangeChangeHandler);  
    

* * *

### subscribeSizeChange()[​](ITimeScaleApi.html#subscribesizechange "Direct link to subscribeSizeChange\(\)")

> **subscribeSizeChange**(`handler`): `void`

Adds a subscription to time scale size changes

#### Parameters[​](ITimeScaleApi.html#parameters-12 "Direct link to Parameters")

• **handler** : [`SizeChangeEventHandler`](../type-aliases/SizeChangeEventHandler.md)

Handler (function) to be called when the time scale size changes

#### Returns[​](ITimeScaleApi.html#returns-20 "Direct link to Returns")

`void`

* * *

### unsubscribeSizeChange()[​](ITimeScaleApi.html#unsubscribesizechange "Direct link to unsubscribeSizeChange\(\)")

> **unsubscribeSizeChange**(`handler`): `void`

Removes a subscription to time scale size changes

#### Parameters[​](ITimeScaleApi.html#parameters-13 "Direct link to Parameters")

• **handler** : [`SizeChangeEventHandler`](../type-aliases/SizeChangeEventHandler.md)

Previously subscribed handler

#### Returns[​](ITimeScaleApi.html#returns-21 "Direct link to Returns")

`void`

* * *

### applyOptions()[​](ITimeScaleApi.html#applyoptions "Direct link to applyOptions\(\)")

> **applyOptions**(`options`): `void`

Applies new options to the time scale.

#### Parameters[​](ITimeScaleApi.html#parameters-14 "Direct link to Parameters")

• **options** : [`DeepPartial`](../type-aliases/DeepPartial.md) <[`HorzScaleOptions`](HorzScaleOptions.md)>

Any subset of options.

#### Returns[​](ITimeScaleApi.html#returns-22 "Direct link to Returns")

`void`

* * *

### options()[​](ITimeScaleApi.html#options "Direct link to options\(\)")

> **options**(): `Readonly` <[`HorzScaleOptions`](HorzScaleOptions.md)>

Returns current options

#### Returns[​](ITimeScaleApi.html#returns-23 "Direct link to Returns")

`Readonly` <[`HorzScaleOptions`](HorzScaleOptions.md)>

Currently applied options
