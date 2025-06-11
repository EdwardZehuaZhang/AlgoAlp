---
title: Update Trading Configurations for an Account
source: reference\patch-patch-v1-trading-accounts-account_id-account-configurations.html
---

patch https://broker-api.sandbox.alpaca.markets/v1/trading/accounts/{account_id}/account/configurations
You can also set the margin settings for your users’ account by passing a PATCH request. By default any account with funds under $2,000 is set a margin multiplier of 1.0, and accounts with over $2,000 are set to 2.0.
