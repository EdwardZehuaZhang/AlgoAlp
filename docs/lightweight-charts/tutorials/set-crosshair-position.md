# Tutorial: Set Crosshair Position

*Source: tutorials\how_to\set-crosshair-position.html*

On this page

Lightweight Charts™ allows the crosshair position to be set programatically using the [`setCrosshairPosition`](../../docs/api/interfaces/IChartApi.html#setcrosshairposition), and cleared using [`clearCrosshairPosition`](../../docs/api/interfaces/IChartApi.html#clearcrosshairposition).

Usually the crosshair position is set automatically by the user's actions. However in some cases you may want to set it explicitly. For example if you want to synchronise the crosshairs of two separate charts.

## Syncing two charts[​](set-crosshair-position.html#syncing-two-charts "Direct link to Syncing two charts")

Show all code
    
    
    // Lightweight Charts™ Example: Crosshair syncing  
    // https://tradingview.github.io/lightweight-charts/tutorials/how_to/set-crosshair-position  
      
    function generateData(startValue, startDate) {  
        const res = [];  
        const time = startDate ?? (new Date(Date.UTC(2018, 0, 1, 0, 0, 0, 0)));  
        for (let i = 0; i < 500; ++i) {  
            res.push({  
                time: time.getTime() / 1000,  
                value: i + startValue,  
            });  
      
            time.setUTCDate(time.getUTCDate() + 1);  
        }  
      
        return res;  
    }  
      
    const chart1 = createChart(  
        document.getElementById('container'),  
        {  
            height: 250,  
            crosshair: {  
                mode: 0,  
            },  
            timeScale: {  
                visible: false,  
            },  
            layout: {  
                background: {  
                    type: 'solid',  
                    color: '#FFF5F5',  
                },  
            },  
        }  
    );  
    const mainSeries1 = chart1.addSeries(LineSeries, {  
        color: 'red',  
    });  
      
    mainSeries1.setData(generateData(0));  
      
    const chart2 = createChart(  
        document.getElementById('container'),  
        {  
            height: 250,  
            layout: {  
                background: {  
                    type: 'solid',  
                    color: '#F5F5FF',  
                },  
            },  
        }  
    );  
      
    const mainSeries2 = chart2.addSeries(LineSeries, {  
        color: 'blue',  
    });  
      
    mainSeries2.setData(generateData(100));  
      
    chart1.timeScale().subscribeVisibleLogicalRangeChange(timeRange => {  
        chart2.timeScale().setVisibleLogicalRange(timeRange);  
    });  
      
    chart2.timeScale().subscribeVisibleLogicalRangeChange(timeRange => {  
        chart1.timeScale().setVisibleLogicalRange(timeRange);  
    });  
      
    function getCrosshairDataPoint(series, param) {  
        if (!param.time) {  
            return null;  
        }  
        const dataPoint = param.seriesData.get(series);  
        return dataPoint || null;  
    }  
      
    function syncCrosshair(chart, series, dataPoint) {  
        if (dataPoint) {  
            chart.setCrosshairPosition(dataPoint.value, dataPoint.time, series);  
            return;  
        }  
        chart.clearCrosshairPosition();  
    }  
    chart1.subscribeCrosshairMove(param => {  
        const dataPoint = getCrosshairDataPoint(mainSeries1, param);  
        syncCrosshair(chart2, mainSeries2, dataPoint);  
    });  
    chart2.subscribeCrosshairMove(param => {  
        const dataPoint = getCrosshairDataPoint(mainSeries2, param);  
        syncCrosshair(chart1, mainSeries1, dataPoint);  
    });  
    

## Tracking without long-press (on mobile)[​](set-crosshair-position.html#tracking-without-long-press-on-mobile "Direct link to Tracking without long-press \(on mobile\)")

If scrolling and scaling is disabled, then the API can be used to enable a kind of tracking mode without the user having to long-press the screen.

Show all code
    
    
    // Lightweight Charts™ Example: Crosshair syncing  
    // https://tradingview.github.io/lightweight-charts/tutorials/how_to/set-crosshair-position  
      
    function generateData() {  
        const res = [];  
        const time = new Date(Date.UTC(2018, 0, 1, 0, 0, 0, 0));  
        for (let i = 0; i < 500; ++i) {  
            res.push({  
                time: time.getTime() / 1000,  
                value: i,  
            });  
      
            time.setUTCDate(time.getUTCDate() + 1);  
        }  
      
        return res;  
    }  
      
    const chart = createChart(  
        document.getElementById('container'),  
        {  
            handleScale: false,  
            handleScroll: false,  
        }  
    );  
      
    const mainSeries = chart.addSeries({  
        priceFormat: {  
            minMove: 1,  
            precision: 0,  
        },  
    });  
      
    mainSeries.setData(generateData());  
      
    chart.timeScale().fitContent();  
      
    document.getElementById('container').addEventListener('touchmove', e => {  
        const bcr = document.getElementById('container').getBoundingClientRect();  
        const x = bcr.left + e.touches[0].clientX;  
        const y = bcr.top + e.touches[0].clientY;  
      
        const price = mainSeries.coordinateToPrice(y);  
        const time = chart.timeScale().coordinateToTime(x);  
      
        if (!Number.isFinite(price) || !Number.isFinite(time)) {  
            return;  
        }  
      
        chart.setCrosshairPosition(price, time, mainSeries);  
    });  
      
    document.getElementById('container').addEventListener('touchend', () => {  
        chart.clearCrosshairPosition();  
    });  
    
