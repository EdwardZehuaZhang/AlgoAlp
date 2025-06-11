# API: Ipaneprimitivewrapper

*Source: docs\api\interfaces\IPanePrimitiveWrapper.html*

Version: 5.0

On this page

Interface for a pane primitive.

## Type parameters[​](IPanePrimitiveWrapper.html#type-parameters "Direct link to Type parameters")

• **T**

• **Options**

## Properties[​](IPanePrimitiveWrapper.html#properties "Direct link to Properties")

### detach()[​](IPanePrimitiveWrapper.html#detach "Direct link to detach\(\)")

> **detach** : () => `void`

Detaches the plugin from the pane.

#### Returns[​](IPanePrimitiveWrapper.html#returns "Direct link to Returns")

`void`

* * *

### getPane()[​](IPanePrimitiveWrapper.html#getpane "Direct link to getPane\(\)")

> **getPane** : () => [`IPaneApi`](IPaneApi.md)<`T`>

Returns the current pane.

#### Returns[​](IPanePrimitiveWrapper.html#returns-1 "Direct link to Returns")

[`IPaneApi`](IPaneApi.md)<`T`>

* * *

### applyOptions()?[​](IPanePrimitiveWrapper.html#applyoptions "Direct link to applyOptions\(\)?")

> `optional` **applyOptions** : (`options`) => `void`

Applies options to the primitive.

#### Parameters[​](IPanePrimitiveWrapper.html#parameters "Direct link to Parameters")

• **options** : [`DeepPartial`](../type-aliases/DeepPartial.md)<`Options`>

Options to apply. The options are deeply merged with the current options.

#### Returns[​](IPanePrimitiveWrapper.html#returns-2 "Direct link to Returns")

`void`
