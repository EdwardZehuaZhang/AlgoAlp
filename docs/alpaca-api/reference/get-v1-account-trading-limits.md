---
title: Retrieve real-time Trading Limits for an Account
source: reference\get-v1-account-trading-limits.html
---

get https://broker-api.sandbox.alpaca.markets/v1/trading/accounts/{account_id}/limits
This endpoint is only available to accounts with the trading limits feature enabled, and not on JIT.  
The daily trading limit is set at the correspondent level (or the account level) and is used as the limit for the total amount due to Alpaca on the date of settlement.  
The limit in use returns the real time usage of this limit, based on the setup it uses the usage is calculated differently.  
If the limit in use reaches the `daily_net_limit` or `available` is zero, further purchasing activity will be halted, however, the limit can be adjusted by reaching out to Alpaca with the proposed new limit and the reason for the change.
