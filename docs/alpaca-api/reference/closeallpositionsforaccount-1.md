---
title: Close All Positions for an Account
source: reference\closeallpositionsforaccount-1.html
---

delete https://broker-api.sandbox.alpaca.markets/v1/trading/accounts/{account_id}/positions
Closes (liquidates) all of the account’s open long and short positions. A response will be provided for each order that is attempted to be cancelled. If an order is no longer cancelable, the server will respond with status 500 and reject the request.
