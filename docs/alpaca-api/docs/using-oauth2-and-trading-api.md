---
title: Using OAuth2 and Trading API
source: docs\using-oauth2-and-trading-api.html
---

By default once you have a valid client_id and client_secret, any paper account and the live account associated with the OAuth Client will be available to connect to your app. We welcome developers to build applications and products that are powered by Alpaca while also protecting the privacy and security of our users. To build using Alpaca’s APIs, please follow the guide below.
> ## ℹ️
> 
> Note
> 
> An single Alpaca OAuth token may authorize access to either:
> 
>   * One live account
>   * One paper account
>   * One live account and one paper account
> 
> 
> For users with multiple paper accounts, the user must go through the authorization flow separately for each account they want to connect.
# 
Getting the Access Token
[](using-oauth2-and-trading-api.html#getting-the-access-token)
At a high level the flow looks like this, we will go into detail about each step
1. User requests a connection between your application and Alpaca
2. User is redirected to Alpaca to login and authorize the application from inside the dashbaord
3. Alpaca grants an authorization token to your application thorugh user-agent
4. You application then makes an access token request
5. Alpaca returns an access token grant. 
## 
1\. Request for Connection on Behalf of User
[](using-oauth2-and-trading-api.html#1-request-for-connection-on-behalf-of-user)
When redirecting a user to Alpaca to authorize access to your application, you’ll need to construct the authorization URL with the correct parameters and scopes. 
GET https://app.alpaca.markets/oauth/authorize?response_type=code&client_id=YOUR_CLIENT_ID&redirect_uri=YOUR_REDIRECT_URL&state=SOMETHING_RANDOM&scope=account:write%20trading&env=live
Here’s a list of parameters you should always specify:
Parameter| Required?| Description  
---|---|---  
`response_type`| Required| Must be `code` to request an authorization code.  
`client_id`| Required| The `client_id` you were provided with when registering your app  
`redirect_uri`| Required| The redirect URL where the user will be sent after authorization. It must match one of the whitelisted redirect URIs for your application.  
`state`| Optional| An unguessable random string, used to protect against request forgery attacks.  
`scope`| Optional| A space-delimited list of scopes your application requests access to. Read-only endpoint access is assumed by default.  
`env`| Optional| If provided, must be one of `live` or `paper`. If not specified, the user will be prompted to authorized both a live and a paper account.  
**Allowed Scopes**
Scope| Description  
---|---  
`account:write`| Write access for account configurations and watchlists.  
`trading`| Place, cancel or modify orders.  
`data`| Access to the Data API.  
## 
2\. Users Authorizing App to Access Alpaca Account
[](using-oauth2-and-trading-api.html#2-users-authorizing-app-to-access-alpaca-account)
After you redirect a user to Alpaca, we will display the following OAuth consent screen and ask the user to authorize your app to connect to their Alpaca account.
![](https://files.readme.io/06f62610cde297ce4ce76d38c3570190006ea4a6e4612eade17a658d03025b6b-Screenshot_2025-02-14_at_12.00.23_PM.png)
If you specify a value for the `env` parameter when redirecting to us, we will ask the user to authorize only a live or a paper account, depending on whether you specified `live` or `paper` respectivley.
For example, if specifying `env=paper` as a query parameter, we will show the following consent screen.
![](https://files.readme.io/9b92fd7ba5d76739d84d77054f4c37f453eb5f86a9fcfa66a57342d1bdef8dfb-Screenshot_2025-02-14_at_11.57.09_AM.png)
## 
3\. Alpaca Redirect Back to App
[](using-oauth2-and-trading-api.html#3-alpaca-redirect-back-to-app)
If the user approves access, Alpaca will redirect them back to your `redirect_uri` with a temporary `code` parameter. If you specified a state parameter in step 1, it will be returned as well. The parameter will always match the value specified in step 1. If the values don’t match, the request should not be trusted.
Example
GET https://example.com/oauth/callback?code=67f74f5a-a2cc-4ebd-88b4-22453fe07994&state=8e02c9c6a3484fadaaf841fb1df290e1
## 
4\. App Receives Authorization Code
[](using-oauth2-and-trading-api.html#4-app-receives-authorization-code)
You can then use this code to exchange for an access token.
## 
5\. App Exchanges Auth Code with Access Token
[](using-oauth2-and-trading-api.html#5-app-exchanges-auth-code-with-access-token)
After you have received the temporary `code`, you can exchange it for an access token. This can be done by making a `POST` call to `https://api.alpaca.markets/oauth/token`
### 
Parameters (All Required)
[](using-oauth2-and-trading-api.html#parameters-all-required)
Parameter| Description  
---|---  
`grant_type`| Must be set to authorization_code for an access token request.  
`code`| The authorization code received in step 4  
`client_id`| The Client ID you received when you registered the application.  
`client_secret`| The Client Secret you received when you registered the application.  
`redirect_uri`| The redirect URI you used for the authorization code request.  
> ## 🚧
> 
> Note
> 
> This request should take place behind-the-scenes from your backend server and shouldn’t be visible to the end users for security purposes.
The content type must be application/x-www-form-urlencoded as defined in RFC.
Example request:
cURL
curl -X POST https://api.alpaca.markets/oauth/token \
-d 'grant_type=authorization_code&code=67f74f5a-a2cc-4ebd-88b4-22453fe07994&client_id=fc9c55efa3924f369d6c1148e668bbe8&client_secret=5b8027074d8ab434882c0806833e76508861c366&redirect_uri=https://example.com/oauth/callback'
After a successful request, a valid access token will be returned in the response:
JSON
{
"access_token": "79500537-5796-4230-9661-7f7108877c60",
"token_type": "bearer",
"scope": "account:write trading"
}
# 
API Calls
[](using-oauth2-and-trading-api.html#api-calls)
Once you have integrated and have a valid access token you can start make calls to Alpaca Trading API v2 on behalf of the end-user.
## 
Example Requests
[](using-oauth2-and-trading-api.html#example-requests)
A 
cURL
curl https://api.alpaca.markets/v2/account /
-H 'Authorization: Bearer 79500537-5796-4230-9661-7f7108877c60'
cURL
curl https://paper-api.alpaca.markets/v2/orders /
-H 'Authorization: Bearer 79500537-5796-4230-9661-7f7108877c60'
The OAuth token can also be used for the trade update websockets stream.
{
"action": "authenticate",
"data": {
"oauth_token": "79500537-5796-4230-9661-7f7108877c60"
}
}
__Updated 4 months ago
* * *
