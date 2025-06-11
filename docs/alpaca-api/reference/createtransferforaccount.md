---
title: Request a New Transfer
source: reference\createtransferforaccount.html
---

post https://broker-api.sandbox.alpaca.markets/v1/accounts/{account_id}/transfers
Create a new transfer to an account to fund it.
In the sandbox environment, you can instantly deposit to or withdraw from an account with a virtual money amount. In the production environment, this endpoint is used only for requesting an outgoing (withdrawal) wire transfer at this moment. For the wire transfer (in production), you need to create a bank resource first using the Bank API. For more on how to fund an account in sandbox please check out this tutorial [here](https://alpaca.markets/learn/fund-broker-api/).
