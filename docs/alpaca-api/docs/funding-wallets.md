---
title: Funding Wallets
source: docs\funding-wallets.html
---

Funding Wallets for Broker API allows you to create a dedicated wallet with a distinct account number for each user to deposit funds into.
# 
**Deposit Flow**
[](funding-wallets.html#deposit-flow)
1. If funding wallet has not yet been created, [create a funding wallet](..-reference-createfundingwallet-1.md)
2. [Retrieve funding wallet details](..-reference-getfundingwallet-1.md)
3. [Retrieve funding details for the funding wallet](..-reference-listfundingdetails-1.md)
4. Create a deposit request 
1. In sandbox, this can be simulated via this [endpoint](..-reference-demodepositfunding-1.md)
2. In production, customer initiates a deposit from the external bank to the funding details from #3
5. [Check the status of transfers](..-reference-getfundingwallettransfers-1.md)
![](https://files.readme.io/7dcb6ad-Funding_wallet_docs_explanation_Deposit2x.png)
# 
**Withdrawal Flow**
[](funding-wallets.html#withdrawal-flow)
1. If recipient bank has not yet been created, [create a recipient bank](..-reference-createfundingwalletrecipientbank-1.md)
1. Do note that depending on the country and beneficiary, the required fields might differ.
2. [Retrieve recipient bank details](..-reference-getfundingwalletrecipientbank-1.md)
3. [Create a withdrawal request](..-reference-createfundingwalletwithdrawal-1.md)
4. [Check the status of transfers](..-reference-getfundingwallettransfers-1.md)
![](https://files.readme.io/2a7393d-Funding_Wallets2x_2.png)
# 
**Statuses and Descriptions**
[](funding-wallets.html#statuses-and-descriptions)
The table below details the possible statuses and their descriptions. Transfers cannot be canceled, and `complete`, `rejected`, `failed` are terminal statuses.
Status| Description  
---|---  
Pending| The transfer is pending to be processed.  
Executed| The transfer has been sent to the bank.  
Complete| The transfer has been settled and the balances have been updated for the accounts involved in the transaction.  
Rejected| The transfer has been rejected by the bank, this is usually due to invalid input.  
Failed| The transfer has failed, this is usually due to bank errors.  
You can read more in this [blog post](https://alpaca.markets/learn/getting-started-with-funding-wallets-for-broker-api/) and our [FAQs](https://alpaca.markets/support/funding-wallets-for-broker-api-2).
# 
**FAQ**
[](funding-wallets.html#faq)
See full list of FAQs for Funding Wallets [here](https://alpaca.markets/support/funding-wallets-for-broker-api-2). 
1. **What local currencies are supported?**
The list can be found [here](https://alpaca.markets/support/funding-wallets-for-broker-api-2). For these local currencies, you can send a swift wire in that local currency for it to be converted to USD. You can also withdraw in these local currencies via a swift wire.
2. **What regions are supported for local rail deposits?**
The list can be found [here](https://alpaca.markets/support/funding-wallets-for-broker-api-2). For these regions, local transfers can be converted to USD.
3. **What regions are supported for local rail withdrawals?**
The list can be found [here](https://alpaca.markets/support/funding-wallets-for-broker-api-2). For these regions, USD can be converted to local currency and paid out locally.
4. **What regions are supported for deposits to Funding Wallets?**
The list can be found [here](https://alpaca.markets/support/funding-wallets-for-broker-api-2). For these regions, we can support deposits via both local rails and swift wires. If a region is not listed here, that means that Currency Cloud (our partner) does not accept deposits from that region due to their own internal risk rating of that region.
5. **Can I test the flow in sandbox?**
Yes the end to end flow can be tested in sandbox using the [demo deposit endpoint](..-reference-demodepositfunding-1.md) to mock receiving a push deposit in the sandbox environment. The only exception to note though is that testing the end to end flow in sandbox using local rails in the US is not currently supported. This is due to a limitation with Currencycloud that prevents us from fetching the local rail deposit instructions on a per account basis. This issue is only limited to the sandbox environment and the end to end flow is functional in the limited live and production environments.
__Updated 7 months ago
* * *
