---
title: ACH Funding
source: docs\ach-funding.html
---

## 
Plaid Integration for Bank Transfers
[](ach-funding.html#plaid-integration-for-bank-transfers)
We have integrated with Plaid to allow you to seamlessly link your Plaid account to Alpaca. The integration will allow your end-users to verify their account instantly through Plaid’s trusted front-end module.
Leveraging this allows you to generate Plaid Processor Tokens on behalf of your end-users, which allows Alpaca to immediately retrieve a user’s bank details in order to deposit or withdraw funds on the Alpaca platform.
You can utilize your Plaid account and activate the Alpaca integration within the Plaid dashboard.
The integration requires [Plaid API Keys](https://plaid.com/docs/auth/partnerships/alpaca/)
### 
Obtaining a Plaid Processor Token
[](ach-funding.html#obtaining-a-plaid-processor-token)
A Plaid processor token is used to enable Plaid integrations with partners. After a customer connects their bank using Plaid Link, a processor token can be generated at any time. Please refer to the Plaid Processor Token using Alpaca page for creating a token and additional details.
Exchange token
curl -X POST <https://sandbox.plaid.com/item/public_token/exchange>  
-H 'Content-Type: application/json'  
-d '{  
"client_id": "PLAID_CLIENT_ID",  
"secret": "PLAID_SECRET",  
"public_token": "PUBLIC_TOKEN"  
}
Create a processor token for a specific account id.
curl -X POST <https://sandbox.plaid.com/processor/token/create>  
-H 'Content-Type: application/json'  
-d '{  
"client_id": "PLAID_CLIENT_ID",  
"secret": "PLAID_SECRET",  
"access_token": "ACCESS_TOKEN",  
"account_id": "ACCOUNT_ID",  
"processor": "alpaca"  
}
For a valid request, the API will return a JSON response similar to:
{  
"processor_token": "processor-sandbox-0asd1-a92nc",  
"request_id": "m8MDnv9okwxFNBV"  
}
### 
Processor Token Flow
[](ach-funding.html#processor-token-flow)
![](https://files.readme.io/c06c778-image.png)
1. End-user links bank account using Plaid.
2. Plaid returns a public token to you.
3. You will submit a public token to Plaid in exchange for an access token.
4. You will submit access token to Plaid’s /processor/token/create endpoint and receive Processor Token (specific to Alpaca).
5. You will make a call to the processor endpoint to pass Alpaca the processor token, to initiate the payment. To pass the processor token use the ACH relationships endpoint (Link).
#### 
Sample Request
[](ach-funding.html#sample-request)
`POST /v1/accounts/{account_id}/ach_relationships`
text
{
"processor_token": "processor-sandbox-161c86dd-d470-47e9-a741-d381c2b2cb6f"
}
#### 
Sample response
[](ach-funding.html#sample-response)
{
"id": "794c3c51-71a8-4186-b5d0-247b6fb4045e",
"account_id": "9d587d7a-7b2c-494f-8ad8-5796bfca0866",
"created_at": "2021-04-08T23:01:53.35743328Z",
"updated_at": "2021-04-08T23:01:53.35743328Z",
"status": "QUEUED",
"account_owner_name": "John Doe",
"nickname": "Bank of America Checking"
}
6. Alpaca makes a call to Plaid to retrieve the Account and Routing number* using the processor token.
7. Alpaca saves the processor token and account and routing number internally for future use. Alpaca uses account information for NACHA file creation and processing.
*Can include Auth, Identity, Balance info - if the broker API wants to initiate a transfer, we use the transfer endpoint.
### 
ACH Status Flow
[](ach-funding.html#ach-status-flow)
![](https://files.readme.io/51382cd-image.png)
__Updated about 1 year ago
* * *
