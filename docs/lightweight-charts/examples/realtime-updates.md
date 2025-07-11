# Example: Realtime Updates

*Source: tutorials\demos\realtime-updates.html*

This sample demonstrates how to mimic real-time updates on a candlestick chart with Lightweight Charts™. The chart initially populates with some historical data. By using `setInterval` function, the chart then begins to receive simulated real-time updates with the usage of `series.update(...)`.

Each real-time update represents a new data point or modifies the latest point, providing the illusion of a live, updating chart. If you scroll the chart and wish to return to the latest data points then you can use the "Go to realtime" button provided which calls the [`scrollToRealtime`](../../docs/api/interfaces/ITimeScaleApi.html#scrolltorealtime) method on the timescale.

How to use the code sample

**The code presented below requires:**

  * That `createChart` has already been imported. See [Getting Started](../../docs.html#creating-a-chart) for more information,
  * and that there is an html div element on the page with an `id` of `container`.

Here is an example skeleton setup: [Code Sandbox](https://codesandbox.io/s/lightweight-charts-skeleton-n67pm6). You can paste the provided code below the `// REPLACE EVERYTHING BELOW HERE` comment.

tip

Some code may be hidden to improve readability. Toggle the checkbox above the code block to reveal all the code.

Show all code
    
    
    // Lightweight Charts™ Example: Realtime updates  
    // https://tradingview.github.io/lightweight-charts/tutorials/demos/realtime-updates  
      
      
    let randomFactor = 25 + Math.random() * 25;  
    const samplePoint = i =>  
        i *  
            (0.5 +  
                Math.sin(i / 1) * 0.2 +  
                Math.sin(i / 2) * 0.4 +  
                Math.sin(i / randomFactor) * 0.8 +  
                Math.sin(i / 50) * 0.5) +  
        200 +  
        i * 2;  
      
    function generateData(  
        numberOfCandles = 500,  
        updatesPerCandle = 5,  
        startAt = 100  
    ) {  
        const createCandle = (val, time) => ({  
            time,  
            open: val,  
            high: val,  
            low: val,  
            close: val,  
        });  
      
        const updateCandle = (candle, val) => ({  
            time: candle.time,  
            close: val,  
            open: candle.open,  
            low: Math.min(candle.low, val),  
            high: Math.max(candle.high, val),  
        });  
      
        randomFactor = 25 + Math.random() * 25;  
        const date = new Date(Date.UTC(2018, 0, 1, 12, 0, 0, 0));  
        const numberOfPoints = numberOfCandles * updatesPerCandle;  
        const initialData = [];  
        const realtimeUpdates = [];  
        let lastCandle;  
        let previousValue = samplePoint(-1);  
        for (let i = 0; i < numberOfPoints; ++i) {  
            if (i % updatesPerCandle === 0) {  
                date.setUTCDate(date.getUTCDate() + 1);  
            }  
            const time = date.getTime() / 1000;  
            let value = samplePoint(i);  
            const diff = (value - previousValue) * Math.random();  
            value = previousValue + diff;  
            previousValue = value;  
            if (i % updatesPerCandle === 0) {  
                const candle = createCandle(value, time);  
                lastCandle = candle;  
                if (i >= startAt) {  
                    realtimeUpdates.push(candle);  
                }  
            } else {  
                const newCandle = updateCandle(lastCandle, value);  
                lastCandle = newCandle;  
                if (i >= startAt) {  
                    realtimeUpdates.push(newCandle);  
                } else if ((i + 1) % updatesPerCandle === 0) {  
                    initialData.push(newCandle);  
                }  
            }  
        }  
      
        return {  
            initialData,  
            realtimeUpdates,  
        };  
    }  
      
    const chartOptions = {  
        layout: {  
            textColor: 'black',  
            background: { type: 'solid', color: 'white' },  
        },  
        height: 200,  
    };  
    const container = document.getElementById('container');  
    /** @type {import('lightweight-charts').IChartApi} */  
    const chart = createChart(container, chartOptions);  
      
    // Only needed within demo page  
    // eslint-disable-next-line no-undef  
    window.addEventListener('resize', () => {  
        chart.applyOptions({ height: 200 });  
    });  
      
    const series = chart.addSeries(CandlestickSeries, {  
        upColor: '#26a69a',  
        downColor: '#ef5350',  
        borderVisible: false,  
        wickUpColor: '#26a69a',  
        wickDownColor: '#ef5350',  
    });  
      
    const data = generateData(2500, 20, 1000);  
      
    series.setData(data.initialData);  
    chart.timeScale().fitContent();  
    chart.timeScale().scrollToPosition(5);  
      
    // simulate real-time data  
    function* getNextRealtimeUpdate(realtimeData) {  
        for (const dataPoint of realtimeData) {  
            yield dataPoint;  
        }  
        return null;  
    }  
    const streamingDataProvider = getNextRealtimeUpdate(data.realtimeUpdates);  
      
    const intervalID = setInterval(() => {  
        const update = streamingDataProvider.next();  
        if (update.done) {  
            clearInterval(intervalID);  
            return;  
        }  
        series.update(update.value);  
    }, 100);  
      
    const styles = `  
        .buttons-container {  
            display: flex;  
            flex-direction: row;  
            gap: 8px;  
        }  
        .buttons-container button {  
            all: initial;  
            font-family: -apple-system, BlinkMacSystemFont, 'Trebuchet MS', Roboto, Ubuntu,  
                sans-serif;  
            font-size: 16px;  
            font-style: normal;  
            font-weight: 510;  
            line-height: 24px; /* 150% */  
            letter-spacing: -0.32px;  
            padding: 8px 24px;  
            color: rgba(19, 23, 34, 1);  
            background-color: rgba(240, 243, 250, 1);  
            border-radius: 8px;  
            cursor: pointer;  
        }  
      
        .buttons-container button:hover {  
            background-color: rgba(224, 227, 235, 1);  
        }  
      
        .buttons-container button:active {  
            background-color: rgba(209, 212, 220, 1);  
        }  
    `;  
      
    const stylesElement = document.createElement('style');  
    stylesElement.innerHTML = styles;  
    container.appendChild(stylesElement);  
      
    const buttonsContainer = document.createElement('div');  
    buttonsContainer.classList.add('buttons-container');  
    const button = document.createElement('button');  
    button.innerText = 'Go to realtime';  
    button.addEventListener('click', () => chart.timeScale().scrollToRealTime());  
    buttonsContainer.appendChild(button);  
      
    container.appendChild(buttonsContainer);  
    
