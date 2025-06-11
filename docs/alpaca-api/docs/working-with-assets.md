---
title: Working with /assets
source: docs\working-with-assets.html
---

# 
Get a List of Assets
[](working-with-assets.html#get-a-list-of-assets)
If you send a `GET` request to our `/v2/assets` endpoint, you’ll receive a list of US equities.
PythonJavaScriptC#Go
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetAssetsRequest
from alpaca.trading.enums import AssetClass
trading_client = TradingClient('api-key', 'secret-key')
# search for US equities
search_params = GetAssetsRequest(asset_class=AssetClass.US_EQUITY)
assets = trading_client.get_all_assets(search_params)
const Alpaca = require("@alpacahq/alpaca-trade-api");
const alpaca = new Alpaca();
// Get a list of all active assets.
const activeAssets = alpaca
.getAssets({
status: "active",
})
.then((activeAssets) => {
// Filter the assets down to just those on NASDAQ.
const nasdaqAssets = activeAssets.filter(
(asset) => asset.exchange == "NASDAQ"
);
console.log(nasdaqAssets);
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
// Get a list of all active assets.
var assets = await client.ListAssetsAsync(
new AssetsRequest { AssetStatus = AssetStatus.Active });
// Filter the assets down to just those on NASDAQ.
var nasdaqAssets = assets.Where(asset => asset.Exchange == Exchange.NyseMkt);
Console.Read();
}
}
}
package main
import (
"github.com/alpacahq/alpaca-trade-api-go/alpaca"
)
func init() {
alpaca.SetBaseUrl("https://paper-api.alpaca.markets")
}
func main() {
// Get a list of all active assets.
status := "active"
assets, err := alpaca.ListAssets(&status)
if err != nil {
panic(err)
}
// Filter the assets down to just those on NASDAQ.
nasdaq_assets := []alpaca.Asset{}
for _, asset := range assets {
if asset.Exchange == "NASDAQ" {
nasdaq_assets = append(nasdaq_assets, asset)
}
}
}
# 
See If a Particular Asset is Tradable on Alpaca
[](working-with-assets.html#see-if-a-particular-asset-is-tradable-on-alpaca)
By sending a symbol along with our request, we can get the information about just one asset. This is useful if we just want to make sure that a particular asset is tradable before we attempt to buy it.
PythonJavaScriptC#Go
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetAssetsRequest
trading_client = TradingClient('api-key', 'secret-key')
# search for AAPL
aapl_asset = trading_client.get_asset('AAPL')
if aapl_asset.tradable:
print('We can trade AAPL.')
const Alpaca = require("@alpacahq/alpaca-trade-api");
const alpaca = new Alpaca();
// Check if AAPL is tradable on the Alpaca platform.
alpaca.getAsset("AAPL").then((aaplAsset) => {
if (aaplAsset.tradable) {
console.log("We can trade AAPL.");
}
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
// Check if AAPL is tradable on the Alpaca platform.
try
{
var asset = await client.GetAssetAsync("AAPL");
if (asset.IsTradable)
{
Console.WriteLine("We can trade AAPL");
}
}
catch (Exception)
{
Console.WriteLine("Asset not found for AAPL.");
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
// Check if AAPL is tradable on the Alpaca platform.
asset, err := alpaca.GetAsset("AAPL")
if err != nil {
fmt.Println("Asset not found for AAPL.")
} else if asset.Tradable {
fmt.Println("We can trade AAPL.")
}
}
__Updated over 1 year ago
* * *
