---
title: Retrieve a List of Account Documents
source: reference\getdocsforaccount.html
---

get https://broker-api.sandbox.alpaca.markets/v1/accounts/{account_id}/documents
This endpoint allows you to query all the account document based on an account ID. You can filter by date, or type of document.
These account documents are tax statements, trade confirmations, etc, generated by the Alpaca system. They are distinct from the owner documents you upload and later access via the account object's documents property.
