---
title: Example Trading App (Ribbit)
source: docs\example-trading-app-ribbit.html
---

# 
What is Ribbit?
[](example-trading-app-ribbit.html#what-is-ribbit)
Ribbit is a skeleton mobile app designed to showcase the capabilities of the Broker API. It’s a fully functional trading application that demonstrates how users would interact with your product. It uses all the different functionality that the Broker API offers including onboarding new users, funding an account, managing market data, and handling trade activity.
# 
User Experience Example
[](example-trading-app-ribbit.html#user-experience-example)
The screenshots below demonstrate how a native user would walk through Ribbit to accomplish various tasks.
## 
Create a New Account
[](example-trading-app-ribbit.html#create-a-new-account)
Once Ribbit users sign up with their email and create a password, it triggers the brokerage account onboarding process to begin. The following screens prompt users to input their information such as name, date of birth, tax ID, and more information that is required by law to open a brokerage account. At the end of this process, Ribbit calls the [Accounts API](account-opening.md) to submit all the information to Alpaca where we verify the information and approve the account application.
The app demonstrates a common flow that brokerage apps have to implement to collect all the necessary data points and required user agreements. For your own app, you may also be interested in performing various input checks on the client side so that the account approval process is as quick as possible. See below screenshots of the actual flow.
Once the account creation flow is completed, Ribbit continues to use the Accounts API to retrieve real-time information about the user’s account. The API can also be used to update the account information as well as request to close an account.
![Beginning and end state of an account opening experience](https://files.readme.io/1c28843-image.png)
Beginning and end state of an account opening experience
## 
Fund an Account
[](example-trading-app-ribbit.html#fund-an-account)
The next step for the new users is to deposit the money to start trading. Ribbit uses [Plaid](https://www.plaid.com) to validate the bank information so that Alpaca can simply link the bank account to the brokerage account. From the Plaid Link component, Ribbit receives the bank routing number and account number for the user and submits the bank link request using [ACH Relationships](..-reference-createachrelationshipforaccount.md).
As a demo app, Ribbit uses the Plaid sandbox which simulates the production environment behavior. When you try the app, use `user_good` and `pass_good` for the credentials with any banks shown in the app. Alpaca’s sandbox where Ribbit simulates the ACH transactions and the virtual money is credited in the user’s account in a moment.
Allowing your end users to connect to their personal bank and fund their account on your app can be intimidating if you aren’t familiar with the high level financial requirements and flows. Fortunately, our [Bank](..-reference-createrecipientbank.md), [ACH Relationships](..-reference-createachrelationshipforaccount.md), and [Transfers APIs](..-reference-createfundingwalletwithdrawal-1.md) make it easy to achieve this! The Bank API lets you create, retrieve, and delete bank relationships between their personal bank and their account on your app. The ACH Relationships API deals with connecting, getting, and deleting your end user’s specific bank account that will be used to initiate and receive ACH transfers from your app. Finally, the Transfers API initiates, lists, and cancels the actual transfer initiated from your app on behalf of your end user. See how this flow is implemented from your user’s perspective below.
![Example of a funding flow using Plaid](https://files.readme.io/a37a6e7-image.png)
Example of a funding flow using Plaid
## 
View and Execute Trades
[](example-trading-app-ribbit.html#view-and-execute-trades)
When it comes to managing stock market data, Alpaca provides seamless integration via the[ Market Data API](about-market-data-api.html-broker-professional.md). Ribbit uses the historical data endpoint to draw the chart in the individual stock screen, and the real-time data endpoint to show the most up-to-date price information in the order screen. See how Ribbit makes use of the Market Data API below.
![Typical screens for trading and portfolio](https://files.readme.io/acf4740-image.png)
Typical screens for trading and portfolio
In the order screen, Ribbit uses the Orders API. It allows you to submit a new order, replace/cancel an open order, and retrieve a list of orders from a user’s history. Ribbit connects to Alpaca’s sandbox environment where an order execution simulator engine runs. This simulator will take the order you submitted on the backend and execute it using the real-time market price which makes it easy to test trading functionality before you launch your app to users.
Ribbit shows all the account activities using the Activities API which returns the relevant transaction history for a given account. As a trading app, some of the important requirements to deliver to your users are monthly statements and trade confirmations. Ribbit accomplishes this by using the Documents API. The documents are generated in PDF format by Alpaca so all you need to do is call the API to retrieve the list of downloadable URLs and show them in the app.
# 
Architecture
[](example-trading-app-ribbit.html#architecture)
The end user interacts with Ribbit’s UI to achieve a task while Ribbit’s backend processes the requests by making calls to Broker API. See the diagram below for an example of how the account creation process works.
![](https://files.readme.io/cdbd289-image.png)
The backend application serves as a thin layer to proxy the API requests coming from the mobile app but makes sure each request is authorized for the appropriate user.
# 
Technology
[](example-trading-app-ribbit.html#technology)
The user interface is written in Swift for iOS and Java for Android. The backend is implemented using Go.
## 
Alpaca APIs
[](example-trading-app-ribbit.html#alpaca-apis)
All of the technology that is needed for users to interact with Ribbit’s core functionality is acheived through the Broker API. Accessing information related to the market is gathered using the Market Data API.
> ## 📘
> 
> Where Can I Access the Source Code?
> 
> The codebase is hosted on GitHub and separated into three different repositories for the implementation of the [backend](https://github.com/alpacahq/ribbit-backend),[ iOS user interface](https://github.com/alpacahq/ribbit-ios), and [Android user interface](https://github.com/alpacahq/ribbit-android).
__Updated over 1 year ago
* * *
