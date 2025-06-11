---
title: Crypto Wallets API
source: docs\crypto-wallets-api.html
---

# 
Wallets API Sandbox Testing Guide
[](crypto-wallets-api.html#wallets-api-sandbox-testing-guide)
_Please note you have to reach out to Alpaca to enable Crypto Wallets API access. Please reach out to your Customer Success Manager or your Sales Representative to enable this feature for you._
In order to test Wallets API in sandbox you’ll need to have access to a testnet wallet so that you can move coins between wallets on the blockchain without touching any real money. This tutorial walks through how to deposit GoerliETH into your external wallet which can be used for testing with Alpaca’s Wallet API.
## 
Step 1: Create a Goerli Wallet
[](crypto-wallets-api.html#step-1-create-a-goerli-wallet)
We recommend creating this via Metamask. If you don’t already have a Metamask account see the tutorial on how to create one [here](https://www.howtogeek.com/800641/how-to-add-a-metamask-wallet-to-iphone-or-android/). Once you have a Metamask account, the Goerli Test Network should be available within your list of networks by default.
![](https://files.readme.io/62daee5b67f381765f6352f74cb44f1b26ac860ddb5f96f5bddfb874872d67b6-goerli_wallet.png) ![](https://files.readme.io/11ad1581505f03f64fa854641885a6415fefc14275e645627eb8f8d7123333c0-select_goerli.png)
If it doesn’t show up as an option, you can add it by clicking “Add a network” and adding the following configurations:
`Network Name: Goerli Test Network RPC Url: https://api.infura.io/v1/jsonrpc/goerli Chain ID: 5 Symbol: ETH Block Explorer URL: https://goerli.etherscan.io`
## 
Step 2: Fund your Goerli Wallet
[](crypto-wallets-api.html#step-2-fund-your-goerli-wallet)
You’ll have to use a faucet like Goerli Faucet to receive GoerliETH. These faucets typically have a limit as to how much you can receive per day so keep that in mind when testing. Clicking on your address in Metamask will copy it to your clipboard so you can paste it into the Goerli Faucet and click “Send Me ETH”. This will initiate a transfer of 0.2 ETH to your wallet. You can then check your Metamask account to confirm the funds have been received.
![](https://files.readme.io/cf7cf984924484591576e9d6b523d944d60607aa07376727f2bb58199d373dbc-address.png) ![](https://files.readme.io/44d093e5282d6de204a8859787c3708f20f2634440eb44c00ba03e25b4f86d8c-GOERLI_FAUCET.png)
## 
Step 3: Deposit Funds to your Alpaca Wallet
[](crypto-wallets-api.html#step-3-deposit-funds-to-your-alpaca-wallet)
If you haven’t already created an ETH wallet with Alpaca’s Wallet API then you can call the `[GET /v1/accounts/:account_id/wallets?asset=ETH](https://docs.alpaca.markets/reference/listcryptofundingwallets-1)` request to create one. Once your address has been created then you can initiate the transfer of GoerliETH from your external wallet to your Alpaca wallet. You can do this in Metamask by clicking “Send” and entering your Alpaca wallet address in the “To” field.
> ## 🚧
> 
> Confirm that you are sending funds from your Goerli wallet and not a real ETH wallet. Depositing real funds to the sandbox environment could result in the permanent loss of those funds.
![](https://files.readme.io/2d46991a5e7f79099df64562ea16089f341a529bf184a99f000269f8e0e541eb-send.png)   
![](https://files.readme.io/1828501dc787cea90074bd989df37ecb0d6581534d8f23feca5e03edde09998a-send_to.png)
Follow the steps in Metamask to finish executing the transfer. Once completed, you can confirm that the funds have been sent to your Alpaca wallet by calling the `[GET /v1/accounts/:account_id/wallets/transfers](https://docs.alpaca.markets/reference/getcryptofundingtransfer-1)` request which will show the incoming transfer. 
Once the status of the transfer is COMPLETE then the funds have landed in your wallet and you have deposited your first transfer to your Alpaca wallet!
__Updated 9 months ago
* * *
