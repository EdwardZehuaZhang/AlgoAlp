---
title: 24/5 Trading
source: docs\245-trading.html
---

**What is Overnight Trading?**
Put simply, Overnight Trading is trading from 8 PM to 4 AM EST Sunday through Thursday. The overnight trading session allows us to provide trading 24/5 for all NMS securities.
* * *
**How does it work?**
Overnight trade executions and market data are provided by [Blue Ocean Alternative Trading System (BOATS)](https://brokercheck.finra.org/firm/summary/306512). BOATS is an Alternative Trading System (ATS) which runs an overnight trading session on its own systems, outside traditional stock exchanges.
* * *
**What is the timing for the overnight session?**
The overnight session bridges the gap between post-market and pre-market trading. The trading sessions are as follows:
Monday- Friday
Overnight: 8PM-4AM EST (Please note that the overnight session starts on the previous day)  
Pre-market: 4AM – 9:30AM EST  
Regular market: 9:30AM-4PM EST  
After-hours: 4PM-8PM EST
Holidays
The overnight session follows the NYSE calendar. When there is a market holiday there will not be an overnight session on the night of the same trade date. 
Example: On April 18th, 2025 there was a holiday, the overnight session didn't open between April 17 8PM to April 18 4AM session as that would be considered the trade date of the 18th.
The overnight session does not follow half days when applicable to NYSE. On those occasions there will be a complete 8PM-4AM session."
* * *
**How do we access overnight trading?**
Please contact your CSM for details on pricing and steps for enabling it for your correspondent.
* * *
**How do we display Market Data?**
We have partnered with Blue Ocean for real time data, we provide a high accuracy indicative feed, please ask for further information from your CSM.
* * *
**Are there any restrictions?**
1. Only LIMIT orders are available. Other order types are not available in the overnight session.
2. TIF Day orders will remain open until the end of the trading day. If un-filled, the order will be automatically cancelled at 8PM EST.
3. TIF GTC orders are currently unavailable.
4. Margin usage is not available in the overnight session. If your order’s dollar amount exceeds your Cash Buying Power, the order will be rejected.
* * *
**What is the integration work required?**
_Assets API_
1. Two new attributes introduced: overnight_tradable and overnight_halted
* overnight_tradable - represents the asset that is eligible for overnight trading
* overnight_halted - represents the asset that could be tradable but halted from active trading (like in the case of corporate actions)
_Market Data API_
1. A new feed has been introduced named 'overnight'
* * *
**How is day trading affected?**
1. Day trades will count within the overnight window. The following rules apply:
* Trades placed in the overnight session between 8PM and 11:59PM are marked with a trade date of T+1. 
* Trades placed in the overnight session between 12AM and 4AM are marked with a trade date of T.  
Example: A trade executed at 9:00PM EST on Monday will have a trade date of Tuesday and will settle on Wednesday (T+1)  
Similary, a trade that executes at 2:00PM EST on Tuesday will have a trade date of Tuesday and will settle on T+1 which is Wednesday.
2. DTBP resets at 8pm
3. DTBP does not apply during the overnight trading session
* * *
**What is tradable in the overnight session?**
All NMS securities are tradable on the overnight session. OTC securities are not part of NMS, and are therefore currently untradable. Assets that are tradable in the overnight session will exposed to you via the Assets API as Overnight_tradable.
* * *
**Which order types are supported?**
Only limit orders are currently supported in overnight trading.
* * *
**Is fractional trading supported during the overnight session?**
Yes, they work the same way as current Extended Hours orders.
* * *
**Are there any limitations on orders?**
1. Only limit orders are currently supported in Extended Hours trading.
2. Currently we only support ""Day"" for TIF (Time in Force) in Extended Hours trading, with plans to add support for GTC soon."
* * *
**Will Corporate Actions(CA) have any effect on overnight trading?**
A pending CA may halt a security from trading whilst it is being processed.
Important to note that due to the way trades are dated during the overnight session, purchasing a stock in overnight trading on the ex-dividend date will not entitle you to that stock’s dividend.
* * *
**Is there any change to the settlement of the asset?**
The overnight session marks the beginning of a new trading day. Therefore, any trades executed between 8:00PM and 12:00AM EST are assigned a trade date corresponding to the next calendar day and will settle on a T+1 basis based on that trade date.
Example: A trade executed at 9:00PM EST on Monday will have a trade date of Tuesday and will settle on Wednesday (T+1)
Similary, a trade that executes at 2:00PM EST on Tuesday will have a trade date of Tuesday and will settle on T+1 which is Wednesday.
* * *
**What happens if my order is not filled overnight?**
If your order is not filled overnight, it will continue into the pre-market session. This means your order remains active and eligible to be executed during both extended and regular trading hours for the same trade day.
* * *
**What are the new attributes introduced in the Assets API related to overnight trading?**
1. Overnight_tradable: represents that an asset is tradable in the overnight session
2. Overnight_halted: represents whether an asset has been halted from active trading in the overnight session
* * *
The content of this article is for general information only and is believed to be accurate as of the posting date, but may be subject to change. Alpaca does not provide investment, tax, or legal advice. Please consult your own independent advisor as to any investment, tax, or legal statements made herein.
Orders placed outside regular trading hours (9:30 a.m. – 4:00 p.m. ET) may experience price fluctuations, partial executions, or delays due to lower liquidity and higher volatility. Orders not designated for extended hours execution will be queued for the next trading session. Additionally, fractional trading may be limited during extended hours. For more details, please review [Alpaca’s Extended Hours Trading Risk Disclosure](https://files.alpaca.markets/disclosures/library/ExtHrsRisk.pdf).
All investments involve risk, and the past performance of a security, or financial product does not guarantee future results or returns. There is no guarantee that any investment strategy will achieve its objectives. Please note that diversification does not ensure a profit, or protect against loss. There is always the potential of losing money when you invest in securities, or other financial products. Investors should consider their investment objectives and risks carefully before investing.
Securities brokerage services are provided by Alpaca Securities LLC (""Alpaca Securities""), member [FINRA](https://www.finra.org/)/[SIPC](https://www.sipc.org/), a wholly-owned subsidiary of AlpacaDB, Inc. Technology and services are offered by AlpacaDB, Inc.
Cryptocurrency services are made available by Alpaca Crypto LLC (""Alpaca Crypto""), a FinCEN registered money services business (NMLS # 2160858), and a wholly-owned subsidiary of AlpacaDB, Inc. Alpaca Crypto is not a member of SIPC or FINRA. Cryptocurrencies are not stocks and your cryptocurrency investments are not protected by either FDIC or SIPC. Please see the[ Disclosure Library](https://alpaca.markets/disclosures) for more information.
This is not an offer, solicitation of an offer, or advice to buy or sell securities or cryptocurrencies or open a brokerage account or cryptocurrency account in any jurisdiction where Alpaca Securities or Alpaca Crypto, respectively, are not registered or licensed, as applicable."
* * *
__Updated about 1 month ago
* * *
