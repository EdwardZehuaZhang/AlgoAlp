---
title: Crypto Spot Trading
source: docs\crypto-trading.html
---

> ##  🚧
> 
> As of November 18, 2022, cryptocurrency trading is open to select international jurisdictions and some U.S. jurisdictions.
> 
> To view the supported US regions for crypto trading, click [here](https://alpaca.markets/support/what-regions-support-cryptocurrency-trading).
# 
Supported Coins
[](crypto-trading.html#supported-coins)
Alpaca supports over 20+ unique crypto assets across 56 trading pairs. Current trading pairs are based on BTC, USD, USDT and USDC) with more assets and trading pairs coming soon.
To query all available crypto assets and pairs you can you use the following API call:
cURL
curl --request GET 'https://api.alpaca.markets/v2/assets?asset_class=crypto' \
--header 'Apca-Api-Key-Id: <KEY>' \
--header 'Apca-Api-Secret-Key: <SECRET>'
Below is a sample trading pair object composed of two assets, BTC and USD.
JSON
{
"id": "276e2673-764b-4ab6-a611-caf665ca6340",
"class": "crypto",
"exchange": "ALPACA",
"symbol": "BTC/USD",
"name": "BTC/USD pair",
"status": "active",
"tradable": true,
"marginable": false,
"shortable": false,
"easy_to_borrow": false,
"fractionable": true,
"min_order_size": "0.0001",
"min_trade_increment": "0.0001",
"price_increment": "1"
}
Note that symbology for trading pairs has changed from our previous format, where `BTC/USD` was previously referred to as `BTCUSD`. Our API has made proper changes to support the legacy convention as well for backwards compatibility.
For further reference see Assets API. **add link**
# 
Supported Orders
[](crypto-trading.html#supported-orders)
When submitting crypto orders through the Orders API and the Alpaca web dashboard, Market, Limit and Stop Limit orders are supported while the supported `time_in_force` values are `gtc`, and `ioc`. We accept fractional orders as well with either `notional` or `qty` provided.
You can submit crypto orders for any supported crypto pair via API, see the below cURL POST request.
cURL
curl --request POST 'https://paper-api.alpaca.markets/v2/orders' \
--header 'Apca-Api-Key-Id: <KEY>' \
--header 'Apca-Api-Secret-Key: <SECRET>' \
--header 'Content-Type: application/json' \
--data-raw '{
"symbol": "BTC/USD",
"qty": "0.0001",
"side": "buy",
"type": "market",
"time_in_force": "gtc"
}'
The above request submits a market order via API to buy 0.0001 BTC with USD (BTC/USD pair) that is good till end of day.
To learn more see **orders** and **fractional trading**.
All cryptocurrency assets are fractionable but the supported decimal points vary depending on the cryptocurrency. See **Assets entity** for information on fractional precisions per asset.
Note these values could change in the future.
# 
Crypto Market Data
[](crypto-trading.html#crypto-market-data)
You can check out the [documentation](historical-crypto-data-1.md) and the [API reference](..-reference-cryptobars-1.md) of our crypto market data.
Here we provide an example to request the latest order book data (bids and asks) for the following three coin pairs: BTC/USD, ETH/BTC, and ETH/USD.
cURL
curl 'https://data.alpaca.markets/v1beta3/crypto/us/latest/orderbooks?symbols=BTC/USD,ETH/BTC,ETH/USD'
JSON
{
"orderbooks": {
"BTC/USD": {
"a": [
{
"p": 66051.621,
"s": 0.275033
},
...
],
"b": [
{
"p": 65986.962,
"s": 0.27813
},
...
],
"t": "2024-07-24T07:31:01.373709495Z"
},
"ETH/USD": { ... }
},
"ETH/BTC": { ... }
}
}
Additionally, you can subscribe to real-time crypto data via Websockets. Example below leverages wscat to subscribe to BTC/USD order book.
JSON
$ wscat -c wss://stream.data.alpaca.markets/v1beta3/crypto/us
Connected (press CTRL+C to quit)
< [{"T":"success","msg":"connected"}]
> {"action":"auth","key":"<YOUR API KEY>","secret":"<YOUR API SECRET>"}
< [{"T":"success","msg":"authenticated"}]
> {"action":"subscribe","quotes":["ETH/USD"]}
< [{"T":"subscription","trades":[],"quotes":["ETH/USD"],"orderbooks":[],"bars":[],"updatedBars":[],"dailyBars":[]}]
< [{"T":"q","S":"ETH/USD","bp":3445.34,"bs":4.339,"ap":3450.2,"as":4.3803,"t":"2024-07-24T07:38:06.88490478Z"}]
< [{"T":"q","S":"ETH/USD","bp":3445.34,"bs":4.339,"ap":3451.1,"as":8.73823,"t":"2024-07-24T07:38:06.88493591Z"}]
< [{"T":"q","S":"ETH/USD","bp":3445.34,"bs":4.339,"ap":3447.03,"as":4.36424,"t":"2024-07-24T07:38:06.88511154Z"}]
< [{"T":"q","S":"ETH/USD","bp":3444.644,"bs":8.797,"ap":3447.03,"as":4.36424,"t":"2024-07-24T07:38:06.88512141Z"}]
< [{"T":"q","S":"ETH/USD","bp":3444.51,"bs":4.33,"ap":3447.03,"as":4.36424,"t":"2024-07-24T07:38:06.88516355Z"}]
For further reference of real-time crypto pricing data see [its documentation](real-time-crypto-pricing-data.md).
# 
Transferring Crypto
[](crypto-trading.html#transferring-crypto)
Alpaca now offers native on-chain crypto transfers with wallets! If you have crypto trading enabled and reside in an eligible US state or international jurisdiction you can access wallets on the web dashboard via the Crypto Transfers tab.
Alpaca wallets currently support transfers for Bitcoin, Ethereum, and all Ethereum (ERC20) based tokens. To learn more on transferring crypto with Alpaca, see **[Crypto Wallets FAQs](https://alpaca.markets/support/crypto-wallet-faq)**
# 
Crypto Spot Trading Fees
[](crypto-trading.html#crypto-spot-trading-fees)
While Alpaca stock trading remains commission-free, crypto trading includes a small fee per trade dependent on your executed volume and order type. Any market or exchange consists of two parties, buyers and sellers. When you place an order to buy crypto on the Alpaca Exchange, there is someone else on the other side of the trade selling what you want to buy. The seller's posted order on the order book is providing liquidity to the exchange and allows for the trade to take place. Note, that both buyers and sellers can be makers or takers depending on the order entered and current quote of the coin. **A maker is someone who adds liquidity, and the order gets placed on the order book. A Taker on the other hand removes the liquidity by placing a market or marketable limit order which executes against posted orders.**
See the below table with volume-tiered fee pricing:
Tier| 30D Trading Volume (USD)| Maker| Taker  
---|---|---|---  
1| 0 - 100,000| 15 bps| 25 bps  
2| 100,000 - 500,000| 12 bps| 22 bps  
3| 500,000 - 1,000,000| 10 bps| 20 bps  
4| 1,000,000 - 10,000,000| 8 bps| 18 bps  
5| 10,000,000 - 25,000,000| 5 bps| 15 bps  
6| 25,000,000 - 50,000,000| 2 bps| 13 bps  
7| 50,000,000 - 100,000,000| 2 bps| 12 bps  
8| 100,000,000+| 0 bps| 10 bps  
The crypto fee will be charged on the credited crypto asset/fiat (what you receive) per trade. Some examples,
* Buy `ETH/BTC`, you receive `ETH`, the fee is denominated in `ETH`
* Sell `ETH/BTC`, you receive `BTC`, the fee is denominated in `BTC`
* Buy `ETH/USD`, you receive `ETH`, the fee is denominated in `ETH`
* Sell `ETH/USD`, you receive `USD`, the fee is denominated in `USD`
To get the fees incurred from crypto trading you can use Activities API to query `activity_type` by `CFEE` or `FEE`. See below example of CFEE object:
JSON
{
"id": "20220812000000000::53be51ba-46f9-43de-b81f-576f241dc680",
"activity_type": "CFEE",
"date": "2022-08-12",
"net_amount": "0",
"description": "Coin Pair Transaction Fee (Non USD)",
"symbol": "ETHUSD",
"qty": "-0.000195",
"price": "1884.5",
"status": "executed"
}
Fees are currently calculated and posted end of day. If you query on same day of trade you might not get results. We will be providing an update for fee posting to be real-time in the near future.
# 
Margin and Short Selling
[](crypto-trading.html#margin-and-short-selling)
Cryptocurrencies cannot be bought on margin. This means that you cannot use leverage to buy them and orders are evaluated against `non_marginable_buying_power`.
Cryptocurrencies can not be sold short.
# 
Trading Hours
[](crypto-trading.html#trading-hours)
Crypto trading is offered for 24 hours everyday and your orders will be executed throughout the day.
# 
Trading Limits
[](crypto-trading.html#trading-limits)
Currently, an order (buy or sell) must not exceed $200k in notional. This is per an order.
__Updated 6 months ago
* * *
