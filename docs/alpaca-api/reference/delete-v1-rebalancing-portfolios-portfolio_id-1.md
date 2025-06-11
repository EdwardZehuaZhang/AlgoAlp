---
title: Inactivate Portfolio By ID
source: reference\delete-v1-rebalancing-portfolios-portfolio_id-1.html
---

delete https://broker-api.sandbox.alpaca.markets/v1/rebalancing/portfolios/{portfolio_id}
Sets a portfolio to “inactive”, so it can be filtered out of the list request. Only permitted if there are no active subscriptions to this portfolio and this portfolio is not a listed in the weights of any active portfolios.
Inactive portfolios cannot be linked in new subscriptions or added as weights to new portfolios.
