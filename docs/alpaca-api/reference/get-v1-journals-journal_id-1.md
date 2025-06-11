---
title: Retrieve a Single Journal Entry
source: reference\get-v1-journals-journal_id-1.html
---

get https://broker-api.sandbox.alpaca.markets/v1/journals/{journal_id}
You can query a specific journal entry that you submitted to Alpaca by passing into the query the journal_id.
Will return a journal entry if a journal entry with journal_id exists, otherwise will throw an error.
