---
title: Create an intant funding request
source: reference\post-v1-instant-funding.html
---

post https://broker-api.sandbox.alpaca.markets/v1/instant_funding
Creates an instant funding request. The request will be processed and the funds will be  
made available to the account in the form of a Memopost non trade activity. Upon settlement  
the Memoposted will be corrected to a CSD activity.
