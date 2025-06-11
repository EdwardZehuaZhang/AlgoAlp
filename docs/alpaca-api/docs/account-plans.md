---
title: Trading Account
source: docs\account-plans.html
---

# 
Alpaca Brokerage Account (Live Trading)
[](account-plans.html#alpaca-brokerage-account-live-trading)
After creating an Alpaca Paper Only Account, you can enable live trading by becoming an Alpaca Brokerage Account holder. This requires you to go through an account on-boarding process with Alpaca Securities LLC, a FINRA member and SEC registered broker-dealer. We now support brokerage accounts for individuals and business entities from around the world.
With a brokerage account, you will be able to fully utilize Alpaca for your automated trading and investing needs. Using the Alpaca API, you’ll be able to buy and sell stocks in your brokerage account, and you’ll receive real-time consolidated market data. In addition, you will continue to be able to test your strategies and simulate your trades in our paper trading environment. And with the Alpaca web dashboard, it’s easy to monitor both your paper trading and your real money brokerage account. All accounts are opened as margin accounts. Accounts with $2,000 or more equity will have access to margin trading and short selling.
## 
Individuals
[](account-plans.html#individuals)
Alpaca Securities LLC supports individual taxable brokerage accounts. At this time, we do not support retirement accounts.
## 
Businesses/Incorporated Entities
[](account-plans.html#businessesincorporated-entities)
You can open a business trading account to use Alpaca for trading purposes, but not for building apps/services.
> ## 👀
> 
> Alpaca currently accepts entities that are _Corporations_ , _LLCs_ and _Partnerships_ in the U.S., and around the world. There is a $50,000 minimum deposit required for opening a business account at Alpaca.
# 
Markets Supported
[](account-plans.html#markets-supported)
Currently, Alpaca only supports trading of listed U.S. stocks and select cryptocurrencies.
# 
The Account Object
[](account-plans.html#the-account-object)
The account API serves important information related to an account, including account status, funds available for trade, funds available for withdrawal, and various flags relevant to an account’s ability to trade.
An account maybe be blocked for just for trades (`trading_blocked` flag) or for both trades and transfers (`account_blocked` flag) if Alpaca identifies the account to be engaging in any suspicious activity. Also, in accordance with FINRA’s pattern day trading rule, an account may be flagged for pattern day trading (`pattern_day_trader` flag), which would inhibit an account from placing any further day-trades.
Please note that cryptocurrencies are not eligible assets to be used as collateral for margin accounts and will require the asset be traded using cash only.
## 
Sample Object
[](account-plans.html#sample-object)
JSON
{
"account_blocked": false,
"account_number": "010203ABCD",
"buying_power": "262113.632",
"cash": "-23140.2",
"created_at": "2019-06-12T22:47:07.99658Z",
"currency": "USD",
"crypto_status": "ACTIVE",
"non_marginable_buying_power": "7386.56",
"accrued_fees": "0",
"pending_transfer_in": "0",
"pending_transfer_out": "0",
"daytrade_count": "0",
"daytrading_buying_power": "262113.632",
"equity": "103820.56",
"id": "e6fe16f3-64a4-4921-8928-cadf02f92f98",
"initial_margin": "63480.38",
"last_equity": "103529.24",
"last_maintenance_margin": "38000.832",
"long_market_value": "126960.76",
"maintenance_margin": "38088.228",
"multiplier": "4",
"pattern_day_trader": false,
"portfolio_value": "103820.56",
"regt_buying_power": "80680.36",
"short_market_value": "0",
"shorting_enabled": true,
"sma": "0",
"status": "ACTIVE",
"trade_suspended_by_user": false,
"trading_blocked": false,
"transfers_blocked": false
}
## 
Account Properties
[](account-plans.html#account-properties)
Attribute| Type| Description  
---|---|---  
`id`| string| Account ID.  
`account_number`| string| Account number.  
`status`| string<account_status>| See detailed account statuses below  
`crypto_status`| string<account_status>| The current status of the crypto enablement. See detailed crypto statuses below.  
`currency`| string| "USD"  
`cash`| string| Cash balance  
`portfolio_value`| string| **[Deprecated]** Total value of cash + holding positions (Equivalent to the equity field)  
`non_marginable_buying_power`| string| Current available non-margin dollar buying power  
`accrued_fees`| string| The fees collected.  
`pending_transfer_in`| string| Cash pending transfer in.  
`pending_transfer_out`| string| Cash pending transfer out  
`pattern_day_trader`| boolean| Whether or not the account has been flagged as a pattern day trader  
`trade_suspended_by_user`| boolean| User setting. If `true`, the account is not allowed to place orders.  
`trading_blocked`| boolean| If `true`, the account is not allowed to place orders.  
`transfers_blocked`| boolean| If `true`, the account is not allowed to request money transfers.  
`account_blocked`| boolean| If `true`, the account activity by user is prohibited.  
`created_at`| string| Timestamp this account was created at  
`shorting_enabled`| boolean| Flag to denote whether or not the account is permitted to short  
`long_market_value`| string| Real-time MtM value of all long positions held in the account  
`short_market_value`| string| Real-time MtM value of all short positions held in the account  
`equity`| string| `cash` \+ `long_market_value` \+ `short_market_value`  
`last_equity`| string| Equity as of previous trading day at 16:00:00 ET  
`multiplier`| string| Buying power (BP) multiplier that represents account margin classification  
Valid values:  
\- **1** (standard limited margin account with 1x BP),  
\- **2** (reg T margin account with 2x intraday and overnight BP; this is the default for all non-PDT accounts with $2,000 or more equity),  
\- **4** (PDT account with 4x intraday BP and 2x reg T overnight BP)  
`buying_power`| string| Current available $ buying power; If multiplier = 4, this is your daytrade buying power which is calculated as (last _equity - (last) maintenance_margin)_ 4; If multiplier = 2, buying _power = max(equity – initial_margin,0)_ 2; If multiplier = 1, buying_power = cash  
`initial_margin`| string| Reg T initial margin requirement (continuously updated value)  
`maintenance_margin`| string| Maintenance margin requirement (continuously updated value)  
`sma`| string| Value of special memorandum account (will be used at a later date to provide additional buying_power)  
`daytrade_count`| int| The current number of daytrades that have been made in the last 5 trading days (inclusive of today)  
`last_maintenance_margin`| string| Your maintenance margin requirement on the previous trading day  
`daytrading_buying_power`| string| Your buying power for day trades (continuously updated value)  
`regt_buying_power`| string| Your buying power under Regulation T (your excess equity - equity minus margin value - times your margin multiplier)  
# 
Account Status ENUMS
[](account-plans.html#account-status-enums)
The following are the possible account status values. Most likely, the account status is `ACTIVE` unless there is an issue. The account status may get to `ACCOUNT_UPDATED` when personal information is being updated from the dashboard, in which case you may not be allowed trading for a short period of time until the change is approved.
status| description  
---|---  
`ONBOARDING`| The account is onboarding.  
`SUBMISSION_FAILED`| The account application submission failed for some reason.  
`SUBMITTED`| The account application has been submitted for review.  
`ACCOUNT_UPDATED`| The account information is being updated.  
`APPROVAL_PENDING`| The final account approval is pending.  
`ACTIVE`| The account is active for trading.  
`REJECTED`| The account application has been rejected.  
__Updated over 1 year ago
* * *
