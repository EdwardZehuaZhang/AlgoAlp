---
title: Crypto Trading
source: docs\crypto-trading-1.html
---

> ##  🌍
> 
> To view the supported US regions for crypto trading, click [here](https://alpaca.markets/support/what-regions-support-cryptocurrency-trading).
# 
Enabling Crypto for an Account
[](crypto-trading-1.html#enabling-crypto-for-an-account)
To enable crypto trading for an account, the crypto agreements must be signed by the user. All account balances will represent the crypto trading activities.
In the case of new users, the crypto agreement can be submitted via the Accounts API where `crypto_agreement` is part of the agreements attribute.
_Part of the request_
JSON
{
"agreements": [
{
"agreement": "crypto_agreement",
"signed_at": "2023-01-01T18:09:33Z"
}
]
}
In the case of existing users the account has to be updated with the `crypto_agreement` which can be submitted on the `PATCH /v1/accounts/{account_id}` endpoint.
_Part of the request_
JSON
{
"agreements": [
{
"agreement": "crypto_agreement",
"signed_at": "2023-01-01T18:13:44Z",
"ip_address": "185.13.21.99"
}
]
}
Once the crypto agreement is added to the user account no further edits can be made to the agreements.
To determine whether the account is all set to start trading crypto, use the `crypto_status` attribute from the Account API endpoint response object.
_Sample Response_
JSON
{
"id": "9feee08f-22d2-4804-89c1-bf01166aad52",
"account_number": "943690069",
"status": "ACTIVE",
"crypto_status": "ACTIVE"
}
Attribute| Description  
---|---  
INACTIVE| Account not enabled to trade crypto live  
ACTIVE| Crypto account is active and can start trading  
SUBMISSION_FAILED| Account submissions has failed  
# 
Supported Assets
[](crypto-trading-1.html#supported-assets)
We have over 20 coins available to trade via our APIs. We constantly evaluate the list and aim to to grow the number of supported currencies.
Tradable cryptocurrencies can be identified through the [Assets API](..-reference-getassets.md) where the asset entity has `class = crypto` and `tradable = true`.
JSON
{
"id": "64bbff51-59d6-4b3c-9351-13ad85e3c752",
"class": "crypto",
"exchange": "CRXL",
"symbol": "BTC/USD",
"name": "Bitcoin",
"status": "active",
"tradable": true,
"marginable": false,
"shortable": false,
"easy_to_borrow": false,
"fractionable": true
}
Please note that the symbol appears with `USD`, such as `BTC/USD` instead of `BTC`.
> ## 🚧
> 
> Crypto Fee Revenue Notice
> 
> If you enable non-USD crypto trading you will receive fees in the quote currency. Currently, non-USD quote crypto assets are BTC, USDC and USDT. As a broker business you would need to be ready to handle collecting crypto fees plus taking care of the necessary conversions if needed.
## 
Minimum Order Size
[](crypto-trading-1.html#minimum-order-size)
The minimum quantity value that is accepted in an order. This value is calculated dynamically based on the selected notional equivalent minimum, based on the last close price of the relevant asset(s). The maximum decimal places accepted is 9 i.e 0.000000001 for all crypto assets. 
For `USD` pairs, the minimum order size calculation is: 1/USD asset price.
For `BTC`, `ETH` and `USDT` pairs, the minimum order size is `0.000000002`.
## 
Min Trade Increment
[](crypto-trading-1.html#min-trade-increment)
The minimum quantity allowed to be added to the `min_order_size`. E.g. if 0.1 we accept an order for 1.1 but we won’t accept 0.9 because it’s under the `min_order_size`. The maximum decimal places accepted are 9 i.e 0.000000001 for all crypto assets. 
Price Increment: The minimum notional value that is accepted in an order. Similar to Min Order Size but for notional orders. The maximum decimal places accepted are 9 i.e 0.000000001 for all crypto assets.
All cryptocurrency assets are fractionable but the supported decimal points vary depending on the cryptocurrency.
# 
Supported Orders
[](crypto-trading-1.html#supported-orders)
When submitting crypto orders through the Orders API, Market, Limit and Stop Limit orders are supported while the supported `time_in_force` values are `gtc`, and `ioc`. We accept fractional orders as well with either `notional` or `qty` provided.
## 
Required Disclosures
[](crypto-trading-1.html#required-disclosures)
Below you will find required disclosure templates to safely support crypto in your applications as a broker with Alpaca.
### 
Onboarding Disclosures
[](crypto-trading-1.html#onboarding-disclosures)
When onboarding your users as a broker offering crypto the following disclosure is required. During your onboarding flow make sure the user is able to read and affirmatively acknowledge, such as through a separate checkbox, the following text:
I have read, understood, and agree to be bound by Alpaca Crypto LLC and [your legal entity] account terms, and all other terms, disclosures and disclaimers applicable to me, as referenced in the Alpaca Crypto Agreement. I also acknowledge that the Alpaca Crypto Agreement contains a pre-dispute arbitration clause in Section 26.
### 
Buy/Sell Order Screen Disclosures
[](crypto-trading-1.html#buysell-order-screen-disclosures)
As a broker enabling the placement of cryptocurrency orders, the following disclosures should appear on the user’s order entry screen, on the app or website, immediately prior to the user submitting the buy or sell order.
#### 
Buy Order Disclosure
[](crypto-trading-1.html#buy-order-disclosure)
By placing an order to buy [$ amount of / number of ] [cryptocurrency], you are directing and authorizing Alpaca Securities LLC to transfer funds necessary to cover the purchase costs from your Alpaca Securities LLC account into your Alpaca Crypto LLC account. Cryptocurrency services are facilitated by Alpaca Crypto LLC. Cryptocurrencies are not securities and are not FDIC insured or protected by SIPC. [Disclosures](crypto-trading-1.md).
#### 
Sell Order Disclosure
[](crypto-trading-1.html#sell-order-disclosure)
By placing an order to sell [$ amount of / number of ] [cryptocurrency], you are directing and authorizing Alpaca Crypto LLC to transfer settled funds from the sale into your Alpaca Securities LLC account. Cryptocurrency services are facilitated by Alpaca Crypto LLC. Cryptocurrencies are not securities and are not FDIC insured or protected by SIPC. Disclosures.
#### 
Crypto Pairs Order Disclosure
[](crypto-trading-1.html#crypto-pairs-order-disclosure)
By placing an order, you are directing and authorizing Alpaca Crypto LLC to exchange [X amount of Cryptocurrency] for [Y amount of cryptocurrency]. Cryptocurrency services are facilitated by Alpaca Crypto LLC. Cryptocurrencies are not securities and are not FDIC insured or protected by SIPC.
# 
Margin and Short Selling
[](crypto-trading-1.html#margin-and-short-selling)
Cryptocurrencies are non-marginable. This means that you cannot use leverage to buy them and orders are evaluated against `non_marginable_buying_power`.
Cryptocurrencies are not shortable.
# 
Trading Hours
[](crypto-trading-1.html#trading-hours)
Crypto trading is offered for 24 hours everyday and your orders will be executed throughout the day.
# 
Trading Limits
[](crypto-trading-1.html#trading-limits)
Currently, an order (buy or sell) must not exceed $200k in notional. This is per an order.
# 
Crypto Order Commissions
[](crypto-trading-1.html#crypto-order-commissions)
Broker can charge a commission on each crypto order by including a commission parameter when submitting orders. Commission support for crypto is limited to the notional commission type, and the amount is specified in the quote currency of the trading pair.  
To enable commission support, Broker must first contact Alpaca to configure your commission structure. Once set up, the commission amount can be provided in each order request, and it will also appear in the order entity of the API response.
### 
Key Points:
[](crypto-trading-1.html#key-points)
* Only the notional commission type is supported for crypto orders.
* The commission is denominated in the quote currency of the order (e.g., USD in a BTC/USD trade).
* For orders filled in multiple executions, the commission is prorated accordingly. For example, if 10% of the order is filled in one execution, 10% of the total commission will be charged on that fill.
# 
Market Data
[](crypto-trading-1.html#market-data)
Alpaca provides crypto data from multiple venues.
Crypto data providers utilized by Alpaca:
Exchange| Exchange Code  
---|---  
`CBSE`| Coinbase  
`CRXL`| Alpaca Crypto Exchange  
`FLCX`| Falcon X  
# 
Features
[](crypto-trading-1.html#features)
## 
Price Band Protection
[](crypto-trading-1.html#price-band-protection)
The price band validation in Alpaca will prevent trades from executing outside a predefined percentage range around an external reference price. Ensures market stability and prevents extreme price fluctuations due to erroneous trades. External reference prices are derived as a weighted average from `Coinbase`, `FalconX`, and `StillmanDigital`.
Orders that would execute at an invalid price will be automatically canceled with following reasons.
1. canceled due to reference price stale – Order was canceled because the reference price used for price band validation was outdated.
2. canceled due to price band protection. Index price: `<index_price>` Price band: `<price_band>`%, Rejected price: `<maker_order_price>` – Order was about to execute at a price exceeding the allowed range
__Updated about 1 month ago
* * *
