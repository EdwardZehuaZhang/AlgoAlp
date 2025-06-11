---
title: Create a Reverse Batch Journal Transaction (Many-to-One)
source: reference\post-v1-journals-reverse_batch.html
---

post https://broker-api.sandbox.alpaca.markets/v1/journals/reverse_batch
You can also create a batch journal request by using the following endpoint. This is enabled on JNLC for now only.
Note that if there is an invalid account_id the whole batch operation will be canceled.  
Every single request must be valid for the entire batch operation to succeed.
In the case of a successful request, the response will contain an array of journal objects with an extra attribute error_message in the case when a specific account fails to submit a journal.
