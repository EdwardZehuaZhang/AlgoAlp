---
title: Top market movers
source: reference\movers-1.html
---

get https://data.alpaca.markets/v1beta1/screener/{market_type}/movers
Returns the top market movers (gainers and losers) based on real time SIP data.  
The change for each symbol is calculated from the previous closing price and the latest closing price.
For stocks, the endpoint resets at market open. Until then, it shows the previous market day's movers.  
The data is split-adjusted. Only tradable symbols in exchanges are included.
For crypto, the endpoint resets at midnight.
