---
title: Estimate an Order
source: reference\get-v1-trading-accounts-account_id-orders-estimation.html
---

post https://broker-api.sandbox.alpaca.markets/v1/trading/accounts/{account_id}/orders/estimation
Order estimation endpoint will display, based on user’s account balance, the estimated quantity and price they will receive for their notional order.
For LCT - customer’s order will include the Alpaca swap_fee, while correspondent side swap_fee is configurable in the API call. Utilising this API does not result in a real order and after the calculation - the user’s buying power reverts to the previous state.
Responses and Errors are the same as with the Orders API
Please note that the estimation is based on the market condition at the time of submission and a live order will differ. The output should be considered indicative.
**Note:** This does not support Crypto or non-market orders at this time.
