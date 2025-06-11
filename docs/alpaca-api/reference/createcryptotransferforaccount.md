---
title: Request a New Withdrawal
source: reference\createcryptotransferforaccount.html
---

post https://paper-api.alpaca.markets/v2/wallets/transfers
Creates a withdrawal request. Note that outgoing withdrawals must be sent to a whitelisted address and you must whitelist addresses at least 24 hours in advance. If you attempt to withdraw funds to a non-whitelisted address then the transfer will be rejected.
