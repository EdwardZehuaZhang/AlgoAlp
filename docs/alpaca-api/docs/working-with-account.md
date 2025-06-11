---
title: Working with /account
source: docs\working-with-account.html
---

# 
View Account Information
[](working-with-account.html#view-account-information)
By sending a `GET` request to our `/v2/account` endpoint, you can see various information about your account, such as the amount of buying power available or whether or not it has a PDT flag.
PythonJavaScriptC#Go
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetAssetsRequest
trading_client = TradingClient('api-key', 'secret-key')
# Get our account information.
account = trading_client.get_account()
# Check if our account is restricted from trading.
if account.trading_blocked:
print('Account is currently restricted from trading.')
# Check how much money we can use to open new positions.
print('${} is available as buying power.'.format(account.buying_power))
const Alpaca = require("@alpacahq/alpaca-trade-api");
const alpaca = new Alpaca();
// Get our account information.
alpaca.getAccount().then((account) => {
// Check if our account is restricted from trading.
if (account.trading_blocked) {
console.log("Account is currently restricted from trading.");
}
// Check how much money we can use to open new positions.
console.log(`$${account.buying_power} is available as buying power.`);
});
using Alpaca.Markets;
using System;
using System.Threading.Tasks;
namespace CodeExamples
{
internal static class Example
{
private static string API_KEY = "your_api_key";
private static string API_SECRET = "your_secret_key";
public static async Task Main(string[] args)
{
// First, open the API connection
var client = Alpaca.Markets.Environments.Paper
.GetAlpacaTradingClient(new SecretKey(API_KEY, API_SECRET));
// Get our account information.
var account = await client.GetAccountAsync();
// Check if our account is restricted from trading.
if (account.IsTradingBlocked)
{
Console.WriteLine("Account is currently restricted from trading.");
}
Console.WriteLine(account.BuyingPower + " is available as buying power.");
Console.Read();
}
}
}
package main
import (
"fmt"
"github.com/alpacahq/alpaca-trade-api-go/alpaca"
)
func init() {
alpaca.SetBaseUrl("https://paper-api.alpaca.markets")
}
func main() {
// Get our account information.
account, err := alpaca.GetAccount()
if err != nil {
panic(err)
}
// Check if our account is restricted from trading.
if account.TradingBlocked {
fmt.Println("Account is currently restricted from trading.")
}
// Check how much money we can use to open new positions.
fmt.Printf("%v is available as buying power.\n", account.BuyingPower)
}
# 
View Gain/Loss of Portfolio
[](working-with-account.html#view-gainloss-of-portfolio)
You can use the information from the account endpoint to do things like calculating the daily profit or loss of your account.
PythonJavaScriptC#Go
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetAssetsRequest
trading_client = TradingClient('api-key', 'secret-key')
# Get our account information.
account = trading_client.get_account()
# Check our current balance vs. our balance at the last market close
balance_change = float(account.equity) - float(account.last_equity)
print(f'Today\'s portfolio balance change: ${balance_change}')
const Alpaca = require("@alpacahq/alpaca-trade-api");
const alpaca = new Alpaca();
// Get account information.
alpaca.getAccount().then((account) => {
// Calculate the difference between current balance and balance at the last market close.
const balanceChange = account.equity - account.last_equity;
console.log("Today's portfolio balance change:", balanceChange);
});
using Alpaca.Markets;
using System;
using System.Linq;
using System.Threading;
using System.Threading.Tasks;
// With the Alpaca API, you can check on your daily profit or loss by
// comparing your current balance to yesterday's balance.
namespace GetPnLExample
{
internal class GetPnL
{
private static string API_KEY = "your_api_key";
private static string API_SECRET = "your_secret_key";
public static async Task Main(string[] args)
{
// First, open the API connection
var client = Alpaca.Markets.Environments.Paper
.GetAlpacaTradingClient(new SecretKey(API_KEY, API_SECRET));
// Get account info
var account = await client.GetAccountAsync();
// Check our current balance vs. our balance at the last market close
var balance_change = account.Equity - account.LastEquity;
Console.WriteLine($"Today's portfolio balance change: ${balance_change}");
}
}
}
package main
import (
"fmt"
"log"
"github.com/alpacahq/alpaca-trade-api-go/alpaca"
)
func main() {
alpaca.SetBaseUrl("https://paper-api.alpaca.markets")
// Get account information.
account, err := alpaca.GetAccount()
if err != nil {
log.Fatalln(err)
}
// Calculate the difference between current balance and balance at the last market close.
balanceChange := account.Equity.Sub(account.LastEquity)
fmt.Println("Today's portfolio balance change:", balanceChange)
}
__Updated about 1 year ago
* * *
