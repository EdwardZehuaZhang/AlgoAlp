---
title: IDs added to the corporate actions endpoint
source: changelog\ids-added-to-the-corporate-actions-endpoint.html
---

### 
<> API Reference
[](ids-added-to-the-corporate-actions-endpoint.html#-api-reference)
* A new `id` field has been added to all corporate action types in the response of the [Corporate Actions](..-reference-corporateactions-1.md) endpoint.
* The `ids` filter has been added to the same endpoint that can be used to query corporate actions by ID. This filter is mutually exclusive to the other filters (e.g. symbols, types) and the number of IDs queried must be less than or equal to the `limit`.
