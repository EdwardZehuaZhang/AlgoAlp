---
title: CUSIP added to API endpoints
source: changelog\cusip.html
---

* CUSIPs have been added to all corporate action types in the corporate actions endpoint. For example reverse splits now have old_cusip and new_cusip.
* The cusips filter has been added to the corporate actions endpoint that can be used to query corporate actions by CUSIP.
* CUSIP has been added as a field for non-trade activities in both the NTA SSE and activities endpoint
* CUSIP has been added as a field in the asset api
* CUSIP is now a valid path parameter when filtering assets by id
_Please note that additional licenses will be required to enable some of the items stated above. Please contact your Alpaca sales representative for further details_
