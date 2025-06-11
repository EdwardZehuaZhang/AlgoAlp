---
title: Retrieve List of Transfers for an Account.
source: reference\gettransfersforaccount-1.html
---

get https://broker-api.sandbox.alpaca.markets/v1/accounts/{account_id}/transfers
You can query a list of transfers for an account.
You can filter requested transfers by values such as direction and status.
Returns a list of transfer entities ordered by created_at
