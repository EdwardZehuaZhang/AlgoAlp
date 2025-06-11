---
title: Retrieve Aggregate Positions
source: reference\get-v1-reporting-eod-aggregate_positions-1.html
---

get https://broker-api.sandbox.alpaca.markets/v1/reporting/eod/aggregate_positions
This API endpoint provides reporting data to partners for aggregate common stock and crypto positions across their account base. Partners can view historical snapshots of their holding across their entire account base. Please note that this API utilizes an 8:00 pm (EST) cutoff which aligns with the end of the Securities extended hours trading session as well as Alpaca’s 24 hour Crypto trading window. Additionally, the endpoint supports indexing to help the partner efficiently filter by key information including date and symbol while being able to include or remove firm accounts.
