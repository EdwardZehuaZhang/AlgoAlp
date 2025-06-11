---
title: Retrieve the Market Calendar
source: reference\querymarketcalendar-1.html
---

get https://broker-api.sandbox.alpaca.markets/v1/calendar
The calendar API serves the full list of market days from 1970 to 2029. It can also be queried by specifying a start and/or end time to narrow down the results. In addition to the dates, the response also contains the specific open and close times for the market days, taking into account early closures.
