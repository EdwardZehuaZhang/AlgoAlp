---
title: Retrieve Daily Trading Limits
source: reference\get-v1-transfers-jit-limits-1.html
---

get https://broker-api.sandbox.alpaca.markets/v1/transfers/jit/limits
The JIT Securities daily trading limit is set at the correspondent level and is used as the limit for the total amount due to Alpaca on the date of settlement. The limit in use returns the real time usage of this limit and is calculated by taking the net of trade and non-trade activity inflows and outflows. If the limit in use reaches the daily net limit, further purchasing activity will be halted, however, the limit can be adjusted by reaching out to Alpaca with the proposed new limit and the reason for the change.
