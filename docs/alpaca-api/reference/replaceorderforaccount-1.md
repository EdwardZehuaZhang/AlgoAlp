---
title: Replace an Order
source: reference\replaceorderforaccount-1.html
---

patch https://broker-api.sandbox.alpaca.markets/v1/trading/accounts/{account_id}/orders/{order_id}
Replaces a single order with updated parameters. Each parameter overrides the corresponding attribute of the existing order. The other attributes remain the same as the existing order.
A success return code from a replaced order does NOT guarantee the existing open order has been replaced. If the existing open order is filled before the replacing (new) order reaches the execution venue, the replacing (new) order is rejected, and these events are sent in the trade_updates stream channel found [here](subscribetotradev2sse.md).
While an order is being replaced, the account's buying power is reduced by the larger of the two orders that have been placed (the old order being replaced, and the newly placed order to replace it). If you are replacing a buy entry order with a higher limit price than the original order, the buying power is calculated based on the newly placed order. If you are replacing it with a lower limit price, the buying power is calculated based on the old order.
Note: Order cannot be replaced when the status is `accepted`, `pending_new`, `pending_cancel` or `pending_replace`.
