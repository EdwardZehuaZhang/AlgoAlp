# Docs

*Source: docs.html*

Version: 5.0

On this page

## Requirements[​](docs.html#requirements "Direct link to Requirements")

Lightweight Charts™ is _a client-side_ library that is not designed to work on the server side, for example, with Node.js.

The library code targets the [_ES2020_ language specification](https://262.ecma-international.org/11.0/). Therefore, the browsers you work with should support this language revision. Consider the following [table](https://compat-table.github.io/compat-table/es2016plus/) to ensure the browser compatibility.

To support previous revisions, you can set up a transpilation process for the `lightweight-charts` package in your build system using tools such as Babel. If you encounter any issues, open a [GitHub issue](https://github.com/tradingview/lightweight-charts/issues) with detailed information, and we will investigate potential solutions.

## Installation[​](docs.html#installation "Direct link to Installation")

To set up the library, install the [`lightweight-charts`](https://www.npmjs.com/package/lightweight-charts) npm package:
    
    
    npm install --save lightweight-charts  
    

The package includes TypeScript declarations, enabling seamless integration within TypeScript projects.

### Build variants[​](docs.html#build-variants "Direct link to Build variants")

The library ships with the following build variants:

Dependencies included| Mode| ES module| IIFE (`window.LightweightCharts`)  
---|---|---|---  
No| PROD| `lightweight-charts.production.mjs`| N/A  
No| DEV| `lightweight-charts.development.mjs`| N/A  
Yes (standalone)| PROD| `lightweight-charts.standalone.production.mjs`| `lightweight-charts.standalone.production.js`  
Yes (standalone)| DEV| `lightweight-charts.standalone.development.mjs`| `lightweight-charts.standalone.development.js`  
  
## License and attribution[​](docs.html#license-and-attribution "Direct link to License and attribution")

The Lightweight Charts™ license **requires** specifying TradingView as the product creator. You should add the following attributes to a public page of your website or mobile application:

  * Attribution notice from the [`NOTICE`](https://github.com/tradingview/lightweight-charts/blob/master/NOTICE) file
  * The <https://www.tradingview.com> link

## Creating a chart[​](docs.html#creating-a-chart "Direct link to Creating a chart")

As a first step, import the library to your file:
    
    
    import { createChart } from 'lightweight-charts';  
    

To create a chart, use the [`createChart`](docs/api/functions/createChart.md) function. You can call the function multiple times to create as many charts as needed:
    
    
    import { createChart } from 'lightweight-charts';  
      
    // ...  
    const firstChart = createChart(document.getElementById('firstContainer'));  
    const secondChart = createChart(document.getElementById('secondContainer'));  
    

As a result, `createChart` returns an [`IChartApi`](docs/api/interfaces/IChartApi.md) object that allows you to interact with the created chart.

## Creating a series[​](docs.html#creating-a-series "Direct link to Creating a series")

When the chart is created, you can display data on it.

The basic primitive to display data is a [series](docs/api/interfaces/ISeriesApi.md). The library supports the following series types:

  * Area
  * Bar
  * Baseline
  * Candlestick
  * Histogram
  * Line

To create a series, use the [`addSeries`](docs/api/interfaces/IChartApi.html#addseries) method from [`IChartApi`](docs/api/interfaces/IChartApi.md). As a parameter, specify a [series type](docs/series-types.md) you would like to create:
    
    
    import { AreaSeries, BarSeries, BaselineSeries, createChart } from 'lightweight-charts';  
      
    const chart = createChart(container);  
      
    const areaSeries = chart.addSeries(AreaSeries);  
    const barSeries = chart.addSeries(BarSeries);  
    const baselineSeries = chart.addSeries(BaselineSeries);  
    // ...  
    

Note that a series **cannot be transferred** from one type to another one, since different series types require different data and options types.

## Setting and updating a data[​](docs.html#setting-and-updating-a-data "Direct link to Setting and updating a data")

When the series is created, you can populate it with data. Note that the API calls remain the same regardless of the series type, although the data format may vary.

### Setting the data to a series[​](docs.html#setting-the-data-to-a-series "Direct link to Setting the data to a series")

To set the data to a series, you should call the [`ISeriesApi.setData`](docs/api/interfaces/ISeriesApi.html#setdata) method:
    
    
    const chartOptions = { layout: { textColor: 'black', background: { type: 'solid', color: 'white' } } };  
    const chart = createChart(document.getElementById('container'), chartOptions);  
    const areaSeries = chart.addSeries(AreaSeries, {  
        lineColor: '#2962FF', topColor: '#2962FF',  
        bottomColor: 'rgba(41, 98, 255, 0.28)',  
    });  
    areaSeries.setData([  
        { time: '2018-12-22', value: 32.51 },  
        { time: '2018-12-23', value: 31.11 },  
        { time: '2018-12-24', value: 27.02 },  
        { time: '2018-12-25', value: 27.32 },  
        { time: '2018-12-26', value: 25.17 },  
        { time: '2018-12-27', value: 28.89 },  
        { time: '2018-12-28', value: 25.46 },  
        { time: '2018-12-29', value: 23.92 },  
        { time: '2018-12-30', value: 22.68 },  
        { time: '2018-12-31', value: 22.67 },  
    ]);  
      
    const candlestickSeries = chart.addSeries(CandlestickSeries, {  
        upColor: '#26a69a', downColor: '#ef5350', borderVisible: false,  
        wickUpColor: '#26a69a', wickDownColor: '#ef5350',  
    });  
    candlestickSeries.setData([  
        { time: '2018-12-22', open: 75.16, high: 82.84, low: 36.16, close: 45.72 },  
        { time: '2018-12-23', open: 45.12, high: 53.90, low: 45.12, close: 48.09 },  
        { time: '2018-12-24', open: 60.71, high: 60.71, low: 53.39, close: 59.29 },  
        { time: '2018-12-25', open: 68.26, high: 68.26, low: 59.04, close: 60.50 },  
        { time: '2018-12-26', open: 67.71, high: 105.85, low: 66.67, close: 91.04 },  
        { time: '2018-12-27', open: 91.04, high: 121.40, low: 82.70, close: 111.40 },  
        { time: '2018-12-28', open: 111.51, high: 142.83, low: 103.34, close: 131.25 },  
        { time: '2018-12-29', open: 131.33, high: 151.17, low: 77.68, close: 96.43 },  
        { time: '2018-12-30', open: 106.33, high: 110.20, low: 90.39, close: 98.10 },  
        { time: '2018-12-31', open: 109.87, high: 114.69, low: 85.66, close: 111.26 },  
    ]);  
      
    chart.timeScale().fitContent();  
    

You can also use `setData` to replace all data items.

### Updating the data in a series[​](docs.html#updating-the-data-in-a-series "Direct link to Updating the data in a series")

If your data is updated, for example in real-time, you may also need to refresh the chart accordingly. To do this, call the [`ISeriesApi.update`](docs/api/interfaces/ISeriesApi.html#update) method that allows you to update the last data item or add a new one.
    
    
    import { AreaSeries, CandlestickSeries, createChart } from 'lightweight-charts';  
      
    const chart = createChart(container);  
      
    const areaSeries = chart.addSeries(AreaSeries);  
    areaSeries.setData([  
        // Other data items  
        { time: '2018-12-31', value: 22.67 },  
    ]);  
      
    const candlestickSeries = chart.addSeries(CandlestickSeries);  
    candlestickSeries.setData([  
        // Other data items  
        { time: '2018-12-31', open: 109.87, high: 114.69, low: 85.66, close: 111.26 },  
    ]);  
      
    // ...  
      
    // Update the most recent bar  
    areaSeries.update({ time: '2018-12-31', value: 25 });  
    candlestickSeries.update({ time: '2018-12-31', open: 109.87, high: 114.69, low: 85.66, close: 112 });  
      
    // Creating the new bar  
    areaSeries.update({ time: '2019-01-01', value: 20 });  
    candlestickSeries.update({ time: '2019-01-01', open: 112, high: 112, low: 100, close: 101 });  
    

We do not recommend calling [`ISeriesApi.setData`](docs/api/interfaces/ISeriesApi.html#setdata) to update the chart, as this method replaces all series data and can significantly affect the performance.
