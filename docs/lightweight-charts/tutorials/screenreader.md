# Tutorial: Screenreader

*Source: tutorials\a11y\screenreader.html*

On this page

Accessibility in web development extends beyond just accommodating keyboard-only users. Many users with varying abilities make use of assistive technologies like screen readers to effectively interact with web applications. [ARIA](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA) (Accessible Rich Internet Applications) roles and states offer a powerful toolkit to improve this interaction by conveying information about the behavior and purpose of interface components.

In the context of our line chart, we'll be looking at how to implement ARIA attributes to further enhance its accessibility in addition to generating descriptive content for our graph.

info

In this tutorial we will only make use of the `aria-live`, `aria-label`, and `aria-hidden` attributes. You can explore a [more comprehensive list of attributes on this MDN page] (<https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Attributes>).

## Use of ARIA attributes in the chart[​](screenreader.html#use-of-aria-attributes-in-the-chart "Direct link to Use of ARIA attributes in the chart")

### aria-live[​](screenreader.html#aria-live "Direct link to aria-live")

To provide real-time updates about the chart to assistive technologies, we use the `aria-live` attribute. It accepts a few potential values, although `"polite"` and `"assertive"` are the most common.

With `aria-live="polite"`, updates are presented at the user's next convenient opportunity, such as when they stop typing or when a task is completed. With `aria-live="assertive"`, updates are presented immediately.

Our chart uses the `"assertive"` value because the description should be read out based on a user action (keyboard action):
    
    
    <div id="chart" aria-live="assertive" tabindex="0"></div>  
    

### aria-label[​](screenreader.html#aria-label "Direct link to aria-label")

The `aria-label` attribute is used to specify a string that labels the current element. It's useful when there isn't any text content that describes this element.

On our chart, it could read something like this:
    
    
    <div  
        id="chart"  
        aria-live="polite"  
        aria-label="interactive line chart"  
        tabindex="0"  
    ></div>  
    

### aria-hidden[​](screenreader.html#aria-hidden "Direct link to aria-hidden")

The `aria-hidden` attribute is used to hide irrelevant or redundant information from assistive technologies. Its value is either "true" or "false".

For example, if our chart contained a decorative element with no semantic meaning, we could use `aria-hidden="true"` to hide it from screen readers:
    
    
    <div id="decorative-element" aria-hidden="true"></div>  
    

### Adding the ARIA attributes to an existing chart via JavaScript[​](screenreader.html#adding-the-aria-attributes-to-an-existing-chart-via-javascript "Direct link to Adding the ARIA attributes to an existing chart via JavaScript")
    
    
    <!-- Template for HTML elements added to the chart container for the A11y improvements -->  
    <template id="a11y-helpers">  
        <div tabindex="-1" role="alert" aria-live="assertive"></div>  
    </template>  
      
    <script>  
        function addAriaAttributesAndAlerter(chart) {  
            const containerEl = chart.chartElement().parentElement;  
            if (!containerEl) return;  
            // make focusable  
            containerEl.tabIndex = 0;  
            containerEl.style.position = 'relative';  
            containerEl.ariaLabel =  
                'Line plot of Accessibility stock price. Press the H key to display the available interaction keys.';  
            chart.chartElement().ariaHidden = 'true';  
      
            const templateElement = document.getElementById('a11y-helpers');  
            const clone = templateElement.content.cloneNode(true);  
            containerEl.appendChild(clone);  
        }  
    </script>  
    

## Generating a description of the chart[​](screenreader.html#generating-a-description-of-the-chart "Direct link to Generating a description of the chart")

In addition to ARIA roles, providing a textual description for our charts helps all users, especially those relying on screen readers or other assistive technologies.

You may generate a description of a chart by applying domain-specific knowledge. It's beneficial to outline the general trend or patterns of the data, highlight any notable points or anomalies, and summarize the implications of the data.

You can add a descriptive section to the chart:
    
    
    <div id="chart-description" aria-live="assertive">  
        <!-- The content here should be dynamically generated based on the chart data -->  
    </div>  
    

