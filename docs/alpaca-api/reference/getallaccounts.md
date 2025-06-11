---
title: Get All Accounts
source: reference\getallaccounts.html
---

get https://broker-api.sandbox.alpaca.markets/v1/accounts
Retrieves the first 1000 accounts that match the query parameters.  
Sorting is based on creation time.  
The created_after/created_before query parameters can be used to paginate the results.  
To further limit the size of the response, the entities query parameter can be used to specify which properties are included in the response.
