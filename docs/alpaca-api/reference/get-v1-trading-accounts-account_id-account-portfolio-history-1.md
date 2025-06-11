---
title: Get Account Portfolio History
source: reference\get-v1-trading-accounts-account_id-account-portfolio-history-1.html
---

get https://broker-api.sandbox.alpaca.markets/v1/trading/accounts/{account_id}/account/portfolio/history
Returns timeseries data about equity and profit/loss (P/L) of the account in requested timespan.
# 
Usage for equity-traders
[](get-v1-trading-accounts-account_id-account-portfolio-history-1.html#usage-for-equity-traders)
By default, for `timeframes` less than 1D, the API returns the data points during market open times, to change this behavior the `intraday_reporting` query can be set to `extended_hours`, to include the premarket and after-hours trading prices.
Any position changes (splits, JNLS, etc.) happening for an equity position off-session hours are accounted for at the next session open. Crypto position changes are applied immediately.
# 
Usage for crypto-traders
[](get-v1-trading-accounts-account_id-account-portfolio-history-1.html#usage-for-crypto-traders)
The API can be used both for crypto and equities trading accounts. By default the API is aiming at the equities trading use-case, however, it can be configured to return data more suited for visualizing crypto portfolios.
For crypto, we recommend setting the following flags:
* `intraday_reporting=continuous` so that 24/7 graphs are returned
* `pnl_reset=no_reset` so that the Profit And Loss calculation is continuous over the given period of time.
The `timeframe` can only be set to less than 1 day, when the requested `period` is less than 30 days.
# 
Engine versions
[](get-v1-trading-accounts-account_id-account-portfolio-history-1.html#engine-versions)
To address known issues with the portfolio history engine we implemented the [v2 version of the engine](https://alpaca.markets/learn/introducing-the-new-portfolio-history-endpoint-at-alpaca/).
The only change compared to the `v1` version, that can be considered a semantically breaking change is that the `v2` engine accounts for any Non Trade Activity (NTA) happened during the day at exactly at the time it happend in the intraday (`timeframe` < 1D) graphs. The `v1` version accounted for those NTAs at the end of the day, thus if a workaround is in place to apply those NTAs during the day, that logic should be disabled before migrating to the `v2` version.
To provide an easy upgrade path for our broker partners we have implemented the `force_engine_version` GET parameter, that allows them to select which version of the engine use on a per-request basis, thus they can compare the output of the two engine versions and do a gradual rollout of the `v2` engine version in their systems.
# 
Profit and loss calculation
[](get-v1-trading-accounts-account_id-account-portfolio-history-1.html#profit-and-loss-calculation)
For profit and loss calculation we are using simple profit and loss to calculate the pnl percentage for a given time:
`pnl_pct = equity/base_value-1`
The v2 responses contain the `base_value_asof` field, which indicates which trading day's closing balance is used for the base value. If the `base_value_asof` is omitted from the response that means that the account doesn't have a prior non-zero closing balance. In such cases the base_value will be the earliest returned data point.
# 
Notes
[](get-v1-trading-accounts-account_id-account-portfolio-history-1.html#notes)
In the case of `continuous` mode (`intraday_reporting`), to calculate the equity values we are using the following prices:
* Between 4:00am and 10:00pm on trading days the valuation will be calculated based on the last trade (extended hours and normal hours respectively).
* After 10:00pm, until the next session open the equities will be valued at their official closing price on the primary exchange.
Regardless of the `intraday_reporting`'s value the 1D chart only contains data for days when the market was open.
The query parameters marked with _v2 only_ are only available if the queries are made using the `v2` version of the engine.
The v2 engine rounds all the cash values returned to the currency precision set for the partner's correspondent, which is by default two digits. All percentage values are rounded to 4 digits.