You can use JavaScript to change the content inside this div whenever the chart data is updated:
    
    
    const descriptionElement = document.getElementById('chart-description');  
    descriptionElement.textContent = generateDescription(mainSeries.data());  
    

Here, `generateDescription(data)` would be a function that you write to translate the chart's data into human-readable insights. The function would vary greatly based on what the charts represent and how much detail you wish to provide.

The example describes the chart based on its first and last visible data points in addition to the highest and lowest points displayed. This is used to generate a description like this:

> The first price is $679.10 at Wed Sep 19 2018. The last price is $555.37 at Wed May 15 2019. The actual change in price was -$123.73, corresponding to a percentage change of -18.22%. The lowest price was $32.76 at Fri Dec 21 2018. The highest price was $951.33 at Sun Mar 24 2019.

The following code could be used as a starting point for generating chart descriptions:
    
    
    function formatDate(time) {  
        return new Date(time * 1000).toDateString();  
    }  
      
    function formatValue(value) {  
        return `${value < 0 ? '-' : ''}$${Math.abs(value).toFixed(2)}`;  
    }  
      
    function getStats(data) {  
        const stats = {  
            start: data[0],  
            close: data[data.length - 1],  
            low: data[0],  
            high: data[0],  
        };  
      
        for (const point of data) {  
            if (point.value > stats.high.value) {  
                stats.high = point;  
            }  
            if (point.value < stats.low.value) {  
                stats.low = point;  
            }  
        }  
      
        return stats;  
    }  
      
    function getVisibleSeriesData(chart, series) {  
        const timeScale = chart.timeScale();  
        const visibleRange = timeScale.getVisibleLogicalRange();  
        const data = [];  
        for (let i = Math.round(visibleRange.from); i <= visibleRange.to; i++) {  
            const d = series.dataByIndex(i, 0);  
            if (d !== null) {  
                data.push(d);  
            }  
        }  
        return data;  
    }  
      
    function describeFinanceChart(data) {  
        if (!data || data.length === 0) {  
            return 'The data set is empty.';  
        }  
      
        const stats = getStats(data);  
      
        const firstPrice = `The first price is ${formatValue(  
            stats.start.value  
        )} at ${formatDate(stats.start.time)}.`;  
        const lastPrice = `The last price is ${formatValue(  
            stats.close.value  
        )} at ${formatDate(stats.close.time)}.`;  
      
        const actualChange = stats.close.value - stats.start.value;  
        const percentChange = (actualChange / stats.start.value) * 100;  
      
        const changeDescription = `The actual change in price was ${formatValue(  
            actualChange  
        )}, corresponding to a percentage change of ${percentChange.toFixed(2)}%.`;  
      
        let lowHigh = '';  
        if (  
            stats.low.time !== stats.start.time &&  
            stats.low.time !== stats.close.time  
        ) {  
            lowHigh += `The lowest price was ${formatValue(  
                stats.low.value  
            )} at ${formatDate(stats.low.time)}.`;  
        }  
        if (  
            stats.high.time !== stats.start.time &&  
            stats.high.time !== stats.close.time  
        ) {  
            lowHigh += ` The highest price was ${formatValue(  
                stats.high.value  
            )} at ${formatDate(stats.high.time)}.`;  
        }  
      
        return `${firstPrice} ${lastPrice} ${changeDescription} ${lowHigh}`.trim();  
    }  
    

## Semantic HTML[​](screenreader.html#semantic-html "Direct link to Semantic HTML")

Using [Semantic HTML](https://developer.mozilla.org/en-US/docs/Glossary/Semantics#semantics_in_html) elements offers several benefits. Firstly, they enhance the accessibility of web content as they provide specific meaning to the browser and assistive technology like screen readers, helping them understand the content's structure and purpose. This is crucial for users with disabilities.

It is suggested that the container provided to the `createChart` method should use a semantic element such as `<figure>` instead of a generic element like `div`.
    
    
    <figure id="chart"></figure>  
    

In the next part, we'll discuss contrast control and font scaling.
