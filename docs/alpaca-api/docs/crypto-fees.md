---
title: Crypto Spot Trading Fees
source: docs\crypto-fees.html
---

While Alpaca stock trading remains commission-free, crypto trading includes a small fee per trade dependent on your executed volume and order type. Any market or exchange consists of two parties, buyers and sellers. When you place an order to buy crypto on the Alpaca Exchange, there is someone else on the other side of the trade selling what you want to buy. The seller's posted order on the order book is providing liquidity to the exchange and allows for the trade to take place. Note, that both buyers and sellers can be makers or takers depending on the order entered and current quote of the coin. **A maker is someone who adds liquidity, and the order gets placed on the order book. A Taker on the other hand removes the liquidity by placing a market or marketable limit order which executes against posted orders.**
See the below table with volume-tiered fee pricing:
Tier| 30D Crypto Volume (USD)| Maker| Take  
---|---|---|---  
1| 0 - 100,000| 0.15%| 0.25%  
2| 100,000 - 500,000| 0.12%| 0.22%  
3| 500,000 - 1,000,000| 0.10%| 0.20%  
4| 1,000,000 - 10,000,000| 0.08%| 0.18%  
5| 10,000,000- 25,000,000| 0.05%| 0.15%  
6| 25,000,000 - 50,000,000| 0.02%| 0.13%  
7| 50,000,000 - 100,000,000| 0.02%| 0.12%  
8| 100,000,000+| 0.00%| 0.10%  
The crypto fee will be charged on the credited crypto asset/fiat (what you receive) per trade. Some examples:
* Buy `ETH/BTC`, you receive `ETH`, the fee is denominated in `ETH`
* Sell `ETH/BTC`, you receive `BTC`, the fee is denominated in `BTC`
* Buy `ETH/USD`, you receive `ETH`, the fee is denominated in `ETH`
* Sell `ETH/USD`, you receive `USD`, the fee is denominated in `USD`
To get the fees incurred from crypto trading you can use Activities API to query `activity_type` by `CFEE` or `FEE`. 
See below example of CFEE object:
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
> ## 📘
> 
> Check out our Crypto Trading FAQ [here](https://alpaca.markets/support/alpaca-crypto-coin-pair-faq)
__Updated 6 months ago
* * *
