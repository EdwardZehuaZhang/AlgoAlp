---
title: Request options trading for an account (BETA)
source: reference\requestoptionsforaccount.html
---

post https://broker-api.sandbox.alpaca.markets/v1/accounts/{account_id}/options/approval
This endpoint requests options trading for an account.  
Following submission, an assigned administrator will review the request.  
Upon approval, the account's options_approved_level parameter will be modified, granting the account the ability to participate in options trading.  
Note: This endpoint is only available for partners who have been enabled for Options BETA.
