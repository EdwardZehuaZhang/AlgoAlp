---
title: Account Status Events for KYCaaS
source: docs\account-status-events-for-kycaas.html
---

For partners who utilize Alpaca’s KYC service for opening brokerage accounts, if an account is moved to `ACTION_REQUIRED` or `APPROVAL_PENDING` then that indicates that additional action may be needed from you or your user to approve the account. These status updates, along with the reason for the status change, will be relayed in real time via the [Account Status Events](..-reference-suscribetoaccountstatussse.md). The specific KYC results that may require action from your end user will wind up in `ACCEPT`, `INDETERMINATE`, or `REJECT`. The `additional_information` field will be used to relay custom messages from our account opening team. If a KYC result is returned via the `ACCEPT` object then no further action is needed to resolve the request. KYC results returned in the `INDETERMINATE` or `REJECT` objects will require further action before the account can be opened. The following tables can be used to determine what is required from the account opener.
**Documentation Required**
KYC Result Code| Government Issued ID Card| Tax ID Card| Statement (utility bill, etc.)| Selfie  
---|---|---|---|---  
`IDENTITY_VERIFICATION`| **REQUIRED**| | |   
`TAX_IDENTIFICATION`| | **REQUIRED**| |   
`ADDRESS_VERIFICATION`| OPTIONAL| | OPTIONAL|   
`DATE_OF_BIRTH`| **REQUIRED**| | |   
`SELFIE_VERIFICATION`| | | | **REQUIRED**  
**Additional Information Required**
KYC Result Code| Additional Information Required  
---|---  
`PEP`| Job title / occupation and address  
`FAMILY_MEMBER_PEP`| Name of politically exposed person if immediate family  
`CONTROL_PERSON`| Company name, company address, and company email  
`AFFILIATED`| Company / firm name, company / firm address, company / firm email  
`VISA_TYPE_OTHER`| Visa type and expiration date  
`W8BEN_CORRECTION`| An updated W8BEN form with corrected information  
`OTHER`| For specific cases our operational team might return with a customized message within the additional_information attribute.  
__Updated about 1 year ago
* * *
