# API: Iseriesapi

*Source: docs\api\interfaces\ISeriesApi.html*

Version: 5.0

On this page

Represents the interface for interacting with series.

## Type parameters[​](ISeriesApi.html#type-parameters "Direct link to Type parameters")

• **TSeriesType** _extends_ [`SeriesType`](../type-aliases/SeriesType.md)

• **HorzScaleItem** = [`Time`](../type-aliases/Time.md)

• **TData** = [`SeriesDataItemTypeMap`](SeriesDataItemTypeMap.md)<`HorzScaleItem`>[`TSeriesType`]

• **TOptions** = [`SeriesOptionsMap`](SeriesOptionsMap.md)[`TSeriesType`]

• **TPartialOptions** = [`SeriesPartialOptionsMap`](SeriesPartialOptionsMap.md)[`TSeriesType`]

## Methods[​](ISeriesApi.html#methods "Direct link to Methods")

### priceFormatter()[​](ISeriesApi.html#priceformatter "Direct link to priceFormatter\(\)")

> **priceFormatter**(): [`IPriceFormatter`](IPriceFormatter.md)

Returns current price formatter

#### Returns[​](ISeriesApi.html#returns "Direct link to Returns")

[`IPriceFormatter`](IPriceFormatter.md)

Interface to the price formatter object that can be used to format prices in the same way as the chart does

* * *

### priceToCoordinate()[​](ISeriesApi.html#pricetocoordinate "Direct link to priceToCoordinate\(\)")

> **priceToCoordinate**(`price`): [`Coordinate`](../type-aliases/Coordinate.md)

Converts specified series price to pixel coordinate according to the series price scale

#### Parameters[​](ISeriesApi.html#parameters "Direct link to Parameters")

• **price** : `number`

Input price to be converted

#### Returns[​](ISeriesApi.html#returns-1 "Direct link to Returns")

[`Coordinate`](../type-aliases/Coordinate.md)

Pixel coordinate of the price level on the chart

* * *

### coordinateToPrice()[​](ISeriesApi.html#coordinatetoprice "Direct link to coordinateToPrice\(\)")

> **coordinateToPrice**(`coordinate`): [`BarPrice`](../type-aliases/BarPrice.md)

Converts specified coordinate to price value according to the series price scale

#### Parameters[​](ISeriesApi.html#parameters-1 "Direct link to Parameters")

• **coordinate** : `number`

Input coordinate to be converted

#### Returns[​](ISeriesApi.html#returns-2 "Direct link to Returns")

[`BarPrice`](../type-aliases/BarPrice.md)

Price value of the coordinate on the chart

* * *

### barsInLogicalRange()[​](ISeriesApi.html#barsinlogicalrange "Direct link to barsInLogicalRange\(\)")

> **barsInLogicalRange**(`range`): [`BarsInfo`](BarsInfo.md)<`HorzScaleItem`>

