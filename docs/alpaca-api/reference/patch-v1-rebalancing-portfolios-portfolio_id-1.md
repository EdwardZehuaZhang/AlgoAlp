---
title: Update Portfolio by ID
source: reference\patch-v1-rebalancing-portfolios-portfolio_id-1.html
---

patch https://broker-api.sandbox.alpaca.markets/v1/rebalancing/portfolios/{portfolio_id}
Updates a portfolio. If weights or conditions are changed, all subscribed accounts will be evaluated for rebalancing at the next opportunity (normal market hours). If a cooldown is active on the portfolio, the rebalancing will occur after the cooldown expired.
