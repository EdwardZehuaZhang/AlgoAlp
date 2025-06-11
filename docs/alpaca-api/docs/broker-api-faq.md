---
title: Broker API FAQs
source: docs.alpaca.markets\docs\broker-api-faq.html
---

# 
Broker API vs. Trading API
### 
What is the Difference Between Trading API and Broker API?
The Broker API is meant to support different use cases for Broker-Dealers, RIAs, and Trading/Investing applications, [see more here](/docs/use-cases).
Instead, the Trading API is meant for Retail users and algotraders to communicate with Alpaca’s brokerage service, [see more here](https://alpaca.markets/docs/api-references/trading-api/).
### 
Is the Authentication Different Between Trading API and Broker API?
Yes, the way a client authenticates with the Broker API is different than the Trading API.
With the Broker API, you’ll need to encode the keys and pass an authentication header that looks like this:
`Authorization: Basic <base64 encoded keys>`
[see more here](https://alpaca.markets/docs/api-references/broker-api/#authentication-and-rate-limit).
The same Broker API credentials with HTTP basic authentication can be used to access Market Data API, as described [here](/docs/about-market-data-api#broker-api).
# 
Accounts
### 
When Do the Values on the Accounts Trading Get Updated?
All the values that **do not** have the prefix - “last_“ are updated Real-Time post trade executions and Corp Action activities. Might update outside market hours as well, post-trade settlements and FEE calculations like REG/TAF fee.
# 
Assets
### 
What is the difference between Tradable and Status Boolean in the Assets API?
### 
[Assets](https://alpaca.markets/docs/api-references/broker-api/assets/#asset-states)
There are some scenarios to consider here:
#### 
`tradable=true` and `status=active`
This is the scenario for most of the stocks listed. For example Apple Inc. This means it's tradable - both BUY and SELL are possible on this stock.
#### 
`tradable=false` and `status=active`
This is one of the rare conditions where we don't allow new opening transactions and only allow closing transactions. This usually happens when an asset is delisted from a US stock exchange and trades over the counter.
#### 
`tradable=false` and `status=inactive`
This is a scenario which can be achieved during the delisting of a company. If a stock is delisted, it is not tradable, which means we neither allow a `BUY` nor a `SELL` order for that particular stock. A delisted stock is either auto-liquidated or users are informed to close the positions within a specific amount of time.
### 
Can OTC tickers be traded?
Yes, you can always close any open positions.
### 
Are OTC symbols available in the Market Data?
No. OTC Market Data requires partners to directly have an agreement with OTC Markets. Once that is done, we can enable the same for our partners.
### 
Is there a way to differentiate between Stocks and ETFs in the Assets API?
Alpaca at this point in time does not support any categorization of Stocks and ETFs. Partner needs to categorize them personally using the names and symbols.
### 
How often does Alpaca refresh the assets master?
Alpaca refreshes the assets master 3 times per day. The 3 refresh times are outside of market hours, with the last refresh scheduled at 8:20 AM ET. If you are storing the list of assets locally, we recommend refreshing it from Alpaca at least once per day, preferably after 8:20 AM ET but before 9:30 AM ET.
# 
Events
### 
How Many SSE Connections Can be Alive Concurrently?
A maximum of **25** connection requests are allowed. Post that you will receive _“Too many requests“_ error.
### 
After How Long Will the SSE Connection Close?
There is no such time. Alpaca would never stop responding, hence we also send “ _heartbeat_ “ to let partners know that the connection is alive. Sometimes the connections are un-knowingly closed by client-networks or network error happens. Nonetheless, you can always re-open and request data after a particular event using `since_id` or `since`.
### 
What is the Use-case for SSE?
Server-sent events can be useful when you want updates on the status of a certain transaction, without making multiple HTTP requests. Events endpoints will return multiple responses when you open a connection, and can also be used in a restful way to make sure you didn’t miss any event.
1. Account Status Updates - [Subscribe to Account Status Events (SSE)](/reference/suscribetoaccountstatussse)
2. Trade Updates - [Subscribe to Trade Events (SSE)](/reference/subscribetotradesse)
3. Journal Updates - [Subscribe to Journal Events (SSE)](/reference/subscribetojournalstatussse)
4. Any Transfer Event - [Subscribe to Transfer Events (SSE)](/reference/subscribetotransferstatussse)
5. Any relevant Non-Trading Activity - [Subscribe to Non-Trading Activities Events (SSE)](/reference/get-v1-events-nta)
# 
Market Data
### 
Does the Market Data API support corporate actions adjustments?
Yes, price adjustments are visible on the Market Data, you'll just need to make sure the adjustment parameter is set to all. The available query parameters for bars are available here - [Historical bars](/reference/stockbars#:~:text=adjustment,for%20the%20stocks.)
### 
Does the Market Data API support local currencies?
Yes. You can retrieve historical market data in the supported local currencies.
# 
Documents
### 
How are trade confirmations and account statements handled by Alpaca and its partners?
1. Both of them need to be mailed to users with [[email protected]](/cdn-cgi/l/email-protection#d4b5a1a0bbf9b5a6b7bcbda2b1f9b6b094b9b5bdb8b1a6fab5b8a4b5b7b5fab9b5a6bfb1a0a7) in BCC.
2. The email should contain the truncated alpaca account number and language as mentioned in the Statement and Confirms Document.
3. If sharing a customized statement or confirmation, in that case, the partner must allow users to have access to the original statements and confirms generated by Alpaca.
### 
When are these documents available?
Daily Trade Confirmations are available on the next day after the BOD job is finished(02:15 AM-02:30 AM EST).
Monthly statements are available after the 1st weekend of the next month.
### 
How can I retrieve these documents?
[Documents | Alpaca Docs](https://alpaca.markets/docs/api-references/broker-api/documents/#retrieving-documents-for-one-account)
Query the above-mentioned endpoint with `type` as `account_statement` or `trade_confirmation`.
### 
Can I find a sample W-8 Ben Form and what details are needed to be filled in?
Can be found here - <https://github.com/alpacahq/bkdocs/files/7756721/W-8Ben_Example_Broker_Docs.pdf>
### 
I’m getting a 400 error (request body format is invalid: JSON: cannot unmarshal object into Go value of type entities.BrokerAccountDocumentUploads) when uploading a W8-Ben. Is this expected?
Yes, the body of the request is an array of documents, make sure you’re using square brackets like in the sample response [Documents | Alpaca Docs](https://alpaca.markets/docs/api-references/broker-api/documents/#sample-request).
# 
Journals
### 
How much time does JNLC’s or Journal usually take?
Most of the time, JNLCs are pretty fast and mostly instantaneous, with a sub-second average delay before the execution is complete. 
There can be a delay of a few hours when exceeding the limits mentioned below.
### 
JNLC with larger amounts are executed the next day. Is this expected?
Yes. We have a limit called the JNLC Transaction Limit. This is the maximum amount of journaling you can do instantaneously. Any amount of journal greater than this would be executed as a part of the BOD job of the next day. The default value is $50.
This is a safeguard mechanism to prevent LARGE withdrawals for any user to prevent partners from the same. This is a “Configurable“ value that can be set to anything on the Sandbox but would require a discussion for the PROD.
There is also a JNLC Daily Limit, which is the summation of all the JNLC done in a day. If the limit is $1000(Default Limit), you can do 10 transactions of $100 each, but the 11th one would not pass. This is a “Configurable“ value that can be set to anything on the Sandbox but would require a discussion for the PROD.
### 
Can I subscribe to a journal status streaming without having to check it again and again?
Absolutely yes. You can listen to the journal server-sent events. - [Events | Alpaca Docs](https://alpaca.markets/docs/api-references/broker-api/events/#journal-status)
## 
What are the use cases for the JNLS?
JNLS are usually used to Reward users for signing up on the platform by our partners.
## 
What is the direction and flow of JNLS?
JNLS can ONLY be done from the SWEEP ACCOUNT to the USER ACCOUNT and not vice-versa. Once, done, it can’t be sent back.
## 
Is the JNLS transactional limit per account configurable?
Yes, they are configurable.
## 
Are JNLS transactional limits per account USD or Stocks based?
They are USD-based.
# 
Trading
## 
Orders
### 
What is the minimum order value?
All buy orders must have a minimum market value of 1$ or the request will be rejected with a 422. Sell orders do not have this validation, so you can close any open position.
### 
What is the precision for notional and qty in the order request body?
A maximum of **2 decimal places** for _notional_ and **9 decimal places** for _qty_ should be used to send orders.
### 
Only limit is allowed as the order type for OCO. Does this rule apply to OTO?
No. OCO implements an order cancellation and hence it might be very difficult to cancel a market order. Whereas in the case of OTO, that isn't an issue and hence _market_ and _limit_ both orders are allowed!
### 
Order replacement is supported for OCO to update limit_price and stop_price.
Can we update the quantity as well? And can we use a notional amount instead of quantity?
Yes, you can update the quantity while patching the order using this API - [Orders | Alpaca Docs](https://alpaca.markets/docs/api-references/broker-api/trading/orders/#patching-an-order) .
No, you can't use the notional amount. The reason for this is, that Alpaca at this point of time **doesn't** support _LIMIT_ orders for _notional_ orders and since OCO orders can only be a _LIMIT_ order, it makes it compulsory to use the **quantity**.
### 
What orders can be cancelled?
We check that the order is in an "open" status before attempting to cancel it.  
The [statuses](https://alpaca.markets/docs/trading/orders/#order-lifecycle "https://alpaca.markets/docs/trading/orders/#order-lifecycle") that we consider open are:
* Accepted
* New
* Partially Filled
* Calculated
* Pending New
* Pending Cancel
* Pending Replace
* Accepted for Bidding
If the order is in one of these statuses you should receive a 204 (unless there was a server error) while if it isn't you're going to receive a 422, as mentioned in the docs.  
To check if the order was actually canceled, I suggest you check its status on the trades SSE or through the REST endpoints.
## 
Trade Settlement
### 
Why is there no cash_withdrawable and cash_transferable increase after selling a stock?
Settlement occurs one business day after the day the order executes, or T+1 (trade date plus one business day). For example, if you were to execute an order on Monday, it would typically settle on Tuesday. The `cash` is updated post the SELL trade is filled, but the `cash_withdrawable` and `cash_transferable` are updated post T+1.
### 
What are some fees, that can be expected while trading stocks?
#### 
REG and TAF Fees
This is charged(REG and TAF individually) to a User Account, every time a SELL Order is executed. This is charged by Alpaca but, is a pass thru fee from the FINRA and SEC itself that is levied to Alpaca on sell orders. The REG and TAF fees change rates periodically. More about this can be read in the blog from our co-founder - [REG/TAF Fee Updates with Alpaca](https://alpaca.markets/blog/reg-taf-fees/)
#### 
ADR Fees
Most ADRs charge a fee of $0.01 to $0.03 per share once or twice a year in order to cover the administrative costs associated with running the ADR program. ADR fees may be charged less frequently depending on how the depository bank runs the ADR program.
ADR fees are charged to clients typically once a month after we are charged by our depository.  
The record date on the charge is usually the month before the actual date of the charge. Even if the client has since liquidated their shares, they will still be charged an ADR fee if they held shares on the record date.
#### 
Rounding rules
We will not charge the ADR fee if the calculated fee is less than a penny. However, if the amount is over a penny we will always round up to the next highest penny. For example, if the charge is .02 cents a share and the client owns 10.1 shares we would charge the client .21 for the ADR fee.
# 
Rebalancing
### 
Can I enter manual trades while using the Rebalancing API?
If the account is subscribed to a portfolio, it cannot execute manual trades or [manual rebalance runs](https://alpaca.markets/docs/api-references/broker-api/rebalancing/#create-run-manual-rebalancing-event "https://alpaca.markets/docs/api-references/broker-api/rebalancing/#create-run-manual-rebalancing-event"). Still, you can [delete the subscription](https://alpaca.markets/docs/api-references/broker-api/rebalancing/#unsubscribe-account-delete-subscription "https://alpaca.markets/docs/api-references/broker-api/rebalancing/#unsubscribe-account-delete-subscription") to execute manual trades or rebalance runs.
### 
How can I see the orders triggered by a rebalancing event?
You can easily retrieve [all the runs with this endpoint](https://alpaca.markets/docs/api-references/broker-api/rebalancing/#list-all-runs "https://alpaca.markets/docs/api-references/broker-api/rebalancing/#list-all-runs") or [a particular run by its ID](https://alpaca.markets/docs/api-references/broker-api/rebalancing/#get-run-by-id "https://alpaca.markets/docs/api-references/broker-api/rebalancing/#get-run-by-id"), where each run will have an array with all the orders that were executed and the ones that failed or were skipped.
# 
Important Links and Reads
1. Alpaca Daily Processes and Reconciliations - [Daily Processes and Reconcilations](/docs/daily-processes-and-reconcilations)
2. PDT - [User Protection](/docs/user-protection#pattern-day-trader-pdt-protection-at-alpaca)
3. Margins - [Margin and Short Selling](/docs/margin-and-short-selling)
4. Understanding Orders and Time in Force - [Orders at Alpaca](/docs/orders-at-alpaca)
* * *
##### 
Securities brokerage services are provided by Alpaca Securities LLC ("Alpaca Securities"), member [FINRA](https://www.finra.org/)/[SIPC](https://www.sipc.org/), a wholly-owned subsidiary of AlpacaDB, Inc. Technology and services are offered by AlpacaDB, Inc.
##### 
This is not an offer, solicitation of an offer, or advice to buy or sell securities or open a brokerage account in any jurisdiction where Alpaca Securities is not registered (Alpaca Securities is registered only in the United States).
__Updated 3 months ago
* * *