Returns bars information for the series in the provided [logical range](../../time-scale.html#logical-range) or `null`, if no series data has been found in the requested range. This method can be used, for instance, to implement downloading historical data while scrolling to prevent a user from seeing empty space.

#### Parameters[​](ISeriesApi.html#parameters-2 "Direct link to Parameters")

• **range** : [`IRange`](IRange.md)<`number`>

The [logical range](../../time-scale.html#logical-range) to retrieve info for.

#### Returns[​](ISeriesApi.html#returns-3 "Direct link to Returns")

[`BarsInfo`](BarsInfo.md)<`HorzScaleItem`>

The bars info for the given logical range.

#### Examples[​](ISeriesApi.html#examples "Direct link to Examples")
    
    
    const barsInfo = series.barsInLogicalRange(chart.timeScale().getVisibleLogicalRange());  
    console.log(barsInfo);  
    
    
    
    function onVisibleLogicalRangeChanged(newVisibleLogicalRange) {  
        const barsInfo = series.barsInLogicalRange(newVisibleLogicalRange);  
        // if there less than 50 bars to the left of the visible area  
        if (barsInfo !== null && barsInfo.barsBefore < 50) {  
            // try to load additional historical data and prepend it to the series data  
        }  
    }  
      
    chart.timeScale().subscribeVisibleLogicalRangeChange(onVisibleLogicalRangeChanged);  
    

* * *

### applyOptions()[​](ISeriesApi.html#applyoptions "Direct link to applyOptions\(\)")

> **applyOptions**(`options`): `void`

Applies new options to the existing series You can set options initially when you create series or use the `applyOptions` method of the series to change the existing options. Note that you can only pass options you want to change.

#### Parameters[​](ISeriesApi.html#parameters-3 "Direct link to Parameters")

• **options** : `TPartialOptions`

Any subset of options.

#### Returns[​](ISeriesApi.html#returns-4 "Direct link to Returns")

`void`

* * *

### options()[​](ISeriesApi.html#options "Direct link to options\(\)")

> **options**(): `Readonly`<`TOptions`>

Returns currently applied options

#### Returns[​](ISeriesApi.html#returns-5 "Direct link to Returns")

`Readonly`<`TOptions`>

Full set of currently applied options, including defaults

* * *

### priceScale()[​](ISeriesApi.html#pricescale "Direct link to priceScale\(\)")

> **priceScale**(): [`IPriceScaleApi`](IPriceScaleApi.md)

Returns the API interface for controlling the price scale that this series is currently attached to.

#### Returns[​](ISeriesApi.html#returns-6 "Direct link to Returns")

[`IPriceScaleApi`](IPriceScaleApi.md)

IPriceScaleApi An interface for controlling the price scale (axis component) currently used by this series

#### Remarks[​](ISeriesApi.html#remarks "Direct link to Remarks")

Important: The returned PriceScaleApi is bound to the specific price scale (by ID and pane) that the series is using at the time this method is called. If you later move the series to a different pane or attach it to a different price scale (e.g., from 'right' to 'left'), the previously returned PriceScaleApi will NOT follow the series. It will continue to control the original price scale it was created for.

To control the new price scale after moving a series, you must call this method again to get a fresh PriceScaleApi instance for the current price scale.

* * *

### setData()[​](ISeriesApi.html#setdata "Direct link to setData\(\)")

> **setData**(`data`): `void`

Sets or replaces series data.

#### Parameters[​](ISeriesApi.html#parameters-4 "Direct link to Parameters")

• **data** : `TData`[]

Ordered (earlier time point goes first) array of data items. Old data is fully replaced with the new one.

#### Returns[​](ISeriesApi.html#returns-7 "Direct link to Returns")

`void`

#### Examples[​](ISeriesApi.html#examples-1 "Direct link to Examples")
    
    
    lineSeries.setData([  
        { time: '2018-12-12', value: 24.11 },  
        { time: '2018-12-13', value: 31.74 },  
    ]);  
    
    
    
    barSeries.setData([  
        { time: '2018-12-19', open: 141.77, high: 170.39, low: 120.25, close: 145.72 },  
        { time: '2018-12-20', open: 145.72, high: 147.99, low: 100.11, close: 108.19 },  
    ]);  
    

* * *

### update()[​](ISeriesApi.html#update "Direct link to update\(\)")

> **update**(`bar`, `historicalUpdate`?): `void`

Adds new data item to the existing set (or updates the latest item if times of the passed/latest items are equal).

#### Parameters[​](ISeriesApi.html#parameters-5 "Direct link to Parameters")

• **bar** : `TData`

A single data item to be added. Time of the new item must be greater or equal to the latest existing time point. If the new item's time is equal to the last existing item's time, then the existing item is replaced with the new one.

• **historicalUpdate?** : `boolean`

If true, allows updating an existing data point that is not the latest bar. Default is false. Updating older data using `historicalUpdate` will be slower than updating the most recent data point.

#### Returns[​](ISeriesApi.html#returns-8 "Direct link to Returns")

`void`

#### Examples[​](ISeriesApi.html#examples-2 "Direct link to Examples")
    
    
    lineSeries.update({  
        time: '2018-12-12',  
        value: 24.11,  
    });  
    
    
    
    barSeries.update({  
        time: '2018-12-19',  
        open: 141.77,  
        high: 170.39,  
        low: 120.25,  
        close: 145.72,  
    });  
    

* * *

### dataByIndex()[​](ISeriesApi.html#databyindex "Direct link to dataByIndex\(\)")

> **dataByIndex**(`logicalIndex`, `mismatchDirection`?): `TData`

Returns a bar data by provided logical index.

#### Parameters[​](ISeriesApi.html#parameters-6 "Direct link to Parameters")

• **logicalIndex** : `number`

Logical index

• **mismatchDirection?** : [`MismatchDirection`](../enumerations/MismatchDirection.md)

Search direction if no data found at provided logical index.

#### Returns[​](ISeriesApi.html#returns-9 "Direct link to Returns")

`TData`

Original data item provided via setData or update methods.

#### Example[​](ISeriesApi.html#example "Direct link to Example")
    
    
    const originalData = series.dataByIndex(10, LightweightCharts.MismatchDirection.NearestLeft);  
    

* * *

### data()[​](ISeriesApi.html#data "Direct link to data\(\)")

> **data**(): readonly `TData`[]

Returns all the bar data for the series.

#### Returns[​](ISeriesApi.html#returns-10 "Direct link to Returns")

readonly `TData`[]

Original data items provided via setData or update methods.

#### Example[​](ISeriesApi.html#example-1 "Direct link to Example")
    
    
    const originalData = series.data();  
    

* * *

### subscribeDataChanged()[​](ISeriesApi.html#subscribedatachanged "Direct link to subscribeDataChanged\(\)")

> **subscribeDataChanged**(`handler`): `void`

Subscribe to the data changed event. This event is fired whenever the `update` or `setData` method is evoked on the series.

#### Parameters[​](ISeriesApi.html#parameters-7 "Direct link to Parameters")

• **handler** : [`DataChangedHandler`](../type-aliases/DataChangedHandler.md)

Handler to be called on a data changed event.

#### Returns[​](ISeriesApi.html#returns-11 "Direct link to Returns")

`void`

#### Example[​](ISeriesApi.html#example-2 "Direct link to Example")
    
    
    function myHandler() {  
        const data = series.data();  
        console.log(`The data has changed. New Data length: ${data.length}`);  
    }  
      
    series.subscribeDataChanged(myHandler);  
    

* * *

### unsubscribeDataChanged()[​](ISeriesApi.html#unsubscribedatachanged "Direct link to unsubscribeDataChanged\(\)")

> **unsubscribeDataChanged**(`handler`): `void`

Unsubscribe a handler that was previously subscribed using [subscribeDataChanged](ISeriesApi.html#subscribedatachanged).

#### Parameters[​](ISeriesApi.html#parameters-8 "Direct link to Parameters")

• **handler** : [`DataChangedHandler`](../type-aliases/DataChangedHandler.md)

Previously subscribed handler

#### Returns[​](ISeriesApi.html#returns-12 "Direct link to Returns")

`void`

#### Example[​](ISeriesApi.html#example-3 "Direct link to Example")
    
    
    chart.unsubscribeDataChanged(myHandler);  
    

* * *

### createPriceLine()[​](ISeriesApi.html#createpriceline "Direct link to createPriceLine\(\)")

> **createPriceLine**(`options`): [`IPriceLine`](IPriceLine.md)

Creates a new price line

#### Parameters[​](ISeriesApi.html#parameters-9 "Direct link to Parameters")

• **options** : [`CreatePriceLineOptions`](../type-aliases/CreatePriceLineOptions.md)

Any subset of options, however `price` is required.

#### Returns[​](ISeriesApi.html#returns-13 "Direct link to Returns")

[`IPriceLine`](IPriceLine.md)

#### Example[​](ISeriesApi.html#example-4 "Direct link to Example")
    
    
    const priceLine = series.createPriceLine({  
        price: 80.0,  
        color: 'green',  
        lineWidth: 2,  
        lineStyle: LightweightCharts.LineStyle.Dotted,  
        axisLabelVisible: true,  
        title: 'P/L 500',  
    });  
    

* * *

### removePriceLine()[​](ISeriesApi.html#removepriceline "Direct link to removePriceLine\(\)")

> **removePriceLine**(`line`): `void`

Removes the price line that was created before.

#### Parameters[​](ISeriesApi.html#parameters-10 "Direct link to Parameters")

• **line** : [`IPriceLine`](IPriceLine.md)

A line to remove.

#### Returns[​](ISeriesApi.html#returns-14 "Direct link to Returns")

`void`

#### Example[​](ISeriesApi.html#example-5 "Direct link to Example")
    
    
    const priceLine = series.createPriceLine({ price: 80.0 });  
    series.removePriceLine(priceLine);  
    

* * *

### priceLines()[​](ISeriesApi.html#pricelines "Direct link to priceLines\(\)")

> **priceLines**(): [`IPriceLine`](IPriceLine.md)[]

Returns an array of price lines.

#### Returns[​](ISeriesApi.html#returns-15 "Direct link to Returns")

[`IPriceLine`](IPriceLine.md)[]

* * *

### seriesType()[​](ISeriesApi.html#seriestype "Direct link to seriesType\(\)")

> **seriesType**(): `TSeriesType`

Return current series type.

#### Returns[​](ISeriesApi.html#returns-16 "Direct link to Returns")

`TSeriesType`

Type of the series.

#### Example[​](ISeriesApi.html#example-6 "Direct link to Example")
    
    
    const lineSeries = chart.addSeries(LineSeries);  
    console.log(lineSeries.seriesType()); // "Line"  
      
    const candlestickSeries = chart.addCandlestickSeries();  
    console.log(candlestickSeries.seriesType()); // "Candlestick"  
    

* * *

### attachPrimitive()[​](ISeriesApi.html#attachprimitive "Direct link to attachPrimitive\(\)")

> **attachPrimitive**(`primitive`): `void`

Attaches additional drawing primitive to the series

#### Parameters[​](ISeriesApi.html#parameters-11 "Direct link to Parameters")

• **primitive** : [`ISeriesPrimitive`](../type-aliases/ISeriesPrimitive.md)<`HorzScaleItem`>

any implementation of ISeriesPrimitive interface

#### Returns[​](ISeriesApi.html#returns-17 "Direct link to Returns")

`void`

* * *

### detachPrimitive()[​](ISeriesApi.html#detachprimitive "Direct link to detachPrimitive\(\)")

> **detachPrimitive**(`primitive`): `void`

Detaches additional drawing primitive from the series

#### Parameters[​](ISeriesApi.html#parameters-12 "Direct link to Parameters")

• **primitive** : [`ISeriesPrimitive`](../type-aliases/ISeriesPrimitive.md)<`HorzScaleItem`>

implementation of ISeriesPrimitive interface attached before Does nothing if specified primitive was not attached

#### Returns[​](ISeriesApi.html#returns-18 "Direct link to Returns")

`void`

* * *

### moveToPane()[​](ISeriesApi.html#movetopane "Direct link to moveToPane\(\)")

> **moveToPane**(`paneIndex`): `void`

Move the series to another pane.

If the pane with the specified index does not exist, the pane will be created.

#### Parameters[​](ISeriesApi.html#parameters-13 "Direct link to Parameters")

• **paneIndex** : `number`

The index of the pane. Should be a number between 0 and the total number of panes.

#### Returns[​](ISeriesApi.html#returns-19 "Direct link to Returns")

`void`

* * *

### seriesOrder()[​](ISeriesApi.html#seriesorder "Direct link to seriesOrder\(\)")

> **seriesOrder**(): `number`

Gets the zero-based index of this series within the list of all series on the current pane.

#### Returns[​](ISeriesApi.html#returns-20 "Direct link to Returns")

`number`

The current index of the series in the pane's series collection.

* * *

### setSeriesOrder()[​](ISeriesApi.html#setseriesorder "Direct link to setSeriesOrder\(\)")

> **setSeriesOrder**(`order`): `void`

Sets the zero-based index of this series within the pane's series collection, thereby adjusting its rendering order.

Note:

  * The chart may automatically recalculate this index after operations such as removing other series or moving this series to a different pane.
  * If the provided index is less than 0, equal to, or greater than the number of series, it will be clamped to a valid range.
  * Price scales derive their formatters from the series with the lowest index; changing the order may affect the price scale's formatting

#### Parameters[​](ISeriesApi.html#parameters-14 "Direct link to Parameters")

• **order** : `number`

The desired zero-based index to set for this series within the pane.

#### Returns[​](ISeriesApi.html#returns-21 "Direct link to Returns")

`void`

* * *

### getPane()[​](ISeriesApi.html#getpane "Direct link to getPane\(\)")

> **getPane**(): [`IPaneApi`](IPaneApi.md)<`HorzScaleItem`>

Returns the pane to which the series is currently attached.

#### Returns[​](ISeriesApi.html#returns-22 "Direct link to Returns")

[`IPaneApi`](IPaneApi.md)<`HorzScaleItem`>

Pane API object to control the pane
