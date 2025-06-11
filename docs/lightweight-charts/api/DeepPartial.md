# API: Deeppartial

*Source: docs\api\type-aliases\DeepPartial.html*

Version: 5.0

On this page

> **DeepPartial** <`T`>: `{ [P in keyof T]?: T[P] extends (infer U)[] ? DeepPartial<U>[] : T[P] extends readonly (infer X)[] ? readonly DeepPartial<X>[] : DeepPartial<T[P]> }`

Represents a type `T` where every property is optional.

## Type parameters[​](DeepPartial.html#type-parameters "Direct link to Type parameters")

• **T**
