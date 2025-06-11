---
title: Websocket Streaming
source: docs\websocket-streaming.html
---

Alpaca’s API offers WebSocket streaming for trade, account, and order updates which follows the [RFC6455 WebSocket protocol](https://datatracker.ietf.org/doc/html/rfc6455).
To connect to the WebSocket follow the standard opening handshake as defined by the RFC specification to `wss://paper-api.alpaca.markets/stream` or `wss://api.alpaca.markets/stream`. Alpaca’s streaming service supports both JSON and MessagePack codecs.
Once the connection is authorized, the client can listen to the `trade_updates` stream to get updates on trade, account, and order changes.
> ## 📘
> 
> Note:
> 
> The `trade_updates` stream coming from `wss://paper-api.alpaca.markets/stream` uses binary frames, which differs from the text frames that comes from the `wss://data.alpaca.markets/stream` stream.
In order to listen to streams, the client sends a `listen` message to the server as follows:
JSON
{
"action": "listen",
"data": {
"streams": ["trade_updates"]
}
}
The server acknowledges by replying a message in the listening stream.
JSON
{
"stream": "listening",
"data": {
"streams": ["trade_updates"]
}
}
If any of the requested streams are not available, they will not appear in the streams list in the acknowledgement. Note that the streams field in the listen message is to tell the set of streams to listen, so if you want to stop receiving updates from the stream, you must send an empty list of streams values as a listen message. Similarly, if you want to add more streams to get updates in addition to the ones you are already doing so, you must send all the stream names, not only the new ones.
Subscribing to real-time trade updates ensures that a user always has the most up-to-date picture of their account actvivity.
> ## 📘
> 
> Note
> 
> To request with MessagePack, add the header: Content-Type: `application/msgpack`.
# 
Authentication
[](websocket-streaming.html#authentication)
The WebSocket client can be authenticated using the same API key when making HTTP requests. Upon connecting to the WebSocket, client must send an authentication message over the WebSocket connection with the API key and secret key as its payload.
JSON
{
"action": "auth",
"key": "{YOUR_API_KEY_ID}",
"secret": "{YOUR_API_SECRET_KEY}"
}
The server will then authorize the connection and respond with either an authorized (successful) response
JSON
{
"stream": "authorization",
"data": {
"status": "authorized",
"action": "authenticate"
}
}
or an unauthorized (unsuccessful) response:
JSON
{
"stream": "authorization",
"data": {
"status": "unauthorized",
"action": "authenticate"
}
}
In the case that the socket connection is not authorized yet, a new message under the authorization stream is issued in response to the listen request.
JSON
{
"stream": "authorization",
"data": {
"status": "unauthorized",
"action": "listen"
}
}
# 
Trade Updates
[](websocket-streaming.html#trade-updates)
With regards to the account associated with the authorized API keys, updates for orders placed at Alpaca are dispatched over the WebSocket connection under the event trade_updates. These messages include any data pertaining to orders that are executed with Alpaca. This includes order fills, partial fills, cancellations and rejections of orders. Clients may listen to this stream by sending a listen message:
JSON
{
"action": "listen",
"data": {
"streams": ["trade_updates"]
}
}
Any listen messages received by the server will be acknowledged via a message on the listening stream. The message’s data payload will include the list of streams the client is currently listening to:
JSON
{
"stream": "listening",
"data": {
"streams": ["trade_updates"]
}
}
The fields present in a message sent over the `trade_updates` stream depend on the type of event they are communicating. All messages contain an `event` type and an `order` field, which is the same as the order object that is returned from the REST API. Potential event types and additional fields that will be in their messages are listed below.
## 
Common Events
[](websocket-streaming.html#common-events)
These are the events that are the expected results of actions you may have taken by sending API requests.
* `new`: Sent when an order has been routed to exchanges for execution.
* `fill`: Sent when an order has been completely filled. 
* `timestamp`: The time at which the order was filled.
* `price`: The price per share for the fill event. This may be different from the average fill price for the order if there were partial fills.
* `qty`: The number of shares for the fill event. This will be different from the filled quantity for the order if there were partial fills.
* `position_qty`: The total size of your position after this event, in shares. Positive for long positions, negative for short positions.
* `partial_fill`: Sent when a number of shares less than the total remaining quantity on your order has been filled. 
* `timestamp`: The time at which the order was partially filled.
* `price`: The price per share for the partial fill event.
* `qty`: The number of shares for the partial fill event.
* `position_qty`: The total size of your position after this event, in shares. Positive for long positions, negative for short positions.
* `canceled`: Sent when your requested cancelation of an order is processed. 
* `timestamp`: The time at which the order was canceled.
* `expired`: Sent when an order has reached the end of its lifespan, as determined by the order’s time in force value. 
* `timestamp`: The time at which the order was expired.
* `done_for_day`: Sent when the order is done executing for the day, and will not receive further updates until the next trading day.
* `replaced`: Sent when your requested replacement of an order is processed. 
* `timestamp`: The time at which the order was replaced.
## 
Less Common Events
[](websocket-streaming.html#less-common-events)
These are events that may rarely be sent due to uncommon circumstances on the exchanges. It is unlikely you will need to design your code around them, but you may still wish to account for the possibility that they can occur.
* `rejected`: Sent when your order has been rejected. 
* `timestamp`: The time at which the order was rejected.
* `pending_new`: Sent when the order has been received by Alpaca and routed to the exchanges, but has not yet been accepted for execution.
* `stopped`: Sent when your order has been stopped, and a trade is guaranteed for the order, usually at a stated price or better, but has not yet occurred.
* `pending_cancel`: Sent when the order is awaiting cancelation. Most cancelations will occur without the order entering this state.
* `pending_replace`: Sent when the order is awaiting replacement.
* `calculated`: Sent when the order has been completed for the day - it is either “filled” or “done_for_day” - but remaining settlement calculations are still pending.
* `suspended`: Sent when the order has been suspended and is not eligible for trading.
* `order_replace_rejected`: Sent when the order replace has been rejected.
* `order_cancel_rejected`: Sent when the order cancel has been rejected.
# 
Example
[](websocket-streaming.html#example)
An example of a message sent over the `trade_updates` stream looks like:
JSON
{
"stream": "trade_updates",
"data": {
"event": "fill",
"execution_id": "2f63ea93-423d-4169-b3f6-3fdafc10c418",
"order": {
"asset_class": "crypto",
"asset_id": "1cf35270-99ee-44e2-a77f-6fab902c7f80",
"cancel_requested_at": null,
"canceled_at": null,
"client_order_id": "4642fd68-d59a-47d7-a9ac-e22f536828d1",
"created_at": "2022-04-19T13:45:04.981350886-04:00",
"expired_at": null,
"extended_hours": false,
"failed_at": null,
"filled_at": "2022-04-19T17:45:05.024916716Z",
"filled_avg_price": "105.8988475",
"filled_qty": "1790.86",
"hwm": null,
"id": "a5be8f5e-fdfa-41f5-a644-7a74fe947a8f",
"legs": null,
"limit_price": null,
"notional": null,
"order_class": "",
"order_type": "market",
"qty": "1790.86",
"replaced_at": null,
"replaced_by": null,
"replaces": null,
"side": "sell",
"status": "filled",
"stop_price": null,
"submitted_at": "2022-04-19T13:45:04.980944666-04:00",
"symbol": "SOLUSD",
"time_in_force": "gtc",
"trail_percent": null,
"trail_price": null,
"type": "market",
"updated_at": "2022-04-19T13:45:05.027690731-04:00"
},
"position_qty": "0",
"price": "105.8988475",
"qty": "1790.86",
"timestamp": "2022-04-19T17:45:05.024916716Z"
}
}
An example message for MultilegOptionsOrder fill event:
JSON
{
"stream": "trade_updates",
"data": {
"at": "2025-01-21T07:32:40.70095Z",
"event_id": "01JJ3WE73W5PG672TC4XACXH5R",
"event": "fill",
"timestamp": "2025-01-21T07:32:40.695569506Z",
"order": {
"id": "31cd620f-3bd5-41b7-8bb2-6834524679d0",
"client_order_id": "fe999618-6435-497b-9fdd-a63d3da3615f",
"created_at": "2025-01-21T07:32:40.678963102Z",
"updated_at": "2025-01-21T07:32:40.699359002Z",
"submitted_at": "2025-01-21T07:32:40.691562346Z",
"filled_at": "2025-01-21T07:32:40.695569506Z",
"expired_at": null,
"cancel_requested_at": null,
"canceled_at": null,
"failed_at": null,
"replaced_at": null,
"replaced_by": null,
"replaces": null,
"asset_id": "00000000-0000-0000-0000-000000000000",
"symbol": "",
"asset_class": "",
"notional": null,
"qty": "1",
"filled_qty": "1",
"filled_avg_price": "1.62",
"order_class": "mleg",
"order_type": "limit",
"type": "limit",
"side": "buy",
"time_in_force": "day",
"limit_price": "2",
"stop_price": null,
"status": "filled",
"extended_hours": false,
"legs": [
{
"id": "3cbe69ef-241c-43ba-9d8c-09361930a1af",
"client_order_id": "e868fb88-ce92-442b-91be-4b16defbc883",
"created_at": "2025-01-21T07:32:40.678963102Z",
"updated_at": "2025-01-21T07:32:40.697474882Z",
"submitted_at": "2025-01-21T07:32:40.687356797Z",
"filled_at": "2025-01-21T07:32:40.695564076Z",
"expired_at": null,
"cancel_requested_at": null,
"canceled_at": null,
"failed_at": null,
"replaced_at": null,
"replaced_by": null,
"replaces": null,
"asset_id": "925af3ed-5c00-4ef1-b89b-e4bd05f04486",
"symbol": "AAPL250321P00200000",
"asset_class": "us_option",
"notional": null,
"qty": "1",
"filled_qty": "1",
"filled_avg_price": "1.6",
"order_class": "mleg",
"order_type": "",
"type": "",
"side": "buy",
"time_in_force": "day",
"limit_price": null,
"stop_price": null,
"status": "filled",
"extended_hours": false,
"legs": null,
"trail_percent": null,
"trail_price": null,
"hwm": null,
"ratio_qty": "1"
},
{
"id": "ec694de5-5028-4347-8f89-d8ea00c9341f",
"client_order_id": "0a1bf1e1-6992-4c23-85a6-9469bbe05f1a",
"created_at": "2025-01-21T07:32:40.678963102Z",
"updated_at": "2025-01-21T07:32:40.699294952Z",
"submitted_at": "2025-01-21T07:32:40.691562346Z",
"filled_at": "2025-01-21T07:32:40.695569506Z",
"expired_at": null,
"cancel_requested_at": null,
"canceled_at": null,
"failed_at": null,
"replaced_at": null,
"replaced_by": null,
"replaces": null,
"asset_id": "9f8c3d65-f5f7-42cd-acbc-9636cc32d3b5",
"symbol": "AAPL250321C00380000",
"asset_class": "us_option",
"notional": null,
"qty": "1",
"filled_qty": "1",
"filled_avg_price": "0.02",
"order_class": "mleg",
"order_type": "",
"type": "",
"side": "buy",
"time_in_force": "day",
"limit_price": null,
"stop_price": null,
"status": "filled",
"extended_hours": false,
"legs": null,
"trail_percent": null,
"trail_price": null,
"hwm": null,
"ratio_qty": "1"
}
],
"trail_percent": null,
"trail_price": null,
"hwm": null
},
"price": "1.62",
"qty": "1",
"position_qtys": {
"AAPL250321P00200000": "1",
"AAPL250321C00380000": "1"
},
"legs": [
{
"execution_id": "69a70e98-f370-427d-bcd3-834dc4800aed",
"qty": "1",
"price": "1.6",
"order_id": "3cbe69ef-241c-43ba-9d8c-09361930a1af",
"symbol": "AAPL250321P00200000",
"timestamp": "2025-01-21T07:32:40.695564076Z"
},
{
"execution_id": "fb878d87-569e-49f3-b42e-a09ad06e3d3a",
"qty": "1",
"price": "0.02",
"order_id": "ec694de5-5028-4347-8f89-d8ea00c9341f",
"symbol": "AAPL250321C00380000",
"timestamp": "2025-01-21T07:32:40.695569506Z"
}
]
}
}
## 
Error messages
[](websocket-streaming.html#error-messages)
In the case of in-stream errors, the server sends an `error` action before closing the connection.
JSON
{
"action": "error",
"data": {
"error_message": "internal server error"
}
}
__Updated 4 months ago
* * *
