---
title: Journals API
source: docs\funding-via-journals.html
---

Journals API allows you to move cash or securities from one account to another.
For more on creating and retrieving journals please check out our [API reference section on journals](..-reference-createjournal.md).
The most common use case is [cash pooling](funding-accounts.html-cash-pooling.md), a funding model where you can send bulk wires into your firm account and then move the money into each individual user account. 
![Cash pooling funds flow](https://files.readme.io/c5b61f3-image.png)
Cash pooling funds flow
There are two types of journals:
**JNLC**  
Journal cash between accounts. You can simulate instant funding in both sandbox and production by journaling funds between your pre-funded sweep accounts and a user’s account.
You can only journal cash from a firm account to a user account and vice-versa but not from customer to customer.
**JNLS**  
Journal securities between accounts. Reward your users upon signing up or referring others by journaling small quantities of shares into their portfolios.
You can only journal securities from a firm account to a user account and not vice-versa or customer-to-customer.
## 
Journals Status
[](funding-via-journals.html#journals-status)
The most common status flow for journals is quite simple:
1. Upon creation, the journal will be created in a `queued` state.
2. Then, the journal will be `sent_to_clearing` meaning that the request has been submitted to our books and records system.
3. Lastly, if there are no issues the journal will be `executed`, meaning that the cash or securities have been successfully moved into the receiving account. 
Still, there are other cases in which the journal is `rejected`, `refused` or requires manual intervention from Alpaca's cashiering team. 
Status| Description  
---|---  
`queued`| This is the initial status when the journal is still in the queue to be processed.  
`sent_to_clearing`| The journal has been sent to be processed by Alpaca’s booking system.  
`executed`| The journal has been completed and the balances have been updated for the accounts involved in the transaction. In some rare cases, journals can be reversed from this status by Alpaca's cashiering team if the transaction is not permitted.  
`pending`| The journal is pending to be processed as it requires manual approval from Alpaca operations, for example, this can be caused by hitting the [journal limits](..-edit-broker-api-faq.md).  
`rejected`| The journal has been manually rejected.  
`canceled`| The journal has been canceled, either via an API request or by Alpaca's operations team.  
`refused`| The journal was never posted in Alpaca's ledger, probably because some of the preliminary checks failed. A common example would be a replayed request in close succession, where the first request is executed and the second request fails the balance check.  
`correct`| The journal has been manually corrected. The previously executed journal is cancelled and a new journal with the correct amount is created.  
`deleted`| The journal has been deleted from our ledger system.  
![Journal statuses flowchart](https://files.readme.io/8b024b3-image.png)
Journal statuses flowchart
__Updated over 1 year ago
* * *
