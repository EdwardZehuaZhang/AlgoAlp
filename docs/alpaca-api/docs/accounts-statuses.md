---
title: Accounts Statuses
source: docs\accounts-statuses.html
---

The following are the possible account status values. Accounts will have both `status` and `crypto_status` with `status` denoting the account's equities trading status and `crypto_status` denoting the account's crypto trading status.
Most likely, the account status is `ACTIVE` unless there is an issue. The account status may get to `ACCOUNT_UPDATED` when personal information is being updated from the API, in which case the end user may not be allowed trading for a short period of time until the change is approved.
For more on creating an account check out our [API reference section on the Accounts Endpoint](..-reference-createaccount-1.md). 
status| description  
---|---  
`INACTIVE`| Account not set to trade given asset.  
`ONBOARDING`| The account has been created but we haven’t performed KYC yet. This is only used with Onfido.  
`SUBMITTED`| The account application has been submitted and is being processed, this is a transitory status.  
`SUBMISSION_FAILED`| The account failed to be created in Alpaca's system. Accounts in this status are resolved by Alpaca and no further action is needed.  
`ACTION_REQUIRED`| The account application requires manual action and a document upload is required from the user. KYCResults contains information about the details.  
`APPROVAL_PENDING`| The application requires manual checks from our team because the account did not pass the KYC automatic check, but most likely no document is required. KYCResults contains information about the details.  
`APPROVED`| The account application has been approved, waiting to be ACTIVE, this is a transitory status.  
`REJECTED`| The account application was rejected by our team. The account will not be able to continue to go active.  
`ACTIVE`| The account is fully active and can start trading the enabled asset.  
`ACCOUNT_UPDATED`| The account personal information is being updated which needs to be reviewed before being moved back to ACTIVE.  
`ACCOUNT_CLOSED`| The account was closed, will not be able to trade or fund anymore.  
![Account statuses flowchart](https://files.readme.io/49871fe-image.png)
Account statuses flowchart
## 
Account Updated
[](accounts-statuses.html#account-updated)
Please note that outgoing transfers are restricted while in this status.
To move accounts from `ACCOUNT_UPDATED` back to `ACTIVE`, Alpaca will handle the process manually. The specific nature of the update will determine the necessary actions to be taken for returning to `ACTIVE` status. For non-material updates, the accounts will be regularly moved back to `ACTIVE` without requiring any action from the end-user or partner.
For material updates, additional documentation or confirmation will be needed, such as IDs, W8BEN corrections, address verifications, or new CIP reports. The required documents and instructions will be communicated to our partners accordingly.
Edits to the below fields will trigger a status change to `ACCOUNT_UPDATED`:
* given_name
* family_name
* street_address
* unit
* city
* state
* postal_code
* country_of_citizenship
* employer_name
* employment_position
* if any of the following disclosures are set to true when they were previously false then that triggers account_updated as well 
* is_control_person
* is_politically_exposed
* immediate_family_exposed
* is_affiliated_exchange_or_finra
__Updated about 1 year ago
* * *
