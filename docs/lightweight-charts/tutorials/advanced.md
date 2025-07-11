# Tutorial: Advanced

*Source: tutorials\react\advanced.html*

info

The following describes a more complex scenario where a user could imagine splitting the responsibilities of the chart between components.

If you want to consult a simpler approach please consult this [example](simple.md).

warning

By following the steps below we assume you're familiar with Lightweight Charts™, how to set up a project using it and how to render a chart.

If not, please follow this [guide](simple.md).

If you're familiar with Lightweight Charts™ you probably already know that a _Chart_ is a container that can contain one or more [_Series_](../../docs/series-types.md). Each _Series_ has its own options (for instance [AreaStyleOptions](../../docs/api/interfaces/AreaStyleOptions.md), [LineStyleOptions](../../docs/api/interfaces/LineStyleOptions.md), etc) in addition to [price](../../docs/price-scale.md) and/or [time](../../docs/time-scale.md) scale.

Based on this principle, one could easily imagine having a main component _Chart_ that could have some _Series_ children that could themselves have other children and so on. Therefore the structure could become something like
    
    
    <Chart component>  
        <Series component 1>  
            <child component />  
        </Series component 1>  
        <Series component n>  
            <child component />  
        </Series component n>  
    </Chart component>  
    

Even though it's possible to create a Chart without a Series, the complexity arises when another component wants to interact with any of its siblings/parent, like updating a series by adding more data or resizing the chart itself.

