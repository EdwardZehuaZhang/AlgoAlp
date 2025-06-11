---
title: Cancel a Pending Journal
source: reference\deletejournalbyid-1.html
---

delete https://broker-api.sandbox.alpaca.markets/v1/journals/{journal_id}
You can only delete a journal if the journal is still in a pending state, if a journal is executed you will not be able to delete. The alternative is to create a mirror journal entry to reverse the flow of funds.
