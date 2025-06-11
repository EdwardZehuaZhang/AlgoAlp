---
title: Real-time Option Data
source: docs\real-time-option-data.html
---

This API provides option market data on a websocket stream. This helps receive the most up to date market information that could help your trading strategy to act upon certain market movements. If you wish to access the latest pricing data, using the stream provides much better accuracy and performance than polling the latest historical endpoints.
You can find the general description of the real-time WebSocket Stream [here](streaming-market-data.md). This page focuses on the option stream.
# 
URL
[](real-time-option-data.html#url)
The URL for the option stream is
wss://stream.data.alpaca.markets/v1beta1/{feed}
Sandbox URL:
wss://stream.data.sandbox.alpaca.markets/v1beta1/{feed}
Substitute `indicative` or `opra` for `{feed}` depending on your subscription. The capabilities and differences for the `indicative` and `opra` subscriptions can be found [[here](about-market-data-api.html-options.md)].
Any attempt to access a data feed not available for your subscription will result in an error during authentication.
# 
Message format
[](real-time-option-data.html#message-format)
> ## 🚧
> 
> Msgpack
> 
> Unlike the stock and crypto stream, the option stream is only available in [msgpack](https://msgpack.org/index.html) format. The SDKs are using this format automatically. For readability, the examples in the rest of this documentation will still be in json format (because msgpack is binary encoded).
# 
Channels
[](real-time-option-data.html#channels)
## 
Trades
[](real-time-option-data.html#trades)
### 
Schema
[](real-time-option-data.html#schema)
Attribute| Type| Notes  
---|---|---  
`T`| string| message type, always “t”  
`S`| string| symbol  
`t`| string| [RFC-3339](https://datatracker.ietf.org/doc/html/rfc3339) formatted timestamp with nanosecond precision  
`p`| number| trade price  
`s`| int| trade size  
`x`| string| exchange code where the trade occurred  
`c`| string| trade condition  
### 
Example
[](real-time-option-data.html#example)
JSON
{
"T": "t",
"S": "AAPL240315C00172500",
"t": "2024-03-11T13:35:35.13312256Z",
"p": 2.84,
"s": 1,
"x": "N",
"c": "S"
}
## 
Quotes
[](real-time-option-data.html#quotes)
### 
Schema
[](real-time-option-data.html#schema-1)
Attribute| Type| Notes  
---|---|---  
`T`| string| message type, always “q”  
`S`| string| symbol  
`t`| string| [RFC-3339](https://datatracker.ietf.org/doc/html/rfc3339) formatted timestamp with nanosecond precision  
`bx`| string| bid exchange code  
`bp`| number| bid price  
`bs`| int| bid size  
`ax`| string| ask exchange code  
`ap`| number| ask price  
`as`| int| ask size  
`c`| string| quote condition  
### 
Example
[](real-time-option-data.html#example-1)
JSON
{
"T": "q",
"S": "SPXW240327P04925000",
"t": "2024-03-12T11:59:38.897261568Z",
"bx": "C",
"bp": 9.46,
"bs": 53,
"ax": "C",
"ap": 9.66,
"as": 38,
"c": "A"
}
# 
Errors
[](real-time-option-data.html#errors)
Other than the [general stream errors](streaming-market-data.html-errors.md), you may receive these option-specific errors during your session:
Error Message| Description  
---|---  
`[{"T":"error","code":412,"msg":"option messages are only available in MsgPack format"}]`| Use the `Content-Type: application/msgpack` header.  
`[{"T":"error","code":413,"msg":"star subscription is not allowed for option quotes"}]`| You cannot subscribe to `*` for option quotes (there are simply too many of them).  
__Updated 4 months ago
* * *
