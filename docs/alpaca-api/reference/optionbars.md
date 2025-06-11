---
title: Historical bars
source: reference\optionbars.html
---

get https://data.alpaca.markets/v1beta1/options/bars
The historical option bars API provides aggregates for a list of option symbols between the specified dates.
The returned results are sorted by symbol first, then by bar timestamp.  
This means that you are likely to see only one symbol in your first response if there are enough bars for that symbol to hit the limit you requested.
In these situations, if you keep requesting again with the `next_page_token` from the previous response, you will eventually reach the other symbols if any bars were found for them.
