---
title: Close a Position for an Account
source: reference\closepositionforaccountbysymbol-1.html
---

delete https://broker-api.sandbox.alpaca.markets/v1/trading/accounts/{account_id}/positions/{symbol_or_asset_id}
Closes (liquidates) the account’s open position for the given symbol. Works for both long and short positions.
