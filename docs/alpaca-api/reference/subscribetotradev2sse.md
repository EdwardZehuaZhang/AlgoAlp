---
title: Subscribe to Trade Events (SSE)
source: reference\subscribetotradev2sse.html
---

get https://broker-api.sandbox.alpaca.markets/v2/events/trades
The Events API provides event push as well as historical queries via SSE (server sent events).
You can listen to events related to trade updates. Most market trades sent during market hours are filled instantly; you can listen to limit order updates through this endpoint.
Historical events are streamed immediately if queried, and updates are pushed as events occur.
Query Params Rules:
* `since` required if `until` specified
* `since_id` required if `until_id` specified
* `since` and `since_id` can’t be used at the same time  
Behavior:
* if `since` or `since_id` not specified this will not return any historic data
* if `until` or `until_id` reached stream will end (status 200)
* * *
Note for people using the clients generated from this OAS spec. Currently OAS-3 doesn't have full support for representing SSE style responses from an API, so if you are using a generated client and don't specify a `since` and `until` there is a good chance the generated clients will hang waiting for the response to end.
If you require the streaming capabilities we recommend not using the generated clients for this specific usecase until the OAS-3 standards come to a consensus on how to represent this correcting in OAS-3.
* * *
**Legacy trade events API**
**Deprecation notice**
As part of the deprecation process,  
the legacy trade events API is now only available for existing broker-partners at: `GET /v1/events/trades` only for compatibility reasons.
All new broker partners will not have the option for the legacy trade event endpoint.
All new broker partners will have to integrate with the new `/v2/events/trades` endpoint.
Also, all existing broker partners are now recommended to upgrade to the `/v2/events/trades` endpoint, which provides faster event delivery times.
The legacy trade events api works the same way as the new one with the exception of the event_id which is an integer except of an ULID. This results in the request’s since_id and until_id are also being integers. This integer is monotonically increasing over time for events.
Please note that the new `/v2` endpoint, is the same as, and was originally available under `/v2beta1`.  
We encourage all customers to adjust their codebase from that interim beta endpoint to the `/v2` stable endpoint.  
In the near future we will setup permanent redirect from `/v2beta1` to `/v2` before we completely remove the beta endpoint.
* * *
### 
Comment messages
[](subscribetotradev2sse.html#comment-messages)
According to the SSE specification, any line that starts with a colon is a comment which does not contain data. It is typically a free text that does not follow any data schema. A few examples mentioned below for comment messages.
##### 
Slow client
[](subscribetotradev2sse.html#slow-client)
The server sends a comment when the client is not consuming messages fast enough. Example: `: you are reading too slowly, dropped 10000 messages`
##### 
Internal server error
[](subscribetotradev2sse.html#internal-server-error)
An error message is sent as a comment when the server closes the connection on an internal server error (only sent by the v2 and v2beta1 endpoints). Example: `: internal server error`
* * *
**Common events**
These are the events that are the expected results of actions you may have taken by sending API requests.
The meaning of the timestamp field changes for each type; the meanings have been specified here for which types the timestamp field will be present.
* `accepted` Sent when an order recieved and accepted by Alpaca
* `pending_new` Sent when the order has been received by Alpaca and routed to the exchanges, but has not yet been accepted for execution.
* `new` Sent when an order has been routed to exchanges for execution.
* `fill` Sent when your order has been completely filled. 
* timestamp: The time at which the order was filled.
* `partial_fill` Sent when a number of shares less than the total remaining quantity on your order has been filled. 
* timestamp: The time at which the shares were filled.
* `canceled` Sent when your requested cancellation of an order is processed. 
* timestamp: The time at which the order was canceled.
* `expired` Sent when an order has reached the end of its lifespan, as determined by the order's time in force value. 
* timestamp: The time at which the order expired.
* `done_for_day` Sent when the order is done executing for the day, and will not receive further updates until the next trading day.
* `replaced` Sent when your requested replacement of an order is processed. 
* timestamp: The time at which the order was replaced.
**Rarer events**
These are events that may rarely be sent due to unexpected circumstances on the exchanges. It is unlikely you will need to design your code around them, but you may still wish to account for the possibility that they will occur.
* `rejected` Sent when your order has been rejected. 
* timestamp: The time at which the rejection occurred.
* `held` For multi-leg orders, the secondary orders (stop loss, take profit) will enter this state while waiting to be triggered.
* `stopped` Sent when your order has been stopped, and a trade is guaranteed for the order, usually at a stated price or better, but has not yet occurred.
* `pending_cancel` Sent when the order is awaiting cancellation. Most cancellations will occur without the order entering this state.
* `pending_replace` Sent when the order is awaiting replacement.
* `calculated` Sent when the order has been completed for the day - it is either filled or done_for_day - but remaining settlement calculations are still pending.
* `suspended` Sent when the order has been suspended and is not eligible for trading.
* `order_replace_rejected` Sent when the order replace has been rejected.
* `order_cancel_rejected` Sent when the order cancel has been rejected.
* `trade_bust`: Sent when a previously reported execution has been canceled (“busted”) by the upstream exchange.
* `trade_correct`: Sent when a previously reported trade has been corrected. For example, the exchange may have updated the price, quantity, or another execution parameter after the trade was initially reported.
* `restated`: Sent when the order is manually modified.
