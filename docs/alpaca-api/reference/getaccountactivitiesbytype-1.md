---
title: Retrieve Account Activities of Specific Type
source: reference\getaccountactivitiesbytype-1.html
---

get https://broker-api.sandbox.alpaca.markets/v1/accounts/activities/{activity_type}
Retrieves an Array of Activies by type
If {activity_type} is provided as part of the URL, category cannot be provided as query parameter. They are mutually exclusive.
Notes:
* Pagination is handled using the `page_token` and `page_size` parameters.
* `page_token` represents the ID of the end of your current page of results.  
for example if in your first response the id of the last Activiy item returned in the array was `20220203000000000::045b3b8d-c566-4bef-b741-2bf598dd6ae7`, you'd pass that value as `page_token` to get the next page of results
* If specified with a `direction` of `desc`, for example, the results will end before the activity with the specified ID.
* If specified with a `direction` of `asc`, results will begin with the activity immediately after the one specified.
* `page_size` is the maximum number of entries to return in the response.
* If `date` is not specified, the default and maximum value is 100.
* If `date` is specified, the default behavior is to return all results, and there is no maximum page size.
