---
title: SSE Events
source: docs\draft-sse-events.html
---

Alpaca Broker API provides replayable and real-time event streams via Server-Sent Event (SSE). The SSE protocol is a simple yet powerful protocol to satisfy a lot of your needs to build flawless user experience. Each endpoint can be queried by the event timestamp or monotonically incremental integer ID to seamlessly subscribe from the past point-in-time event to the real-time pushes with a simple HTTP request. While all SSE endpoints follow the same JSON object model as other REST endpoints, SSE protocol is a lightweight addition on top of the basic HTTP protocol which is a bit different from REST protocol. Please make sure your client program handles the SSE protocol correctly.
# 
Why Use SSE?
[](draft-sse-events.html#why-use-sse)
* Low Latency: Receive updates in real-time for timely decisions about your customers
* Resource Efficiency: A single connection serves multiple updates and streamlines where you receive updates about your customers
* Simplicity: Integration requires fewer lines of code compared to WebSockets.
## 
Best Practices
[](draft-sse-events.html#best-practices)
* Connection Health: Implement heartbeat checks.
* Error Recovery: Code for auto-reconnection.
* Selective Listening: Subscribe to specific event types relevant to your use case.
> ## 🛠️
> 
> Note about /v1 and /v2beta1
> 
> We are in the process of switching from integer IDs to ULIDs for our Events Streaming. ULIDs are designed to be lexicographically sortable, thanks to their structure that encodes a timestamp. This allows you to better sort and filter records based on when they occured. While they are more complex to read than integer IDs, they contain more information. 
> 
> Currently only Admin Action Events and Trade Events leverage ULIDs, and over the next months we will be migrating the rest. Check back here to know which SSEs are on the new endpoint.
> 
> ### 
> 
> What Should You Do?
> 
> [](draft-sse-events.html#what-should-you-do)
> 
> Legacy Events that still use an integer ID and have now an additional field called since_ulid and until_ulid. We highly recommend that you use those today so that you don't face any issues when we will eventually migrate the remaining events (account status, journal status, transfer status, trade status and non-trade-activity notifications) and deprecate the old ones.
# 
Types of SSE Events
[](draft-sse-events.html#types-of-sse-events)
## 
Account Status Events
[](draft-sse-events.html#account-status-events)
Stay abreast of changes to account statuses. [Learn more here](..-reference-suscribetoaccountstatussse.md).
You can find some sample responses below:
Equity & Crypto AccountEquity Only Account
{
"account_blocked": false,
"account_id": "9ab15e44-569c-4c32-952c-b83ab7076549",
"account_number": "",
"admin_configurations": {
"allow_instant_ach": true,
"disable_shorting": true
},
"at": "2023-10-13T13:34:28.30629Z",
"crypto_status_from": "",
"crypto_status_to": "APPROVED",
"event_id": 12627517,
"event_ulid": "01HCMKXQYJ3ZBV66Q21KCT1CRR",
"pattern_day_trader": false,
"status_from": "",
"status_to": "APPROVED",
"trading_blocked": false
}
{
"account_id": "50333df9-66f0-46b9-a083-4212b152f749",
"account_number": "307137914",
"at": "2023-10-13T13:34:29.668043Z",
"event_id": 12627518,
"event_ulid": "01HCMKXS94ST351NFGEZR57EHV",
"status_from": "APPROVED",
"status_to": "ACTIVE"
}
:heartbeat
{
"account_id": "9ab15e44-569c-4c32-952c-b83ab7076549",
"account_number": "307645030",
"at": "2023-10-13T13:35:18.145917Z",
"crypto_status_from": "APPROVED",
"crypto_status_to": "ACTIVE",
"event_id": 12627519,
"event_ulid": "01HCMKZ8M2XPNC9Y8HE159P2WK",
"status_from": "APPROVED",
"status_to": "APPROVED"
}
:heartbeat
{
"account_id": "9ab15e44-569c-4c32-952c-b83ab7076549",
"account_number": "307645030",
"at": "2023-10-13T13:40:17.417798Z",
"event_id": 12627521,
"event_ulid": "01HCMM8CWAQETWNM75VJKA0YX2",
"status_from": "APPROVED",
"status_to": "ACTIVE"
}
{
"account_blocked": false,
"account_id": "d16f0c84-2bcc-4caf-bd68-a97889986d74",
"account_number": "",
"admin_configurations": {
"allow_instant_ach": true,
"disable_shorting": true
},
"at": "2023-10-13T13:18:16.936397Z",
"crypto_status_from": "",
"crypto_status_to": "INACTIVE",
"event_id": 12627496,
"event_ulid": "01HCMK03B8JV4YDB8W2HZ0K6V2",
"pattern_day_trader": false,
"status_from": "",
"status_to": "APPROVED",
"trading_blocked": false
}
{
"account_id": "d16f0c84-2bcc-4caf-bd68-a97889986d74",
"account_number": "307781498",
"at": "2023-10-13T13:18:18.472537Z",
"event_id": 12627497,
"event_ulid": "01HCMK04V979EMCGB96Z6T0H00",
"status_from": "APPROVED",
"status_to": "ACTIVE"
}
## 
Journal Events
[](draft-sse-events.html#journal-events)
Stay notified on the status of journal transactions to make sure they have been executed and the cash has been moved from one account to another. [More details here](..-edit-funding-via-journals.md).
You can find a sample response below:
JSON
{
"at": "2023-10-13T13:11:10.57913Z",
"entry_type": "JNLC",
"event_id": 11751531,
"event_ulid": "01HCMJK2ZKCPTYXMJYS66T0QJJ",
"journal_id": "ddd26344-86af-4ba7-ae6a-bcec63129808",
"status_from": "",
"status_to": "queued"
}
{
"at": "2023-10-13T13:11:10.634443Z",
"entry_type": "JNLC",
"event_id": 11751532,
"event_ulid": "01HCMJK31AVBME4WNSH3C8E4HJ",
"journal_id": "ddd26344-86af-4ba7-ae6a-bcec63129808",
"status_from": "queued",
"status_to": "sent_to_clearing"
}
{
"at": "2023-10-13T13:11:10.67241Z",
"entry_type": "JNLC",
"event_id": 11751533,
"event_ulid": "01HCMJK32GSBH2QG92TKZKDRRV",
"journal_id": "ddd26344-86af-4ba7-ae6a-bcec63129808",
"status_from": "sent_to_clearing",
"status_to": "executed"
}
## 
Transfer Events
[](draft-sse-events.html#transfer-events)
Be notified instantly when the statuses of deposits and withdrawals are updated. [Read further here](..-reference-subscribetotransferstatussse.md).
You can find a sample response below:
JSON
{
"account_id":"8e00606a-c9ac-409a-ba45-f55e8f77984a",
"at":"2021-06-10T19:49:12.579109Z",
"event_id":15960,
"status_from":"",
"status_to":"queued",
"transfer_id":"c4ed4206-697b-4859-ab71-b9de6649859d"
}
{
"account_id":"8e00606a-c9ac-409a-ba45-f55e8f77984a",
"at":"2021-06-10T19:52:24.066998Z",
"event_id":15961,
"status_from":"queued",
"status_to":"sent_to_clearing",
"transfer_id":"c4ed4206-697b-4859-ab71-b9de6649859d"
}
{
"account_id":"8e00606a-c9ac-409a-ba45-f55e8f77984a",
"at":"2021-06-10T20:02:24.280178Z",
"event_id":15962,
"status_from":"sent_to_clearing",
"status_to":"executed",
"transfer_id":"c4ed4206-697b-4859-ab71-b9de6649859d"
}
## 
Trade Events
[](draft-sse-events.html#trade-events)
Keep tabs on the status of orders, trades, and executions in real-time. [Documentation here](..-reference-subscribetotradev2sse.md).
v2beta1v1
{
"account_id": "aa4439c3-cf7d-4251-8689-a575a169d6d3",
"at": "2023-10-13T13:28:58.387652Z",
"event_id": "01HCMKKNRK7S5C1JYP50QGDECQ",
"event": "new",
"timestamp": "2023-10-13T13:28:58.37957033Z",
"order": {
"id": "bb2403bc-88ec-430b-b41c-f9ee80c8f0e1",
"client_order_id": "508789e5-cea3-4235-b546-6c62ff92bd79",
"created_at": "2023-10-13T13:28:58.361530031Z",
"updated_at": "2023-10-13T13:28:58.386058029Z",
"submitted_at": "2023-10-13T13:28:58.360070731Z",
"filled_at": null,
"expired_at": null,
"cancel_requested_at": null,
"canceled_at": null,
"failed_at": null,
"replaced_at": null,
"replaced_by": null,
"replaces": null,
"asset_id": "b0b6dd9d-8b9b-48a9-ba46-b9d54906e415",
"symbol": "AAPL",
"asset_class": "us_equity",
"notional": "10",
"qty": null,
"filled_qty": "0",
"filled_avg_price": null,
"order_class": "",
"order_type": "market",
"type": "market",
"side": "buy",
"time_in_force": "day",
"limit_price": null,
"stop_price": null,
"status": "new",
"extended_hours": false,
"legs": null,
"trail_percent": null,
"trail_price": null,
"hwm": null,
"commission": "0"
},
"execution_id": "7922ab44-5b33-4049-ab9a-0cfd805ba989"
}
:heartbeat
{
"account_id": "aa4439c3-cf7d-4251-8689-a575a169d6d3",
"at": "2023-10-13T13:30:00.664778Z",
"event_id": "01HCMKNJJRJ4E3RNFA1XR8CX7R",
"event": "fill",
"timestamp": "2023-10-13T13:30:00.658443088Z",
"order": {
"id": "db04069d-2e5a-48d4-a42f-6a0dea8ea0b8",
"client_order_id": "be139e2d-8153-4ae8-83ee-7b98b4e17419",
"created_at": "2023-10-13T13:22:21.887914Z",
"updated_at": "2023-10-13T13:30:00.661902331Z",
"submitted_at": "2023-10-13T13:23:05.411141Z",
"filled_at": "2023-10-13T13:30:00.658443088Z",
"expired_at": null,
"cancel_requested_at": null,
"canceled_at": null,
"failed_at": null,
"replaced_at": null,
"replaced_by": null,
"replaces": null,
"asset_id": "b0b6dd9d-8b9b-48a9-ba46-b9d54906e415",
"symbol": "AAPL",
"asset_class": "us_equity",
"notional": "10",
"qty": null,
"filled_qty": "0.05513895",
"filled_avg_price": "181.36",
"order_class": "",
"order_type": "market",
"type": "market",
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
"commission": "0"
},
"price": "181.36",
"qty": "0.05513895",
"position_qty": "0.05513895",
"execution_id": "a958bb42-b034-4d17-bf07-805cf0820ffe"
}
{
"account_id": "aa4439c3-cf7d-4251-8689-a575a169d6d3",
"at": "2023-10-13T13:30:00.673857Z",
"event_id": "01HCMKNJK1Y0R7VF6Q6CAC3SH7",
"event": "fill",
"timestamp": "2023-10-13T13:30:00.658388668Z",
"order": {
"id": "bb2403bc-88ec-430b-b41c-f9ee80c8f0e1",
"client_order_id": "508789e5-cea3-4235-b546-6c62ff92bd79",
"created_at": "2023-10-13T13:28:58.361530031Z",
"updated_at": "2023-10-13T13:30:00.665807961Z",
"submitted_at": "2023-10-13T13:28:58.360070731Z",
"filled_at": "2023-10-13T13:30:00.658388668Z",
"expired_at": null,
"cancel_requested_at": null,
"canceled_at": null,
"failed_at": null,
"replaced_at": null,
"replaced_by": null,
"replaces": null,
"asset_id": "b0b6dd9d-8b9b-48a9-ba46-b9d54906e415",
"symbol": "AAPL",
"asset_class": "us_equity",
"notional": "10",
"qty": null,
"filled_qty": "0.05513895",
"filled_avg_price": "181.36",
"order_class": "",
"order_type": "market",
"type": "market",
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
"commission": "0"
},
"price": "181.36",
"qty": "0.05513895",
"position_qty": "0.1102779",
"execution_id": "33cbb614-bfc0-468b-b4d0-ccf08588ef77"
}
:heartbeat
{
"account_id": "aa4439c3-cf7d-4251-8689-a575a169d6d3",
"at": "2024-09-23T13:30:00.673857Z",
"event_id": "01HCMQR4S73L9G6EHI0JKL2M3N",
"event": "trade_bust",
"timestamp": "2024-09-23T15:30:48.601741737Z",
"order": {
"id": "c86e4d6c-2cdf-4b81-b658-5728bdc8310b",
"client_order_id": "10671b99-2cb3-43c3-92a0-96054edd59a8",
"created_at": "2024-09-23T15:30:48.599363562Z",
"updated_at": "2024-09-23T16:09:21.642880502Z",
"submitted_at": "2024-09-23T15:30:48.601741737Z",
"filled_at": "2024-09-23T20:09:21.635Z",
"expired_at": null,
"cancel_requested_at": null,
"canceled_at": null,
"failed_at": null,
"replaced_at": null,
"replaced_by": null,
"replaces": null,
"asset_id": "a153fd9c-fd4e-4416-9adc-f9040aa2e125",
"symbol": "JTAI",
"asset_class": "us_equity",
"notional": null,
"qty": "2",
"filled_qty": "0",
"filled_avg_price": "0.107703",
"order_class": "",
"order_type": "market",
"type": "market",
"side": "buy",
"time_in_force": "day",
"limit_price": null,
"stop_price": null,
"status": "filled",
"extended_hours": false,
"legs": null,
"trail_percent": null,
"trail_price": null,
"hwm": null
},
"price": "0.107703",
"qty": "-2",
"position_qty": "0",
"execution_id": "df61d6ec-511f-4cc1-ae61-20456b0cb7a5",
"previous_execution_id": "aeb60660-412f-4537-8d1f-1101b3fc8f64"
}
{
"account_id": "aa4439c3-cf7d-4251-8689-a575a169d6d3",
"at": "2024-10-18T13:30:00.673857Z",
"event_id": "01HCMQR4S73L9G6EHI0JKL2M3N",
"event": "trade_correct",
"timestamp": "2024-10-18T22:26:32.988Z",
"order": {
"id": "390cd7d0-07fa-4ab0-8b99-7ffb8d7408ff",
"client_order_id": "21975666-5eae-4149-b86f-3682f4fd8c69",
"created_at": "2024-10-18T09:10:13.311667892Z",
"updated_at": "2024-10-18T18:26:32.996327532Z",
"submitted_at": "2024-10-18T09:10:13.31490803Z",
"filled_at": "2024-10-18T22:26:32.988Z",
"expired_at": null,
"cancel_requested_at": null,
"canceled_at": null,
"failed_at": null,
"replaced_at": null,
"replaced_by": null,
"replaces": null,
"asset_id": "6b0137a2-4efb-4fba-aa39-9f64f6afe5f4",
"symbol": "BSRR",
"asset_class": "us_equity",
"notional": null,
"qty": "1",
"filled_qty": "1",
"filled_avg_price": "25",
"order_class": "",
"order_type": "limit",
"type": "limit",
"side": "buy",
"time_in_force": "day",
"limit_price": "28.93",
"stop_price": null,
"status": "filled",
"extended_hours": true,
"legs": null,
"trail_percent": null,
"trail_price": null,
"hwm": null
},
"price": "25",
"qty": "1",
"position_qty": "1",
"execution_id": "2ff98545-9082-469a-8aa8-7f6c09ac258f",
"previous_execution_id": "f116d6c7-fc4a-49b1-a649-317aace34783"
}
{
"account_id": "aa4439c3-cf7d-4251-8689-a575a169d6d3",
"at": "2023-10-13T13:22:21.927554Z",
"event": "accepted",
"event_id": 10676063,
"event_ulid": "01HCMK7JJ3EJD9P4JSM1M0HTZ0",
"order": {
"asset_class": "us_equity",
"asset_id": "b0b6dd9d-8b9b-48a9-ba46-b9d54906e415",
"cancel_requested_at": null,
"canceled_at": null,
"client_order_id": "be139e2d-8153-4ae8-83ee-7b98b4e17419",
"commission": "0",
"created_at": "2023-10-13T09:22:21.887913787-04:00",
"expired_at": null,
"extended_hours": false,
"failed_at": null,
"filled_at": null,
"filled_avg_price": null,
"filled_qty": "0",
"hwm": null,
"id": "db04069d-2e5a-48d4-a42f-6a0dea8ea0b8",
"legs": null,
"limit_price": null,
"notional": "10",
"order_class": "",
"order_type": "market",
"qty": null,
"replaced_at": null,
"replaced_by": null,
"replaces": null,
"side": "buy",
"status": "accepted",
"stop_price": null,
"submitted_at": "2023-10-13T09:22:21.886066537-04:00",
"symbol": "AAPL",
"time_in_force": "day",
"trail_percent": null,
"trail_price": null,
"type": "market",
"updated_at": "2023-10-13T09:22:21.887913787-04:00"
},
"timestamp": "2023-10-13T09:22:21.888053477-04:00"
}
:heartbeat
{
"account_id": "aa4439c3-cf7d-4251-8689-a575a169d6d3",
"at": "2023-10-13T13:30:01.118487Z",
"event": "fill",
"event_id": 10676567,
"event_ulid": "01HCMKNJJRJ4E3RNFA1XR8CX7R",
"execution_id": "a958bb42-b034-4d17-bf07-805cf0820ffe",
"order": {
"asset_class": "us_equity",
"asset_id": "b0b6dd9d-8b9b-48a9-ba46-b9d54906e415",
"cancel_requested_at": null,
"canceled_at": null,
"client_order_id": "be139e2d-8153-4ae8-83ee-7b98b4e17419",
"commission": "0",
"created_at": "2023-10-13T13:22:21.887914Z",
"expired_at": null,
"extended_hours": false,
"failed_at": null,
"filled_at": "2023-10-13T13:30:00.658443088Z",
"filled_avg_price": "181.36",
"filled_qty": "0.05513895",
"hwm": null,
"id": "db04069d-2e5a-48d4-a42f-6a0dea8ea0b8",
"legs": null,
"limit_price": null,
"notional": "10",
"order_class": "",
"order_type": "market",
"qty": null,
"replaced_at": null,
"replaced_by": null,
"replaces": null,
"side": "buy",
"status": "filled",
"stop_price": null,
"submitted_at": "2023-10-13T13:23:05.411141Z",
"symbol": "AAPL",
"time_in_force": "day",
"trail_percent": null,
"trail_price": null,
"type": "market",
"updated_at": "2023-10-13T09:30:00.661902331-04:00"
},
"position_qty": "0.05513895",
"price": "181.36",
"qty": "0.05513895",
"timestamp": "2023-10-13T13:30:00.658443088Z"
}
{
"account_id": "aa4439c3-cf7d-4251-8689-a575a169d6d3",
"at": "2023-10-13T13:30:02.667443Z",
"event": "fill",
"event_id": 10676601,
"event_ulid": "01HCMKNJK1Y0R7VF6Q6CAC3SH7",
"execution_id": "33cbb614-bfc0-468b-b4d0-ccf08588ef77",
"order": {
"asset_class": "us_equity",
"asset_id": "b0b6dd9d-8b9b-48a9-ba46-b9d54906e415",
"cancel_requested_at": null,
"canceled_at": null,
"client_order_id": "508789e5-cea3-4235-b546-6c62ff92bd79",
"commission": "0",
"created_at": "2023-10-13T09:28:58.361530031-04:00",
"expired_at": null,
"extended_hours": false,
"failed_at": null,
"filled_at": "2023-10-13T13:30:00.658388668Z",
"filled_avg_price": "181.36",
"filled_qty": "0.05513895",
"hwm": null,
"id": "bb2403bc-88ec-430b-b41c-f9ee80c8f0e1",
"legs": null,
"limit_price": null,
"notional": "10",
"order_class": "",
"order_type": "market",
"qty": null,
"replaced_at": null,
"replaced_by": null,
"replaces": null,
"side": "buy",
"status": "filled",
"stop_price": null,
"submitted_at": "2023-10-13T09:28:58.360070731-04:00",
"symbol": "AAPL",
"time_in_force": "day",
"trail_percent": null,
"trail_price": null,
"type": "market",
"updated_at": "2023-10-13T09:30:00.665807961-04:00"
},
"position_qty": "0.1102779",
"price": "181.36",
"qty": "0.05513895",
"timestamp": "2023-10-13T13:30:00.658388668Z"
}
### 
Message Ordering
[](draft-sse-events.html#message-ordering)
For the messages received on the SSE stream we guarantee that the order of the received events is the same as the order they were happening on a per account basis.
Example: if event E1 has been received earlier then another event E2 for the same account, then E1 happened before E2 according to our bookkeeping.
We do not have this guarantee across accounts: if two events for different accounts are received it is the consumer’s responsibility to decide which event happened first based on the timestamp/ulid fields of the event.
Example: E1 happened for account A1 before E2 which was affecting A2. The streaming endpoint might return the events in E1, E2 or E2, E1 ordering. Both responses should be considered valid.
Note: since ULIDs contain a random part other events might have arrived in the same millisecond as the last event received being lexiographicly less than the previous event.
If the stream is used for recon purposes, we recommend to restart the stream from a since that is a few mintues before the time of latest event received.
This approach means that the consumer will receive some events twice when restarting a stream: it is the consumer’s responsibility to process the recevied messages in an idempotent manner so that duplicate messages get ignored on the consumer side.
Note: since and until parameters are parsing as RFC3339 where timezone can be specified (e.g 2006-01-02T15:04:05+07:00), however plus sign character (+) is a special character in HTTP, so use the URL encoded version instead, e.g. ...events/trades?since=2006-01-02T15:04:05%2B07:00
### 
Comment messages
[](draft-sse-events.html#comment-messages)
According to the SSE specification, any line that starts with a colon is a comment which does not contain data. It is typically a free text that does not follow any data schema. A few examples mentioned below for comment messages.
##### 
Slow client
[](draft-sse-events.html#slow-client)
The server sends a comment when the client is not consuming messages fast enough. Example: `: you are reading too slowly, dropped 10000 messages`
##### 
Internal server error
[](draft-sse-events.html#internal-server-error)
An error message is sent as a comment when the server closes the connection on an internal server error (only sent by the v2 and v2beta1 endpoints). Example: `: internal server error`
## 
Admin Action Events
[](draft-sse-events.html#admin-action-events)
These events pertain to administrative actions like account suspensions and liquidations performed by Alpaca Administrators. [See more here](..-reference-subscribetoadminactionsse.md).
Account status change
[
{
"event_id": "01GTVS4FVS2KJDTPYH2WM6NAXF",
"at": "2023-09-21T10:52:38.429059991Z",
"note": "Status changed to REJECTED.", 
"type": "legacy_note_admin_event", 
"context": {}, 
"category": "other", 
"event_id": "03HBVNXKMWYGFTKTGNVR5R41F2", 
"correspondent": "ABCD", 
"belongs_to_kind": "account", 
"created_by_kind": "admin", 
"belongs_to_id_reference": "b4fe44b0-e51c-48f4-b674-990bea6cf8d7", 
"created_by_id_reference": "f0e150df-94ad-48f9-8b0f-05433a3b53c3"
}
]
## 
Non-Trade Activities Events
[](draft-sse-events.html#non-trade-activities-events)
Covering non-trade activities like dividends, stock splits, and other corporate actions. [Read more here](..-reference-get-v1-events-nta.md).
You can find some sample responses below:
Cash DIVStock DIVDIVNRASPLITSPINCash MAStock MASCMAREORGREG FEETAF FEEORF FEEOCC FEENRV FEENRC FEELCT FEECSDCSWNCVOFJNLCJNLSOPTRDOPEXPOPASNOPEXCINTACATCACATSMGN INTQII INTSWP INTDIV.CDIV (options)NC.SNC (options)SPLIT.RSPLIT (options)SPLIT.FSPLIT (options)MA.SMA (options)SPIN (options)ACATS (options)
{
"id": "{GUID}",
"qty": 0,
"price": null,
"status": "executed",
"symbol": "MMS",
"cusip": "577933104",
"entry_type": "DIV",
"net_amount": 0.78,
"description": "Cash DIV @ 0.3, Pos QTY: 2.607144585, Rec Date: 2024-11-15",
"settle_date": "2024-11-29",
"system_date": "2024-12-02",
"entry_sub_type": "CDIV",
"per_share_amount": 0.3,
"account_id": "{ACCID}",
"at": "2024-12-02T05:09:50.214Z",
"event_ulid": "{ULID}"
}
{
"id": "{GUID}",
"qty": 0.12,
"price": null,
"status": "executed",
"symbol": "ICNP",
"cusip": "450958202",
"entry_type": "DIV",
"net_amount": 0,
"description": "Stock DIV @ 1.12, Pos QTY: 1, Rec Date: 2024-08-26",
"settle_date": "2024-08-26",
"system_date": "2024-11-22",
"entry_sub_type": "SDIV",
"per_share_amount": 1.12,
"account_id": "{ACCID}",
"at": "2024-11-22T07:43:57.279Z",
"event_ulid": "{ULID}" 
}
{
"id": "{GUID}",
"qty": 0,
"price": null,
"status": "executed",
"symbol": "ALE",
"cusip": "018522300",
"entry_type": "DIVNRA",
"net_amount": -0.3,
"description": "DIV tax withholding on $1.2 at 25% for tax country IND; w8w9: w8",
"settle_date": "2024-11-29",
"system_date": "2024-12-02",
"per_share_amount": null,
"account_id": "{ACCID}",
"at": "2024-12-02T08:01:06.529338Z",
"event_ulid": "{ULID}"
}
# Reverse SPLIT
{
"id": "{GUID}",
"qty": -0.29194239,
"price": 5.138,
"status": "executed",
"symbol": "FTCI",
"cusip": "30320C103",
"entry_type": "SPLIT",
"net_amount": 0,
"description": "REMOVE, From QTY:-0.29194239, To QTY:0.029194239, Position Value:1.5",
"settle_date": "2024-12-02",
"system_date": "2024-12-02",
"entry_sub_type": "RSPLIT",
"per_share_amount": null,
"account_id": "{ACCID}",
"at": "2024-12-01T22:30:42.997Z",
"event_ulid": "{ULID}"
}
{
"id": "{GUID}",
"qty": 0.029194239,
"price": 51.38,
"status": "executed",
"symbol": "FTCI",
"cusip": "30320C301",
"entry_type": "SPLIT",
"net_amount": 0,
"description": "ADD, From QTY:-0.29194239, To QTY:0.029194239, Position Value:1.5",
"settle_date": "2024-12-02",
"system_date": "2024-12-02",
"entry_sub_type": "RSPLIT",
"per_share_amount": null,
"account_id": "{ACCID}",
"at": "2024-12-01T22:33:41.647Z",
"event_ulid": "{ULID}"
}
# Forward SPLIT
{
"id": "{GUID}",
"qty": -0.000807009,
"price": 102.428,
"status": "executed",
"symbol": "ANET",
"cusip": "040413106",
"entry_type": "SPLIT",
"net_amount": 0,
"description": "REMOVE, From QTY:-0.000807009, To QTY:0.003228036, Position Value:0.08",
"settle_date": "2024-12-04",
"system_date": "2024-12-04",
"entry_sub_type": "FSPLIT",
"per_share_amount": null,
"account_id": "{ACCID}",
"at": "2024-12-03T23:27:03.971Z",
"event_ulid": "{ULID}"
}
{
"id": "{GUID}",
"qty": 0.003228036,
"price": 25.607,
"status": "executed",
"symbol": "ANET",
"cusip": "040413205",
"entry_type": "SPLIT",
"net_amount": 0,
"description": "ADD, From QTY:-0.000807009, To QTY:0.003228036, Position Value:0.08",
"settle_date": "2024-12-04",
"system_date": "2024-12-04",
"entry_sub_type": "FSPLIT",
"per_share_amount": null,
"account_id": "{ACCID}",
"at": "2024-12-03T23:36:20.775Z",
"event_ulid": "{ULID}"  
}
{
"id": "{GUID}",
"qty": 0.054339042,
"price": 12.8328,
"status": "executed",
"symbol": "CON",
"cusip": "20603L102",
"entry_type": "SPIN",
"net_amount": 0,
"description": "Target Symbol: CON, Initiating Symbol: SEM, 0.806971 CON for each 1 SEM",
"settle_date": "2024-11-26",
"system_date": "2024-11-26",
"per_share_amount": null,
"account_id": "{ACCID}",
"at": "2024-11-26T00:31:04.184Z",
"event_ulid": "{ULID}"
}
{
"id": "{GUID}",
"qty": 0.067337044,
"price": 11.9203,
"status": "executed",
"symbol": "SEM",
"cusip": "81619Q105",
"entry_type": "SPIN",
"net_amount": 0,
"description": "ADD, Cost basis adjustment for source company",
"settle_date": "2024-11-26",
"system_date": "2024-11-26",
"per_share_amount": null,
"account_id": "{ACCID}",
"at": "2024-11-26T08:01:06.529338Z",
"event_ulid": "{ULID}"
}
{
"id": "{GUID}",
"qty": -0.067337044,
"price": 22.276,
"status": "executed",
"symbol": "SEM",
"cusip": "81619Q105",
"entry_type": "SPIN",
"net_amount": 0,
"description": "REMOVE, Cost basis adjustment for source company",
"settle_date": "2024-11-26",
"system_date": "2024-11-26",
"per_share_amount": null,
"account_id": "{ACCID}",
"at": "2024-11-26T08:01:06.529338Z",
"event_ulid": "{ULID}"
}
{
"id": "{GUID}",
"qty": -2,
"price": 5.88,
"status": "executed",
"symbol": "HIE",
"cusip": "600379101",
"entry_type": "MA",
"net_amount": 0,
"description": "Cash Merger $12.6341694 per share",
"settle_date": "2024-11-25",
"system_date": "2024-11-25",
"entry_sub_type": "CMA",
"per_share_amount": null,
"account_id": "{ACCID}",
"at": "2024-11-25T10:59:08.776Z",
"event_ulid": "{ULID}"
}
{
"id": "{GUID}",
"qty": 0,
"price": null,
"status": "executed",
"symbol": "HIE",
"cusip": "600379101",
"entry_type": "MA",
"net_amount": 25.27,
"description": "Cash Merger $12.6341694 per share",
"settle_date": "2024-11-25",
"system_date": "2024-11-25",
"entry_sub_type": "CMA",
"per_share_amount": null,
"account_id": "{ACCID}",
"at": "2024-11-25T10:59:08.776Z",
"event_ulid": "{ULID}"
}
{
"id": "{GUID}",
"qty": -0.716836558,
"price": 24.1617,
"status": "executed",
"symbol": "MRO",
"cusip": "718507106",
"entry_type": "MA",
"net_amount": 0,
"description": "Stock Merger 0.255 COP for 1 MRO",
"settle_date": "2024-11-22",
"system_date": "2024-11-22",
"entry_sub_type": "SMA",
"per_share_amount": null,
"account_id": "{ACCID}",
"at": "2024-11-21T23:16:27.145Z",
"event_ulid": "{ULID}"
}
{
"id": "{GUID}",
"qty": 0.182793322,
"price": 94.7518,
"status": "executed",
"symbol": "COP",
"cusip": "912656105",
"entry_type": "MA",
"net_amount": 0,
"description": "Stock Merger 0.255 COP for 1 MRO",
"settle_date": "2024-11-22",
"system_date": "2024-11-22",
"entry_sub_type": "SMA",
"per_share_amount": null,
"account_id": "{ACCID}",
"at": "2024-11-21T23:17:07.588Z",
"event_ulid": "{ULID}"
}
# Removal of old shares
{
"id": "{GUID}",
"qty": -6.522449746,
"price": 9.4663,
"status": "executed",
"symbol": "PSTX",
"cusip": "73730P108",
"entry_type": "MA",
"net_amount": 0,
"description": "Stock Cash Merger 1 737CVR019 and $9 for 1 PSTX",
"settle_date": "2025-01-13",
"system_date": "2025-01-13",
"entry_sub_type": "SCMA",
"per_share_amount": null,
"account_id": "{ACCID}",
"at": "2025-01-13T23:01:06.529338Z",
"event_ulid": "{ULID}"
}
# Allocation of new shares
{
"id": "{GUID}",
"qty": 6.522449746,
"price": 0.4663,
"status": "executed",
"symbol": "737CVR019",
"cusip": "737CVR019",
"entry_type": "MA",
"net_amount": 0,
"description": "Stock Cash Merger 1 737CVR019 and $9 for 1 PSTX",
"settle_date": "2025-01-13",
"system_date": "2025-01-13",
"entry_sub_type": "SCMA",
"per_share_amount": null,
"account_id": "{ACCID}",
"at": "2025-01-13T23:01:06.529338Z",
"event_ulid": "{ULID}"
}
# Allocation of cash
{
"id": "{GUID}",
"qty": 0,
"price": null,
"status": "executed",
"symbol": "PSTX",
"cusip": "73730P108",
"entry_type": "MA",
"net_amount": 58.7,
"description": "Stock Cash Merger 1 737CVR019 and $9 for 1 PSTX",
"settle_date": "2025-01-13",
"system_date": "2025-01-13",
"entry_sub_type": "SCMA",
"per_share_amount": null,
"account_id": "{ACCID}",
"at": "2025-01-13T23:01:06.529338Z",
"event_ulid": "{ULID}"
}
{
"id": "{GUID}",
"qty": -8,
"price": null,
"status": "executed",
"symbol": "SRV.RT",
"cusip": "231631128",
"entry_type": "REORG",
"net_amount": 0,
"description": "Worthless Removal - SRV.RT",
"settle_date": "2024-11-27",
"system_date": "2024-11-27",
"per_share_amount": null,
"account_id": "{ACCID}",
"at": "2024-11-26T23:13:33.604Z",
"event_ulid": "{ULID}"
}
{
"id": "{GUID}",
"qty": 0,
"price": null,
"status": "executed",
"symbol": "",
"entry_type": "FEE",
"net_amount": -0.01,
"description": "REG fee for proceed of $15.37 on 2024-12-10 by {ACCOUNT_NUMBER}",
"settle_date": "2024-12-11",
"system_date": "2024-12-10",
"entry_sub_type": "REG",
"per_share_amount": null,
"account_id": "{ACCID}",
"at": "2024-12-10T17:19:17.525338Z",
"event_ulid": "{ULID}"
}
{
"id": "{GUID}",
"qty": 0,
"price": null,
"status": "executed",
"symbol": "",
"entry_type": "FEE",
"net_amount": -0.01,
"description": "TAF fee for proceed of 1.371115174 shares (2 trades) on 2024-12-10 by {ACCOUNT_NUMBER}",
"settle_date": "2024-12-11",
"system_date": "2024-12-10",
"entry_sub_type": "TAF",
"per_share_amount": null,
"account_id": "{ACCID}",
"at": "2024-12-10T17:19:17.525338Z",
"event_ulid": "{ULID}"
}
{
"id": "{GUID}",
"qty": 0,
"price": null,
"status": "executed",
"symbol": "",
"entry_type": "FEE",
"net_amount": -0.17,
"description": "ORF fee for proceed of 6 contracts on 2024-06-18 by 399748018",
"settle_date": "2024-06-18",
"system_date": "2024-06-18",
"per_share_amount": null,
"account_id": "{ACCID}",
"at": "2024-06-18T08:01:06.529338Z",
"event_ulid": "{ULID}"
}
{
"id": "{GUID}",
"qty": 0,
"price": null,
"status": "executed",
"symbol": "",
"entry_type": "FEE",
"net_amount": -0.02,
"description": "OCC Clearing Fee",
"settle_date": "2024-06-18",
"system_date": "2024-06-18",
"execution_id": "{EXID}",
"per_share_amount": null,
"account_id": "{ACCID}",
"at": "2024-06-18T08:01:06.529338Z",
"event_ulid": "{ULID}" 
}
{
"id": "{GUID}",
"qty": 0,
"price": null,
"status": "executed",
"symbol": "",
"entry_type": "FEE",
"net_amount": 0.05,
"description": "2024-11-27 Non-Retail - Exchange Fees/Rebates",
"settle_date": "2024-11-29",
"system_date": "2024-11-29",
"entry_sub_type": "NRV",
"per_share_amount": null,
"account_id": "{ACCID}",
"at": "2024-11-29T08:01:06.529338Z",
"event_ulid": "{ULID}" 
}
{
"id": "{GUID}",
"qty": 1341,
"price": 0.0025,
"status": "executed",
"symbol": "",
"entry_type": "FEE",
"net_amount": -3.35,
"description": "2024-11-27 Non-Retail - Alpaca Trading Fee",
"settle_date": "2024-11-29",
"system_date": "2024-11-29",
"entry_sub_type": "NRC",
"per_share_amount": null,
"account_id": "{ACCID}",
"at": "2024-11-29T08:01:06.529338Z",
"event_ulid": "{ULID}" 
}
{
"id": "{GUID}",
"qty": 0,
"price": null,
"status": "executed",
"symbol": "",
"swap_rate": 143.6265,
"entry_type": "FEE",
"net_amount": -1,
"description": "Swap Fee Gross Income",
"settle_date": "2024-10-02",
"system_date": "2024-10-01",
"execution_id": "{EXEC ID}",
"entry_sub_type": "LCT",
"per_share_amount": null,
"account_id": "{ACCID}",
"at": "2023-08-01T08:01:06.529338Z",
"event_ulid": "{ULID}"
}
{
"id": "{GUID}",
"qty": 0,
"price": null,
"status": "executed",
"symbol": "",
"entry_type": "CSD",
"net_amount": 100,
"description": "",
"settle_date": "2024-03-11",
"system_date": "2024-03-11",
"per_share_amount": null,
"account_id": "{ACCID}",
"at": "2024-03-11T08:01:06.529338Z",
"event_ulid": "{ULID}"
}
{
"id": "{GUID}",
"qty": 0,
"price": null,
"status": "executed",
"symbol": "",
"entry_type": "CSW",
"net_amount": -32.97,
"description": "type: ach, subtype: none, statement_id: 4f0cfc49-0395-475c-b8ca-3586e394d256, direction: OUTGOING",
"settle_date": "2024-09-20",
"system_date": "2024-09-20",
"account_id": "{ACCID}",
"event_ulid": "{ULID}",
"at": "2024-09-20T08:01:06.529338Z",
"per_share_amount": null
}
# Symbol Name Change (SNC)
{
"id": "{GUID}",
"qty": -1.25,
"price": 9.99,
"status": "executed",
"symbol": "YTEN",
"cusip": "591018809",
"entry_type": "NC",
"net_amount": 0,
"description": "Name Change from YTEN to YTENQ",
"settle_date": "2024-12-10",
"system_date": "2024-12-10",
"entry_sub_type": "SNC",
"per_share_amount": null,
"account_id": "{ACCID}",
"at": "2024-12-09T23:01:06.529338Z",
"event_ulid": "{ULID}"
}
{
"id": "{GUID}",
"qty": 1.25,
"price": 9.99,
"status": "executed",
"symbol": "YTENQ",
"cusip": "591018809",
"entry_type": "NC",
"net_amount": 0,
"description": "Name Change from YTEN to YTENQ",
"settle_date": "2024-12-10",
"system_date": "2024-12-10",
"entry_sub_type": "SNC",
"per_share_amount": null,
"account_id": "{ACCID}",
"at": "2024-12-09T23:01:06.529338Z",
"event_ulid": "{ULID}"
}
# CUSIP Name Change (CNC)
{
"id": "{GUID}",
"qty": -150,
"price": 0.045,
"status": "executed",
"symbol": "RMSGW",
"cusip": "591018809",
"entry_type": "NC",
"net_amount": 0,
"description": "Name Change from RMSGW to RMSGW",
"settle_date": "2024-11-21",
"system_date": "2024-11-21",
"entry_sub_type": "CNC",
"per_share_amount": null,
"account_id": "{ACCID}",
"at": "2024-11-21T00:22:06.529338Z",
"event_ulid": "{ULID}"
}
{
"id": "{GUID}",
"qty": 150,
"price": 0.045,
"status": "executed",
"symbol": "RMSGW",
"cusip": "591018809",
"entry_type": "NC",
"net_amount": 0,
"description": "Name Change from RMSGW to RMSGW",
"settle_date": "2024-11-21",
"system_date": "2024-11-21",
"entry_sub_type": "CNC",
"per_share_amount": null,
"account_id": "{ACCID}",
"at": "2024-11-21T00:22:06.529338Z",
"event_ulid": "{ULID}"
}
# Symbol & CUSIP Name Change (SCNC)
{
"id": "{GUID}",
"qty": -29,
"price": 0.3166,
"status": "executed",
"symbol": "DXFFY",
"cusip": "591018809",
"entry_type": "NC",
"net_amount": 0,
"description": "Name Change from DXFFY to DXFFD",
"settle_date": "2024-12-04",
"system_date": "2024-12-04",
"entry_sub_type": "SCNC",
"per_share_amount": null,
"account_id": "{ACCID}",
"at": "2024-12-03T23:11:06.529338Z",
"event_ulid": "{ULID}"
}
{
"id": "{GUID}",
"qty": 29,
"price": 0.3166,
"status": "executed",
"symbol": "DXFFD",
"cusip": "591018809",
"entry_type": "NC",
"net_amount": 0,
"description": "Name Change from DXFFY to DXFFD",
"settle_date": "2024-12-04",
"system_date": "2024-12-04",
"entry_sub_type": "SCNC",
"per_share_amount": null,
"account_id": "{ACCID}",
"at": "2024-12-03T23:12:06.529338Z",
"event_ulid": "{ULID}"
}
{
"id": "{GUID}",
"qty": 2650,
"price": null,
"status": "executed",
"symbol": "067RGT019",
"cusip": "067RGT019",
"entry_type": "VOF",
"net_amount": 0,
"description": "BNED rights distribution",
"settle_date": "2024-05-17",
"system_date": "2024-05-17",
"per_share_amount": null,
"account_id": "{ACCID}",
"at": "2024-05-17T08:01:06.529338Z",
"event_ulid": "{ULID}"
}
{
"id": "{GUID}", 
"qty": -2500, 
"price": null, 
"status": "executed", 
"symbol": "067RGT019", 
"cusip": "067RGT019",
"entry_type": "VOF", 
"net_amount": 0, 
"description": "Rights Exercise (symbol BNED; expiration 06/05/24)", 
"settle_date": "2024-06-05", 
"system_date": "2024-06-05", 
"per_share_amount": null,
"account_id": "{ACCID}",
"at": "2024-06-05T08:01:06.529338Z",
"event_ulid": "{ULID}"
}
{
"id": "{GUID}",
"qty": 0,
"price": null,
"status": "pending",
"symbol": "",
"entry_type": "JNLC",
"net_amount": -0.29,
"description": "Journal ID: {Journal ID}",
"settle_date": "2024-05-17",
"system_date": "2024-05-17",
"per_share_amount": null,
"account_id": "{ACCID}",
"at": "2024-05-17T08:01:06.529338Z",
"event_ulid": "{ULID}"
}
{
"id": "{GUID}",
"qty": -0.008611,
"price": 993,
"status": "executed",
"symbol": "TSLA",
"cusip": "88160R101",
"entry_type": "JNLS",
"net_amount": 0,
"description": "ID: {ACCID} - {ACCID}",
"settle_date": "2023-07-18",
"system_date": "2023-07-18",
"per_share_amount": null,
"account_id": "{ACCID}",
"at": "2023-07-18T08:01:06.529338Z",
"event_ulid": "{ULID}"
}
{
"id": "{GUID}",
"qty": -300,
"price": 21.5,
"status": "executed",
"symbol": "HOOD",
"entry_type": "OPTRD",
"net_amount": 6450,
"description": "Options Trade",
"settle_date": "2024-06-17",
"system_date": "2024-06-17",
"per_share_amount": null,
"account_id": "{ACCID}",
"at": "2024-06-17T08:01:06.529338Z",
"event_ulid": "{ULID}"
}
{
"id": "{GUID}",
"qty": 1,
"price": null,
"status": "executed",
"symbol": "HOOD240614P00021500",
"entry_type": "OPEXP",
"net_amount": 0,
"description": "Options Expiry",
"settle_date": "2024-06-17",
"system_date": "2024-06-17",
"per_share_amount": null,
"account_id": "{ACCID}",
"at": "2024-06-17T08:01:06.529338Z",
"event_ulid": "{ULID}"
}
{
"id": "{GUID}",
"qty": 3,
"price": null,
"status": "executed",
"symbol": "HOOD240614C00021500",
"entry_type": "OPASN",
"net_amount": 0,
"description": "",
"settle_date": "2024-06-17",
"system_date": "2024-06-17",
"per_share_amount": null,
"account_id": "{ACCID}",
"at": "2024-06-17T08:01:06.529338Z",
"event_ulid": "{ULID}"
}
{
"id": "{GUID}",
"qty": -1,
"price": null,
"status": "executed",
"symbol": "AAPL240614C00202500",
"entry_type": "OPEXC",
"net_amount": 0,
"description": "Options Exercise",
"settle_date": "2024-05-17",
"system_date": "2024-05-17",
"per_share_amount": null,
"account_id": "{ACCID}",
"at": "2024-05-17T08:01:06.529338Z",
"event_ulid": "{ULID}"
}
{
"id": "{GUID}",
"qty": 0,
"price": null,
"status": "executed",
"symbol": "",
"entry_type": "INT",
"net_amount": -0.02,
"description": "Monthly Int - {Month} {Year}",
"settle_date": "2023-07-31",
"system_date": "2023-08-01",
"per_share_amount": null,
"account_id": "{ACCID}",
"at": "2023-08-01T08:01:06.529338Z",
"event_ulid": "{ULID}"
}
{
"id": "{GUID}",
"qty": 0,
"price": null,
"status": "executed",
"symbol": "",
"swap_rate": 1,
"entry_type": "ACATC",
"net_amount": 5,
"description": "",
"settle_date": "2024-05-17",
"system_date": "2024-05-17",
"per_share_amount": null,
"account_id": "{ACCID}",
"at": "2024-05-17T08:01:06.529338Z",
"event_ulid": "{ULID}"
}
{
"id": "{GUID}",
"qty": 6,
"price": 135.34,
"status": "executed",
"symbol": "NVDA",
"cusip": "67066G104",
"entry_type": "ACATS",
"net_amount": 0,
"description": "DTC TRANSFER",
"settle_date": "2024-12-02",
"system_date": "2024-12-02",
"per_share_amount": null,
"account_id": "{ACCID}",
"at": "2024-12-02T08:01:06.529338Z",
"event_ulid": "{ULID}"
}
{
"id": "{GUID}",
"qty": 0,
"price": null,
"status": "executed",
"symbol": "",
"entry_type": "INT",
"net_amount": -54.14,
"description": "Monthly Int - SEPTEMBER 2024",
"settle_date": "2024-09-30",
"system_date": "2024-10-01",
"entry_sub_type": "MGN",
"per_share_amount": null,
"account_id": "{ACCID}",
"at": "2023-08-01T08:01:06.529338Z",
"event_ulid": "{ULID}"
}
{
"id": "{GUID}",
"qty": 0,
"price": null,
"status": "executed",
"symbol": "TLT",
"cusip": "464287432",
"entry_type": "INT",
"net_amount": 0.2,
"description": "Qualified interest income reallocation for 2024",
"settle_date": "2024-12-06",
"system_date": "2024-12-06",
"entry_sub_type": "QII",
"per_share_amount": null,
"account_id": "{ACCID}",
"at": "2023-08-01T08:01:06.529338Z",
"event_ulid": "{ULID}"
}
{
"id": "{GUID}",
"qty": 9.25,
"price": null,
"status": "executed",
"symbol": "SWEEPFDIC",
"cusip": "SWEEPFDIC",
"entry_type": "INT",
"net_amount": 0,
"description": "September 2024 Sweep",
"settle_date": "2024-09-30",
"system_date": "2024-09-30",
"entry_sub_type": "SWP",
"per_share_amount": null,
"account_id": "{ACCID}",
"at": "2023-08-01T08:01:06.529338Z",
"event_ulid": "{ULID}"
}
{
"id": "{GUID}",
"qty": 5,
"price": 0.49,
"status": "executed",
"symbol": "F250228P00010000",
"entry_type": "OPCA",
"net_amount": -245,
"description": "REMOVE old contract symbol",
"settle_date": "2025-02-18",
"system_date": "2025-02-18",
"entry_sub_type": "DIV.CDIV",
"per_share_amount": null,
"account_id": "{ACCID}",
"at": "2024-05-17T08:01:06.529338Z",
"event_ulid": "{ULID}"
}
{
"id": "{GUID}",
"qty": -5,
"price": 0.49,
"status": "executed",
"symbol": "F250228P00009850",
"entry_type": "OPCA",
"net_amount": 245,
"description": "ADD new contract symbol",
"settle_date": "2025-02-18",
"system_date": "2025-02-18",
"entry_sub_type": "DIV.CDIV",
"per_share_amount": null,
"account_id": "{ACCID}",
"at": "2024-05-17T08:01:06.529338Z",
"event_ulid": "{ULID}"
}
{
"id": "{GUID}",
"qty": -2,
"price": 1.13,
"status": "executed",
"symbol": "NKLA270115C00000500",
"entry_type": "OPCA",
"net_amount": 226,
"description": "REMOVE old contract symbol",
"settle_date": "2025-02-26",
"system_date": "2025-02-26",
"entry_sub_type": "NC.SNC",
"per_share_amount": null,
"account_id": "{ACCID}",
"at": "2024-05-17T08:01:06.529338Z",
"event_ulid": "{ULID}"
}
{
"id": "{GUID}",
"qty": 2,
"price": 1.13,
"status": "executed",
"symbol": "NKLAQ270115C00000500",
"entry_type": "OPCA",
"net_amount": -226,
"description": "ADD new contract symbol",
"settle_date": "2025-02-26",
"system_date": "2025-02-26",
"entry_sub_type": "NC.SNC",
"per_share_amount": null,
"account_id": "{ACCID}",
"at": "2024-05-17T08:01:06.529338Z",
"event_ulid": "{ULID}"
}
{
"id": "{GUID}",
"qty": -15,
"price": 0.08,
"status": "executed",
"symbol": "WKHS250417C00002000",
"entry_type": "OPCA",
"net_amount": 120,
"description": "REMOVE old contract symbol",
"settle_date": "2025-03-17",
"system_date": "2025-03-17",
"entry_sub_type": "SPLIT.RSPLIT",
"per_share_amount": null,
"account_id": "{ACCID}",
"at": "2024-05-17T08:01:06.529338Z",
"event_ulid": "{ULID}"
}
{
"id": "{GUID}",
"qty": 15,
"price": 0.08,
"status": "executed",
"symbol": "WKHS2250417C00002000",
"entry_type": "OPCA",
"net_amount": -120,
"description": "ADD new contract symbol",
"settle_date": "2025-03-17",
"system_date": "2025-03-17",
"entry_sub_type": "SPLIT.RSPLIT",
"per_share_amount": null,
"account_id": "{ACCID}",
"at": "2024-05-17T08:01:06.529338Z",
"event_ulid": "{ULID}"
}
{
"id": "{GUID}",
"qty": -1,
"price": 10.5,
"status": "executed",
"symbol": "LRCX241115C00950000",
"entry_type": "OPCA",
"net_amount": 1050,
"description": "REMOVE old contract symbol",
"settle_date": "2024-10-03",
"system_date": "2024-10-03",
"entry_sub_type": "SPLIT.FSPLIT",
"per_share_amount": null,
"account_id": "{ACCID}",
"at": "2024-05-17T08:01:06.529338Z",
"event_ulid": "{ULID}"
}
{
"id": "{GUID}",
"qty": 10,
"price": 1.05,
"status": "executed",
"symbol": "LRCX241115C00095000",
"entry_type": "OPCA",
"net_amount": -1050,
"description": "ADD new contract symbol",
"settle_date": "2024-10-03",
"system_date": "2024-10-03",
"entry_sub_type": "SPLIT.FSPLIT",
"per_share_amount": null,
"account_id": "{ACCID}",
"at": "2024-05-17T08:01:06.529338Z",
"event_ulid": "{ULID}"
}
{
"id": "{GUID}",
"qty": 2,
"price": 0.65,
"status": "executed",
"symbol": "CEIX250117P00095000",
"entry_type": "OPCA",
"net_amount": -130,
"description": "REMOVE old contract symbol",
"settle_date": "2025-01-15",
"system_date": "2025-01-15",
"entry_sub_type": "MA.SMA",
"per_share_amount": null,
"account_id": "{ACCID}",
"at": "2024-05-17T08:01:06.529338Z",
"event_ulid": "{ULID}"
}
{
"id": "{GUID}",
"qty": -2,
"price": 0.65,
"status": "executed",
"symbol": "CNR1250117P00095000",
"entry_type": "OPCA",
"net_amount": 130,
"description": "ADD new contract symbol",
"settle_date": "2025-01-15",
"system_date": "2025-01-15",
"entry_sub_type": "MA.SMA",
"per_share_amount": null,
"account_id": "{ACCID}",
"at": "2024-05-17T08:01:06.529338Z",
"event_ulid": "{ULID}"
}
{
"id": "{GUID}",
"qty": -1,
"price": 0.24,
"status": "executed",
"symbol": "CMPO250417C00020000",
"entry_type": "OPCA",
"net_amount": 24,
"description": "REMOVE old contract symbol",
"settle_date": "2025-02-28",
"system_date": "2025-02-28",
"entry_sub_type": "SPIN",
"per_share_amount": null,
"account_id": "{ACCID}",
"at": "2024-05-17T08:01:06.529338Z",
"event_ulid": "{ULID}"
}
{
"id": "{GUID}",
"qty": 1,
"price": 0.24,
"status": "executed",
"symbol": "CMPO1250417C00020000",
"entry_type": "OPCA",
"net_amount": -24,
"description": "ADD new contract symbol",
"settle_date": "2025-02-28",
"system_date": "2025-02-28",
"entry_sub_type": "SPIN",
"per_share_amount": null,
"account_id": "{ACCID}",
"at": "2024-05-17T08:01:06.529338Z",
"event_ulid": "{ULID}"
}
{
"id": "{GUID}",
"qty": 1,
"price": 23.75,
"status": "executed",
"symbol": "PLTR261218C00120000",
"entry_type": "ACATS",
"net_amount": 0,
"description": "ACAT Transfer 20250500034276",
"settle_date": "2025-02-27",
"system_date": "2025-02-27",
"per_share_amount": null,
"account_id": "{ACCID}",
"at": "2025-02-27T08:01:06.529338Z",
"event_ulid": "{ULID}"
}
__Updated 23 days ago
* * *
