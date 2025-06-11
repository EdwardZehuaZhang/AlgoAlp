---
title: Get instant funding limits
source: reference\get-v1-instant-funding-correspondent-limits.html
---

get https://broker-api.sandbox.alpaca.markets/v1/instant_funding/limits
Returns globally configured limits for the correspondent. These limits are used to determine  
the maximum amount that can be extended to all accounts, and reaching this limit will result  
in further requests to create instant funding requests being rejected.
