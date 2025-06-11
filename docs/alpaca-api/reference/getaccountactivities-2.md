---
title: Retrieve Account Activities
source: reference\getaccountactivities-2.html
---

get https://paper-api.alpaca.markets/v2/account/activities
Returns a list of activities
Notes:
* Pagination is handled using the `page_token` and `page_size` parameters.
* `page_token` represents the ID of the last item on your current page of results.  
For example, if the ID of the last activity in your first response is `20220203000000000::045b3b8d-c566-4bef-b741-2bf598dd6ae7`, you would pass that value as `page_token` to retrieve the next page of results.
