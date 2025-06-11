# API: Createimagewatermark

*Source: docs\api\functions\createImageWatermark.html*

Version: 5.0

On this page

> **createImageWatermark** <`T`>(`pane`, `imageUrl`, `options`): [`IImageWatermarkPluginApi`](../type-aliases/IImageWatermarkPluginApi.md)<`T`>

Creates an image watermark.

## Type parameters[​](createImageWatermark.html#type-parameters "Direct link to Type parameters")

• **T**

## Parameters[​](createImageWatermark.html#parameters "Direct link to Parameters")

• **pane** : [`IPaneApi`](../interfaces/IPaneApi.md)<`T`>

Target pane.

• **imageUrl** : `string`

Image URL.

• **options** : [`DeepPartial`](../type-aliases/DeepPartial.md) <[`ImageWatermarkOptions`](../interfaces/ImageWatermarkOptions.md)>

Watermark options.

## Returns[​](createImageWatermark.html#returns "Direct link to Returns")

[`IImageWatermarkPluginApi`](../type-aliases/IImageWatermarkPluginApi.md)<`T`>

Image watermark wrapper.

## Example[​](createImageWatermark.html#example "Direct link to Example")
    
    
    import { createImageWatermark } from 'lightweight-charts';  
      
    const firstPane = chart.panes()[0];  
    const imageWatermark = createImageWatermark(firstPane, '/images/my-image.png', {  
      alpha: 0.5,  
      padding: 20,  
    });  
    // to change options  
    imageWatermark.applyOptions({ padding: 10 });  
    // to remove watermark from the pane  
    imageWatermark.detach();  
    
