---
title: Market Data FAQ
source: docs\market-data-faq.html
---

# 
General
[](market-data-faq.html#general)
## 
Why am I getting HTTP 403 (Forbidden)?
[](market-data-faq.html#why-am-i-getting-http-403-forbidden)
The market data endpoints return HTTP 403 if any of the following conditions are true:
* the request was not authenticated
* the provided credentials were incorrect
* the authenticated user has insufficient permissions
To fix these issues, there are two checklists, one for regular users and one for broker partners. If you're unsure which refers to you, check this [FAQ](broker-api-faq.html-what-is-the-difference-between-trading-api-and-broker-api.md). If you're still unsure, then check your access key. If it starts with the letter `C`, then you're a broker partner, otherwise you're a regular user. If you don't have an access key yet, generate it on the right-hand side of the Alpaca [dashboard](https://app.alpaca.markets/brokerage/dashboard/overview).
### 
Checklist for regular users
[](market-data-faq.html#checklist-for-regular-users)
* make sure you provide your credentials in the following HTTP headers: 
* `APCA-API-KEY-ID`
* `APCA-API-SECRET-KEY`
* make sure your credentials are valid: 
* check the key on the[ web UI](https://app.alpaca.markets/brokerage/dashboard/overview)
* when you reset your paper account, you need to regenerate your credentials
* make sure the host is `data.alpaca.markets` [for historical](historical-api.html-base-url.md) or `stream.data.alpaca.markets` [for live](streaming-market-data.html-connection.md)
* if you get a message like `subscription does not permit querying recent SIP data` in the HTTP response body, make sure you have the proper [subscription](about-market-data-api.html-subscription-plans.md)
* for example to query any SIP trades or quotes in the last 15 minutes, you need the Algo Trader Plus subscription
### 
Checklist for broker partners
[](market-data-faq.html#checklist-for-broker-partners)
* make sure you provide your credentials in [HTTP basic authentication](about-market-data-api.html-subscription-plans.md)
* make sure your credentials are valid
* make sure you're using the right host based on your environment: 
* the production host is `data.alpaca.markets` [for historical](historical-api.html-base-url.md) and `stream.data.alpaca.markets` [for live](streaming-market-data.html-connection.md)
* the sandbox host (for testing) is `data.sandbox.alpaca.markets` [for historical](historical-api.html-base-url.md) and `stream.data.sandbox.alpaca.markets` [for live](streaming-market-data.html-connection.md)
* if you get a message like `subscription does not permit querying recent SIP data` in the HTTP response body, make sure you have the proper [subscription](about-market-data-api.html-broker-partners.md)
* for example, to query any SIP trades or quotes in the last 15 minutes, you need a special subscription
## 
How do I subscribe to AlgoTrader Plus?
[](market-data-faq.html#how-do-i-subscribe-to-algotrader-plus)
You can subscribe to AlgoTrader Plus on the [Alpaca UI](https://app.alpaca.markets/account/plans-and-features): on the left sidebar of the main page click on "Plans & Features" and on that page click on "Upgrade to AlgoTrader Plus" inside the Market Data box.
# 
Stocks
[](market-data-faq.html#stocks)
## 
What's the difference between IEX and SIP data?
[](market-data-faq.html#whats-the-difference-between-iex-and-sip-data)
SIP is short for [Securities Information Processor](https://en.wikipedia.org/wiki/Securities_information_processor). All US exchanges are mandated by the regulators to report their activities (trades and quotes) to the consolidated tape. This is what we call SIP data.
IEX ([Investors Exchange](https://en.wikipedia.org/wiki/IEX)) is a single stock exchange.
#### 
[Websocket stream](real-time-stock-pricing-data.md)
[](market-data-faq.html#websocket-stream)
Our free market data offering includes live data only from the IEX exchange:
wss://stream.data.alpaca.markets/v2/iex
The Algo Trader Plus subscription on the other hand offers SIP data:
wss://stream.data.alpaca.markets/v2/sip
#### 
[Historical data](..-reference-stockbars-1.md)
[](market-data-faq.html#historical-data)
On the historical endpoints, use the `feed` parameter to switch between the two data feeds:
JSON
$ curl -s -H "APCA-API-KEY-ID: ${APCA_API_KEY_ID}" -H "APCA-API-SECRET-KEY: ${APCA_API_SECRET_KEY}" \
"https://data.alpaca.markets/v2/stocks/AAPL/bars?feed=sip&timeframe=1Day&start=2023-09-29&limit=1" | jq .
{
"bars": [
{
"t": "2023-09-29T04:00:00Z",
"o": 172.02,
"h": 173.07,
"l": 170.341,
"c": 171.21,
"v": 51861083,
"n": 535134,
"vw": 171.599691
}
],
"symbol": "AAPL",
"next_page_token": "QUFQTHxEfDIwMjMtMDktMjlUMDQ6MDA6MDAuMDAwMDAwMDAwWg=="
}
$ curl -s -H "APCA-API-KEY-ID: ${APCA_API_KEY_ID}" -H "APCA-API-SECRET-KEY: ${APCA_API_SECRET_KEY}" \
"https://data.alpaca.markets/v2/stocks/AAPL/bars?feed=iex&timeframe=1Day&start=2023-09-29&limit=1" | jq .
{
"bars": [
{
"t": "2023-09-29T04:00:00Z",
"o": 172.015,
"h": 173.06,
"l": 170.36,
"c": 171.29,
"v": 923134,
"n": 12630,
"vw": 171.716432
}
],
"symbol": "AAPL",
"next_page_token": null
}
In this example (2023-09-29 Apple daily bar), you can clearly see the difference between the two feeds: there were **12 630** eligible trades on the IEX exchange that day and more than **535 136** trades in total across all exchanges (naturally including IEX). Similar differences can be seen between their volumes.
All the latest endpoints (including the [snapshot](..-reference-stocksnapshotsingle.md) endpoint), require a subscription to be used with the SIP feed. For historical queries, the `end` parameter must be at least 15 minutes old to query SIP data without a subscription. The default value for `feed` is always the "best" available feed based on the user's subscription.
JSON
$  curl -s -H "APCA-API-KEY-ID: ${APCA_API_KEY_ID}" -H "APCA-API-SECRET-KEY: ${APCA_API_SECRET_KEY}" \
"https://data.alpaca.markets/v2/stocks/AAPL/trades/latest" | jq .
{
"symbol": "AAPL",
"trade": {
"t": "2023-09-29T19:59:59.246196362Z",
"x": "V",  // << IEX exchange code
"p": 171.29,
"s": 172,
"c": [
"@"
],
"i": 12727,
"z": "C"
}
}
$ curl -H "APCA-API-KEY-ID: ${APCA_API_KEY_ID}" -H "APCA-API-SECRET-KEY: ${APCA_API_SECRET_KEY}" \
"https://data.alpaca.markets/v2/stocks/AAPL/trades/latest?feed=sip"
{"code":42210000,"message":"subscription does not permit querying recent SIP data"}
In this example, we're querying the latest AAPL trade without a subscription. The default `feed` in this case is `iex`. If we were to try to query the SIP feed, we would get an error. To fix that error, we need to subscribe to [Algo Trader Plus](about-market-data-api.html-subscription-plans.md).
## 
Why can't I find market data for a particular symbol (e.g. CGRNQ)?
[](market-data-faq.html#why-cant-i-find-market-data-for-a-particular-symbol-eg-cgrnq)
### 
OTC
[](market-data-faq.html#otc)
Make sure the symbol is not traded in OTC using the [assets endpoint](..-reference-get-v2-assets-symbol_or_asset_id.md). `https://api.alpaca.markets/v2/assets/CGRNQ` returns
JSON
{
"id": "dc2d8be9-33b5-4a32-8f57-5b7d209d2c82",
"class": "us_equity",
"exchange": "OTC", // << This symbol is traded in OTC
"symbol": "CGRNQ",
"name": "CAPSTONE GREEN ENERGY CORP COM PAR $.001",
"status": "active",
"tradable": false,
"marginable": false,
"maintenance_margin_requirement": 100,
"shortable": true,
"easy_to_borrow": true,
"fractionable": true,
"attributes": []
}
Market data for OTC symbols can only be queried with a special subscription currently available only for broker partners. If you do have the subscription, you can use `feed=otc` to query the data.
### 
Inactive
[](market-data-faq.html#inactive)
Make sure the asset is active. Check the `status` field of the [same endpoint](..-reference-get-v2-assets-symbol_or_asset_id.md). 
### 
Halt
[](market-data-faq.html#halt)
Make sure the symbol isn't or wasn't halted at the time you're querying. You can check the [current halts](https://www.nasdaqtrader.com/trader.aspx?id=TradeHalts) or the [historical halts](https://www.nasdaqtrader.com/Trader.aspx?id=TradingHaltSearch) on the Nasdaq website. For example, the symbol SVA has been halted since 2019-02-22.
## 
What happens when a ticker symbol of a company changes?
[](market-data-faq.html#what-happens-when-a-ticker-symbol-of-a-company-changes)
Perhaps the most famous example for this was when Facebook decided to [rename itself ](https://about.fb.com/news/2021/10/facebook-company-is-now-meta/)to Meta and to change its ticker symbol from FB to META. This transition happened on 2022-06-09.
### 
Latest endpoints
[](market-data-faq.html#latest-endpoints)
On the latest endpoints ([latest trades](..-reference-stocklatesttrades-1.md), [latest quotes](..-reference-stocklatestquotes-1.md), [latest bars](..-reference-stocklatestbars-1.md) and [snapshots](..-reference-stocksnapshots-1.md)), the data is never manipulated in any way. These endpoints always return the data as it was received at the time (this is also why there is no `adjustment` parameter on the [latest bars](..-reference-stocklatestbars-1.md)). So, in this case, the latest FB trade returns the last trade when the company was still called FB:
JSON
$ curl -s -H "APCA-API-KEY-ID: ${APCA_API_KEY_ID}" -H "APCA-API-SECRET-KEY: ${APCA_API_SECRET_KEY}" "${APCA_API_DATA_URL}/v2/stocks/trades/latest?symbols=FB" | jq .
{
"trades": {
"FB": {
"c": [
"@",
"T"
],
"i": 31118,
"p": 196.29,
"s": 121,
"t": "2022-06-08T23:59:55.103033856Z",
"x": "P",
"z": "C"
}
}
}
Note the timestamp in the response is 2022-06-08, the night before the name change.
### 
Stream endpoints
[](market-data-faq.html#stream-endpoints)
The symbols always reflect the ones used by the companies at the time of the transmission on the [streaming endpoints](..-edit-real-time-stock-pricing-data.md) as well. In practice this means that a stream client must resubscribe to the new symbol after a name change to continue receiving data. The resubscribe requires no reconnection, in the Facebook example you could simply send a [subscribe message](streaming-market-data.html-subscription.md) to META.
### 
Historical endpoints
[](market-data-faq.html#historical-endpoints)
On the historical endpoints we introduced the `asof` parameter to link together the data before and after the rename. By default, this parameter is "enabled", so even if you don't specify it, you will get the data for both the old and new symbol when querying the new symbol after the rename.
For the example of the FB - META rename, we can simply query the daily bars for META for the whole week (the rename happened on Thursday), yet we see the bars for Monday, Tuesday and Wednesday as well, even though on those days, the company was still called FB.
Shell
$ curl -s -H "APCA-API-KEY-ID: ${APCA_API_KEY_ID}" -H "APCA-API-SECRET-KEY: ${APCA_API_SECRET_KEY}" \
"${APCA_API_DATA_URL}/v2/stocks/bars?timeframe=1Day&symbols=META&start=2022-06-06&end=2022-06-11" | \
jq -r '.bars.META[] | [.t, .o, .h, .l, .c] | @tsv'
2022-06-06T04:00:00Z    193.99  196.92  188.4   194.25
2022-06-07T04:00:00Z    191.93  196.53  191.49  195.65
2022-06-08T04:00:00Z    194.67  202.03  194.41  196.64
2022-06-09T04:00:00Z    194.28  199.45  183.68  184
2022-06-10T04:00:00Z    183.04  183.1   175.02  175.57
If you disable the `asof` parameter, you won't get the FB bars:
Shell
$ curl -s -H "APCA-API-KEY-ID: ${APCA_API_KEY_ID}" -H "APCA-API-SECRET-KEY: ${APCA_API_SECRET_KEY}" \
"${APCA_API_DATA_URL}/v2/stocks/bars?timeframe=1Day&symbols=META&start=2022-06-06&end=2022-06-11&asof=-" | \
jq -r '.bars.META[] | [.t, .o, .h, .l, .c] | @tsv'
2022-06-09T04:00:00Z    194.28  199.45  183.68  184
2022-06-10T04:00:00Z    183.04  183.1   175.02  175.57
If you set `asof` to a date before the rename, you can query by the old ticker:
Shell
$ curl -s -H "APCA-API-KEY-ID: ${APCA_API_KEY_ID}" -H "APCA-API-SECRET-KEY: ${APCA_API_SECRET_KEY}" \
"${APCA_API_DATA_URL}/v2/stocks/bars?timeframe=1Day&symbols=FB&start=2022-06-06&end=2022-06-11&asof=2022-06-06" | \
jq -r '.bars.FB[] | [.t, .o, .h, .l, .c] | @tsv'
2022-06-06T04:00:00Z    193.99  196.92  188.4   194.25
2022-06-07T04:00:00Z    191.93  196.53  191.49  195.65
2022-06-08T04:00:00Z    194.67  202.03  194.41  196.64
2022-06-09T04:00:00Z    194.28  199.45  183.68  184
2022-06-10T04:00:00Z    183.04  183.1   175.02  175.57
Unfortunately, the `asof` mapping is only available on our historical endpoints the day after the rename. In the FB-META example, it was available since 2022-06-10, so running the same queries on the day of the rename (2022-06-09) didn't return the FB bars. This is because of a limitation of one of our data sources. We're actively working on improving this and doing the mapping before the market opens with the new symbol.
## 
How are bars aggregated?
[](market-data-faq.html#how-are-bars-aggregated)
Minute and daily bars are aggregated from trades. The (SIP) timestamp of the trade is truncated to the minute for minute bars and to the day (in New York) for daily bars. For example, a trade at 14:52:28 belongs to the 14:52:00 minute bar, which contains all the trades between 14:52:00 (inclusive) and 14:53:00 (exclusive). The timestamp of the bar is the left side of the interval (14:52:00 in this example).
There are three parts of the bar that a trade can potentially update:
* open / close price
* high / low price
* volume
The rules of these updates depend on 
* the tape of the trade (`A`, `B`: NYSE, `C`: Nasdaq, `O`: OTC)
* the conditions of the trade
* the type of the bar (`M`: minute, `D`: daily) 
* Some rules are different for minute and daily bars. For example `P` (Prior Reference Price) relates to an obligation to trade at an earlier point in the trading day. This will update the high / low price of a daily bar but will not update the high / low price of a minute bar, because that price possibly happened in another minute.
The rules are based on the guidelines of the SIPs:
* the [CTS specification](https://www.ctaplan.com/publicdocs/ctaplan/CTS_Pillar_Output_Specification.pdf) for NYSE (tape `A` and `B`)
* the [UTP specification](https://utpplan.com/DOC/UtpBinaryOutputSpec.pdf) for Nasdaq (tape `C`)
* the [TDDS specification](https://www.finra.org/sites/default/files/2022-05/TDDS-2.1-MOLD.pdf) for OTC (tape `O`)
The following table contains all the updating rules:
Tape| Bar type| Condition code| Condition description| Update open / close| Update high / low| Update volume  
---|---|---|---|---|---|---  
AB| MD| ` `| Regular Sale| 🟢| 🟢| 🟢  
CO| MD| `@`| Regular Sale| 🟢| 🟢| 🟢  
C| MD| `A`| Acquisition| 🟢| 🟢| 🟢  
AB| MD| `B`| Average Price Trade| 🔴| 🔴| 🟢  
C| MD| `B`| Bunched Trade| 🟢| 🟢| 🟢  
ABCO| MD| `C`| Cash Sale| 🔴| 🔴| 🟢  
C| MD| `D`| Distribution| 🟢| 🟢| 🟢  
AB| MD| `E`| Automatic Execution| 🟢| 🟢| 🟢  
ABC| MD| `F`| Intermarket Sweep| 🟢| 🟢| 🟢  
C| M| `G`| Bunched Sold Trade| 🔴| 🔴| 🟢  
C| D| `G`| Bunched Sold Trade| 🟡| 🟢| 🟢  
ABC| MD| `H`| Price Variation Trade| 🔴| 🔴| 🟢  
ABCO| MD| `I`| Odd Lot Trade| 🔴| 🔴| 🟢  
ABC| MD| `K`| Rule 127 or Rule 155| 🟢| 🟢| 🟢  
ABC| MD| `L`| Sold Last| 🟢| 🟢| 🟢  
ABC| MD| `M`| Market Center Official Close| 🔴| 🔴| 🔴  
ABCO| MD| `N`| Next Day| 🔴| 🔴| 🟢  
ABC| MD| `O`| Market Center Opening Trade| 🟢| 🟢| 🟢  
ABCO| M| `P`| Prior Reference Price| 🔴| 🔴| 🟢  
ABCO| D| `P`| Prior Reference Price| 🟡| 🟢| 🟢  
ABC| MD| `Q`| Market Center Official Open| 🔴| 🔴| 🔴  
ABCO| MD| `R`| Seller| 🔴| 🔴| 🟢  
ABCO| M| `T`| Extended Hours Trade| 🟢| 🟢| 🟢  
ABCO| D| `T`| Extended Hours Trade| 🔴| 🔴| 🟢  
ABCO| MD| `U`| Extended Trading Hours| 🔴| 🔴| 🟢  
ABC| MD| `V`| Contingent Trade| 🔴| 🔴| 🟢  
CO| MD| `W`| Average Price Trade| 🔴| 🔴| 🟢  
ABC| MD| `X`| Cross Trade| 🟢| 🟢| 🟢  
C| MD| `Y`| Yellow Flag Regular Trade| 🟢| 🟢| 🟢  
ABC| M| `Z`| Sold Out Of Sequence| 🔴| 🔴| 🟢  
ABC| D| `Z`| Sold Out Of Sequence| 🟡| 🟢| 🟢  
ABC| M| `4`| Derivatively Priced| 🔴| 🔴| 🟢  
ABC| D| `4`| Derivatively Priced| 🟡| 🟢| 🟢  
ABC| MD| `5`| Market Center Reopening Trade| 🟢| 🟢| 🟢  
ABC| MD| `6`| Market Center Closing Trade| 🟢| 🟢| 🟢  
ABC| MD| `7`| Qualified Contingent Trade| 🔴| 🔴| 🟢  
ABC| M| `9`| Corrected Consolidated Close| 🔴| 🔴| 🔴  
ABC| D| `9`| Corrected Consolidated Close| 🟢| 🟢| 🔴  
* 🟢 means that the given condition updates the value
* 🟡 means that the given condition updates the open / close price only if the trade is the first trade of the bar
* 🔴 means that the given condition does not update the value
In the original [CTS](https://www.ctaplan.com/publicdocs/ctaplan/CTS_Pillar_Output_Specification.pdf) / [UTP](https://utpplan.com/DOC/UtpBinaryOutputSpec.pdf) specifications, there are some more complicated update rules (see the footnotes in the linked specifications), but we don't use any of these. In most of the cases, we simply use 🟡 (or 🟢) instead.
A trade can have more than one condition. In this case the strictest rule is applied. For example, if a Nasdaq trade has these conditions: `@`, `4`, `I` and a daily bar is being generated, none of the prices of the bar are going to be updated (both open / close and high / low is 🔴 because it's an odd lot trade), only the volume 🟢 is going to be updated. If the trade had no `I` condition (`@` and `4` only), then the open / close price would only be updated if this is the first trade of the bar 🟡 , and both the high / low price 🟢 and the volume 🟢 would be updated. If it was a regular trade (`@`), then all of its values would be updated.
Once the combined updating rule of the trade has been calculated, the bar's fields are updated:
* Open is set if it hasn't been set yet and the update open / close rule is 🟢 or 🟡
* High is set if it hasn't been set yet or if the price of the trade is higher than the previous high and the update high / low is 🟢
* Low is set if it hasn't been set yet or if the price of the trade is lower than the previous low and the update high / low rule is 🟢
* Close is set if the update open / close rule is 🟢 or if it's 🟡 and the close price hasn't been set yet
* Volume is increased by the size of the trade if the update volume rule is 🟢
* The trade count is increased by one if the update volume rule is 🟢
* [VWAP](https://en.wikipedia.org/wiki/Volume-weighted_average_price) is the ratio of these two internal variables: 
* The volume-weighted total price is increased by the product of the trade's price and volume if both the update high / low rule and the update volume rule is 🟢
* The total volume is increased by the size of the trade if both the update high / low rule and the update volume rule is 🟢. This means that this volume can be different from the "normal" volume field of the bar if there are trades in the bar that update the volume but not the high / low price (for example condition `R`)
Finally, the bar is only emitted if none of its fields (open, high, low, close, volume) are 0. So if there are no trades in the bar's interval, or if there's only a single `I` trade (which only updates the volume, but none of the prices), then no bar is generated.
All the other non-minute and non-daily bars are aggregated from the minute and daily bars. For example, an hour (`1Hour`) bar is aggregated from all the minute bars in the given hour and a weekly bar (`1Week`) is aggregated from all the daily bars in the given week. This aggregation no longer considers the actual trades that happened in the given interval, but instead the bars are aggregated using these rules:
* Open is the open of the first bar
* High is the maximum of the bars' high prices
* Low is the minimum of the bars' low prices
* Close is the close of the last bar
* Volume is the sum of the bars' volumes
* Trade count is the sum of the bars' trade counts
* VWAP is the volume-weighted average of the bars' VWAPs
# 
Crypto
[](market-data-faq.html#crypto)
## 
Why are there crypto bars with 0 volume / trade count?
[](market-data-faq.html#why-are-there-crypto-bars-with-0-volume--trade-count)
Our crypto market data reflects trades and quotes from our own Alpaca exchange. Due to the volatility of some cryptocurrencies, including lack of trade volume at any given time, we include the quote midpoint prices to offer a better data experience. If within a bar no trade happens, the volume will be 0, but the prices will be determined by the quote prices.
__Updated 4 months ago
* * *
