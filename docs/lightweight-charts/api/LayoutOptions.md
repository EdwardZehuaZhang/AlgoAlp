# API: Layoutoptions

*Source: docs\api\interfaces\LayoutOptions.html*

Version: 5.0

On this page

Represents layout options

## Properties[​](LayoutOptions.html#properties "Direct link to Properties")

### background[​](LayoutOptions.html#background "Direct link to background")

> **background** : [`Background`](../type-aliases/Background.md)

Chart and scales background color.

#### Default Value[​](LayoutOptions.html#default-value "Direct link to Default Value")

`{ type: ColorType.Solid, color: '#FFFFFF' }`

* * *

### textColor[​](LayoutOptions.html#textcolor "Direct link to textColor")

> **textColor** : `string`

Color of text on the scales.

#### Default Value[​](LayoutOptions.html#default-value-1 "Direct link to Default Value")

`'#191919'`

* * *

### fontSize[​](LayoutOptions.html#fontsize "Direct link to fontSize")

> **fontSize** : `number`

Font size of text on scales in pixels.

#### Default Value[​](LayoutOptions.html#default-value-2 "Direct link to Default Value")

`12`

* * *

### fontFamily[​](LayoutOptions.html#fontfamily "Direct link to fontFamily")

> **fontFamily** : `string`

Font family of text on the scales.

#### Default Value[​](LayoutOptions.html#default-value-3 "Direct link to Default Value")

`-apple-system, BlinkMacSystemFont, 'Trebuchet MS', Roboto, Ubuntu, sans-serif`

* * *

### panes[​](LayoutOptions.html#panes "Direct link to panes")

> **panes** : [`LayoutPanesOptions`](LayoutPanesOptions.md)

Panes options.

#### Default Value[​](LayoutOptions.html#default-value-4 "Direct link to Default Value")

`{ enableResize: true, separatorColor: '#2B2B43', separatorHoverColor: 'rgba(178, 181, 189, 0.2)'}`

* * *

### attributionLogo[​](LayoutOptions.html#attributionlogo "Direct link to attributionLogo")

> **attributionLogo** : `boolean`

Display the TradingView attribution logo on the main chart pane.

The licence for library specifies that you add the "attribution notice" from the NOTICE file to your code and a link to <https://www.tradingview.com/> to the page of your website or mobile application that is available to your users. Using this attribution logo is sufficient for meeting this linking requirement. However, if you already fulfill this requirement then you can disable this attribution logo.

#### Default Value[​](LayoutOptions.html#default-value-5 "Direct link to Default Value")
    
    
    true  
    

* * *

### colorSpace[​](LayoutOptions.html#colorspace "Direct link to colorSpace")

> **colorSpace** : [`ColorSpace`](../type-aliases/ColorSpace.md)

Specifies the color space of the rendering context for the internal canvas elements.

Note: this option should only be specified during the chart creation and not changed at a later stage by using `applyOptions`.

#### Default Value[​](LayoutOptions.html#default-value-6 "Direct link to Default Value")

`srgb`

See [HTMLCanvasElement: getContext() method - Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API/HTMLCanvasElement/getContext#colorspace) for more info

* * *

### colorParsers[​](LayoutOptions.html#colorparsers "Direct link to colorParsers")

> **colorParsers** : [`CustomColorParser`](../type-aliases/CustomColorParser.md)[]

Array of custom color parser functions to handle color formats outside of standard sRGB values. Each parser function takes a string input and should return either:

  * An [Rgba](../type-aliases/Rgba.md) array [r,g,b,a] for valid colors (with values 0-255 for rgb and 0-1 for a)
  * null if the parser cannot handle that color string, allowing the next parser to attempt it

Parsers are tried in order until one returns a non-null result. This allows chaining multiple parsers to handle different color space formats.

Note: this option should only be specified during the chart creation and not changed at a later stage by using `applyOptions`.

The library already supports these color formats by default:

  * Hex colors (#RGB, #RGBA, #RRGGBB, #RRGGBBAA)
  * RGB/RGBA functions (rgb(), rgba())
  * HSL/HSLA functions (hsl(), hsla())
  * HWB function (hwb())
  * Named colors (red, blue, etc.)
  * 'transparent' keyword

Custom parsers are only needed for other color spaces like:

  * Display P3: color(display-p3 r g b)
  * CIE Lab: lab(l a b)
  * LCH: lch(l c h)
  * Oklab: oklab(l a b)
  * Oklch: oklch(l c h)
  * ...

