---
title: Retrieve an Onfido SDK Token
source: reference\get-v1-accounts-account_id-onfido-sdk-tokens-1.html
---

get https://broker-api.sandbox.alpaca.markets/v1/accounts/{account_id}/onfido/sdk/tokens
Get an SDK token to activate the Onfido SDK flow within your app. You will have to keep track of the SDK token so you can pass it back when you upload the SDK outcome. We recommend storing the token in memory rather than persistent storage to reduce any unnecessary overhead in your app.
