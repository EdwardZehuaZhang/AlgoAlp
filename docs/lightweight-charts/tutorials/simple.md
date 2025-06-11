# Tutorial: Simple

*Source: tutorials\react\simple.html*

info

The following only describes a relatively simple example that only renders an [area series](../../docs/series-types.html#area) that could be tweaked to render any other type of [series](../../docs/series-types.md).

For a more complete scenario where you could wrap Lightweight Charts™ into a component having sub components, please consult this [example](advanced.md).

On this page you will learn how to easily use Lightweight Charts™ with React.

## Preparing your project[​](simple.html#preparing-your-project "Direct link to Preparing your project")

For the example purpose we are using [Parcel starter kit](https://github.com/brandiqa/react-parcel-starter) but feel free to use any other tool or starter kit.
    
    
    git clone git@github.com:brandiqa/react-parcel-starter.git lwc-react  
    cd lwc-react  
    npm install  
    

To run your project simply
    
    
    npm start  
    

This will create a web page accessible by default on <http://localhost:1234>.

## Creating a charting component[​](simple.html#creating-a-charting-component "Direct link to Creating a charting component")

The example _React component_ on this page may not fit your requirements completely. Creating a general purpose declarative wrapper for Lightweight Charts™ imperative API is a challenge, but hopefully you can adapt this example to your use case.

info

For this example we are using props to set chart colors based on the current theme (light or dark). In your real code it might be a better idea to use a [Context](https://reactjs.org/docs/context.html#when-to-use-context).
    
    
      
    import { AreaSeries, createChart, ColorType } from 'lightweight-charts';  
    import React, { useEffect, useRef } from 'react';  
      
    export const ChartComponent = props => {  
        const {  
            data,  
            colors: {  
                backgroundColor = 'white',  
                lineColor = '#2962FF',  
                textColor = 'black',  
                areaTopColor = '#2962FF',  
                areaBottomColor = 'rgba(41, 98, 255, 0.28)',  
            } = {},  
        } = props;  
      
        const chartContainerRef = useRef();  
      
        useEffect(  
            () => {  
                const handleResize = () => {  
                    chart.applyOptions({ width: chartContainerRef.current.clientWidth });  
                };  
      
                const chart = createChart(chartContainerRef.current, {  
                    layout: {  
                        background: { type: ColorType.Solid, color: backgroundColor },  
                        textColor,  
                    },  
                    width: chartContainerRef.current.clientWidth,  
                    height: 300,  
                });  
                chart.timeScale().fitContent();  
      
                const newSeries = chart.addSeries(AreaSeries, { lineColor, topColor: areaTopColor, bottomColor: areaBottomColor });  
                newSeries.setData(data);  
      
                window.addEventListener('resize', handleResize);  
      
                return () => {  
                    window.removeEventListener('resize', handleResize);  
      
                    chart.remove();  
                };  
            },  
            [data, backgroundColor, lineColor, textColor, areaTopColor, areaBottomColor]  
        );  
      
        return (  
            <div  
                ref={chartContainerRef}  
            />  
        );  
    };  
      
    const initialData = [  
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
    ];  
      
    export function App(props) {  
        return (  
            <ChartComponent {...props} data={initialData}></ChartComponent>  
        );  
    }  
    

and you'll have a reusable component that could then be enhanced, tweaked to meet your needs, adding properties and even functionalities.

If you've successfully followed all the steps you should see something similar to
