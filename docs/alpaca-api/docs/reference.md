---
title: Authentication
source: docs.alpaca.markets\reference.html
---

# 
Live Trading
Alpaca’s live API domain is `https://api.alpaca.markets`.
Every private API call requires key-based authentication. API keys can be acquired in the developer web console. The client must provide a pair of API key ID and secret key in the HTTP request headers named `APCA-API-KEY-ID` and `APCA-API-SECRET-KEY`, respectively.
Here is an example using curl showing how to authenticate with the API.
cURL
curl -X GET \
-H "APCA-API-KEY-ID: {YOUR_API_KEY_ID}"  
-H "APCA-API-SECRET-KEY: {YOUR_API_SECRET_KEY}"  
https://{apiserver_domain}/v2/account
# 
Paper Trading
Alpaca’s paper trading service uses a different domain and different credentials from the live API. You’ll need to connect to the right domain so that you don’t run your paper trading algo on your live account.
To use the paper trading api, set `APCA-API-KEY-ID `and `APCA-API-SECRET-KEY` to your paper credentials, and set the domain to `https://paper-api.alpaca.markets`.
After you have tested your algo in the paper environment and are ready to start running your algo in the live environment, you can switch the domain to the live domain, and the credentials to your live credentials. Your algo will then start trading with real money.
To learn more about paper trading, visit the **paper trading** page.
