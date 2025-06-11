---
title: Working with /positions
source: docs\working-with-positions.html
---

You can view the positions in your portfolio by making a `GET` request to the `/v2/positions` endpoint. If you specify a symbol, you’ll see only your position for the associated stock.
PythonJavaScriptC#Go
from alpaca.trading.client import TradingClient
trading_client = TradingClient('api-key', 'secret-key')
# Get our position in AAPL.
aapl_position = trading_client.get_open_position('AAPL')
# Get a list of all of our positions.
portfolio = trading_client.get_all_positions()
# Print the quantity of shares for each position.
for position in portfolio:
print("{} shares of {}".format(position.qty, position.symbol))
const Alpaca = require("@alpacahq/alpaca-trade-api");
const alpaca = new Alpaca();
// Get our position in AAPL.
aaplPosition = alpaca.getPosition("AAPL");
// Get a list of all of our positions.
alpaca.getPositions().then((portfolio) => {
// Print the quantity of shares for each position.
portfolio.forEach(function (position) {
console.log(`${position.qty} shares of ${position.symbol}`);
});
});
using Alpaca.Markets;
using System;
using System.Linq;
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
// Get our position in AAPL.
var aaplPosition = await client.GetPositionAsync("AAPL");
// Get a list of all of our positions.
var positions = await client.ListPositionsAsync();
// Print the quantity of shares for each position.
foreach (var position in positions)
{
Console.WriteLine($"{position.Quantity} shares of {position.Symbol}.");
}
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
// Get our position in AAPL.
aapl_position, err := alpaca.GetPosition("AAPL")
if err != nil {
fmt.Println("No AAPL position.")
} else {
fmt.Printf("AAPL position: %v shares.\n", aapl_position.Qty)
}
// Get a list of all of our positions.
positions, err := alpaca.ListPositions()
if err != nil {
fmt.Println("No positions found.")
} else {
// Print the quantity of shares for each position.
for _, position := range positions {
fmt.Printf("%v shares in %s", position.Qty, position.Symbol)
}
}
}
The current price reflected will be based on the following:
**4:00 am ET - 9:30 am ET** \- Last trade based on the premarket 
**9:30 am ET - 4pm ET** \- Last trade
**4:00 pm ET - 10:00 pm ET** \- Last trade based on after-hours trading 
**10 pm ET - 4:00 am ET next trading day** \- Official closing price from the primary exchange at 4 pm ET.
__Updated over 1 year ago
* * *
