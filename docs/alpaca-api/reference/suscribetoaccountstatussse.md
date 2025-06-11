---
title: Subscribe to Account Status Events (SSE)
source: reference\suscribetoaccountstatussse.html
---

get https://broker-api.sandbox.alpaca.markets/v1/events/accounts/status
The accounts events API provides streaming of account changes as they occur, via SSE (server sent events). Past events can also be queried.
Events are generated for changes to the following account properties:
* account_blocked
* admin_configurations
* cash_interest
* crypto_status
* kyc_results
* pattern_day_trader
* status
* trading_blocked
Only the changed properties are included in the event payload.
Query Parameter Rules:
* `since` is required if `until` specified
* `since_id` is required if `until_id` specified
* `since_ulid` is required if `until_ulid` specified
* `since`, `since_id` and `since_ulid` can’t be used at the same time
Behavior:  
This API supports querying a range of events, starting now or in the past. If the end of the range is in the future or not specified, the connection is kept open and future events are pushed.
To be specific:
* if `since`, `since_id` or `since_ulid` is not specified, this will not return any historic data
* if `until`, `until_id` or `until_ulid` is reached, the stream will end with a status of 200
* * *
Note for people using the clients generated from this OAS spec. Currently OAS-3 doesn't have full support for representing SSE style responses from an API, so if you are using a generated client and don't specify a `since` and `until` there is a good chance the generated clients will hang waiting for the response to end.
If you require the streaming capabilities we recommend not using the generated clients for this specific usecase until the OAS-3 standards come to a consensus on how to represent this correcting in OAS-3.
