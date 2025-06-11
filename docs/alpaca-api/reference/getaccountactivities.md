---
title: Retrieve Account Activities
source: reference\getaccountactivities.html
---

get https://broker-api.sandbox.alpaca.markets/v1/accounts/activities
Returns a list of activities
Notes:
* Pagination is handled using the `page_token` and `page_size` parameters.
* `page_token` represents the ID of the last item on your current page of results.  
For example, if the ID of the last activity in your first response is `20220203000000000::045b3b8d-c566-4bef-b741-2bf598dd6ae7`, you would pass that value as `page_token` to retrieve the next page of results.
* If specified with a `direction` of `desc`, for example, the results will end before the activity with the specified ID.
* If specified with a `direction` of `asc`, results will begin with the activity immediately after the one specified.
* `page_size` is the maximum number of entries to return in the response.
* If `date` is not specified, the default and maximum value is 100.
* If `date` is specified, the default behavior is to return all results, and there is no maximum page size.
