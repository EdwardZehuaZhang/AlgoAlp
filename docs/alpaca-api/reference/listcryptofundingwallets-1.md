---
title: Retrieve Crypto Funding Wallets
source: reference\listcryptofundingwallets-1.html
---

get https://broker-api.sandbox.alpaca.markets/v1/accounts/{account_id}/wallets
Lists wallets for the account given in the path parameter. If an asset is specified and no wallet for the account and asset pair exists one will be created. If no asset is specified only existing wallets will be listed for the account. An account may have at most one wallet per asset.
