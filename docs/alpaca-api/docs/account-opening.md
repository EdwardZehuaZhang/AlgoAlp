---
title: Customer Account Opening
source: docs\account-opening.html
---

# 
Trading/Investing App and RIA
[](account-opening.html#tradinginvesting-app-and-ria)
In this use case, Alpaca is responsible for the account approval step, while you can own the user experiences for collecting the end-customer information. We require you to collect a set of the information required for our approval process.
Upon the POST request, the account status starts from `SUBMITTED` status. Alpaca system will run the automatic KYC process asynchronously and update the KYC result as the account status. You can receive such updates in the [Event API](..-reference-subscribetotransferstatussse.md) stream.
If all KYC information is verified without problems, the account status will be `APPROVED` and shortly transition to `ACTIVE`. In some cases, if the final approval is pending, the account status becomes `APPROVAL_PENDING` which will transition to `APPROVED` once it is approved. In the case of some action is required, the status becomes `ACTION_REQUIRED` and you will receive the reason for this. In most cases, you will need to collect additional information from the end user. One example would be that the residential address is not verified, so a copy of a document such as a utility bill needs to be uploaded. You can use [Document API](..-reference-getdocsforaccount.md) to upload additional documents when requested.
# 
Fully-Disclosed Broker-Dealer
[](account-opening.html#fully-disclosed-broker-dealer)
As a reminder, in this setup, you are required to have a proper broker-dealer license in your local jurisdiction and you are the broker on the record. Alpaca relies on your KYC process to open customers' accounts which you will send via the [CIP API](..-reference-post-v1-accounts-account_id-cip.md).
In this case, as soon as a `POST` request is made and all fields are validated, we will first screen the account against our internal list of blacklisted accounts and an exact, or similar, match against this list will result in the account moving to either `REJECTED` or `APPROVAL_PENDING`. If there is no match then the account status starts from `APPROVED` status, meaning you have approved the account opening. Therefore, you need to complete your KYC for the account before making the `POST` request.
# 
Omnibus Broker-Dealer
[](account-opening.html#omnibus-broker-dealer)
In an omnibus setup, you will not request any new account opening. Your trading accounts will be set up by Alpaca when the go-live is approved. That said, you may want to simulate this structure using [Account API](..-reference-createaccount-1.md) and you can open as many accounts as you want in the sandbox environment even if you are an omnibus.
# 
Account Type
[](account-opening.html#account-type)
Alpaca currently opens all accounts as margin accounts. We support individual taxable accounts and business accounts. Other types of accounts such as cash and IRA accounts are on our roadmap.
Even though all accounts at Alpaca are margin accounts, you have the ability to set accounts to be cash accounts (100% buying power) to disable margin trading for your users through account configurations [here](..-reference-patch-patch-v1-trading-accounts-account_id-account-configurations-1.md).
__Updated about 1 year ago
* * *
