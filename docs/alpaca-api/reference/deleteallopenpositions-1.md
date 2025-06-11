---
title: Close All Positions
source: reference\deleteallopenpositions-1.html
---

delete https://paper-api.alpaca.markets/v2/positions
Closes (liquidates) all of the account’s open long and short positions. A response will be provided for each order that is attempted to be cancelled. If an order is no longer cancelable, the server will respond with status 500 and reject the request.
