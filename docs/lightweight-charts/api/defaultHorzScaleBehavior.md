# API: Defaulthorzscalebehavior

*Source: docs\api\functions\defaultHorzScaleBehavior.html*

Version: 5.0

On this page

> **defaultHorzScaleBehavior**(): () => [`IHorzScaleBehavior`](../interfaces/IHorzScaleBehavior.md) <[`Time`](../type-aliases/Time.md)>

Provides the default implementation of the horizontal scale (time-based) that can be used as a base for extending the horizontal scale with custom behavior. This allows for the introduction of custom functionality without re-implementing the entire [IHorzScaleBehavior](../interfaces/IHorzScaleBehavior.md)<[Time](../type-aliases/Time.md)> interface.

For further details, refer to the [createChartEx](createChartEx.md) chart constructor method.

## Returns[​](defaultHorzScaleBehavior.html#returns "Direct link to Returns")

`Function`

An uninitialized class implementing the [IHorzScaleBehavior](../interfaces/IHorzScaleBehavior.md)<[Time](../type-aliases/Time.md)> interface

### Returns[​](defaultHorzScaleBehavior.html#returns-1 "Direct link to Returns")

[`IHorzScaleBehavior`](../interfaces/IHorzScaleBehavior.md) <[`Time`](../type-aliases/Time.md)>
