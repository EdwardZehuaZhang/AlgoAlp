---
title: Local Currency Trading (LCT)
source: docs\local-currency-trading-lct.html
---

API responses are all in your local currency, with all calculations handled by Alpaca.
Further below, we will examine the some common scenarios with LCT. The recurring theme you will notice is that many of Alpaca’s API commands are almost the same, it is just the response that have changed. In some cases, barring the introduction of a currency specification or a swap rate, the only indication of the trade being in Local Currency is the inclusion of a USD second order JSON.
For further questions about LCT, such as supported currencies or any other relevant details, see [LCT FAQs](https://alpaca.markets/support/local-currency-trading-faq).
# 
Supported Features
[](local-currency-trading-lct.html#supported-features)
Features| LCT| Broker API (USD)  
---|---|---  
Allows trading in user's/broker local currency of US equities| ✅| ⛔️  
Supports JIT| ✅| ✅  
Stop and Limit orders with Extended-Hours| ✅| ✅  
Swap rate on the orders endpoint| ✅| ⛔️  
Supports crypto trading| ⛔️| ✅  
Market Data| ✅ (in local currency)| ⛔️  
Omnibus| ✅| ✅  
Omnibus in subledger| ✅| ✅  
Fully-disclosed account type| ✅| ✅  
SSE Events| ✅| ✅  
Rebalancing| ⛔️| ✅  
Margin Trading| ⛔️| ✅  
# 
Get Market Data
[](local-currency-trading-lct.html#get-market-data)
With LCT, we have introduced a currency parameter for stock market data. You can request pricing data for any equity and we will handle the necessary conversions to quote the asset in the requested local currency.
The example below shows how to get pricing data for AAPL in JPY. The pricing information is converted from USD to the relevant local currency on the fly with the latest FX rate at the point in time of query.
cURL
curl --request GET 'https://data.alpaca.markets/v2/stocks/AAPL/bars?start=2024-08-01T0:00:00Z&end=2024-08-19T11:00:00Z&timeframe=1Min&currency=JPY'
JSON
{
"bars": [
{
"c": 33481.21,
"h": 33536.65,
"l": 33476.71,
"n": 129,
"o": 33536.65,
"t": "2024-08-01T08:00:00Z",
"v": 2750,
"vw": 33519.41
},
...
],
"currency": "JPY",
"next_page_token": "QUFQTHxNfDE3MjI1OTg1NjAwMDAwMDAwMDA=",
"symbol": "AAPL"
}
Note currency key value is `JPY`. Request the same endpoint without the `currency` parameter to compare the pricing data against its `USD` equivalent.
# 
Create an LCT Account
[](local-currency-trading-lct.html#create-an-lct-account)
For LCT, you can leverage the traditional [Accounts API](..-reference-getallaccounts.md) to create any of the following account types:
* Fully Disclosed
* Omnibus
* Omnibus via the Alpaca Sub Ledger Solution
Below we provide an example of creating a account for a fully-disclosed setup with JPY as the local currency.
JSON
{
"contact": {
"email_address": "[[email protected]](../cdn-cgi/l/email-protection.html)",
"phone_number": "555-666-7788",
"street_address": ["20 N San Mateo Dr"],
"city": "San Mateo",
"state": "CA",
"postal_code": "94401",
"country": "USA"
},
"identity": {
"given_name": "John",
"family_name": "Doe",
"date_of_birth": "1990-01-01",
"tax_id": "666-55-4321",
"tax_id_type": "USA_SSN",
"country_of_citizenship": "USA",
"country_of_birth": "USA",
"country_of_tax_residence": "USA",
"funding_source": ["employment_income"],
"annual_income_min": "30000",
"annual_income_max": "50000",
"liquid_net_worth_min": "100000",
"liquid_net_worth_max": "150000"
},
"disclosures": {
"is_control_person": false,
"is_affiliated_exchange_or_finra": false,
"is_politically_exposed": false,
"immediate_family_exposed": false
},
"agreements": [
{
"agreement": "customer_agreement",
"signed_at": "2020-09-11T18:13:44Z",
"ip_address": "185.13.21.99",
"revision": "19.2022.02"
},
{
"agreement": "crypto_agreement",
"signed_at": "2020-09-11T18:13:44Z",
"ip_address": "185.13.21.99",
"revision": "04.2021.10"
}
],
"documents": [
{
"document_type": "identity_verification",
"document_sub_type": "passport",
"content": "/9j/Cg==",
"mime_type": "image/jpeg"
}
],
"trusted_contact": {
"given_name": "Jane",
"family_name": "Doe",
"email_address": "[[email protected]](../cdn-cgi/l/email-protection.html)"
},
"currency": "JPY"
}
Note the newly introduced `currency` parameter as part of the payload to create a new code.
# 
Fund LCT Account
[](local-currency-trading-lct.html#fund-lct-account)
Accounts can be funded for LCT by either:
* Bank Wire
* Just in Time Cash
* Just In Time
The below example funds one of our JPY accounts created above, with JIT API `POST /v1/transfers/jit/transactions` with the following body:
JSON
{
"account_id": "27529bc0-3ab5-34f5-ac29-54a98162472d",
"entry_type": "JTD",
"currency": "JPY",
"amount": "500000",
"description": "Test JIT JPY"
}
Calling the above mentioned API yields the following response,
JSON
{
"id": "9a0ab8c2-4575-46b6-a6cc-f280c899b756",
"account_id": "27529bc0-3ab5-34f5-ac29-54a98162472d",
"created_at": "2022-08-31T16:29:44-04:00",
"system_date": "2022-08-31",
"entry_type": "JTD",
"amount": "500000",
"currency": "JPY",
"description": "Test JIT JPY"
}
# 
Estimate Stock Order
[](local-currency-trading-lct.html#estimate-stock-order)
Customers using LCT for the first time may not be sure how much their local currency can buy of a US stock. To address this pain point we created the [Order Estimation Endpoint](..-reference-get-v1-trading-accounts-account_id-orders-estimation.md). The customer can enter:
* the security
* the notional value
* on the developer side you can input your swap rate to return the realistic value that your customer will receive.
We get in return indicative quantity, average price and USD value.
JSON
{
"symbol": "AAPL",
"side": "buy",
"type": "market",
"time_in_force": "day",
"notional": "4000",
"swap_fee_bps": 100
}
The above payload will get an estimation for a market order to purchase AAPL stock with a notional amount of 4000 JPY.
JSON
{
"id": "2f88dc2f-b9d8-4d52-aa35-fa8e076be3a3",
"client_order_id": "8cfc4159-1e07-438b-bdda-1d37a0176bc7",
"created_at": "2024-08-20T09:58:57.119084817Z",
"updated_at": "2024-08-20T09:58:57.137113377Z",
"submitted_at": "2024-08-20T09:58:57.119084817Z",
"filled_at": "2024-08-20T09:58:57.119084817Z",
"expired_at": null,
"canceled_at": null,
"failed_at": null,
"replaced_at": null,
"replaced_by": null,
"replaces": null,
"asset_id": "b0b6dd9d-8b9b-48a9-ba46-b9d54906e415",
"symbol": "AAPL",
"asset_class": "us_equity",
"notional": "4000",
"qty": null,
"filled_qty": "0.1189",
"filled_avg_price": "33109.4937825",
"order_class": "",
"order_type": "market",
"type": "market",
"side": "buy",
"position_intent": "buy_to_open",
"time_in_force": "day",
"limit_price": null,
"stop_price": null,
"status": "filled",
"extended_hours": false,
"legs": null,
"trail_percent": null,
"trail_price": null,
"hwm": null,
"commission": "0",
"swap_rate": "146.4795",
"swap_fee_bps": "150",
"subtag": null,
"source": null,
"usd": {
"notional": "27.3075",
"filled_avg_price": "226.035",
"limit_price": null,
"stop_price": null
}
}
Note the `usd` object at the bottom.
# 
Submit Order
[](local-currency-trading-lct.html#submit-order)
Alpaca currently supports LCT trading for market, limit, stop & stop limit orders with a **time in force=Day** , accommodating both fractional quantities and notional values. You can pass either a fractional amount (qty), or a notional value (notional) in your local currency in any POST/v2/orders request. Note that entering a value for either parameters, will automatically nullify the other. If both qty and notional are entered the request will be rejected with an error status 400.
Moreover, we support fractional shares trading not only during standard market hours, but extending into pre-market (4:00 a.m. - 9:30 a.m. ET) and post-market (4:00 p.m. - 8:00 p.m. ET) hours, offering global investors the ability to trade during the full extended hours session.
## 
Submit a Stock Market Order
[](local-currency-trading-lct.html#submit-a-stock-market-order)
Once having estimated a given order, we can actually commit to and execute the order using the usual [Orders API](..-reference-createorderforaccount-1.md).
We note here a few key LCT specific order attributes:
* `swap_fee_bps` \- this is the correspondent spread. You as the correspondent can increase or decrease this as you require. **Note: Alpaca will have a separate spread**
* Quantity-based orders will also be accepted
NotionalQuantity
{
"side": "buy",
"type": "market",
"time_in_force": "day",
"commission_type": "notional",
"symbol": "AAPL",
"notional": "4000",
"swap_fee_bps": "100"
}
{
"side": "buy",
"type": "market",
"time_in_force": "day",
"commission_type": "notional",
"symbol": "AAPL",
"qty": "1",
"swap_fee_bps": "100"
}
The responses for the purchase of `AAPL` worth 4000 JPY can be seen below,
NotionalQuantity
{
"id": "c02b6a70-4fa1-4906-a6b8-1a6c6acc66c5",
"client_order_id": "c0f1f5b0-9234-4356-89cf-181c9efb54ef",
"created_at": "2024-08-19T10:25:55.259941759Z",
"updated_at": "2024-08-19T10:25:55.261581339Z",
"submitted_at": "2024-08-19T10:25:55.259941759Z",
"filled_at": null,
"expired_at": null,
"canceled_at": null,
"failed_at": null,
"replaced_at": null,
"replaced_by": null,
"replaces": null,
"asset_id": "b0b6dd9d-8b9b-48a9-ba46-b9d54906e415",
"symbol": "AAPL",
"asset_class": "us_equity",
"notional": "4000",
"qty": null,
"filled_qty": "0",
"filled_avg_price": null,
"order_class": "",
"order_type": "market",
"type": "market",
"side": "buy",
"position_intent": "buy_to_open",
"time_in_force": "day",
"limit_price": null,
"stop_price": null,
"status": "accepted",
"extended_hours": false,
"legs": null,
"trail_percent": null,
"trail_price": null,
"hwm": null,
"commission": "0",
"commission_type": "notional",
"swap_rate": "146.4085",
"swap_fee_bps": "150",
"subtag": null,
"source": null,
"usd": {
"notional": "27.3208",
"filled_avg_price": null,
"limit_price": null,
"stop_price": null
}
}
{
"id": "eafe73ef-107f-40fc-9fed-75bc1b3f145f",
"client_order_id": "7f31aa39-fabd-4d35-a1dd-a0db3fd2ca0b",
"created_at": "2024-08-19T10:27:50.850340619Z",
"updated_at": "2024-08-19T10:27:50.851623759Z",
"submitted_at": "2024-08-19T10:27:50.850340619Z",
"filled_at": null,
"expired_at": null,
"canceled_at": null,
"failed_at": null,
"replaced_at": null,
"replaced_by": null,
"replaces": null,
"asset_id": "b0b6dd9d-8b9b-48a9-ba46-b9d54906e415",
"symbol": "AAPL",
"asset_class": "us_equity",
"notional": null,
"qty": "1",
"filled_qty": "0",
"filled_avg_price": null,
"order_class": "",
"order_type": "market",
"type": "market",
"side": "buy",
"position_intent": "buy_to_open",
"time_in_force": "day",
"limit_price": null,
"stop_price": null,
"status": "accepted",
"extended_hours": false,
"legs": null,
"trail_percent": null,
"trail_price": null,
"hwm": null,
"commission": "0",
"commission_type": "notional",
"swap_rate": "146.4515",
"swap_fee_bps": "150",
"subtag": null,
"source": null,
"usd": {
"notional": null,
"filled_avg_price": null,
"limit_price": null,
"stop_price": null
}
}
## 
Submit a Stock Limit Order
[](local-currency-trading-lct.html#submit-a-stock-limit-order)
We note here a few key LCT specific order attributes:
* `limit_price` field in the request payload is in USD currency while in the response payload it is in local currency.
* `swap_fee_bps` \- this is the correspondent spread. You as the correspondent can increase or decrease this as you require. **Note: Alpaca will have a separate spread**
* Quantity-based orders will also be accepted
* Extended-Hours orders will also be accepted
NotionalQuantityNotional Extended-HoursQuantity Extended-Hours
{
"side": "buy",
"type": "limit",
"time_in_force": "day",
"commission_type": "notional",
"notional": "4000",
"symbol": "AAPL",
"limit_price": "226",
"swap_fee_bps": "100"
}
{
"side": "buy",
"type": "limit",
"time_in_force": "day",
"commission_type": "notional",
"symbol": "AAPL",
"limit_price": "226",
"swap_fee_bps": "100",
"qty": "1"
}
{
"side": "buy",
"type": "limit",
"time_in_force": "day",
"commission_type": "notional",
"notional": "4000",
"symbol": "AAPL",
"limit_price": "226",
"swap_fee_bps": "100",
"extended_hours": true
}
{
"side": "buy",
"type": "limit",
"time_in_force": "day",
"commission_type": "notional",
"symbol": "AAPL",
"limit_price": "226",
"swap_fee_bps": "100",
"qty": "1",
"extended_hours": true
}
The responses for the purchase of `AAPL` worth 4000 JPY can be seen below,
NotionalQuantityNotional Extended-HoursQuantity Extended-Hours
{
"id": "49a5badc-a480-4d56-a765-71808c970885",
"client_order_id": "78f3d279-c8bd-41ea-9e6e-3b76846f8b22",
"created_at": "2024-08-19T10:52:35.927390475Z",
"updated_at": "2024-08-19T10:52:35.928676035Z",
"submitted_at": "2024-08-19T10:52:35.927390475Z",
"filled_at": null,
"expired_at": null,
"canceled_at": null,
"failed_at": null,
"replaced_at": null,
"replaced_by": null,
"replaces": null,
"asset_id": "b0b6dd9d-8b9b-48a9-ba46-b9d54906e415",
"symbol": "AAPL",
"asset_class": "us_equity",
"notional": "4000",
"qty": null,
"filled_qty": "0",
"filled_avg_price": null,
"order_class": "",
"order_type": "limit",
"type": "limit",
"side": "buy",
"position_intent": "buy_to_open",
"time_in_force": "day",
"limit_price": "33387",
"stop_price": null,
"status": "accepted",
"extended_hours": false,
"legs": null,
"trail_percent": null,
"trail_price": null,
"hwm": null,
"commission": "0",
"commission_type": "notional",
"swap_rate": "147.72765",
"swap_fee_bps": "150",
"subtag": null,
"source": null,
"usd": {
"notional": "27.0768",
"filled_avg_price": null,
"limit_price": "226",
"stop_price": null
}
}
{
"id": "f86b3bee-8f40-4951-8805-e489b42bbdff",
"client_order_id": "2db8a272-4948-4416-afb7-d8af74621d51",
"created_at": "2024-08-19T10:54:35.993838801Z",
"updated_at": "2024-08-19T10:54:35.995571381Z",
"submitted_at": "2024-08-19T10:54:35.993838801Z",
"filled_at": null,
"expired_at": null,
"canceled_at": null,
"failed_at": null,
"replaced_at": null,
"replaced_by": null,
"replaces": null,
"asset_id": "b0b6dd9d-8b9b-48a9-ba46-b9d54906e415",
"symbol": "AAPL",
"asset_class": "us_equity",
"notional": null,
"qty": "1",
"filled_qty": "0",
"filled_avg_price": null,
"order_class": "",
"order_type": "limit",
"type": "limit",
"side": "buy",
"position_intent": "buy_to_open",
"time_in_force": "day",
"limit_price": "33389",
"stop_price": null,
"status": "accepted",
"extended_hours": false,
"legs": null,
"trail_percent": null,
"trail_price": null,
"hwm": null,
"commission": "0",
"commission_type": "notional",
"swap_rate": "147.738255",
"swap_fee_bps": "150",
"subtag": null,
"source": null,
"usd": {
"notional": null,
"filled_avg_price": null,
"limit_price": "226",
"stop_price": null
}
}
{
"id": "9562cde5-cb43-49fe-a85e-c8342df2b55e",
"client_order_id": "1d5dc589-9566-4f17-b6d9-d0b028bfe16a",
"created_at": "2024-08-19T10:56:03.761481808Z",
"updated_at": "2024-08-19T10:56:03.763734497Z",
"submitted_at": "2024-08-19T10:56:03.761481808Z",
"filled_at": null,
"expired_at": null,
"canceled_at": null,
"failed_at": null,
"replaced_at": null,
"replaced_by": null,
"replaces": null,
"asset_id": "b0b6dd9d-8b9b-48a9-ba46-b9d54906e415",
"symbol": "AAPL",
"asset_class": "us_equity",
"notional": "4000",
"qty": null,
"filled_qty": "0",
"filled_avg_price": null,
"order_class": "",
"order_type": "limit",
"type": "limit",
"side": "buy",
"position_intent": "buy_to_open",
"time_in_force": "day",
"limit_price": "33404",
"stop_price": null,
"status": "pending_new",
"extended_hours": true,
"legs": null,
"trail_percent": null,
"trail_price": null,
"hwm": null,
"commission": "0",
"commission_type": "notional",
"swap_rate": "147.804915",
"swap_fee_bps": "150",
"subtag": null,
"source": null,
"usd": {
"notional": "27.0626",
"filled_avg_price": null,
"limit_price": "226",
"stop_price": null
}
}
{
"id": "89986aad-d019-468f-bbc6-c83abd391f4b",
"client_order_id": "af5236c7-5b3e-44c7-8ef5-2be2a6f921f8",
"created_at": "2024-08-19T10:57:33.6435754Z",
"updated_at": "2024-08-19T10:57:33.64546282Z",
"submitted_at": "2024-08-19T10:57:33.6435754Z",
"filled_at": null,
"expired_at": null,
"canceled_at": null,
"failed_at": null,
"replaced_at": null,
"replaced_by": null,
"replaces": null,
"asset_id": "b0b6dd9d-8b9b-48a9-ba46-b9d54906e415",
"symbol": "AAPL",
"asset_class": "us_equity",
"notional": null,
"qty": "1",
"filled_qty": "0",
"filled_avg_price": null,
"order_class": "",
"order_type": "limit",
"type": "limit",
"side": "buy",
"position_intent": "buy_to_open",
"time_in_force": "day",
"limit_price": "33407",
"stop_price": null,
"status": "pending_new",
"extended_hours": true,
"legs": null,
"trail_percent": null,
"trail_price": null,
"hwm": null,
"commission": "0",
"commission_type": "notional",
"swap_rate": "147.81653",
"swap_fee_bps": "150",
"subtag": null,
"source": null,
"usd": {
"notional": null,
"filled_avg_price": null,
"limit_price": "226",
"stop_price": null
}
}
## 
Submit a Stock Stop Order
[](local-currency-trading-lct.html#submit-a-stock-stop-order)
We note here a few key LCT specific order attributes:
* `stop_price` field in the request payload is in USD currency while in the response payload it is in local currency.
* Stop buy orders are automatically converted into Stop Limit Buy orders for risk protection [Stop Orders Conversion](orders-at-alpaca.html-stop-orders.md).
* `swap_fee_bps` \- this is the correspondent spread. You as the correspondent can increase or decrease this as you require. **Note: Alpaca will have a separate spread**
* Quantity-based orders will also be accepted
NotionalQuantity
{
"side": "buy",
"type": "stop",
"time_in_force": "day",
"commission_type": "notional",
"notional": "4000",
"symbol": "AAPL",
"stop_price": "230"
}
{
"side": "buy",
"type": "stop",
"time_in_force": "day",
"commission_type": "notional",
"symbol": "AAPL",
"stop_price": "230",
"qty": "1"
}
The responses for the purchase of `AAPL` worth 4000 JPY can be seen below,
NotionalQuantity
{
"id": "274361ce-7c05-4ad0-83ed-517603685f17",
"client_order_id": "eb829da0-7c58-4efd-be76-a5707c3548dd",
"created_at": "2024-08-19T11:01:47.400438062Z",
"updated_at": "2024-08-19T11:01:47.402600012Z",
"submitted_at": "2024-08-19T11:01:47.400438062Z",
"filled_at": null,
"expired_at": null,
"canceled_at": null,
"failed_at": null,
"replaced_at": null,
"replaced_by": null,
"replaces": null,
"asset_id": "b0b6dd9d-8b9b-48a9-ba46-b9d54906e415",
"symbol": "AAPL",
"asset_class": "us_equity",
"notional": "4000",
"qty": null,
"filled_qty": "0",
"filled_avg_price": null,
"order_class": "",
"order_type": "stop",
"type": "stop",
"side": "buy",
"position_intent": "buy_to_open",
"time_in_force": "day",
"limit_price": null,
"stop_price": "34001",
"status": "new",
"extended_hours": false,
"legs": null,
"trail_percent": null,
"trail_price": null,
"hwm": null,
"commission": "0",
"commission_type": "notional",
"swap_rate": "147.82663",
"swap_fee_bps": "100",
"subtag": null,
"source": null,
"usd": {
"notional": "27.0587",
"filled_avg_price": null,
"limit_price": "235.75",
"stop_price": "230"
}
}
{
"id": "fb9546aa-9e27-4bfb-b758-5fa23571da56",
"client_order_id": "6da8e54a-568b-4252-bef0-d06c3aabac4e",
"created_at": "2024-08-19T11:05:43.513481595Z",
"updated_at": "2024-08-19T11:05:43.515201354Z",
"submitted_at": "2024-08-19T11:05:43.513481595Z",
"filled_at": null,
"expired_at": null,
"canceled_at": null,
"failed_at": null,
"replaced_at": null,
"replaced_by": null,
"replaces": null,
"asset_id": "b0b6dd9d-8b9b-48a9-ba46-b9d54906e415",
"symbol": "AAPL",
"asset_class": "us_equity",
"notional": null,
"qty": "1",
"filled_qty": "0",
"filled_avg_price": null,
"order_class": "",
"order_type": "stop",
"type": "stop",
"side": "buy",
"position_intent": "buy_to_open",
"time_in_force": "day",
"limit_price": null,
"stop_price": "33983",
"status": "accepted",
"extended_hours": false,
"legs": null,
"trail_percent": null,
"trail_price": null,
"hwm": null,
"commission": "0",
"commission_type": "notional",
"swap_rate": "147.749365",
"swap_fee_bps": "100",
"subtag": null,
"source": null,
"usd": {
"notional": null,
"filled_avg_price": null,
"limit_price": "235.75",
"stop_price": "230"
}
}
## 
Submit a Stock Stop Limit Order
[](local-currency-trading-lct.html#submit-a-stock-stop-limit-order)
We note here a few key LCT specific order attributes:
* `stop_price` field in the request payload is in USD currency while in the response payload it is in local currency.
* `limit_price` field in the request payload is in USD currency while in the response payload it is in local currency.
* `swap_fee_bps` \- this is the correspondent spread. You as the correspondent can increase or decrease this as you require. **Note: Alpaca will have a separate spread**
* Quantity-based orders will also be accepted
NotionalQuantity
{
"side": "buy",
"type": "stop_limit",
"time_in_force": "day",
"commission_type": "notional",
"notional": "4000",
"symbol": "AAPL",
"stop_price": "230",
"limit_price": "235"
}
{
"side": "buy",
"type": "stop_limit",
"time_in_force": "day",
"commission_type": "notional",
"symbol": "AAPL",
"stop_price": "230",
"qty": "1",
"limit_price": "235"
}
The responses for the purchase of `AAPL` worth 4000 JPY can be seen below,
NotionalQuantity
{
"id": "1a643eba-f503-4add-ac55-c605680e17a7",
"client_order_id": "ad4edbad-14dc-4323-ac71-03114945adfd",
"created_at": "2024-08-19T11:36:10.751938789Z",
"updated_at": "2024-08-19T11:36:10.763268199Z",
"submitted_at": "2024-08-19T11:36:10.751938789Z",
"filled_at": null,
"expired_at": null,
"canceled_at": null,
"failed_at": null,
"replaced_at": null,
"replaced_by": null,
"replaces": null,
"asset_id": "b0b6dd9d-8b9b-48a9-ba46-b9d54906e415",
"symbol": "AAPL",
"asset_class": "us_equity",
"notional": "4000",
"qty": null,
"filled_qty": "0",
"filled_avg_price": null,
"order_class": "",
"order_type": "stop_limit",
"type": "stop_limit",
"side": "buy",
"position_intent": "buy_to_open",
"time_in_force": "day",
"limit_price": "34704",
"stop_price": "33966",
"status": "new",
"extended_hours": false,
"legs": null,
"trail_percent": null,
"trail_price": null,
"hwm": null,
"commission": "0",
"commission_type": "notional",
"swap_rate": "147.675635",
"swap_fee_bps": "100",
"subtag": null,
"source": null,
"usd": {
"notional": "27.0863",
"filled_avg_price": null,
"limit_price": "235",
"stop_price": "230"
}
}
{
"id": "b964b06e-fd4f-4650-9658-e4997a8972d0",
"client_order_id": "6d94f717-ea4d-4dc3-bdba-b9aee88b1639",
"created_at": "2024-08-19T11:37:05.102784954Z",
"updated_at": "2024-08-19T11:37:05.105484514Z",
"submitted_at": "2024-08-19T11:37:05.102784954Z",
"filled_at": null,
"expired_at": null,
"canceled_at": null,
"failed_at": null,
"replaced_at": null,
"replaced_by": null,
"replaces": null,
"asset_id": "b0b6dd9d-8b9b-48a9-ba46-b9d54906e415",
"symbol": "AAPL",
"asset_class": "us_equity",
"notional": null,
"qty": "1",
"filled_qty": "0",
"filled_avg_price": null,
"order_class": "",
"order_type": "stop_limit",
"type": "stop_limit",
"side": "buy",
"position_intent": "buy_to_open",
"time_in_force": "day",
"limit_price": "34700",
"stop_price": "33961",
"status": "accepted",
"extended_hours": false,
"legs": null,
"trail_percent": null,
"trail_price": null,
"hwm": null,
"commission": "0",
"commission_type": "notional",
"swap_rate": "147.655435",
"swap_fee_bps": "100",
"subtag": null,
"source": null,
"usd": {
"notional": null,
"filled_avg_price": null,
"limit_price": "235",
"stop_price": "230"
}
}
# 
Get Account Position
[](local-currency-trading-lct.html#get-account-position)
The below position is the `AAPL` stock purchased previously with 4000 JPY.
JSON
[
{
"asset_id": "b0b6dd9d-8b9b-48a9-ba46-b9d54906e415",
"symbol": "AAPL",
"exchange": "NASDAQ",
"asset_class": "us_equity",
"asset_marginable": true,
"qty": "0.1199",
"avg_entry_price": "33001.59760325",
"side": "long",
"market_value": "3957.039656317",
"cost_basis": "3956.89155263",
"unrealized_pl": "0.148103687",
"unrealized_plpc": "0.0000374293015187",
"unrealized_intraday_pl": "0.148103687325",
"unrealized_intraday_plpc": "0.0000374293016008",
"current_price": "33002.83283",
"lastday_price": "33043.76295",
"change_today": "-0.0012386640123866",
"swap_rate": "146.179",
"avg_entry_swap_rate": "146.1745",
"usd": {
"avg_entry_price": "225.7685",
"market_value": "27.069823",
"cost_basis": "27.0696431500022234",
"unrealized_pl": "0.0010131666450037",
"unrealized_plpc": "0.0000374293015187",
"unrealized_intraday_pl": "0.001013166647227",
"unrealized_intraday_plpc": "0.0000374293016008",
"current_price": "225.77",
"lastday_price": "226.05",
"change_today": "-0.0000084736112053"
},
"qty_available": "0.1199"
}
]
# 
Journaling Local Currency
[](local-currency-trading-lct.html#journaling-local-currency)
Journalling in LCT is almost exactly the same as our regular Journals API.
In this example we will journal some JPY between two accounts.
JSON
{
"from_account": "51461a2a-8f98-3aa5-ae51-fad8d03037b3",
"entry_type": "JNLC",
"to_account": "27529bc0-3ab5-34f5-ac29-54a98162472d",
"amount": "3000",
"currency": "JPY",
"description": "Test JPY Journal"
}
and the response
JSON
{
"id": "1717b9c7-f516-4e85-a21b-bbeb7ef7a87a",
"entry_type": "JNLC",
"from_account": "51461a2a-8f98-3aa5-ae51-fad8d03037b3",
"to_account": "27529bc0-3ab5-34f5-ac29-54a98162472d",
"symbol": "",
"qty": null,
"price": "0",
"status": "queued",
"settle_date": null,
"system_date": null,
"net_amount": "4000",
"description": "Test JPY Journal",
"currency": "JPY"
}
__Updated 10 months ago
* * *
