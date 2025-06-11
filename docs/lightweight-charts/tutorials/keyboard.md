# Tutorial: Keyboard

*Source: tutorials\a11y\keyboard.html*

On this page

## Purpose of keyboard navigation[​](keyboard.html#purpose-of-keyboard-navigation "Direct link to Purpose of keyboard navigation")

One cornerstone of web accessibility is ensuring that sites and applications are fully operable via keyboard alone. This navigation method benefits a wide range of users, especially those who are unable to use a mouse or have visual impairments.

Screen readers and other assistive technologies rely heavily on keyboard interaction, and some users choose this method due to an acquired skill set or personal preference. By including keyboard navigation in our charts, we make the tool more accessible and user-friendly, living up to the principles of inclusive design.

## Implementing keyboard actions with Lightweight Charts™[​](keyboard.html#implementing-keyboard-actions-with-lightweight-charts "Direct link to Implementing keyboard actions with Lightweight Charts™")

The Lightweight Charts™ API provides numerous methods that enable handling chart actions programmatically, making it possible to tie these actions to keyboard events.

Here's a walk-through of how to add keyboard navigation to the chart.

### Setting focus on the chart[​](keyboard.html#setting-focus-on-the-chart "Direct link to Setting focus on the chart")

Firstly, we must ensure the chart is programmatically focusable for keyboard interaction. We can achieve this by placing a `tabindex` attribute to the chart's container div:
    
    
    <div id="chart" tabindex="0"></div>  
    

This can also be achieved via JavaScript:
    
    
    const containerEl = chart.chartElement().parentElement;  
    containerEl.tabIndex = 0;  
    

### Adding event listener for keyboard actions[​](keyboard.html#adding-event-listener-for-keyboard-actions "Direct link to Adding event listener for keyboard actions")

Following that, we will tie specific chart interactions to keypress events using JavaScript's `addEventListener` method. This will allow us to control the chart using specific keystrokes:
    
    
    const chartContainer = document.getElementById('chart');  
    chartContainer.addEventListener('keydown', event => {  
        switch (event.key) {  
        case 'ArrowLeft':  
            // Action for ArrowLeft key  
            break;  
        case 'ArrowRight':  
            // Action for ArrowRight key  
            break;  
            // ... more cases  
        }  
    });  
    

The `addEventListener` function lets us listen to `keydown` events that occur when the user presses a key.

### Utilizing Lightweight Chart's API for actions[​](keyboard.html#utilizing-lightweight-charts-api-for-actions "Direct link to Utilizing Lightweight Chart's API for actions")

Next, for each case, we use Lightweight Chart's API for desired actions.

Let's assume we want the left arrow key to scroll the chart to the left, and the right arrow key to scroll it to the right:
    
    
    function shiftChart(diff) {  
        const currentPos = chart.timeScale().scrollPosition();  
        chart.timeScale().scrollToPosition(currentPos + diff, false);  
    }  
      
    chartContainer.addEventListener('keydown', event => {  
        switch (event.key) {  
        case 'ArrowLeft':  
            shiftChart(-10);  
            break;  
        case 'ArrowRight':  
            shiftChart(10);  
            break;  
        }  
    });  
    

In the above JavaScript code, the `timeScale().scrollToPosition()` method from Lightweight Charts™ API is used inside the event listener to scroll the chart whenever the left or right arrow key is pressed.

Additionally, we can assign the up and down arrow keys to adjust the zoom level of the chart:
    
    
    function scaleChart(pct, zoomIn) {  
        const currentRange = chart.timeScale().getVisibleLogicalRange();  
        if (currentRange) {  
            const bars = currentRange.to - currentRange.from;  
            const direction = zoomIn ? -1 : 1;  
            const newRangeBars = bars * pct * direction + bars;  
            chart.timeScale().setVisibleLogicalRange({  
                to: currentRange.to,  
                from: currentRange.to - newRangeBars,  
            });  
        }  
    }  
      
    chartContainer.addEventListener('keydown', event => {  
        switch (event.key) {  
        // ...  
        case 'ArrowUp':  
            scaleChart(1 / 8, true);  
            break;  
        case 'ArrowDown':  
            scaleChart(1 / 8, false);  
            break;  
        }  
    });  
    

We are scaling the chart by adjusting the `visibleLogicalRange` instead of changing the `barSpacing` option on the time scale. In this example, we are keeping the right data point fixed when zooming in or out by retaining the `to` value and only modifying the `from` value.

* * *

This keyboard navigation inclusion makes the chart's underlying data more accessible to a wider audience, ensuring a diverse user base can fully interact with the chart's functions.

tip

Note that more keyboard actions can be added according to project-specific requirements, thereby further enhancing the navigation controls and accessibility.

In the next section, we'll continue enhancing our accessible charts by integrating ARIA (Accessible Rich Internet Applications) roles and properties and generating descriptive content.
