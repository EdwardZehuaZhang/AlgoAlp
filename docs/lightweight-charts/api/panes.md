# API: Panes

*Source: docs\panes.html*

Version: 5.0

On this page

Panes are essential elements that help segregate data visually within a single chart. Panes are useful when you have a chart that needs to show more than one kind of data. For example, you might want to see a stock's price over time in one pane and its trading volume in another. This setup helps users get a fuller picture without cluttering the chart.

By default, Lightweight Charts™ has a single pane, however, you can add more panes to the chart to display different series in separate areas. For detailed examples and code snippets on how to implement panes in your charts [see tutorial](../tutorials/how_to/panes.md).

## Customization Options[​](panes.html#customization-options "Direct link to Customization Options")

Lightweight Charts™ offers a few [customization options](api/interfaces/LayoutPanesOptions.md) to tailor the appearance and behavior of panes:

  * [Pane Separator Color](api/interfaces/LayoutPanesOptions.html#separatorcolor): Customize the color of the pane separators to match the chart design or improve visibility.

  * [Separator Hover Color](api/interfaces/LayoutPanesOptions.html#separatorhovercolor): Enhance user interaction by changing the color of separators on mouse hover.

  * [Resizable Panes](api/interfaces/LayoutPanesOptions.html#enableresize): Opt to enable or disable the resizing of panes by the user, offering flexibility in how data is displayed.

## Managing Panes[​](panes.html#managing-panes "Direct link to Managing Panes")

While the specific methods to manipulate panes are covered in the detailed [example](../tutorials/how_to/panes.md), it's important to note that Lightweight Charts™ provides an [API for pane management](api/interfaces/IPaneApi.md). This includes adding new panes, moving series between panes, adjusting pane height, and removing panes. The API ensures that developers have full control over the pane lifecycle and organization within their charts.
