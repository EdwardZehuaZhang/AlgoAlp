---
title: Subscribe to Non-Trading Activities Events (SSE)
source: reference\get-v1-events-nta.html
---

get https://broker-api.sandbox.alpaca.markets/v1/events/nta
The Events API provides event push as well as historical queries via SSE (server sent events).
You can listen to non-trading activities updates as they get processed by our backoffice, for both end-user and firm accounts.
Historical events are streamed immediately if queried, and updates are pushed as events occur.
You can listen to when NTAs are pushed such as CSDs, JNLC (journals) or FEEs.
Query Params Rules:
* `since` required if `until` specified
* `since_id` required if `until_id` specified
* `since_ulid` required if `until_ulid` specified
* `since`, `since_id` or `since_ulid` can’t be used at the same time  
Behavior:
* if `since`, `since_id` or `since_ulid` not specified this will not return any historic data
* if `until`, `until_id` or `until_ulid` reached stream will end (status 200)'
