---
title: Subscribe to Journal Events (SSE) (Legacy)
source: reference\subscribetojournalstatussse.html
---

get https://broker-api.sandbox.alpaca.markets/v1/events/journals/status
The Events API provides event push as well as historical queries via SSE (server sent events).
You can listen to journal status updates as they get processed by our backoffice.
Historical events are streamed immediately if queried, and updates are pushed as events occur.
Query Params Rules:
* `since` required if `until` specified
* `since_id` required if `until_id` specified
* `since_ulid` required if `until_ulid` specified
* `since`, `since_id` or `since_ulid` can’t be used at the same time  
Behavior:
* if `since`, `since_id` or `since_ulid` not specified this will not return any historic data
* if `until`, `until_id` or `until_ulid` reached stream will end (status 200)
* * *
There is no compatibility between /v1/events/journals/status and /v2beta1/events/journals/status, the ids (ulid) are always different, and the number of events might also different
* * *
Note for people using the clients generated from this OAS spec. Currently OAS-3 doesn't have full support for representing SSE style responses from an API, so if you are using a generated client and don't specify a `since` and `until` there is a good chance the generated clients will hang waiting for the response to end.
If you require the streaming capabilities we recommend not using the generated clients for this specific usecase until the OAS-3 standards come to a consensus on how to represent this correcting in OAS-3.
