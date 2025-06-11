---
title: Get Account Portfolio History
source: reference\getaccountportfoliohistory-1.html
---

get https://paper-api.alpaca.markets/v2/account/portfolio/history
Returns timeseries data about equity and profit/loss (P/L) of the account in requested timespan.
# 
Usage for equity-traders
[](getaccountportfoliohistory-1.html#usage-for-equity-traders)
By default, for `timeframes` less than 1D, the API returns the data points during market open times, to change this behavior the `intraday_reporting` query can be set to `extended_hours`, to include the premarket and after-hours trading prices.
# 
Usage for crypto-traders
[](getaccountportfoliohistory-1.html#usage-for-crypto-traders)
The API can be used both for crypto and equities trading accounts. By default the API is aiming at the equities trading use-case, however, it can be configured to return data more suited for visualizing crypto portfolios.
For crypto, we recommend setting the following flags:
* `intraday_reporting=continuous` so that 24/7 graphs are returned
* `pnl_reset=no_reset` so that the Profit And Loss calculation is continuous over the given period of time.
The `timeframe` can only be set to less than 1 day, when the requested `period` is less than 30 days.
# 
Profit and loss calculation
[](getaccountportfoliohistory-1.html#profit-and-loss-calculation)
For profit and loss calculation we are using simple profit and loss to calculate the pnl percentage for a given time:
`pnl_pct = equity/base_value-1`
The v2 responses contain the `base_value_asof` field, which indicates which trading day's closing balance is used for the base value. If the `base_value_asof` is omitted from the response that means that the account doesn't have a prior non-zero closing balance. In such cases the base_value will be the earliest returned data point.
# 
Notes
[](getaccountportfoliohistory-1.html#notes)
In the case of `continuous` mode (`intraday_reporting`), the To calculate the equity values we are using the following prices:
* Between 4:00am and 10:00pm on trading days the valuation will be calculated based on the last trade (extended hours and normal hours respectively).
* After 10:00pm, until the next session open the equities will be valued at their official closing price on the primary exchange.
Regardless of the `intraday_reporting`'s value the 1D chart only contains data for days when the market was open.
The v2 engine rounds all the cash values returned to two digits. All percentage values are rounded to 4 digits.
