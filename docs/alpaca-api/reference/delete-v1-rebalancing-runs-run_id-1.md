---
title: Cancel Run by ID
source: reference\delete-v1-rebalancing-runs-run_id-1.html
---

delete https://broker-api.sandbox.alpaca.markets/v1/rebalancing/runs/{run_id}
Cancels a run. Only runs within certain statuses (QUEUED, CANCELED, SELLS_IN_PROGRESS, BUYS_IN_PROGRESS) are cancelable. If this endpoint is called after orders have been submitted, we’ll attempt to cancel the orders.
