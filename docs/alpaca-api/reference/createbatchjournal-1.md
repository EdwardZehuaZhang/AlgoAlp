---
title: Create a Batch Journal Transaction (One-to-Many)
source: reference\createbatchjournal-1.html
---

post https://broker-api.sandbox.alpaca.markets/v1/journals/batch
You can create a batch of journal requests by using this endpoint. This is enabled on JNLC type Journals for now only.
Every single request must be valid for the entire batch operation to succeed.
In the case of a successful request, the response will contain an array of journal objects with an extra attribute error_message in the case when a specific account fails to receive a journal.
