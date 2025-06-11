---
title: Subscribe to Admin Action Events (SSE)
source: reference\subscribetoadminactionsse.html
---

get https://broker-api.sandbox.alpaca.markets/v2/events/admin-actions
The Events API provides event push as well as historical queries via SSE (server sent events).
This endpoint streams events related to administrative actions performed by our systems.
Historical events are streamed immediately if queried, and updates are pushed as events occur.
Query Params Rules:
* `since` required if `until` specified
* `since_id` required if `until_id` specified
* `since` and `since_id` can’t be used at the same time  
Behavior:
* if `since` or `since_id` not specified this will not return any historic data
* if `until` or `until_id` reached stream will end (status 200)
* * *
Warning: Currently OAS-3 doesn't have full support for representing SSE style responses from an API.
In case the client code is generated from this OAS spec, don't specify a `since` and `until` there is a good chance the generated clients will hang forever waiting for the response to end.
If you require the streaming capabilities we recommend not using the generated clients for this specific endpoint until the OAS-3 standards come to a consensus on how to represent this behavior in OAS-3.
* * *
### 
Comment messages
[](subscribetoadminactionsse.html#comment-messages)
According to the SSE specification, any line that starts with a colon is a comment which does not contain data. It is typically a free text that does not follow any data schema. A few examples mentioned below for comment messages.
##### 
Slow client
[](subscribetoadminactionsse.html#slow-client)
The server sends a comment when the client is not consuming messages fast enough. Example: `: you are reading too slowly, dropped 10000 messages`
##### 
Internal server error
[](subscribetoadminactionsse.html#internal-server-error)
An error message is sent as a comment when the server closes the connection on an internal server error (only sent by the v2 and v2beta1 endpoints). Example: `: internal server error`
* * *
**Event Types**
* **LegacyNote:** Old free text based admin notes
* **Liquidation:** Event for a position liquidation which initialized by an admin
* **TransactionCancel:** Event for a manually cancelled transaction
