# Tutorial: Price Line

*Source: tutorials\how_to\price-line.html*

On this page

A price line is a horizontal line drawn across the width of the chart at a specific price value. This example shows how to add price lines to your chart.

## Short answer[​](price-line.html#short-answer "Direct link to Short answer")

A price line can be added to a chart by using the [`createPriceLine`](../../docs/api/interfaces/ISeriesApi.html#createpriceline) method on an existing series ([ISeriesApi](../../docs/api/interfaces/ISeriesApi.md)) instance.
    
    
    const myPriceLine = {  
        price: 1234,  
        color: '#3179F5',  
        lineWidth: 2,  
        lineStyle: 2, // LineStyle.Dashed  
        axisLabelVisible: true,  
        title: 'my label',  
    };  
      
    series.createPriceLine(myPriceLine);  
    

You can see a full [working example](price-line.html#full-example) below.

## Tips[​](price-line.html#tips "Direct link to Tips")

You may wish to disable the default price line drawn by Lightweight Charts™ for the last value in the series (and it's label). You can do this by adjusting the series options as follows:
    
    
    series.applyOptions({  
        lastValueVisible: false,  
        priceLineVisible: false,  
    });  
    

## Resources[​](price-line.html#resources "Direct link to Resources")

You can view the related APIs here:

  * [createPriceLine](../../docs/api/interfaces/ISeriesApi.html#createpriceline) \- Method to create a new Price Line.
  * [PriceLineOptions](../../docs/api/interfaces/PriceLineOptions.md) \- Price Line options.
  * [LineStyle](../../docs/api/enumerations/LineStyle.md) \- Available line styles.

## Full example[​](price-line.html#full-example "Direct link to Full example")

How to use the code sample

**The code presented below requires:**

  * That `createChart` has already been imported. See [Getting Started](../../docs.html#creating-a-chart) for more information,
  * and that there is an html div element on the page with an `id` of `container`.

Here is an example skeleton setup: [Code Sandbox](https://codesandbox.io/s/lightweight-charts-skeleton-n67pm6). You can paste the provided code below the `// REPLACE EVERYTHING BELOW HERE` comment.

tip

Some code may be hidden to improve readability. Toggle the checkbox above the code block to reveal all the code.

Show all code
    
    
    // Lightweight Charts™ Example: Price Lines  
    // https://tradingview.github.io/lightweight-charts/tutorials/how_to/price-line  
      
    const chartOptions = {  
        layout: {  
            textColor: 'black',  
            background: { type: 'solid', color: 'white' },  
        },  
    };  
    /** @type {import('lightweight-charts').IChartApi} */  
    const chart = createChart(document.getElementById('container'), chartOptions);  
      
    const series = chart.addSeries(LineSeries, {  
        color: '#2962FF',  
        lineWidth: 2,  
        // disabling built-in price lines  
        lastValueVisible: false,  
        priceLineVisible: false,  
    });  
      
    const data = [  
        { time: { year: 2018, month: 1, day: 1 }, value: 27.58405298746434 },  
        { time: { year: 2018, month: 1, day: 2 }, value: 31.74088841431117 },  
        { time: { year: 2018, month: 1, day: 3 }, value: 35.892978753808926 },  
        { time: { year: 2018, month: 1, day: 4 }, value: 39.63642029045179 },  
        { time: { year: 2018, month: 1, day: 5 }, value: 40.79167357702531 },  
        { time: { year: 2018, month: 1, day: 6 }, value: 47.691740220947764 },  
        { time: { year: 2018, month: 1, day: 7 }, value: 49.377161099825415 },  
        { time: { year: 2018, month: 1, day: 8 }, value: 52.47379203136591 },  
        { time: { year: 2018, month: 1, day: 9 }, value: 50.40209743179448 },  
        { time: { year: 2018, month: 1, day: 10 }, value: 61.47316837848548 },  
        { time: { year: 2018, month: 1, day: 11 }, value: 58.22831552141069 },  
        { time: { year: 2018, month: 1, day: 12 }, value: 59.36868132891698 },  
        { time: { year: 2018, month: 1, day: 13 }, value: 62.10845687168416 },  
        { time: { year: 2018, month: 1, day: 14 }, value: 51.259701958506724 },  
        { time: { year: 2018, month: 1, day: 15 }, value: 56.247578870411644 },  
        { time: { year: 2018, month: 1, day: 16 }, value: 55.483307642385164 },  
        { time: { year: 2018, month: 1, day: 17 }, value: 55.85295564734231 },  
        { time: { year: 2018, month: 1, day: 18 }, value: 48.3138216778343 },  
        { time: { year: 2018, month: 1, day: 19 }, value: 53.071901176203866 },  
        { time: { year: 2018, month: 1, day: 20 }, value: 50.873781097281885 },  
        { time: { year: 2018, month: 1, day: 21 }, value: 49.7840315054249 },  
        { time: { year: 2018, month: 1, day: 22 }, value: 52.34956807336156 },  
        { time: { year: 2018, month: 1, day: 23 }, value: 53.79112543285674 },  
        { time: { year: 2018, month: 1, day: 24 }, value: 53.984887985424805 },  
        { time: { year: 2018, month: 1, day: 25 }, value: 58.56902893497121 },  
        { time: { year: 2018, month: 1, day: 26 }, value: 54.76191372282466 },  
        { time: { year: 2018, month: 1, day: 27 }, value: 63.38042554684846 },  
        { time: { year: 2018, month: 1, day: 28 }, value: 55.452618512103065 },  
        { time: { year: 2018, month: 1, day: 29 }, value: 65.60820758942769 },  
        { time: { year: 2018, month: 1, day: 30 }, value: 56.82795136583009 },  
        { time: { year: 2018, month: 1, day: 31 }, value: 70.3148022984224 },  
        { time: { year: 2018, month: 2, day: 1 }, value: 65.86230944167264 },  
        { time: { year: 2018, month: 2, day: 2 }, value: 72.05467846676524 },  
        { time: { year: 2018, month: 2, day: 3 }, value: 72.99238887850564 },  
        { time: { year: 2018, month: 2, day: 4 }, value: 67.03373730222785 },  
        { time: { year: 2018, month: 2, day: 5 }, value: 69.97670934736414 },  
        { time: { year: 2018, month: 2, day: 6 }, value: 73.08910595492105 },  
        { time: { year: 2018, month: 2, day: 7 }, value: 81.43976528732057 },  
        { time: { year: 2018, month: 2, day: 8 }, value: 73.62230936920984 },  
        { time: { year: 2018, month: 2, day: 9 }, value: 82.15522801870938 },  
        { time: { year: 2018, month: 2, day: 10 }, value: 77.99384538574678 },  
        { time: { year: 2018, month: 2, day: 11 }, value: 85.62489628897463 },  
        { time: { year: 2018, month: 2, day: 12 }, value: 86.93090666568217 },  
        { time: { year: 2018, month: 2, day: 13 }, value: 75.99689788850394 },  
        { time: { year: 2018, month: 2, day: 14 }, value: 88.46418548355727 },  
        { time: { year: 2018, month: 2, day: 15 }, value: 86.20760396539865 },  
        { time: { year: 2018, month: 2, day: 16 }, value: 81.88757639758437 },  
        { time: { year: 2018, month: 2, day: 17 }, value: 79.58151786389108 },  
        { time: { year: 2018, month: 2, day: 18 }, value: 80.96845249711073 },  
        { time: { year: 2018, month: 2, day: 19 }, value: 73.54901807055447 },  
        { time: { year: 2018, month: 2, day: 20 }, value: 75.65626118347262 },  
        { time: { year: 2018, month: 2, day: 21 }, value: 78.41307347680399 },  
        { time: { year: 2018, month: 2, day: 22 }, value: 74.60352602043042 },  
        { time: { year: 2018, month: 2, day: 23 }, value: 72.28241570381236 },  
        { time: { year: 2018, month: 2, day: 24 }, value: 72.24427397962566 },  
        { time: { year: 2018, month: 2, day: 25 }, value: 64.80996965592134 },  
        { time: { year: 2018, month: 2, day: 26 }, value: 67.37511361319652 },  
        { time: { year: 2018, month: 2, day: 27 }, value: 65.5449131917524 },  
        { time: { year: 2018, month: 2, day: 28 }, value: 65.4802711362433 },  
        { time: { year: 2018, month: 3, day: 1 }, value: 62.207767815581086 },  
        { time: { year: 2018, month: 3, day: 2 }, value: 59.78884720470812 },  
        { time: { year: 2018, month: 3, day: 3 }, value: 67.51846586137782 },  
        { time: { year: 2018, month: 3, day: 4 }, value: 68.752834400291 },  
        { time: { year: 2018, month: 3, day: 5 }, value: 66.63416073573323 },  
        { time: { year: 2018, month: 3, day: 6 }, value: 65.58601621691751 },  
        { time: { year: 2018, month: 3, day: 7 }, value: 57.33498792621458 },  
        { time: { year: 2018, month: 3, day: 8 }, value: 56.93436946311955 },  
        { time: { year: 2018, month: 3, day: 9 }, value: 58.31144672902557 },  
        { time: { year: 2018, month: 3, day: 10 }, value: 59.96407207657268 },  
        { time: { year: 2018, month: 3, day: 11 }, value: 55.7861486424976 },  
        { time: { year: 2018, month: 3, day: 12 }, value: 52.91803500214551 },  
        { time: { year: 2018, month: 3, day: 13 }, value: 54.491591573038306 },  
        { time: { year: 2018, month: 3, day: 14 }, value: 51.924409342593385 },  
        { time: { year: 2018, month: 3, day: 15 }, value: 41.90263950118436 },  
        { time: { year: 2018, month: 3, day: 16 }, value: 40.514436076485694 },  
        { time: { year: 2018, month: 3, day: 17 }, value: 41.065887666854486 },  
        { time: { year: 2018, month: 3, day: 18 }, value: 40.44445534031683 },  
        { time: { year: 2018, month: 3, day: 19 }, value: 42.13922977216152 },  
        { time: { year: 2018, month: 3, day: 20 }, value: 42.317162952084495 },  
        { time: { year: 2018, month: 3, day: 21 }, value: 39.02881877743751 },  
        { time: { year: 2018, month: 3, day: 22 }, value: 39.81917993955704 },  
        { time: { year: 2018, month: 3, day: 23 }, value: 36.753197056053374 },  
        { time: { year: 2018, month: 3, day: 24 }, value: 37.02203306330588 },  
        { time: { year: 2018, month: 3, day: 25 }, value: 36.36014042161194 },  
        { time: { year: 2018, month: 3, day: 26 }, value: 33.56275879100148 },  
        { time: { year: 2018, month: 3, day: 27 }, value: 34.39112540787079 },  
        { time: { year: 2018, month: 3, day: 28 }, value: 30.57170225544929 },  
        { time: { year: 2018, month: 3, day: 29 }, value: 33.56826040802756 },  
        { time: { year: 2018, month: 3, day: 30 }, value: 32.89895543218274 },  
        { time: { year: 2018, month: 3, day: 31 }, value: 31.015658561825738 },  
        { time: { year: 2018, month: 4, day: 1 }, value: 33.189179815787455 },  
        { time: { year: 2018, month: 4, day: 2 }, value: 29.530756945582162 },  
        { time: { year: 2018, month: 4, day: 3 }, value: 29.250978140719916 },  
        { time: { year: 2018, month: 4, day: 4 }, value: 27.89635178919736 },  
        { time: { year: 2018, month: 4, day: 5 }, value: 26.995427160624686 },  
        { time: { year: 2018, month: 4, day: 6 }, value: 25.89631885043023 },  
        { time: { year: 2018, month: 4, day: 7 }, value: 28.71812492475548 },  
        { time: { year: 2018, month: 4, day: 8 }, value: 23.56476085365468 },  
        { time: { year: 2018, month: 4, day: 9 }, value: 23.8550787876547 },  
        { time: { year: 2018, month: 4, day: 10 }, value: 23.27046572075657 },  
        { time: { year: 2018, month: 4, day: 11 }, value: 25.73099630369951 },  
        { time: { year: 2018, month: 4, day: 12 }, value: 23.398760738394646 },  
        { time: { year: 2018, month: 4, day: 13 }, value: 22.97970501784193 },  
        { time: { year: 2018, month: 4, day: 14 }, value: 22.145587244500526 },  
        { time: { year: 2018, month: 4, day: 15 }, value: 20.622578956226192 },  
        { time: { year: 2018, month: 4, day: 16 }, value: 21.99297423796017 },  
        { time: { year: 2018, month: 4, day: 17 }, value: 20.756081302371527 },  
        { time: { year: 2018, month: 4, day: 18 }, value: 18.1983338834302 },  
        { time: { year: 2018, month: 4, day: 19 }, value: 16.419404563645198 },  
        { time: { year: 2018, month: 4, day: 20 }, value: 18.38192363882247 },  
        { time: { year: 2018, month: 4, day: 21 }, value: 17.41452255210322 },  
        { time: { year: 2018, month: 4, day: 22 }, value: 17.39866711593896 },  
        { time: { year: 2018, month: 4, day: 23 }, value: 14.859371316920733 },  
        { time: { year: 2018, month: 4, day: 24 }, value: 14.49488592297959 },  
        { time: { year: 2018, month: 4, day: 25 }, value: 14.183858665721397 },  
        { time: { year: 2018, month: 4, day: 26 }, value: 12.754187935636056 },  
        { time: { year: 2018, month: 4, day: 27 }, value: 14.467536059608742 },  
        { time: { year: 2018, month: 4, day: 28 }, value: 14.72962730689032 },  
        { time: { year: 2018, month: 4, day: 29 }, value: 16.591675981296518 },  
        { time: { year: 2018, month: 4, day: 30 }, value: 17.560385679284135 },  
        { time: { year: 2018, month: 5, day: 1 }, value: 22.386250317504064 },  
        { time: { year: 2018, month: 5, day: 2 }, value: 23.697029442697385 },  
        { time: { year: 2018, month: 5, day: 3 }, value: 23.453148128592442 },  
        { time: { year: 2018, month: 5, day: 4 }, value: 23.164700105036882 },  
        { time: { year: 2018, month: 5, day: 5 }, value: 23.919034678006323 },  
        { time: { year: 2018, month: 5, day: 6 }, value: 25.18353870528509 },  
        { time: { year: 2018, month: 5, day: 7 }, value: 26.982824465076394 },  
        { time: { year: 2018, month: 5, day: 8 }, value: 29.122512185000712 },  
        { time: { year: 2018, month: 5, day: 9 }, value: 29.60160406576696 },  
        { time: { year: 2018, month: 5, day: 10 }, value: 30.845749384528016 },  
        { time: { year: 2018, month: 5, day: 11 }, value: 33.03296938636202 },  
        { time: { year: 2018, month: 5, day: 12 }, value: 33.784707082446104 },  
        { time: { year: 2018, month: 5, day: 13 }, value: 36.08545410406137 },  
        { time: { year: 2018, month: 5, day: 14 }, value: 36.80597815439238 },  
        { time: { year: 2018, month: 5, day: 15 }, value: 34.56062188644443 },  
        { time: { year: 2018, month: 5, day: 16 }, value: 36.52666657165473 },  
        { time: { year: 2018, month: 5, day: 17 }, value: 34.76705735297833 },  
        { time: { year: 2018, month: 5, day: 18 }, value: 39.01598033743525 },  
        { time: { year: 2018, month: 5, day: 19 }, value: 37.60979560604685 },  
        { time: { year: 2018, month: 5, day: 20 }, value: 42.403895121650436 },  
        { time: { year: 2018, month: 5, day: 21 }, value: 45.55998014298455 },  
        { time: { year: 2018, month: 5, day: 22 }, value: 39.76704752577289 },  
        { time: { year: 2018, month: 5, day: 23 }, value: 41.83196178430985 },  
        { time: { year: 2018, month: 5, day: 24 }, value: 46.99399105885453 },  
        { time: { year: 2018, month: 5, day: 25 }, value: 48.553566318637984 },  
        { time: { year: 2018, month: 5, day: 26 }, value: 48.918166891087594 },  
        { time: { year: 2018, month: 5, day: 27 }, value: 42.95391588314584 },  
        { time: { year: 2018, month: 5, day: 28 }, value: 51.267649950057546 },  
        { time: { year: 2018, month: 5, day: 29 }, value: 44.86104374986037 },  
        { time: { year: 2018, month: 5, day: 30 }, value: 46.7183564731453 },  
        { time: { year: 2018, month: 5, day: 31 }, value: 52.753001379260766 },  
        { time: { year: 2018, month: 6, day: 1 }, value: 56.04835638442964 },  
        { time: { year: 2018, month: 6, day: 2 }, value: 54.82119793390652 },  
        { time: { year: 2018, month: 6, day: 3 }, value: 57.718938021257685 },  
        { time: { year: 2018, month: 6, day: 4 }, value: 53.9914459224653 },  
        { time: { year: 2018, month: 6, day: 5 }, value: 59.33050624063286 },  
        { time: { year: 2018, month: 6, day: 6 }, value: 50.79074268713266 },  
        { time: { year: 2018, month: 6, day: 7 }, value: 53.15657316197036 },  
        { time: { year: 2018, month: 6, day: 8 }, value: 59.43675134021954 },  
        { time: { year: 2018, month: 6, day: 9 }, value: 63.28437595760727 },  
        { time: { year: 2018, month: 6, day: 10 }, value: 58.07099287435428 },  
        { time: { year: 2018, month: 6, day: 11 }, value: 56.68728978119396 },  
        { time: { year: 2018, month: 6, day: 12 }, value: 57.05079700873323 },  
        { time: { year: 2018, month: 6, day: 13 }, value: 65.65087785161663 },  
        { time: { year: 2018, month: 6, day: 14 }, value: 59.20877581396441 },  
        { time: { year: 2018, month: 6, day: 15 }, value: 64.30200099280857 },  
        { time: { year: 2018, month: 6, day: 16 }, value: 68.60774992100288 },  
        { time: { year: 2018, month: 6, day: 17 }, value: 67.16628680993453 },  
        { time: { year: 2018, month: 6, day: 18 }, value: 62.89644591741811 },  
        { time: { year: 2018, month: 6, day: 19 }, value: 61.42888198118138 },  
        { time: { year: 2018, month: 6, day: 20 }, value: 64.89813095653885 },  
        { time: { year: 2018, month: 6, day: 21 }, value: 72.72701573552945 },  
        { time: { year: 2018, month: 6, day: 22 }, value: 67.85006296129148 },  
        { time: { year: 2018, month: 6, day: 23 }, value: 74.8567814889 },  
        { time: { year: 2018, month: 6, day: 24 }, value: 66.24228046316296 },  
        { time: { year: 2018, month: 6, day: 25 }, value: 68.09192660329269 },  
        { time: { year: 2018, month: 6, day: 26 }, value: 75.30075953672075 },  
        { time: { year: 2018, month: 6, day: 27 }, value: 68.7478054620306 },  
        { time: { year: 2018, month: 6, day: 28 }, value: 76.2285023801364 },  
        { time: { year: 2018, month: 6, day: 29 }, value: 82.945167109736 },  
        { time: { year: 2018, month: 6, day: 30 }, value: 76.91811779365663 },  
        { time: { year: 2018, month: 7, day: 1 }, value: 73.4904875247808 },  
        { time: { year: 2018, month: 7, day: 2 }, value: 78.37882382739707 },  
        { time: { year: 2018, month: 7, day: 3 }, value: 77.00224598364632 },  
        { time: { year: 2018, month: 7, day: 4 }, value: 74.96345662377028 },  
        { time: { year: 2018, month: 7, day: 5 }, value: 85.54303380001907 },  
        { time: { year: 2018, month: 7, day: 6 }, value: 74.23916926437794 },  
        { time: { year: 2018, month: 7, day: 7 }, value: 86.38109732705232 },  
        { time: { year: 2018, month: 7, day: 8 }, value: 88.36203657839357 },  
        { time: { year: 2018, month: 7, day: 9 }, value: 81.63303116061893 },  
        { time: { year: 2018, month: 7, day: 10 }, value: 78.05188105610182 },  
        { time: { year: 2018, month: 7, day: 11 }, value: 93.73294498110195 },  
        { time: { year: 2018, month: 7, day: 12 }, value: 86.3226018109303 },  
        { time: { year: 2018, month: 7, day: 13 }, value: 83.18571530136985 },  
        { time: { year: 2018, month: 7, day: 14 }, value: 92.45097319531271 },  
        { time: { year: 2018, month: 7, day: 15 }, value: 82.61971871486392 },  
        { time: { year: 2018, month: 7, day: 16 }, value: 84.39935112744469 },  
        { time: { year: 2018, month: 7, day: 17 }, value: 86.84420907417798 },  
        { time: { year: 2018, month: 7, day: 18 }, value: 81.50766784637338 },  
        { time: { year: 2018, month: 7, day: 19 }, value: 88.74841709228694 },  
        { time: { year: 2018, month: 7, day: 20 }, value: 85.84190975050336 },  
        { time: { year: 2018, month: 7, day: 21 }, value: 86.9594938103096 },  
        { time: { year: 2018, month: 7, day: 22 }, value: 83.72572564120199 },  
        { time: { year: 2018, month: 7, day: 23 }, value: 83.42754326770913 },  
        { time: { year: 2018, month: 7, day: 24 }, value: 80.40755818165856 },  
        { time: { year: 2018, month: 7, day: 25 }, value: 81.40515523172276 },  
        { time: { year: 2018, month: 7, day: 26 }, value: 88.6671912474792 },  
        { time: { year: 2018, month: 7, day: 27 }, value: 83.98197434091429 },  
        { time: { year: 2018, month: 7, day: 28 }, value: 79.93747419607003 },  
        { time: { year: 2018, month: 7, day: 29 }, value: 88.74666581089701 },  
        { time: { year: 2018, month: 7, day: 30 }, value: 88.4887222568271 },  
        { time: { year: 2018, month: 7, day: 31 }, value: 91.70282162754224 },  
        { time: { year: 2018, month: 8, day: 1 }, value: 81.82327312829118 },  
        { time: { year: 2018, month: 8, day: 2 }, value: 89.56625546634567 },  
        { time: { year: 2018, month: 8, day: 3 }, value: 83.60742160062637 },  
        { time: { year: 2018, month: 8, day: 4 }, value: 92.16271144958857 },  
        { time: { year: 2018, month: 8, day: 5 }, value: 92.93451790057534 },  
        { time: { year: 2018, month: 8, day: 6 }, value: 97.10629615852636 },  
        { time: { year: 2018, month: 8, day: 7 }, value: 93.18989484413193 },  
        { time: { year: 2018, month: 8, day: 8 }, value: 99.52744238602173 },  
        { time: { year: 2018, month: 8, day: 9 }, value: 90.84973685659028 },  
        { time: { year: 2018, month: 8, day: 10 }, value: 98.37517814040118 },  
        { time: { year: 2018, month: 8, day: 11 }, value: 90.13525425607658 },  
        { time: { year: 2018, month: 8, day: 12 }, value: 95.55125798221395 },  
        { time: { year: 2018, month: 8, day: 13 }, value: 82.77346455876308 },  
        { time: { year: 2018, month: 8, day: 14 }, value: 83.24854499361042 },  
        { time: { year: 2018, month: 8, day: 15 }, value: 95.41999231944423 },  
        { time: { year: 2018, month: 8, day: 16 }, value: 93.80228527345439 },  
        { time: { year: 2018, month: 8, day: 17 }, value: 95.6453232668047 },  
        { time: { year: 2018, month: 8, day: 18 }, value: 85.15427147925779 },  
        { time: { year: 2018, month: 8, day: 19 }, value: 84.96447951638784 },  
        { time: { year: 2018, month: 8, day: 20 }, value: 95.92739640648459 },  
        { time: { year: 2018, month: 8, day: 21 }, value: 96.44143870862634 },  
        { time: { year: 2018, month: 8, day: 22 }, value: 101.23323393804354 },  
        { time: { year: 2018, month: 8, day: 23 }, value: 92.12092707164649 },  
        { time: { year: 2018, month: 8, day: 24 }, value: 101.74117610271144 },  
        { time: { year: 2018, month: 8, day: 25 }, value: 96.38311956379351 },  
        { time: { year: 2018, month: 8, day: 26 }, value: 98.18485692799554 },  
        { time: { year: 2018, month: 8, day: 27 }, value: 102.60080903938159 },  
        { time: { year: 2018, month: 8, day: 28 }, value: 97.48394132428021 },  
        { time: { year: 2018, month: 8, day: 29 }, value: 101.41501247525068 },  
        { time: { year: 2018, month: 8, day: 30 }, value: 94.9501205245301 },  
        { time: { year: 2018, month: 8, day: 31 }, value: 89.11429564465982 },  
        { time: { year: 2018, month: 9, day: 1 }, value: 104.1842141132897 },  
        { time: { year: 2018, month: 9, day: 2 }, value: 97.36185743859737 },  
        { time: { year: 2018, month: 9, day: 3 }, value: 97.34376526297034 },  
        { time: { year: 2018, month: 9, day: 4 }, value: 103.73609636859413 },  
        { time: { year: 2018, month: 9, day: 5 }, value: 86.89420264148593 },  
        { time: { year: 2018, month: 9, day: 6 }, value: 90.99445484839778 },  
        { time: { year: 2018, month: 9, day: 7 }, value: 92.0197876339847 },  
        { time: { year: 2018, month: 9, day: 8 }, value: 87.35412911434453 },  
        { time: { year: 2018, month: 9, day: 9 }, value: 97.40224787139312 },  
        { time: { year: 2018, month: 9, day: 10 }, value: 98.14732375673768 },  
        { time: { year: 2018, month: 9, day: 11 }, value: 101.5147062059064 },  
        { time: { year: 2018, month: 9, day: 12 }, value: 93.11950437404803 },  
        { time: { year: 2018, month: 9, day: 13 }, value: 98.41765784798642 },  
        { time: { year: 2018, month: 9, day: 14 }, value: 89.08499357950659 },  
        { time: { year: 2018, month: 9, day: 15 }, value: 96.29213559344964 },  
        { time: { year: 2018, month: 9, day: 16 }, value: 103.57528341068684 },  
        { time: { year: 2018, month: 9, day: 17 }, value: 98.94258099235431 },  
        { time: { year: 2018, month: 9, day: 18 }, value: 92.43383394007822 },  
        { time: { year: 2018, month: 9, day: 19 }, value: 105.39681697822706 },  
        { time: { year: 2018, month: 9, day: 20 }, value: 100.52663985092036 },  
        { time: { year: 2018, month: 9, day: 21 }, value: 98.84754340440189 },  
        { time: { year: 2018, month: 9, day: 22 }, value: 93.78502517034752 },  
        { time: { year: 2018, month: 9, day: 23 }, value: 95.51435402626828 },  
        { time: { year: 2018, month: 9, day: 24 }, value: 91.94633821567461 },  
        { time: { year: 2018, month: 9, day: 25 }, value: 98.18484857755837 },  
        { time: { year: 2018, month: 9, day: 26 }, value: 102.51694320185617 },  
        { time: { year: 2018, month: 9, day: 27 }, value: 97.40549024974396 },  
        { time: { year: 2018, month: 9, day: 28 }, value: 103.49718807374374 },  
        { time: { year: 2018, month: 9, day: 29 }, value: 108.24441490057781 },  
        { time: { year: 2018, month: 9, day: 30 }, value: 103.24675412744978 },  
        { time: { year: 2018, month: 10, day: 1 }, value: 97.05089568637521 },  
        { time: { year: 2018, month: 10, day: 2 }, value: 91.85875309835458 },  
        { time: { year: 2018, month: 10, day: 3 }, value: 72.24590653541385 },  
        { time: { year: 2018, month: 10, day: 4 }, value: 70.73707674373722 },  
        { time: { year: 2018, month: 10, day: 5 }, value: 61.2106378263602 },  
        { time: { year: 2018, month: 10, day: 6 }, value: 62.35889407826063 },  
        { time: { year: 2018, month: 10, day: 7 }, value: 56.311930696659 },  
        { time: { year: 2018, month: 10, day: 8 }, value: 51.462743547904374 },  
        { time: { year: 2018, month: 10, day: 9 }, value: 47.99928302521288 },  
        { time: { year: 2018, month: 10, day: 10 }, value: 42.735011616511976 },  
        { time: { year: 2018, month: 10, day: 11 }, value: 35.82291867003256 },  
        { time: { year: 2018, month: 10, day: 12 }, value: 28.706141122035454 },  
        { time: { year: 2018, month: 10, day: 13 }, value: 24.289344698634036 },  
        { time: { year: 2018, month: 10, day: 14 }, value: 22.56513000253429 },  
        { time: { year: 2018, month: 10, day: 15 }, value: 18.862530899060324 },  
        { time: { year: 2018, month: 10, day: 16 }, value: 18.164416367748263 },  
        { time: { year: 2018, month: 10, day: 17 }, value: 16.25993836760582 },  
        { time: { year: 2018, month: 10, day: 18 }, value: 15.849033589978859 },  
        { time: { year: 2018, month: 10, day: 19 }, value: 12.581184324950792 },  
        { time: { year: 2018, month: 10, day: 20 }, value: 12.46960767886934 },  
        { time: { year: 2018, month: 10, day: 21 }, value: 13.203284995561251 },  
        { time: { year: 2018, month: 10, day: 22 }, value: 12.751819244602629 },  
        { time: { year: 2018, month: 10, day: 23 }, value: 13.815126496529205 },  
        { time: { year: 2018, month: 10, day: 24 }, value: 14.44156419046133 },  
        { time: { year: 2018, month: 10, day: 25 }, value: 12.030505290672643 },  
        { time: { year: 2018, month: 10, day: 26 }, value: 13.426535837756518 },  
        { time: { year: 2018, month: 10, day: 27 }, value: 13.141003741491893 },  
        { time: { year: 2018, month: 10, day: 28 }, value: 12.216411608284261 },  
        { time: { year: 2018, month: 10, day: 29 }, value: 12.437867813477077 },  
        { time: { year: 2018, month: 10, day: 30 }, value: 12.228521667932771 },  
        { time: { year: 2018, month: 10, day: 31 }, value: 13.587126038913974 },  
        { time: { year: 2018, month: 11, day: 1 }, value: 12.016792589137491 },  
        { time: { year: 2018, month: 11, day: 2 }, value: 13.01948020515645 },  
        { time: { year: 2018, month: 11, day: 3 }, value: 12.70475528902004 },  
        { time: { year: 2018, month: 11, day: 4 }, value: 13.018454073452016 },  
        { time: { year: 2018, month: 11, day: 5 }, value: 12.505487262036313 },  
        { time: { year: 2018, month: 11, day: 6 }, value: 13.467522897553604 },  
        { time: { year: 2018, month: 11, day: 7 }, value: 13.748796553616549 },  
        { time: { year: 2018, month: 11, day: 8 }, value: 11.974873751121669 },  
        { time: { year: 2018, month: 11, day: 9 }, value: 11.8316362912944 },  
        { time: { year: 2018, month: 11, day: 10 }, value: 13.864291857325023 },  
        { time: { year: 2018, month: 11, day: 11 }, value: 12.071675684436165 },  
        { time: { year: 2018, month: 11, day: 12 }, value: 12.314581956701367 },  
        { time: { year: 2018, month: 11, day: 13 }, value: 13.223445358310986 },  
        { time: { year: 2018, month: 11, day: 14 }, value: 12.346191421746546 },  
        { time: { year: 2018, month: 11, day: 15 }, value: 12.0232072259563 },  
        { time: { year: 2018, month: 11, day: 16 }, value: 13.367039701380252 },  
        { time: { year: 2018, month: 11, day: 17 }, value: 12.232635114201212 },  
        { time: { year: 2018, month: 11, day: 18 }, value: 13.348220671014012 },  
        { time: { year: 2018, month: 11, day: 19 }, value: 13.508314659502604 },  
        { time: { year: 2018, month: 11, day: 20 }, value: 12.630893498655155 },  
        { time: { year: 2018, month: 11, day: 21 }, value: 12.632952849963768 },  
        { time: { year: 2018, month: 11, day: 22 }, value: 11.645073051089117 },  
        { time: { year: 2018, month: 11, day: 23 }, value: 13.845637677048611 },  
        { time: { year: 2018, month: 11, day: 24 }, value: 12.567519871595463 },  
        { time: { year: 2018, month: 11, day: 25 }, value: 13.927270152127294 },  
        { time: { year: 2018, month: 11, day: 26 }, value: 12.179362670863737 },  
        { time: { year: 2018, month: 11, day: 27 }, value: 12.471835488646303 },  
        { time: { year: 2018, month: 11, day: 28 }, value: 11.71761488042106 },  
        { time: { year: 2018, month: 11, day: 29 }, value: 12.181312973409113 },  
        { time: { year: 2018, month: 11, day: 30 }, value: 12.662272671374286 },  
        { time: { year: 2018, month: 12, day: 1 }, value: 13.859774226603497 },  
        { time: { year: 2018, month: 12, day: 2 }, value: 11.643237368800426 },  
        { time: { year: 2018, month: 12, day: 3 }, value: 11.646083130428282 },  
        { time: { year: 2018, month: 12, day: 4 }, value: 13.3486102643562 },  
        { time: { year: 2018, month: 12, day: 5 }, value: 13.421817450001853 },  
        { time: { year: 2018, month: 12, day: 6 }, value: 13.734844672048157 },  
        { time: { year: 2018, month: 12, day: 7 }, value: 11.808371821628475 },  
        { time: { year: 2018, month: 12, day: 8 }, value: 13.906976670383472 },  
        { time: { year: 2018, month: 12, day: 9 }, value: 13.161627469585584 },  
        { time: { year: 2018, month: 12, day: 10 }, value: 13.642368164712535 },  
        { time: { year: 2018, month: 12, day: 11 }, value: 12.755167209621261 },  
        { time: { year: 2018, month: 12, day: 12 }, value: 12.13947468588139 },  
        { time: { year: 2018, month: 12, day: 13 }, value: 13.68979129854326 },  
        { time: { year: 2018, month: 12, day: 14 }, value: 11.812050924695251 },  
        { time: { year: 2018, month: 12, day: 15 }, value: 11.71992287051065 },  
        { time: { year: 2018, month: 12, day: 16 }, value: 13.003823991463284 },  
        { time: { year: 2018, month: 12, day: 17 }, value: 13.124946877570311 },  
        { time: { year: 2018, month: 12, day: 18 }, value: 11.844736927132542 },  
        { time: { year: 2018, month: 12, day: 19 }, value: 11.770961792864846 },  
        { time: { year: 2018, month: 12, day: 20 }, value: 10.926179837275598 },  
        { time: { year: 2018, month: 12, day: 21 }, value: 11.155771630851676 },  
        { time: { year: 2018, month: 12, day: 22 }, value: 11.63008791780728 },  
        { time: { year: 2018, month: 12, day: 23 }, value: 10.216268005840389 },  
        { time: { year: 2018, month: 12, day: 24 }, value: 13.611694182717626 },  
        { time: { year: 2018, month: 12, day: 25 }, value: 17.47706580052263 },  
        { time: { year: 2018, month: 12, day: 26 }, value: 20.900697260373697 },  
        { time: { year: 2018, month: 12, day: 27 }, value: 20.44940301651778 },  
        { time: { year: 2018, month: 12, day: 28 }, value: 23.47128311932538 },  
        { time: { year: 2018, month: 12, day: 29 }, value: 28.63506505828928 },  
        { time: { year: 2018, month: 12, day: 30 }, value: 29.567577074788517 },  
    ];  
    series.setData(data);  
      
    let minimumPrice = data[0].value;  
    let maximumPrice = minimumPrice;  
    for (let i = 1; i < data.length; i++) {  
        const price = data[i].value;  
        if (price > maximumPrice) {  
            maximumPrice = price;  
        }  
        if (price < minimumPrice) {  
            minimumPrice = price;  
        }  
    }  
    const avgPrice = (maximumPrice + minimumPrice) / 2;  
      
    const lineWidth = 2;  
    const minPriceLine = {  
        price: minimumPrice,  
        color: '#ef5350',  
        lineWidth: lineWidth,  
        lineStyle: 2, // LineStyle.Dashed  
        axisLabelVisible: true,  
        title: 'min price',  
    };  
    const avgPriceLine = {  
        price: avgPrice,  
        color: 'black',  
        lineWidth: lineWidth,  
        lineStyle: 1, // LineStyle.Dotted  
        axisLabelVisible: true,  
        title: 'ave price',  
    };  
    const maxPriceLine = {  
        price: maximumPrice,  
        color: '#26a69a',  
        lineWidth: lineWidth,  
        lineStyle: 2, // LineStyle.Dashed  
        axisLabelVisible: true,  
        title: 'max price',  
    };  
      
    series.createPriceLine(minPriceLine);  
    series.createPriceLine(avgPriceLine);  
    series.createPriceLine(maxPriceLine);  
      
    chart.timeScale().fitContent();  
    
