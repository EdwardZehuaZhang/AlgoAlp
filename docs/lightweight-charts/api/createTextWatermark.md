# API: Createtextwatermark

*Source: docs\api\functions\createTextWatermark.html*

Version: 5.0

On this page

> **createTextWatermark** <`T`>(`pane`, `options`): [`ITextWatermarkPluginApi`](../type-aliases/ITextWatermarkPluginApi.md)<`T`>

Creates an image watermark.

## Type parameters[​](createTextWatermark.html#type-parameters "Direct link to Type parameters")

• **T**

## Parameters[​](createTextWatermark.html#parameters "Direct link to Parameters")

• **pane** : [`IPaneApi`](../interfaces/IPaneApi.md)<`T`>

Target pane.

• **options** : [`DeepPartial`](../type-aliases/DeepPartial.md) <[`TextWatermarkOptions`](../interfaces/TextWatermarkOptions.md)>

Watermark options.

## Returns[​](createTextWatermark.html#returns "Direct link to Returns")

[`ITextWatermarkPluginApi`](../type-aliases/ITextWatermarkPluginApi.md)<`T`>

Image watermark wrapper.

## Example[​](createTextWatermark.html#example "Direct link to Example")
    
    
    import { createTextWatermark } from 'lightweight-charts';  
      
    const firstPane = chart.panes()[0];  
    const textWatermark = createTextWatermark(firstPane, {  
          horzAlign: 'center',  
          vertAlign: 'center',  
          lines: [  
            {  
              text: 'Hello',  
              color: 'rgba(255,0,0,0.5)',  
              fontSize: 100,  
              fontStyle: 'bold',  
            },  
            {  
              text: 'This is a text watermark',  
              color: 'rgba(0,0,255,0.5)',  
              fontSize: 50,  
              fontStyle: 'italic',  
              fontFamily: 'monospace',  
            },  
          ],  
    });  
    // to change options  
    textWatermark.applyOptions({ horzAlign: 'left' });  
    // to remove watermark from the pane  
    textWatermark.detach();  
    
