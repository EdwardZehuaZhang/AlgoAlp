---
title: Introduce activity_sub_type
source: changelog\introduce-activity_sub_type-in-get-activities.html
---

## 
<> API Reference
[](introduce-activity_sub_type-in-get-activities.html#-api-reference)
### 
Activities API
[](introduce-activity_sub_type-in-get-activities.html#activities-api)
* The `GET /activities` response payload now includes a new optional field `activity_sub_type`. This field provides a more detailed classification, in addition to the existing `activity_type` field.
* A new `entry_type`, **OPCA** (Options Corporate Action), has been introduced to improve the classification and reporting of options corporate action activities.
* For further details, refer to the Activities API documentation: 
* [Activities API - Trading](..-reference-getaccountactivities-2.md)
* [Activities API - Broker](..-reference-getaccountactivities.md)
