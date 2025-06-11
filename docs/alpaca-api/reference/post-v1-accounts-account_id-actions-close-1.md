---
title: Close an Account
source: reference\post-v1-accounts-account_id-actions-close-1.html
---

post https://broker-api.sandbox.alpaca.markets/v1/accounts/{account_id}/actions/close
This operation closes an active account. The underlying records and information of the account are not deleted by this operation.
**Before closing an account, you are responsible for closing all the positions and withdrawing all the money associated with that account. Learn more in the Positions Documentation.**
