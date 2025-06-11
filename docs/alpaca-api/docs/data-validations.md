---
title: Data Validations
source: docs\data-validations.html
---

As part of Alpaca Securities LLC’s regulatory obligation to comply with new reporting requirements defined by FINRA, we are required to submit user information to comply with FINRA’s Customer & Account Information System (CAIS). The CAIS system will begin validating the data for correct formatting so we need to ensure that data is provided in correct format at the time of account creation to avoid errors and potential delays with reporting. 
This validation will be live in production on **March 25, 2024**. The validation will be released in sandbox first on **March 5, 2024** so you can carry out any testing required.
## 
Validation Criteria
[](data-validations.html#validation-criteria)
A validation check on user information submitted via the account creation ([POST /v1/accounts](..-reference-createaccount-1.md)) and update ([PATCH /v1/accounts/{account_id}](..-reference-patchaccount-1.md)) endpoints will return a 422 error if the information submitted does not meet our validation criteria. The validation criteria will include the following:
* Name and Address Romanization 
* `given_name`, `middle_name`, `family_name`, `street_address`, `unit`, `city`, `state`, `postal_code`, `email_address`, and `tax_id` are all required to be provided in latin characters. The accepted input for these fields will be limited to ASCII character range 32-126
* We have introduced the following fields to continue accepting name and address information in its original script if desired - `local_given_name`, `local_middle_name`, `local_family_name`, `local_street_address`, `local_unit`, `local_city`, and `local_state`
* `given_name` is now required for all users
* Tax ID Number Validation 
* `tax_id` is required for securities accounts
* If the tax ID type is `USA_SSN` or `USA_TIN` then the following must be met: 
* No values having an Area Number (first three digits) of 000 nor 666.
* No values having a Group Number (middle two digits) of 00.
* No values having a Serial Number (last four digits) of 0000.
* No values all of the same digit such as 000-00-0000, 111-11-1111, 333-33-3333, 666-66- 6666, 999-99-9999, nor all increasing or decreasing characters i.e. 123-45-6789 or 987-65-4321.
* Values must be exactly 9 characters in length after dashes have been stripped
* All tax ID types will undergo the following validation: 
* The length must be greater than 1 character i.e. submitting 0 as a tax ID will not be permitted
* No values all of the same digit such as 000-00-0000, 111-11-1111, 333-33-3333, 666-66- 6666, 999-99-9999, nor all increasing or decreasing characters i.e. 123-45-6789 or 987-65-4321.
* Max length of 40 characters
* Only letters, digits, dashes (denoted by ASCII char 45), periods, and plus (+) signs will be permitted
* Value most contain digits (i.e. submitting TIN_NOT_ISSUED or xxx-xxx-xxxx will not be permitted) 
* As a general reminder to our partners that onboard users in regions where tax ID numbers are not issued, there is still a requirement for a unique identifier to be submitted for those users. The identifier should be either a national identity card number, passport number, permanent resident number, drivers license number, etc. We have introduced the following tax_id_type values to support these classifications. These are also available in our documentation [here](..-reference-createaccount-1.md). 
* `NATIONAL_ID`
* `PASSPORT`
* `PERMANENT_RESIDENT`
* `DRIVER_LICENSE`
* `OTHER_GOV_ID`
* `street_address` Validation 
* No values consisting of only digits
* Length must be greater than 1 character
* Postal Code Validation 
* If country of tax residence = USA: 
* The `postal_code` attribute will be required upon account creation
* No values less than 5 characters in length and the first 5 characters must only contain digits
* No values greater than 10 digits
* `date_of_birth` Validation 
* No values greater than or less than 10 characters in length. Values must be in YYYY-MM-DD format.
* Email addresses, after aliases are removed, are restricted to a maxim of 60 characters in length. Alpaca defines an alias as all characters after a + sign and before the @ sign.
* State Validation 
* For all countries 
* The max length for state should not be greater than 50 characters
* State cannot consist of only digits. It can be alphanumeric
* If country of tax residence = USA 
* State will be limited to either the 2 letter abbreviation code for the state or the complete name of the state as defined in our documentation [here](domestic-usa-accounts.md)
* The `city` attribute cannot consist of only digits. It can be alphanumeric
* Whitespace validation 
* The following validation will be applied to the `given_name`, `middle_name`, `family_name`, `street_address`, `unit`, `city`, `state`, `postal_code`, `email_address`, `tax_id_type`, and `tax_id` fields on the Accounts API: 
* The space character, denoted by ASCII character 32, will be the only whitespace character we accept
* Leading and trailing spaces present in the string will return a 422 error
* Additionally, we will be cleaning up the existing accounts in our system that contain invalid whitespace characters. We will follow up directly with the affected partners and share the complete list of accounts and data points that we will be updating.
__Updated about 1 year ago
* * *
