# Tutorial: Price And Volume

*Source: tutorials\how_to\price-and-volume.html*

On this page

This example shows how to include a volume study on your chart.

## How to add a volume histogram[​](price-and-volume.html#how-to-add-a-volume-histogram "Direct link to How to add a volume histogram")

An additional series can be added to a chart as an 'overlay' by setting the series' [`priceScaleId`](../../docs/api/interfaces/SeriesOptionsCommon.html#pricescaleid) to `''`. An overlay doesn't make use of either the left or right price scale, and it's positioning is controlled by setting the [`scaleMargins`](../../docs/api/interfaces/PriceScaleOptions.html#scalemargins) property on the price scale options associated with the series.
    
    
    const volumeSeries = chart.addSeries(HistogramSeries, {  
        priceFormat: {  
            type: 'volume',  
        },  
        priceScaleId: '', // set as an overlay by setting a blank priceScaleId  
    });  
    volumeSeries.priceScale().applyOptions({  
        // set the positioning of the volume series  
        scaleMargins: {  
            top: 0.7, // highest point of the series will be 70% away from the top  
            bottom: 0,  
        },  
    });  
    

We are using the [Histogram](../../docs/series-types.html#histogram) series type to draw the volume bars. We can set the `priceFormat` option to `'volume'` to have the values display correctly within the crosshair line label.

We adjust the position of the overlay series to the bottom 30% of the chart by setting the [`scaleMargins`](../../docs/api/interfaces/PriceScaleOptions.html#scalemargins) properties as follows:
    
    
    volumeSeries.priceScale().applyOptions({  
        scaleMargins: {  
            top: 0.7, // highest point of the series will be 70% away from the top  
            bottom: 0, // lowest point will be at the very bottom.  
        },  
    });  
    

Similarly, we can set the position of the main series using the same approach. By setting the `bottom` margin value to `0.4` we can ensure that the two series don't overlap each other.
    
    
    mainSeries.priceScale().applyOptions({  
        scaleMargins: {  
            top: 0.1, // highest point of the series will be 10% away from the top  
            bottom: 0.4, // lowest point will be 40% away from the bottom  
        },  
    });  
    

We can control the color of the histogram bars by directly specifying color inside the data set.
    
    
    histogramSeries.setData([  
        { time: '2018-10-19', value: 19103293.0, color: 'green' },  
        { time: '2018-10-20', value: 20345000.0, color: 'red' },  
    ]);  
    

You can see a full [working example](price-and-volume.html#full-example) below.

## Resources[​](price-and-volume.html#resources "Direct link to Resources")

  * [OverlayPriceScale Options](../../docs/api/type-aliases/OverlayPriceScaleOptions.md)
  * [Histogram Series Type](../../docs/series-types.html#histogram)
  * [PriceFormat Types](../../docs/api/interfaces/PriceFormatBuiltIn.html#type)
  * [Scale Margins](../../docs/api/interfaces/PriceScaleOptions.html#scalemargins)

## Full example[​](price-and-volume.html#full-example "Direct link to Full example")

How to use the code sample

**The code presented below requires:**

  * That `createChart` has already been imported. See [Getting Started](../../docs.html#creating-a-chart) for more information,
  * and that there is an html div element on the page with an `id` of `container`.

Here is an example skeleton setup: [Code Sandbox](https://codesandbox.io/s/lightweight-charts-skeleton-n67pm6). You can paste the provided code below the `// REPLACE EVERYTHING BELOW HERE` comment.

tip

Some code may be hidden to improve readability. Toggle the checkbox above the code block to reveal all the code.

Show all code
    
    
    // Lightweight Charts™ Example: Price and Volume  
    // https://tradingview.github.io/lightweight-charts/tutorials/how_to/price-and-volume  
      
    const chartOptions = {  
        layout: {  
            textColor: 'black',  
            background: { type: 'solid', color: 'white' },  
        },  
        rightPriceScale: {  
            borderVisible: false,  
        },  
    };  
    /** @type {import('lightweight-charts').IChartApi} */  
    const chart = createChart(document.getElementById('container'), chartOptions);  
      
    const areaSeries = chart.addSeries(AreaSeries, {  
        topColor: '#2962FF',  
        bottomColor: 'rgba(41, 98, 255, 0.28)',  
        lineColor: '#2962FF',  
        lineWidth: 2,  
    });  
    areaSeries.priceScale().applyOptions({  
        scaleMargins: {  
            // positioning the price scale for the area series  
            top: 0.1,  
            bottom: 0.4,  
        },  
    });  
      
    const volumeSeries = chart.addSeries(HistogramSeries, {  
        color: '#26a69a',  
        priceFormat: {  
            type: 'volume',  
        },  
        priceScaleId: '', // set as an overlay by setting a blank priceScaleId  
        // set the positioning of the volume series  
        scaleMargins: {  
            top: 0.7, // highest point of the series will be 70% away from the top  
            bottom: 0,  
        },  
    });  
    volumeSeries.priceScale().applyOptions({  
        scaleMargins: {  
            top: 0.7, // highest point of the series will be 70% away from the top  
            bottom: 0,  
        },  
    });  
      
    areaSeries.setData([  
        { time: '2018-10-19', value: 54.90 },  
        { time: '2018-10-22', value: 54.98 },  
        { time: '2018-10-23', value: 57.21 },  
        { time: '2018-10-24', value: 57.42 },  
        { time: '2018-10-25', value: 56.43 },  
        { time: '2018-10-26', value: 55.51 },  
        { time: '2018-10-29', value: 56.48 },  
        { time: '2018-10-30', value: 58.18 },  
        { time: '2018-10-31', value: 57.09 },  
        { time: '2018-11-01', value: 56.05 },  
        { time: '2018-11-02', value: 56.63 },  
        { time: '2018-11-05', value: 57.21 },  
        { time: '2018-11-06', value: 57.21 },  
        { time: '2018-11-07', value: 57.65 },  
        { time: '2018-11-08', value: 58.27 },  
        { time: '2018-11-09', value: 58.46 },  
        { time: '2018-11-12', value: 58.72 },  
        { time: '2018-11-13', value: 58.66 },  
        { time: '2018-11-14', value: 58.94 },  
        { time: '2018-11-15', value: 59.08 },  
        { time: '2018-11-16', value: 60.21 },  
        { time: '2018-11-19', value: 60.62 },  
        { time: '2018-11-20', value: 59.46 },  
        { time: '2018-11-21', value: 59.16 },  
        { time: '2018-11-23', value: 58.64 },  
        { time: '2018-11-26', value: 59.17 },  
        { time: '2018-11-27', value: 60.65 },  
        { time: '2018-11-28', value: 60.06 },  
        { time: '2018-11-29', value: 59.45 },  
        { time: '2018-11-30', value: 60.30 },  
        { time: '2018-12-03', value: 58.16 },  
        { time: '2018-12-04', value: 58.09 },  
        { time: '2018-12-06', value: 58.08 },  
        { time: '2018-12-07', value: 57.68 },  
        { time: '2018-12-10', value: 58.27 },  
        { time: '2018-12-11', value: 58.85 },  
        { time: '2018-12-12', value: 57.25 },  
        { time: '2018-12-13', value: 57.09 },  
        { time: '2018-12-14', value: 57.08 },  
        { time: '2018-12-17', value: 55.95 },  
        { time: '2018-12-18', value: 55.65 },  
        { time: '2018-12-19', value: 55.86 },  
        { time: '2018-12-20', value: 55.07 },  
        { time: '2018-12-21', value: 54.92 },  
        { time: '2018-12-24', value: 53.05 },  
        { time: '2018-12-26', value: 54.44 },  
        { time: '2018-12-27', value: 55.15 },  
        { time: '2018-12-28', value: 55.27 },  
        { time: '2018-12-31', value: 56.22 },  
        { time: '2019-01-02', value: 56.02 },  
        { time: '2019-01-03', value: 56.22 },  
        { time: '2019-01-04', value: 56.36 },  
        { time: '2019-01-07', value: 56.72 },  
        { time: '2019-01-08', value: 58.38 },  
        { time: '2019-01-09', value: 57.05 },  
        { time: '2019-01-10', value: 57.60 },  
        { time: '2019-01-11', value: 58.02 },  
        { time: '2019-01-14', value: 58.03 },  
        { time: '2019-01-15', value: 58.10 },  
        { time: '2019-01-16', value: 57.08 },  
        { time: '2019-01-17', value: 56.83 },  
        { time: '2019-01-18', value: 57.09 },  
        { time: '2019-01-22', value: 56.99 },  
        { time: '2019-01-23', value: 57.76 },  
        { time: '2019-01-24', value: 57.07 },  
        { time: '2019-01-25', value: 56.40 },  
        { time: '2019-01-28', value: 55.07 },  
        { time: '2019-01-29', value: 53.28 },  
        { time: '2019-01-30', value: 54.00 },  
        { time: '2019-01-31', value: 55.06 },  
        { time: '2019-02-01', value: 54.55 },  
        { time: '2019-02-04', value: 54.04 },  
        { time: '2019-02-05', value: 54.14 },  
        { time: '2019-02-06', value: 53.79 },  
        { time: '2019-02-07', value: 53.57 },  
        { time: '2019-02-08', value: 53.95 },  
        { time: '2019-02-11', value: 54.05 },  
        { time: '2019-02-12', value: 54.42 },  
        { time: '2019-02-13', value: 54.48 },  
        { time: '2019-02-14', value: 54.03 },  
        { time: '2019-02-15', value: 55.16 },  
        { time: '2019-02-19', value: 55.44 },  
        { time: '2019-02-20', value: 55.76 },  
        { time: '2019-02-21', value: 56.15 },  
        { time: '2019-02-22', value: 56.92 },  
        { time: '2019-02-25', value: 56.78 },  
        { time: '2019-02-26', value: 56.64 },  
        { time: '2019-02-27', value: 56.72 },  
        { time: '2019-02-28', value: 56.92 },  
        { time: '2019-03-01', value: 56.96 },  
        { time: '2019-03-04', value: 56.24 },  
        { time: '2019-03-05', value: 56.08 },  
        { time: '2019-03-06', value: 55.68 },  
        { time: '2019-03-07', value: 56.30 },  
        { time: '2019-03-08', value: 56.53 },  
        { time: '2019-03-11', value: 57.58 },  
        { time: '2019-03-12', value: 57.43 },  
        { time: '2019-03-13', value: 57.66 },  
        { time: '2019-03-14', value: 57.95 },  
        { time: '2019-03-15', value: 58.39 },  
        { time: '2019-03-18', value: 58.07 },  
        { time: '2019-03-19', value: 57.50 },  
        { time: '2019-03-20', value: 57.67 },  
        { time: '2019-03-21', value: 58.29 },  
        { time: '2019-03-22', value: 59.76 },  
        { time: '2019-03-25', value: 60.08 },  
        { time: '2019-03-26', value: 60.63 },  
        { time: '2019-03-27', value: 60.88 },  
        { time: '2019-03-28', value: 59.08 },  
        { time: '2019-03-29', value: 59.13 },  
        { time: '2019-04-01', value: 59.09 },  
        { time: '2019-04-02', value: 58.53 },  
        { time: '2019-04-03', value: 58.87 },  
        { time: '2019-04-04', value: 58.99 },  
        { time: '2019-04-05', value: 59.09 },  
        { time: '2019-04-08', value: 59.13 },  
        { time: '2019-04-09', value: 58.40 },  
        { time: '2019-04-10', value: 58.61 },  
        { time: '2019-04-11', value: 58.56 },  
        { time: '2019-04-12', value: 58.74 },  
        { time: '2019-04-15', value: 58.71 },  
        { time: '2019-04-16', value: 58.79 },  
        { time: '2019-04-17', value: 57.78 },  
        { time: '2019-04-18', value: 58.04 },  
        { time: '2019-04-22', value: 58.37 },  
        { time: '2019-04-23', value: 57.15 },  
        { time: '2019-04-24', value: 57.08 },  
        { time: '2019-04-25', value: 55.85 },  
        { time: '2019-04-26', value: 56.58 },  
        { time: '2019-04-29', value: 56.84 },  
        { time: '2019-04-30', value: 57.19 },  
        { time: '2019-05-01', value: 56.52 },  
        { time: '2019-05-02', value: 56.99 },  
        { time: '2019-05-03', value: 57.24 },  
        { time: '2019-05-06', value: 56.91 },  
        { time: '2019-05-07', value: 56.63 },  
        { time: '2019-05-08', value: 56.38 },  
        { time: '2019-05-09', value: 56.48 },  
        { time: '2019-05-10', value: 56.91 },  
        { time: '2019-05-13', value: 56.75 },  
        { time: '2019-05-14', value: 56.55 },  
        { time: '2019-05-15', value: 56.81 },  
        { time: '2019-05-16', value: 57.38 },  
        { time: '2019-05-17', value: 58.09 },  
        { time: '2019-05-20', value: 59.01 },  
        { time: '2019-05-21', value: 59.50 },  
        { time: '2019-05-22', value: 59.25 },  
        { time: '2019-05-23', value: 58.87 },  
        { time: '2019-05-24', value: 59.32 },  
        { time: '2019-05-28', value: 59.57 },  
    ]);  
      
    // setting the data for the volume series.  
    // note: we are defining each bars color as part of the data  
    volumeSeries.setData([  
        { time: '2018-10-19', value: 19103293.00, color: '#26a69a' },  
        { time: '2018-10-22', value: 21737523.00, color: '#26a69a' },  
        { time: '2018-10-23', value: 29328713.00, color: '#26a69a' },  
        { time: '2018-10-24', value: 37435638.00, color: '#26a69a' },  
        { time: '2018-10-25', value: 25269995.00, color: '#ef5350' },  
        { time: '2018-10-26', value: 24973311.00, color: '#ef5350' },  
        { time: '2018-10-29', value: 22103692.00, color: '#26a69a' },  
        { time: '2018-10-30', value: 25231199.00, color: '#26a69a' },  
        { time: '2018-10-31', value: 24214427.00, color: '#ef5350' },  
        { time: '2018-11-01', value: 22533201.00, color: '#ef5350' },  
        { time: '2018-11-02', value: 14734412.00, color: '#26a69a' },  
        { time: '2018-11-05', value: 12733842.00, color: '#26a69a' },  
        { time: '2018-11-06', value: 12371207.00, color: '#26a69a' },  
        { time: '2018-11-07', value: 14891287.00, color: '#26a69a' },  
        { time: '2018-11-08', value: 12482392.00, color: '#26a69a' },  
        { time: '2018-11-09', value: 17365762.00, color: '#26a69a' },  
        { time: '2018-11-12', value: 13236769.00, color: '#26a69a' },  
        { time: '2018-11-13', value: 13047907.00, color: '#ef5350' },  
        { time: '2018-11-14', value: 18288710.00, color: '#26a69a' },  
        { time: '2018-11-15', value: 17147123.00, color: '#26a69a' },  
        { time: '2018-11-16', value: 19470986.00, color: '#26a69a' },  
        { time: '2018-11-19', value: 18405731.00, color: '#26a69a' },  
        { time: '2018-11-20', value: 22028957.00, color: '#ef5350' },  
        { time: '2018-11-21', value: 18482233.00, color: '#ef5350' },  
        { time: '2018-11-23', value: 7009050.00, color: '#ef5350' },  
        { time: '2018-11-26', value: 12308876.00, color: '#26a69a' },  
        { time: '2018-11-27', value: 14118867.00, color: '#26a69a' },  
        { time: '2018-11-28', value: 18662989.00, color: '#ef5350' },  
        { time: '2018-11-29', value: 14763658.00, color: '#ef5350' },  
        { time: '2018-11-30', value: 31142818.00, color: '#26a69a' },  
        { time: '2018-12-03', value: 27795428.00, color: '#ef5350' },  
        { time: '2018-12-04', value: 21727411.00, color: '#ef5350' },  
        { time: '2018-12-06', value: 26880429.00, color: '#ef5350' },  
        { time: '2018-12-07', value: 16948126.00, color: '#ef5350' },  
        { time: '2018-12-10', value: 16603356.00, color: '#26a69a' },  
        { time: '2018-12-11', value: 14991438.00, color: '#26a69a' },  
        { time: '2018-12-12', value: 18892182.00, color: '#ef5350' },  
        { time: '2018-12-13', value: 15454706.00, color: '#ef5350' },  
        { time: '2018-12-14', value: 13960870.00, color: '#ef5350' },  
        { time: '2018-12-17', value: 18902523.00, color: '#ef5350' },  
        { time: '2018-12-18', value: 18895777.00, color: '#ef5350' },  
        { time: '2018-12-19', value: 20968473.00, color: '#26a69a' },  
        { time: '2018-12-20', value: 26897008.00, color: '#ef5350' },  
        { time: '2018-12-21', value: 55413082.00, color: '#ef5350' },  
        { time: '2018-12-24', value: 15077207.00, color: '#ef5350' },  
        { time: '2018-12-26', value: 17970539.00, color: '#26a69a' },  
        { time: '2018-12-27', value: 17530977.00, color: '#26a69a' },  
        { time: '2018-12-28', value: 14771641.00, color: '#26a69a' },  
        { time: '2018-12-31', value: 15331758.00, color: '#26a69a' },  
        { time: '2019-01-02', value: 13969691.00, color: '#ef5350' },  
        { time: '2019-01-03', value: 19245411.00, color: '#26a69a' },  
        { time: '2019-01-04', value: 17035848.00, color: '#26a69a' },  
        { time: '2019-01-07', value: 16348982.00, color: '#26a69a' },  
        { time: '2019-01-08', value: 21425008.00, color: '#26a69a' },  
        { time: '2019-01-09', value: 18136000.00, color: '#ef5350' },  
        { time: '2019-01-10', value: 14259910.00, color: '#26a69a' },  
        { time: '2019-01-11', value: 15801548.00, color: '#26a69a' },  
        { time: '2019-01-14', value: 11342293.00, color: '#26a69a' },  
        { time: '2019-01-15', value: 10074386.00, color: '#26a69a' },  
        { time: '2019-01-16', value: 13411691.00, color: '#ef5350' },  
        { time: '2019-01-17', value: 15223854.00, color: '#ef5350' },  
        { time: '2019-01-18', value: 16802516.00, color: '#26a69a' },  
        { time: '2019-01-22', value: 18284771.00, color: '#ef5350' },  
        { time: '2019-01-23', value: 15109007.00, color: '#26a69a' },  
        { time: '2019-01-24', value: 12494109.00, color: '#ef5350' },  
        { time: '2019-01-25', value: 17806822.00, color: '#ef5350' },  
        { time: '2019-01-28', value: 25955718.00, color: '#ef5350' },  
        { time: '2019-01-29', value: 33789235.00, color: '#ef5350' },  
        { time: '2019-01-30', value: 27260036.00, color: '#26a69a' },  
        { time: '2019-01-31', value: 28585447.00, color: '#26a69a' },  
        { time: '2019-02-01', value: 13778392.00, color: '#ef5350' },  
        { time: '2019-02-04', value: 15818901.00, color: '#ef5350' },  
        { time: '2019-02-05', value: 14124794.00, color: '#26a69a' },  
        { time: '2019-02-06', value: 11391442.00, color: '#ef5350' },  
        { time: '2019-02-07', value: 12436168.00, color: '#ef5350' },  
        { time: '2019-02-08', value: 12011657.00, color: '#26a69a' },  
        { time: '2019-02-11', value: 9802798.00, color: '#26a69a' },  
        { time: '2019-02-12', value: 11227550.00, color: '#26a69a' },  
        { time: '2019-02-13', value: 11884803.00, color: '#26a69a' },  
        { time: '2019-02-14', value: 11190094.00, color: '#ef5350' },  
        { time: '2019-02-15', value: 15719416.00, color: '#26a69a' },  
        { time: '2019-02-19', value: 12272877.00, color: '#26a69a' },  
        { time: '2019-02-20', value: 11379006.00, color: '#26a69a' },  
        { time: '2019-02-21', value: 14680547.00, color: '#26a69a' },  
        { time: '2019-02-22', value: 12534431.00, color: '#26a69a' },  
        { time: '2019-02-25', value: 15051182.00, color: '#ef5350' },  
        { time: '2019-02-26', value: 12005571.00, color: '#ef5350' },  
        { time: '2019-02-27', value: 8962776.00, color: '#26a69a' },  
        { time: '2019-02-28', value: 15742971.00, color: '#26a69a' },  
        { time: '2019-03-01', value: 10942737.00, color: '#26a69a' },  
        { time: '2019-03-04', value: 13674737.00, color: '#ef5350' },  
        { time: '2019-03-05', value: 15749545.00, color: '#ef5350' },  
        { time: '2019-03-06', value: 13935530.00, color: '#ef5350' },  
        { time: '2019-03-07', value: 12644171.00, color: '#26a69a' },  
        { time: '2019-03-08', value: 10646710.00, color: '#26a69a' },  
        { time: '2019-03-11', value: 13627431.00, color: '#26a69a' },  
        { time: '2019-03-12', value: 12812980.00, color: '#ef5350' },  
        { time: '2019-03-13', value: 14168350.00, color: '#26a69a' },  
        { time: '2019-03-14', value: 12148349.00, color: '#26a69a' },  
        { time: '2019-03-15', value: 23715337.00, color: '#26a69a' },  
        { time: '2019-03-18', value: 12168133.00, color: '#ef5350' },  
        { time: '2019-03-19', value: 13462686.00, color: '#ef5350' },  
        { time: '2019-03-20', value: 11903104.00, color: '#26a69a' },  
        { time: '2019-03-21', value: 10920129.00, color: '#26a69a' },  
        { time: '2019-03-22', value: 25125385.00, color: '#26a69a' },  
        { time: '2019-03-25', value: 15463411.00, color: '#26a69a' },  
        { time: '2019-03-26', value: 12316901.00, color: '#26a69a' },  
        { time: '2019-03-27', value: 13290298.00, color: '#26a69a' },  
        { time: '2019-03-28', value: 20547060.00, color: '#ef5350' },  
        { time: '2019-03-29', value: 17283871.00, color: '#26a69a' },  
        { time: '2019-04-01', value: 16331140.00, color: '#ef5350' },  
        { time: '2019-04-02', value: 11408146.00, color: '#ef5350' },  
        { time: '2019-04-03', value: 15491724.00, color: '#26a69a' },  
        { time: '2019-04-04', value: 8776028.00, color: '#26a69a' },  
        { time: '2019-04-05', value: 11497780.00, color: '#26a69a' },  
        { time: '2019-04-08', value: 11680538.00, color: '#26a69a' },  
        { time: '2019-04-09', value: 10414416.00, color: '#ef5350' },  
        { time: '2019-04-10', value: 8782061.00, color: '#26a69a' },  
        { time: '2019-04-11', value: 9219930.00, color: '#ef5350' },  
        { time: '2019-04-12', value: 10847504.00, color: '#26a69a' },  
        { time: '2019-04-15', value: 7741472.00, color: '#ef5350' },  
        { time: '2019-04-16', value: 10239261.00, color: '#26a69a' },  
        { time: '2019-04-17', value: 15498037.00, color: '#ef5350' },  
        { time: '2019-04-18', value: 13189013.00, color: '#26a69a' },  
        { time: '2019-04-22', value: 11950365.00, color: '#26a69a' },  
        { time: '2019-04-23', value: 23488682.00, color: '#ef5350' },  
        { time: '2019-04-24', value: 13227084.00, color: '#ef5350' },  
        { time: '2019-04-25', value: 17425466.00, color: '#ef5350' },  
        { time: '2019-04-26', value: 16329727.00, color: '#26a69a' },  
        { time: '2019-04-29', value: 13984965.00, color: '#26a69a' },  
        { time: '2019-04-30', value: 15469002.00, color: '#26a69a' },  
        { time: '2019-05-01', value: 11627436.00, color: '#ef5350' },  
        { time: '2019-05-02', value: 14435436.00, color: '#26a69a' },  
        { time: '2019-05-03', value: 9388228.00, color: '#26a69a' },  
        { time: '2019-05-06', value: 10066145.00, color: '#ef5350' },  
        { time: '2019-05-07', value: 12963827.00, color: '#ef5350' },  
        { time: '2019-05-08', value: 12086743.00, color: '#ef5350' },  
        { time: '2019-05-09', value: 14835326.00, color: '#26a69a' },  
        { time: '2019-05-10', value: 10707335.00, color: '#26a69a' },  
        { time: '2019-05-13', value: 13759350.00, color: '#ef5350' },  
        { time: '2019-05-14', value: 12776175.00, color: '#ef5350' },  
        { time: '2019-05-15', value: 10806379.00, color: '#26a69a' },  
        { time: '2019-05-16', value: 11695064.00, color: '#26a69a' },  
        { time: '2019-05-17', value: 14436662.00, color: '#26a69a' },  
        { time: '2019-05-20', value: 20910590.00, color: '#26a69a' },  
        { time: '2019-05-21', value: 14016315.00, color: '#26a69a' },  
        { time: '2019-05-22', value: 11487448.00, color: '#ef5350' },  
        { time: '2019-05-23', value: 11707083.00, color: '#ef5350' },  
        { time: '2019-05-24', value: 8755506.00, color: '#26a69a' },  
        { time: '2019-05-28', value: 3097125.00, color: '#26a69a' },  
    ]);  
      
    chart.timeScale().fitContent();  
    
