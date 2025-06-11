---
title: Retrieve Crypto Funding Wallets
source: reference\listcryptofundingwallets.html
---

get https://paper-api.alpaca.markets/v2/wallets
Lists wallets for the account given in the path parameter. If an asset is specified and no wallet for the account and asset pair exists one will be created. If no asset is specified only existing wallets will be listed for the account. An account may have at most one wallet per asset.
