---
title: Create Run (Manual rebalancing event)
source: reference\post-v1-rebalancing-runs.html
---

post https://broker-api.sandbox.alpaca.markets/v1/rebalancing/runs
Manually creates a run.
The determination of a run’s orders and the execution of a run take place during normal market hours
Runs can be initiated either by the system (when the system evaluates the rebalance conditions specified at the portfolio level) or by API call (manual run creation using POST /v1/rebalancing/runs). Runs can be initiated manually outside of the normal market hours but will remain in the QUEUED status until normal market hours
Only 1 run in a non-terminal status is allowed at any time.
Manually executing a run is currently only allowed for accounts who do not have an active subscription.
