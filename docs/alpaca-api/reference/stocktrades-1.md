---
title: Historical trades
source: reference\stocktrades-1.html
---

get https://data.alpaca.markets/v2/stocks/trades
The historical stock trades API provides trade data for a list of stock symbols between the specified dates.
The returned results are sorted by symbol first then by trade timestamp.  
This means that you are likely to see only one symbol in your first response if there are enough trades for that symbol to hit the limit you requested.
In these situations, if you keep requesting again with the `next_page_token` from the previous response, you will eventually reach the other symbols if any trades were found for them.
