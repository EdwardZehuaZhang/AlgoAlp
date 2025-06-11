---
title: Create Portfolio
source: reference\post-v1-rebalancing-portfolios.html
---

post https://broker-api.sandbox.alpaca.markets/v1/rebalancing/portfolios
Creates a portfolio allocation containing securities and/or cash. Having no rebalancing conditions is allowed but the rebalance event would need to be triggered manually. Portfolios created with API may have multiple rebalance_conditions, but only one of type calendar.
