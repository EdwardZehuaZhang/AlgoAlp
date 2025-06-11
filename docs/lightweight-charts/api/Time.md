# API: Time

*Source: docs\api\type-aliases\Time.html*

Version: 5.0

On this page

> **Time** : [`UTCTimestamp`](UTCTimestamp.md) | [`BusinessDay`](../interfaces/BusinessDay.md) | `string`

The Time type is used to represent the time of data items.

Values can be a [UTCTimestamp](UTCTimestamp.md), a [BusinessDay](../interfaces/BusinessDay.md), or a business day string in ISO format.

## Example[​](Time.html#example "Direct link to Example")
    
    
    const timestamp = 1529899200; // Literal timestamp representing 2018-06-25T04:00:00.000Z  
    const businessDay = { year: 2019, month: 6, day: 1 }; // June 1, 2019  
    const businessDayString = '2021-02-03'; // Business day string literal  
    
