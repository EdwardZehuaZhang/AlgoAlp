---
title: Historical Crypto Data
source: docs\historical-crypto-data-1.html
---

This API provides historical market data for crypto. Check the [API Reference](..-reference-cryptobars-1.md) for the detailed descriptions of all the endpoints.
Since Alpaca now executes all crypto orders in its own exchange, the v1beta3 crypto market data endpoints no longer distribute data from other providers, but from Alpaca itself.
> ## 📘
> 
> Crypto bars contain quote mid-prices
> 
> Due to the volatility of some currencies, including lack of trade volume at any given time, we include the quote midpoint prices in the bars to offer a better data experience. If in a bar no trade happens, the volume will be 0, but the prices will be determined by the quote prices.
__Updated about 1 year ago
* * *
