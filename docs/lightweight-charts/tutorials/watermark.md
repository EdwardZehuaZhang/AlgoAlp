# Tutorial: Watermark

*Source: tutorials\how_to\watermark.html*

On this page

Lightweight Charts™ has a built-in feature for displaying simple text watermarks on your chart. This example shows how to configure and add this simple text watermark to your chart. If you are looking to add a more complex watermark then have a look at the [image watermark example](watermark.html#image-watermark-example) included below.

## Short answer[​](watermark.html#short-answer "Direct link to Short answer")

A simple text watermark can be configured and added by using the [`createTextWatermark`](../../docs/next/api/functions/createTextWatermark.md) function exported from the library as follows:
    
    
    import { createTextWatermark } from 'lightweight-charts';  
      
    const firstPane = chart.panes()[0];  
    const textWatermark = createTextWatermark(firstPane, {  
        horzAlign: 'center',  
        vertAlign: 'center',  
        lines: [  
            {  
                text: 'Watermark Example',  
                color: 'rgba(171, 71, 188, 0.5)',  
                fontSize: 24,  
            },  
        ],  
    });  
      
    

The options available for the watermark are: [TextWatermark Options](../../docs/next/api/interfaces/TextWatermarkOptions.md).

You can see full [working examples](watermark.html#examples) below.

## Resources[​](watermark.html#resources "Direct link to Resources")

  * [`createTextWatermark` function](../../docs/next/api/functions/createTextWatermark.md).
  * [TextWatermark Options](../../docs/next/api/interfaces/TextWatermarkOptions.md)

## Examples[​](watermark.html#examples "Direct link to Examples")

How to use the code sample

**The code presented below requires:**

  * That `createChart` has already been imported. See [Getting Started](../../docs.html#creating-a-chart) for more information,
  * and that there is an html div element on the page with an `id` of `container`.

Here is an example skeleton setup: [Code Sandbox](https://codesandbox.io/s/lightweight-charts-skeleton-n67pm6). You can paste the provided code below the `// REPLACE EVERYTHING BELOW HERE` comment.

tip

Some code may be hidden to improve readability. Toggle the checkbox above the code block to reveal all the code.

### Simple Watermark Example[​](watermark.html#simple-watermark-example "Direct link to Simple Watermark Example")

Show all code
    
    
    // Lightweight Charts™ Example: Watermark Simple  
    // https://tradingview.github.io/lightweight-charts/tutorials/how_to/watermark  
      
    const chartOptions = {  
        layout: {  
            textColor: 'black',  
            background: { type: 'solid', color: 'white' },  
        },  
    };  
    /** @type {import('lightweight-charts').IChartApi} */  
    const chart = createChart(document.getElementById('container'), chartOptions);  
      
    /** @type {import('lightweight-charts').createTextWatermark} */  
    createTextWatermark(chart.panes()[0], {  
        horzAlign: 'center',  
        vertAlign: 'center',  
        lines: [  
            {  
                text: 'Watermark Example',  
                color: 'rgba(171, 71, 188, 0.5)',  
                fontSize: 24,  
            },  
        ],  
    });  
      
    const lineSeries = chart.addSeries(AreaSeries, {  
        topColor: '#2962FF',  
        bottomColor: 'rgba(41, 98, 255, 0.28)',  
        lineColor: '#2962FF',  
        lineWidth: 2,  
    });  
      
    const data = [  
        { value: 0, time: 1642425322 },  
        { value: 8, time: 1642511722 },  
        { value: 10, time: 1642598122 },  
        { value: 20, time: 1642684522 },  
        { value: 3, time: 1642770922 },  
        { value: 43, time: 1642857322 },  
        { value: 41, time: 1642943722 },  
        { value: 43, time: 1643030122 },  
        { value: 56, time: 1643116522 },  
        { value: 46, time: 1643202922 },  
    ];  
      
    lineSeries.setData(data);  
      
    chart.timeScale().fitContent();  
    

### Image Watermark Example[​](watermark.html#image-watermark-example "Direct link to Image Watermark Example")

If a simple text watermark doesn't meet your requirements then you can use the Image watermark via [`createImageWatermark`](../../docs/next/api/functions/createImageWatermark.md) function exported from the library as follows:
    
    
    import { createImageWatermark } from 'lightweight-charts';  
      
    const firstPane = chart.panes()[0];  
    const imageWatermark = createImageWatermark(firstPane, '/images/my-image.png', {  
        alpha: 0.5,  
        padding: 20,  
    });  
    

The options available for the watermark are: [ImageWatermark Options](../../docs/next/api/interfaces/ImageWatermarkOptions.md).

You can see full [working examples](watermark.html#examples) below.

## Resources[​](watermark.html#resources-1 "Direct link to Resources")

  * [`createImageWatermark` pane primitive](../../docs/next/api/functions/createTextWatermark.md).
  * [ImageWatermark Options](../../docs/next/api/interfaces/ImageWatermarkOptions.md)

tip

Since the watermark image is black content with a transparent background, it may not be visible when viewing the documentation site in dark mode.

Show all code
    
    
    // Lightweight Charts™ Example: Image Watermark  
    // https://tradingview.github.io/lightweight-charts/tutorials/how_to/watermark  
      
    const chartOptions = {  
        layout: {  
            textColor: 'black',  
            background: { type: 'solid', color: 'white' },  
        },  
    };  
    /** @type {import('lightweight-charts').IChartApi} */  
    const chart = createChart(document.getElementById('container'), chartOptions);  
      
    // imageDataUrl would usually be an url like '/images/my-image.png'  
    const imageDataUrl = 'data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyOTIiIGhlaWdodD0iMTI4IiB2aWV3Qm94PSIwIDAgMjkyIDEyOCI+PHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBkPSJtMTgyLjkzIDcuNi42My0uMzdhNjQuMSA2NC4xIDAgMCAwIDIuNDMtNS4zMWw0Ljc3LTEuMzlhNjQuNjggNjQuNjggMCAwIDEtNC43MiAxMC41NGMuMzggMTAuNDUtMy45MyAyMS4xNS0xMS4xIDI5LjM3LTExLjY2IDEzLjQxLTI2Ljk4IDE1Ljk3LTQzLjU3IDEzLjc4bDEuMDctLjk4YTIxLjEgMjEuMSAwIDAgMCAzLjcyLTQuMDUgNDguMzcgNDguMzcgMCAwIDEtMTEuMDQgMi44NGMtMTAuNjUtNS41NC0yMS42NC0xNC45NC0yNC4yNy0yNy4yNyA5LjE5LTE3IDI4Ljk1LTI0LjAxIDQ3LjM5LTE5Ljk0YTIyLjU3IDIyLjU3IDAgMCAwIDUuODYgOS4wMmMtLjEyLTEuOTItLjEtMy44NC0uMS01Ljc2bC4wMS0xLjc4YzQuOCAyLjk2IDkuNjYgNS44NSAxNS41MiA1LjcgNC4wOC0uMSA4LjQtMS41MiAxMy40LTQuNFptLTIyLjU1IDIzLjI4YTguNDggOC40OCAwIDAgMC0xMi40NS0uMzNsLTcuOS03LjI2QTguNiA4LjYgMCAwIDAgMTMyIDEyYy02LjE0IDAtMTAuMjUgNi42My03LjcgMTIuMDlsLTEzLjAyIDEyLjE5Yy00LjEtNC45Ny01LjY4LTkuMy02LjE3LTEwLjk0IDguMzYtMTMuNzIgMjQuNDYtMjAuMTggNDAuMTUtMTcuMDcgMi45MyA2LjkgOC4zOCAxMC43MiAxNC43NyAxMy45NmwtLjMzLTEuMTRjLS43NC0yLjU2LTEuNDctNS4xLTEuNjItNy43OCA3LjA1IDMuNDUgMTQuNiAzLjM1IDIxLjc2LjMxLTQuNzYgNy4yNy0xMS4xMyAxNC4yMi0xOS40NiAxNy4yNlptLTIyLjU2LTQuMTkgOC4wMyA3LjM4QTguNiA4LjYgMCAwIDAgMTU0IDQ1YTguNiA4LjYgMCAwIDAgOC4yNS0xMC41NWM3Ljk5LTMuMDggMTQuMzctOS4zOCAxOS4yOC0xNi4yMy0zLjQ3IDE5LjQ3LTIxLjk2IDM0LjYxLTQxLjkgMzIuOTggMS43Ny0yLjg0IDIuNDktNi4wNiAzLjIxLTkuMjhsLjM1LTEuNTZjLTUuNDcgMy43Ny0xMC42NyA2LjM4LTE3LjM3IDcuNTJhNDkuOSA0OS45IDAgMCAxLTExLjg1LTguNjVsMTIuODMtMTJhOC41OCA4LjU4IDAgMCAwIDExLjAyLS41NFpNMTMyIDE2YTQuNSA0LjUgMCAxIDAgMCA5IDQuNSA0LjUgMCAwIDAgMC05Wm0xNy41IDIwLjVhNC41IDQuNSAwIDEgMSA5IDAgNC41IDQuNSAwIDAgMS05IDBaTTIxLjYzIDcxLjhhMi4zMyAyLjMzIDAgMCAxIDIuMzMgMi4zNCAyLjM0IDIuMzQgMCAwIDEtMi4zMyAyLjM3IDIuMzggMi4zOCAwIDAgMS0yLjM3LTIuMzcgMi4zOCAyLjM4IDAgMCAxIDIuMzctMi4zM1ptMS43NiA4LjJ2MTZoLTMuNTJWODBoMy41MlptLTYuNDYgMTZIMi43OFY3My4yOGgzLjc1djE5LjE0aDEwLjRWOTZabTI2LjM5LTEuMDlWODBIMzkuOHYyLjE0YTYuMjYgNi4yNiAwIDAgMC01LjEyLTIuNDZjLTQuMzIgMC03LjY4IDMuNTgtNy42OCA4LjEgMCA0LjU0IDMuMzYgOC4xMiA3LjY4IDguMTIgMi4yIDAgNC4xNi0xLjA4IDUuMTItMi41djEuNDhjMCAzLjIzLTIuMTggNS00LjgzIDVhNy4wMyA3LjAzIDAgMCAxLTUuMzItMi4zNGwtMi4xNCAyLjUyYzEuNTcgMS43NiA0LjM1IDIuOTUgNy40OSAyLjk1IDQuNzMgMCA4LjMyLTIuNTMgOC4zMi04LjFabS0xMi43Ny03LjEzYTQuNyA0LjcgMCAwIDEgNC43Ny00LjkgNC43IDQuNyAwIDAgMSA0Ljc3IDQuOSA0LjcgNC43IDAgMCAxLTQuNzcgNC45IDQuNyA0LjcgMCAwIDEtNC43Ny00LjlaTTUxLjU4IDk2aC0zLjUyVjcyaDMuNTJ2MTAuMThjLjk2LTEuNiAyLjc4LTIuNSA0Ljg2LTIuNSAzLjcxIDAgNi4xMSAyLjYyIDYuMTEgNi42OVY5NmgtMy41MnYtOS4wNmMwLTIuNTItMS4yOC00LjA2LTMuMzMtNC4wNi0yLjMzIDAtNC4xMiAxLjgyLTQuMTIgNS4yNVY5NlptMjQuODYtLjJ2LTMuMTNjLS41Mi4yLTEuMjIuMzItMS45LjMyLTEuODIgMC0yLjY4LS43My0yLjY4LTIuNzJ2LTcuMTNoNC41OFY4MGgtNC41OHYtNC40NWgtMy41MlY4MGgtMy4zM3YzLjE0aDMuMzN2Ny43YzAgMy42MiAyLjQgNS4zMiA1LjQ3IDUuMzIgMS4wOSAwIDEuOTItLjEzIDIuNjMtLjM1Wm0yMC4zLjJIOTMuNGwtMy41Mi0xMC4zN0w4Ni4zOSA5NmgtMy4zMmwtNS4zOC0xNmgzLjcybDMuNDUgMTEgMy42OC0xMWgyLjY5bDMuNjUgMTEgMy40OS0xMWgzLjc0bC01LjM4IDE2Wm02Ljc2LThjMCA0Ljg2IDMuNDkgOC4zMiA4LjM1IDguMzIgMy4zNiAwIDUuODYtMS40NCA3LjMtMy43MWwtMi43LTEuOTJhNS4wMyA1LjAzIDAgMCAxLTQuNTcgMi40M2MtMi42NSAwLTQuNzctMS43My00LjkzLTQuMzVoMTIuNThjLjAzLS41MS4wMy0uOC4wMy0xLjE1IDAtNS4xNi0zLjUyLTcuOTQtNy43MS03Ljk0QTguMTIgOC4xMiAwIDAgMCAxMDMuNSA4OFptOC4yMi01LjM0YzIuMDUgMCAzLjkgMS4yNCA0LjI5IDMuNTVoLTguOWMuNDgtMi4zNyAyLjU2LTMuNTUgNC42MS0zLjU1Wm0xMy4yMi0xMC44NWEyLjMzIDIuMzMgMCAwIDEgMi4zNCAyLjMzIDIuMzQgMi4zNCAwIDAgMS0yLjM0IDIuMzcgMi4zOCAyLjM4IDAgMCAxLTIuMzctMi4zNyAyLjM4IDIuMzggMCAwIDEgMi4zNy0yLjMzWm0yMS43IDIzLjFWODBoLTMuNTN2Mi4xNGE2LjI2IDYuMjYgMCAwIDAtNS4xMi0yLjQ2Yy00LjMyIDAtNy42OCAzLjU4LTcuNjggOC4xIDAgNC41NCAzLjM2IDguMTIgNy42OCA4LjEyIDIuMiAwIDQuMTYtMS4wOCA1LjEyLTIuNXYxLjQ4YzAgMy4yMy0yLjE4IDUtNC44MyA1YTcuMDMgNy4wMyAwIDAgMS01LjMxLTIuMzRsLTIuMTUgMi41MmMxLjU3IDEuNzYgNC4zNiAyLjk1IDcuNSAyLjk1IDQuNzMgMCA4LjMxLTIuNTMgOC4zMS04LjFaTTEyNi43IDk2aC0zLjUyVjgwaDMuNTJ2MTZabTcuMTYtOC4yMmE0LjcgNC43IDAgMCAxIDQuNzctNC45IDQuNyA0LjcgMCAwIDEgNC43NyA0LjkgNC43IDQuNyAwIDAgMS00Ljc3IDQuOSA0LjcgNC43IDAgMCAxLTQuNzctNC45Wk0xNTQuOSA5NmgtMy41MlY3MmgzLjUydjEwLjE4Yy45Ni0xLjYgMi43OC0yLjUgNC44Ni0yLjUgMy43MSAwIDYuMTEgMi42MiA2LjExIDYuNjlWOTZoLTMuNTJ2LTkuMDZjMC0yLjUyLTEuMjgtNC4wNi0zLjMyLTQuMDYtMi4zNCAwLTQuMTMgMS44Mi00LjEzIDUuMjVWOTZabTI0Ljg2LS4ydi0zLjEzYy0uNTEuMi0xLjIyLjMyLTEuODkuMzItMS44MiAwLTIuNjktLjczLTIuNjktMi43MnYtNy4xM2g0LjU4VjgwaC00LjU4di00LjQ1aC0zLjUyVjgwaC0zLjMzdjMuMTRoMy4zM3Y3LjdjMCAzLjYyIDIuNCA1LjMyIDUuNDcgNS4zMiAxLjEgMCAxLjkyLS4xMyAyLjYzLS4zNVptMjEuNTkuNThhMTEuNjcgMTEuNjcgMCAwIDEtMTEuNzUtMTEuNzRjMC02LjU2IDUuMjItMTEuNzQgMTEuNzUtMTEuNzQgNC40NSAwIDguMjIgMi4yNyAxMC4yNCA1Ljc2bC0zLjIzIDEuODVhNy45NCA3Ljk0IDAgMCAwLTcuMDEtNCA3Ljk2IDcuOTYgMCAwIDAtNy45NyA4LjEzIDcuOTYgNy45NiAwIDAgMCA3Ljk3IDguMTMgNy45NCA3Ljk0IDAgMCAwIDctNGwzLjI0IDEuODVhMTEuNjYgMTEuNjYgMCAwIDEtMTAuMjQgNS43NlptMTMuNC0uMzhoMy41MnYtNy44N2MwLTMuNDMgMS44LTUuMjUgNC4xMy01LjI1IDIuMDUgMCAzLjMzIDEuNTQgMy4zMyA0LjA2Vjk2aDMuNTJ2LTkuNjNjMC00LjA3LTIuNC02LjY5LTYuMTEtNi42OS0yLjA4IDAtMy45LjktNC44NyAyLjVWNzJoLTMuNTJ2MjRabTI1LjU2LjMyYy00LjM4IDAtNy43LTMuNzQtNy43LTguMzJzMy4zMi04LjMyIDcuNy04LjMyYzIuMyAwIDQuMjMgMS4xOCA1LjEyIDIuNDZWODBoMy41MnYxNmgtMy41MnYtMi4xNGE2LjM4IDYuMzggMCAwIDEtNS4xMiAyLjQ2Wm0uNjQtMy4yYzIuODUgMCA0Ljc3LTIuMjQgNC43Ny01LjEycy0xLjkyLTUuMTItNC43Ny01LjEyYy0yLjg0IDAtNC43NiAyLjI0LTQuNzYgNS4xMnMxLjkxIDUuMTIgNC43NiA1LjEyWk0yNTMuNzEgOTZoMy41MnYtNy44YzAtMy4yIDEuODMtNC45IDMuODQtNC45LjY0IDAgMS4xNS4xIDEuNzYuMjh2LTMuNjFjLS40OC0uMS0uOTMtLjEzLTEuMzctLjEzYTQuNSA0LjUgMCAwIDAtNC4yMyAzVjgwaC0zLjUydjE2Wm0yMS43My0zLjMzdjMuMTRjLS43LjIyLTEuNTQuMzUtMi42My4zNS0zLjA3IDAtNS40Ny0xLjctNS40Ny01LjMxdi03LjcxaC0zLjMzVjgwaDMuMzN2LTQuNDVoMy41MlY4MGg0LjU4djMuMTRoLTQuNTh2Ny4xM2MwIDEuOTkuODYgMi43MiAyLjY5IDIuNzIuNjcgMCAxLjM3LS4xMyAxLjg5LS4zMlptMTQuMjEtMS4zMWMwLTIuNjItMS42Ni00LjAzLTQuNDgtNC44NmwtMS42My0uNDhjLTEuNTctLjQ1LTEuOTItMS4xMi0xLjkyLTEuOSAwLS45NSAxLjA5LTEuNSAyLjE1LTEuNSAxLjMgMCAyLjMzLjY0IDMuMDQgMS42NGwyLjQzLTEuODZjLTEuMTItMS43Ni0zLjAxLTIuNzItNS40MS0yLjcyLTMuMiAwLTUuNyAxLjczLTUuNzMgNC41OC0uMDMgMi4zNiAxLjQxIDQuMTIgNC4yIDQuOWwxLjQuMzhjMS45Mi41NyAyLjQ3IDEuMTIgMi40NyAyLjA0IDAgMS4xMi0xLjA2IDEuNy0yLjMgMS43LTEuNjQgMC0zLjItLjgtMy44NS0yLjJsLTIuNTkgMS44NWMxLjE1IDIuMjcgMy41OCAzLjM5IDYuNDMgMy4zOSAzLjMgMCA1LjgtMS44OSA1LjgtNC45NlptLTE0My4zOCAyMS40YzAgLjQ2LS4zNy44NC0uODMuODRhLjg2Ljg2IDAgMCAxLS44Ny0uODVjMC0uNDYuMzktLjg1Ljg3LS44NS40NiAwIC44My4zOS44My44NVptLS4yOSAxMS4yNGgtMS4xMnYtOGgxLjEydjhabS01Mi4wMi4xNmE0LjA0IDQuMDQgMCAwIDAgMy45OC00LjE2IDQuMDQgNC4wNCAwIDAgMC0zLjk4LTQuMTZjLTEuMjQgMC0yLjM5LjY0LTIuOTYgMS41VjExMmgtMS4xMnYxMkg5MXYtMS4zNGMuNTcuODYgMS43MiAxLjUgMi45NiAxLjVabS0uMTItMS4wNGMtMS43NCAwLTIuOTQtMS40LTIuOTQtMy4xMiAwLTEuNzMgMS4yLTMuMTIgMi45NC0zLjEyIDEuNzUgMCAyLjk1IDEuNCAyLjk1IDMuMTIgMCAxLjczLTEuMiAzLjEyLTIuOTUgMy4xMlptNy45IDQuMjIgNS4zLTExLjM0aC0xLjI2bC0yLjkzIDYuMzUtMi45My02LjM1aC0xLjI0bDMuNTUgNy42LTEuNzYgMy43NGgxLjI2Wk0xMTUuMyAxMjRoLTEuMnYtMTAuMmgtMy42OHYtMS4xNmg4LjU2djEuMTVoLTMuNjhWMTI0Wm0zLjgyIDBoMS4xMnYtNC4wMmMwLTIuMDQgMS4yMy0yLjk0IDIuMjItMi45NC4yNCAwIC40NS4wMy42Ny4xMXYtMS4xN2EyLjQ0IDIuNDQgMCAwIDAtMi45IDEuNjZWMTE2aC0xLjExdjhabTExLjcyLTEuMzRhMy42NCAzLjY0IDAgMCAxLTIuOTYgMS41IDQuMDQgNC4wNCAwIDAgMS0zLjk4LTQuMTYgNC4wNCA0LjA0IDAgMCAxIDMuOTgtNC4xNmMxLjIzIDAgMi4zOS42NCAyLjk2IDEuNVYxMTZoMS4xMnY4aC0xLjEydi0xLjM0Wm0tNS44LTIuNjZjMCAxLjczIDEuMiAzLjEyIDIuOTUgMy4xMiAxLjc1IDAgMi45NS0xLjQgMi45NS0zLjEyIDAtMS43My0xLjItMy4xMi0yLjk1LTMuMTItMS43NCAwLTIuOTQgMS40LTIuOTQgMy4xMlptMTIuOTggNC4xNmMxLjIzIDAgMi4zOS0uNjQgMi45Ni0xLjVWMTI0aDEuMTJ2LTEySDE0MXY1LjM0YTMuNjQgMy42NCAwIDAgMC0yLjk2LTEuNSA0LjA0IDQuMDQgMCAwIDAtMy45OCA0LjE2IDQuMDQgNC4wNCAwIDAgMCAzLjk4IDQuMTZabS4xMS0xLjA0Yy0xLjc0IDAtMi45NC0xLjQtMi45NC0zLjEyIDAtMS43MyAxLjItMy4xMiAyLjk0LTMuMTIgMS43NSAwIDIuOTUgMS40IDIuOTUgMy4xMiAwIDEuNzMtMS4yIDMuMTItMi45NSAzLjEyWm0xMC42Ljg4aDEuMTF2LTMuOThjMC0xLjk5IDEuMS0zLjE0IDIuNS0zLjE0IDEuMTkgMCAyLjAyLjg2IDIuMDIgMi4yN1YxMjRoMS4xMnYtNWMwLTEuOTYtMS4yNy0zLjE2LTMuMDEtMy4xNi0xLjA0IDAtMi4wNS40NS0yLjYzIDEuNVYxMTZoLTEuMTF2OFptMTYuNzEtLjQyYzAgMi42MS0xLjcyIDMuOTItMy45NSAzLjkyLTEuODQgMC0zLjE3LS44My0zLjc3LTEuNzRsLjg4LS43NWEzLjQgMy40IDAgMCAwIDIuOSAxLjQ1YzEuMzcgMCAyLjgyLS44MyAyLjgyLTIuOTR2LTEuMDJjLS41Ny44Ni0xLjcgMS41LTIuOTIgMS41YTMuOTQgMy45NCAwIDAgMS0zLjk2LTQuMDggMy45NCAzLjk0IDAgMCAxIDMuOTYtNC4wOGMxLjIzIDAgMi4zNS42NCAyLjkyIDEuNVYxMTZoMS4xMnY3LjU4Wm0tNi44NC0zLjY2YzAgMS43MyAxLjE2IDMuMDQgMi45IDMuMDQgMS43NSAwIDIuOTItMS4zMSAyLjkyLTMuMDRzLTEuMTctMy4wNC0yLjkxLTMuMDRjLTEuNzUgMC0yLjkxIDEuMzEtMi45MSAzLjA0Wm0xMy41NSA0LjA4IDQuODgtMTEuMzZoLTEuMzVsLTQuMDMgOS4zOC00LjAzLTkuMzhoLTEuMzZsNC45IDExLjM2aC45OVptNy44NC0xMS4yNWMwIC40Ny0uMzcuODUtLjgzLjg1YS44Ni44NiAwIDAgMS0uODYtLjg1YzAtLjQ2LjM4LS44NS44Ni0uODUuNDcgMCAuODMuMzkuODMuODVabS0uMjggMTEuMjVoLTEuMTN2LThoMS4xM3Y4Wm02LjIuMTZhMy45IDMuOSAwIDAgMCAzLjU2LTEuOTVsLS45MS0uNmEyLjc4IDIuNzggMCAwIDEtMi42NCAxLjUxIDIuODcgMi44NyAwIDAgMS0yLjk2LTIuOTNoNi43NXYtLjNjLS4wMi0yLjU2LTEuNjgtNC4wNS0zLjc2LTQuMDVhNC4wNSA0LjA1IDAgMCAwLTQuMTUgNC4xNmMwIDIuMyAxLjYgNC4xNiA0LjEyIDQuMTZabS0uMDEtNy4yOGMxLjM0IDAgMi40NS44OCAyLjY0IDIuMzJoLTUuNDlhMi44NCAyLjg0IDAgMCAxIDIuODUtMi4zMlptMTMuNTUgNy4xMmgtLjkzbC0yLjEtNi4xLTIuMTQgNi4xaC0uOTJsLTIuNzQtOGgxLjE1bDIuMDggNi4wOCAyLjExLTYuMDhoLjg3bDIuMTEgNi4wOCAyLjA4LTYuMDhoMS4xN2wtMi43NCA4WiIgZmlsbD0iY3VycmVudENvbG9yIj48L3BhdGg+PC9zdmc+';  
    createImageWatermark(chart.panes()[0], imageDataUrl, {  
        alpha: 0.5,  
        padding: 20,  
    });  
      
    const lineSeries = chart.addSeries(AreaSeries, {  
        topColor: '#2962FF',  
        bottomColor: 'rgba(41, 98, 255, 0.28)',  
        lineColor: '#2962FF',  
        lineWidth: 2,  
    });  
      
    const data = [  
        { value: 0, time: 1642425322 },  
        { value: 8, time: 1642511722 },  
        { value: 10, time: 1642598122 },  
        { value: 20, time: 1642684522 },  
        { value: 3, time: 1642770922 },  
        { value: 43, time: 1642857322 },  
        { value: 41, time: 1642943722 },  
        { value: 43, time: 1643030122 },  
        { value: 56, time: 1643116522 },  
        { value: 46, time: 1643202922 },  
    ];  
      
    lineSeries.setData(data);  
      
    chart.timeScale().fitContent();  
    
