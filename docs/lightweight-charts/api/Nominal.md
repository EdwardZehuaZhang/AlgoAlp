# API: Nominal

*Source: docs\api\type-aliases\Nominal.html*

Version: 5.0

On this page

> **Nominal** <`T`, `Name`>: `T` & `object`

This is the generic type useful for declaring a nominal type, which does not structurally matches with the base type and the other types declared over the same base type

## Examples[​](Nominal.html#examples "Direct link to Examples")
    
    
    type Index = Nominal<number, 'Index'>;  
    // let i: Index = 42; // this fails to compile  
    let i: Index = 42 as Index; // OK  
    
    
    
    type TagName = Nominal<string, 'TagName'>;  
    

## Type declaration[​](Nominal.html#type-declaration "Direct link to Type declaration")

### [species][​](Nominal.html#species "Direct link to \[species\]")

> **[species]** : `Name`

The 'name' or species of the nominal.

## Type parameters[​](Nominal.html#type-parameters "Direct link to Type parameters")

• **T**

• **Name** _extends_ `string`
