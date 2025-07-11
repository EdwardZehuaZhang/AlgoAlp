# Tutorial: Readability

*Source: tutorials\a11y\readability.html*

On this page

## High contrast and scalable font size[​](readability.html#high-contrast-and-scalable-font-size "Direct link to High contrast and scalable font size")

Ensuring accessibility in web development means accommodating various user preferences and physical abilities. High contrast mode and scalable font size are two such distinct features that have been included in our chart, catering to diverse user needs.

### High contrast mode[​](readability.html#high-contrast-mode "Direct link to High contrast mode")

Certain users with specific visual impairments may struggle to distinguish between colors or interpret text and image details in low contrast. For these users, a high-contrast mode can be immensely helpful.

In our chart application, we leverage the built-in browser feature `window.matchMedia()` to ascertain if the user has indicated a preference for higher contrast in their system settings.

Here's how we determine if the user prefers a high-contrast mode:
    
    
    // Check if user prefers high contrast mode  
    function checkHighContrast() {  
        // Use window.matchMedia to check 'prefers-contrast' media feature  
        const highContrast = window.matchMedia('(prefers-contrast: high)').matches;  
        return highContrast; // Returns true if high contrast is enabled, false otherwise  
    }  
      
    // Subscribe to changes  
    const highContrastMediaQuery = window.matchMedia('(prefers-contrast: high)');  
    highContrastMediaQuery.addListener(() => {  
        setHighContrast(highContrastMediaQuery.matches);  
    });  
    

A `setHighContrast` function could be implemented as follows:
    
    
    const seriesBaseContrastSettings = {  
        color: 'rgb(41, 98, 255)',  
        lineWidth: 2,  
    };  
    const chartBaseContrastSettings = {  
        layout: {  
            textColor: '#191919',  
        },  
        grid: {  
            vertLines: {  
                color: '#D6DCDE',  
            },  
            horzLines: {  
                color: '#D6DCDE',  
            },  
        },  
    };  
    const seriesHighContrastSettings = {  
        color: 'rgb(0, 0, 0)',  
        lineWidth: 4,  
    };  
    const chartHighContrastSettings = {  
        layout: {  
            textColor: '#000000',  
        },  
        grid: {  
            vertLines: {  
                color: '#777777',  
            },  
            horzLines: {  
                color: '#777777',  
            },  
        },  
    };  
      
    function setHighContrast(enabled) {  
        mainSeries.applyOptions(  
            enabled ? seriesHighContrastSettings : seriesBaseContrastSettings  
        );  
        chart.applyOptions(  
            enabled ? chartHighContrastSettings : chartBaseContrastSettings  
        );  
    }  
    

Our `setHighContrast(highContrast)` function updates the chart's colors based on the user's preference. If the user prefers high contrast, a higher contrast color scheme is applied. If not, the colors switch back to the default, low-contrast scheme.

### Scalable font size[​](readability.html#scalable-font-size "Direct link to Scalable font size")

Another key aspect of web accessibility is the option to scale font sizes. Users with visual impairments may benefit from larger text sizes, improving readability.

We provide an option for these users to adjust the text size through a checkbox, which changes text size in the chart:
    
    
    <input type="checkbox" id="large-font-checkbox" tabindex="0" />  
    <label for="large-font-checkbox">Toggle Larger Font</label>  
    

Then, we create an event listener in JavaScript for this checkbox input, which increases the text size:
    
    
    function setFontSize(large) {  
        chart.applyOptions({  
            layout: {  
                fontSize: large ? 16 : 12,  
            },  
        });  
    }  
      
    document  
        .querySelector('#large-font-checkbox')  
        .addEventListener('change', event => {  
            setFontSize(event.target.checked);  
        });  
    

In this example, when the 'Increase Font Size' input is checked, the font size in the chart increases to 16px.

Including these additional accessibility features adheres to the principles of creating an inclusive web, where design embraces all user types, abilities, and preferences. Note that you should conduct rigorous accessibility testing before deployment.