Given this tutorial is about React this is how we are going to define components relying on React [Hooks](https://reactjs.org/docs/hooks-intro.html) and [composition](https://reactjs.org/docs/composition-vs-inheritance.html).

However, one drawback with the way React and its hooks like _useEffect_ [work](https://github.com/facebook/react/issues/16728) in a parent/children implementation is that their respective hooks are called in a bottom-up order for instanciation but top-to-bottom when it comes to clean-up.

The following skeleton illustrates the mechanism.
    
    
    import React, { useEffect } from 'react';  
      
    export const ParentComponent = () => {  
        // this effect will be triggered in position 3  
        useEffect(() =>  
            () => {  
                // this clean up will be triggered in position 1  
            }  
        , []);  
      
        // this effect will be triggered in position 4  
        useEffect(() =>  
            () => {  
                // this clean up will be triggered in position 2  
            }  
        , []);  
      
        // The parent will then return Following bit is to propagate all props & internalRef object down to children  
        return (  
            <ChildComponent />  
        );  
    };  
    ParentComponent.displayName = 'ParentComponent';  
      
    export const ChildComponent = () => {  
        // this effect will be triggered in position 1  
        useEffect(() =>  
            () => {  
                // this clean up will be triggered in position 3  
            }  
        , []);  
      
        // this effect will be triggered in position 2  
        useEffect(() =>  
            () => {  
                // this clean up will be triggered in position 4  
            }  
        , []);  
      
        return (  
            <div />  
        );  
    };  
    ChildComponent.displayName = 'ChildComponent';  
    

In essence, taking the example above, it means that a `ChildComponent` (aka Series) would be created first whilst requiring a `ParentComponent` (aka Chart).

To achieve that, we will have to rely on a few hooks and take advantage of the way they work in addition to use [ref/forwardRef](https://reactjs.org/docs/forwarding-refs.html) which is a technique to pass down properties from one component to its children.

In the end the "visible" structure and usage will be alike but internally it will be something like:
    
    
    <Chart component>  
        <ChartContainer>  
            <Series component 1>  
                <child component />  
            </Series component 1>  
            <Series component n>  
                <child component />  
            </Series component n>  
        </ChartContainer>  
    </Chart component>  
    

where the ChartContainer's role would be needed to attach a DOMElement on which the chart will render. ChartContainer will be responsible for creating a **ref** erence that will hold functions to handle the lifecycle of the chart. That reference will then be propagated down to the Series.

The same technique will be used within the Series component to handle this time the lifecycle of any Series along with adding data to be plotted.

Moreover those 2 "main" components will "expose" whatever functions the user wants from the internal reference object at a higher level, meaning once those references are accessible any other component would then be able to act on either the Chart or any Series.

Here's a skeleton of what the final structure would be like:
    
    
    import React, { useEffect, useImperativeHandle, useRef, createContext, forwardRef } from 'react';  
      
    const Context = createContext();  
      
    export const MainComponent = props =>  
        // Creates the first reference and instanciate a ParentComponent  
        (  
            <div ref={chartReference}>  
                <ParentComponent {...props} container={container} />  
            </div>  
        );  
      
    export const ParentComponent = forwardRef((props, ref) => {  
        const internalRef = useRef({  
            method1() {  
                // This function would be responsible for creating the chart for instance  
            },  
            methodn() {  
                // This function would be responsible for cleaning up the chart  
            },  
        });  
      
        // this effect will be triggered in position 3  
        useEffect(() =>  
            () => {  
                // this clean up will be triggered in position 1  
            }  
        , []);  
      
        // this effect will be triggered in position 4  
        useEffect(() =>  
            () => {  
                // this clean up will be triggered in position 2  
            }  
        , []);  
      
        useImperativeHandle(ref, () => {  
            // That's the hook responsible for exposing part of/entirety of internalRef  
        }, []);  
      
        // Following bit is to propagate all props & internalRef object down to children  
        return (  
            <Context.Provider value={internalRef.current}>  
                {props.children}  
            </Context.Provider>  
        );  
    });  
    ParentComponent.displayName = 'ParentComponent';  
      
    export const ChildComponent = forwardRef((props, ref) => {  
        const internalRef = useRef({  
            method1() {  
                // This function would be responsible for creating a series  
            },  
            methodn() {  
                // This function would be responsible for removing it  
            },  
        });  
      
        // this effect will be triggered in position 1  
        useEffect(() =>  
            () => {  
                // this clean up will be triggered in position 3  
            }  
        , []);  
      
        // this effect will be triggered in position 2  
        useEffect(() =>  
            () => {  
                // this clean up will be triggered in position 4  
            }  
        , []);  
      
        useImperativeHandle(ref, () => {  
            // That's the hook responsible for exposing part of/entirety of internalRef  
        }, []);  
      
        // Following bit is to propagate all props & internalRef object down to children  
        return (  
            <Context.Provider value={internalRef.current}>  
                {props.children}  
            </Context.Provider>  
        );  
    });  
    ChildComponent.displayName = 'ChildComponent';  
    

By considering all the above you could end up with Chart/Series components looking like the following

info

For this example we are using props to set chart colors based on the current theme (light or dark). In your real code it might be a better idea to use a [Context](https://reactjs.org/docs/context.html#when-to-use-context).
    
    
      
    import { createChart, LineSeries, AreaSeries } from 'lightweight-charts';  
    import React, {  
        createContext,  
        forwardRef,  
        useCallback,  
        useContext,  
        useEffect,  
        useImperativeHandle,  
        useLayoutEffect,  
        useRef,  
        useState,  
    } from 'react';  
      
    const Context = createContext();  
      
    const initialData = [  
        { time: '2018-10-11', value: 52.89 },  
        { time: '2018-10-12', value: 51.65 },  
        { time: '2018-10-13', value: 51.56 },  
        { time: '2018-10-14', value: 50.19 },  
        { time: '2018-10-15', value: 51.86 },  
        { time: '2018-10-16', value: 51.25 },  
    ];  
      
    const initialData2 = [  
        { time: '2018-10-11', value: 42.89 },  
        { time: '2018-10-12', value: 41.65 },  
        { time: '2018-10-13', value: 41.56 },  
        { time: '2018-10-14', value: 40.19 },  
        { time: '2018-10-15', value: 41.86 },  
        { time: '2018-10-16', value: 41.25 },  
    ];  
    const currentDate = new Date(initialData[initialData.length - 1].time);  
      
    export const App = props => {  
        const {  
            colors: {  
                backgroundColor = 'white',  
                lineColor = '#2962FF',  
                textColor = 'black',  
            } = {},  
        } = props;  
      
        const [chartLayoutOptions, setChartLayoutOptions] = useState({});  
        // The following variables illustrate how a series could be updated.  
        const series1 = useRef(null);  
        const series2 = useRef(null);  
        const [started, setStarted] = useState(false);  
        const [isSecondSeriesActive, setIsSecondSeriesActive] = useState(false);  
      
        // The purpose of this effect is purely to show how a series could  
        // be updated using the `reference` passed to the `Series` component.  
        useEffect(() => {  
            if (series1.current === null) {  
                return;  
            }  
            let intervalId;  
      
            if (started) {  
                intervalId = setInterval(() => {  
                    currentDate.setDate(currentDate.getDate() + 1);  
                    const next = {  
                        time: currentDate.toISOString().slice(0, 10),  
                        value: 53 - 2 * Math.random(),  
                    };  
                    series1.current.update(next);  
                    if (series2.current) {  
                        series2.current.update({  
                            ...next,  
                            value: 43 - 2 * Math.random(),  
                        });  
                    }  
                }, 1000);  
            }  
            return () => clearInterval(intervalId);  
        }, [started]);  
      
        useEffect(() => {  
            setChartLayoutOptions({  
                background: {  
                    color: backgroundColor,  
                },  
                textColor,  
            });  
        }, [backgroundColor, textColor]);  
      
        return (  
            <>  
                <button type="button" onClick={() => setStarted(current => !current)}>  
                    {started ? 'Stop updating' : 'Start updating series'}  
                </button>  
                <button type="button" onClick={() => setIsSecondSeriesActive(current => !current)}>  
                    {isSecondSeriesActive ? 'Remove second series' : 'Add second series'}  
                </button>  
                <Chart layout={chartLayoutOptions}>  
                    <Series  
                        ref={series1}  
                        type={'line'}  
                        data={initialData}  
                        color={lineColor}  
                    />  
                    {isSecondSeriesActive && <Series  
                        ref={series2}  
                        type={'area'}  
                        data={initialData2}  
                        color={lineColor}  
                    />}  
                </Chart>  
            </>  
        );  
    };  
      
    export function Chart(props) {  
        const [container, setContainer] = useState(false);  
        const handleRef = useCallback(ref => setContainer(ref), []);  
        return (  
            <div ref={handleRef}>  
                {container && <ChartContainer {...props} container={container} />}  
            </div>  
        );  
    }  
      
    export const ChartContainer = forwardRef((props, ref) => {  
        const { children, container, layout, ...rest } = props;  
      
        const chartApiRef = useRef({  
            isRemoved: false,  
            api() {  
                if (!this._api) {  
                    this._api = createChart(container, {  
                        ...rest,  
                        layout,  
                        width: container.clientWidth,  
                        height: 300,  
                    });  
                    this._api.timeScale().fitContent();  
                }  
                return this._api;  
            },  
            free(series) {  
                if (this._api && series) {  
                    this._api.removeSeries(series);  
                }  
            },  
        });  
      
        useLayoutEffect(() => {  
            const currentRef = chartApiRef.current;  
            const chart = currentRef.api();  
      
            const handleResize = () => {  
                chart.applyOptions({  
                    ...rest,  
                    width: container.clientWidth,  
                });  
            };  
      
            window.addEventListener('resize', handleResize);  
            return () => {  
                window.removeEventListener('resize', handleResize);  
                chartApiRef.current.isRemoved = true;  
                chart.remove();  
            };  
        }, []);  
      
        useLayoutEffect(() => {  
            const currentRef = chartApiRef.current;  
            currentRef.api();  
        }, []);  
      
        useLayoutEffect(() => {  
            const currentRef = chartApiRef.current;  
            currentRef.api().applyOptions(rest);  
        }, []);  
      
        useImperativeHandle(ref, () => chartApiRef.current.api(), []);  
      
        useEffect(() => {  
            const currentRef = chartApiRef.current;  
            currentRef.api().applyOptions({ layout });  
        }, [layout]);  
      
        return (  
            <Context.Provider value={chartApiRef.current}>  
                {props.children}  
            </Context.Provider>  
        );  
    });  
    ChartContainer.displayName = 'ChartContainer';  
      
    export const Series = forwardRef((props, ref) => {  
        const parent = useContext(Context);  
        const context = useRef({  
            api() {  
                if (!this._api) {  
                    const { children, data, type, ...rest } = props;  
                    this._api =  
                        type === 'line'  
                            ? parent.api().addSeries(LineSeries, rest)  
                            : parent.api().addSeries(AreaSeries, rest);  
                    this._api.setData(data);  
                }  
                return this._api;  
            },  
            free() {  
                // check if parent component was removed already  
                if (this._api && !parent.isRemoved) {  
                    // remove only current series  
                    parent.free(this._api);  
                }  
            },  
        });  
      
        useLayoutEffect(() => {  
            const currentRef = context.current;  
            currentRef.api();  
      
            return () => currentRef.free();  
        }, []);  
      
        useLayoutEffect(() => {  
            const currentRef = context.current;  
            const { children, data, ...rest } = props;  
            currentRef.api().applyOptions(rest);  
        });  
      
        useImperativeHandle(ref, () => context.current.api(), []);  
      
        return (  
            <Context.Provider value={context.current}>  
                {props.children}  
            </Context.Provider>  
        );  
    });  
    Series.displayName = 'Series';  
    

The code above will produce a line series. Given a `series1` reference is created to be passed to the Series component you could reuse that object via `series1.current.[any function applicable on Series]`.

For instance and as shown below `series1.current.update(new data)` is used upon clicking on the button.

Start updating seriesAdd second series
