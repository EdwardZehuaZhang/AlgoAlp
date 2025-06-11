---
title: Deprecate the old announcements endpoint
source: changelog\deprecate-the-old-announcements-endpoint.html
---

The [old announcements endpoint](..-reference-get-v2-corporate_actions-announcements-1.md) has been deprecated in favour of the more recent [corporate actions endpoint](..-reference-corporateactions-1.md). The new endpoint offers more structured response (different schema for each corporate action type) and better overall data quality.
The version of the new endpoint has been increased from `v1beta1` to `v1`. This means that we now promise backward compatibility guarantee for the endpoint: we will not introduce breaking changes. The previous `v1beta1` version can still be used, so no migration is required if you've already been using the endpoint.
