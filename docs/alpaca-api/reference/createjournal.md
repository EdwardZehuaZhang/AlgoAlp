---
title: Create a Journal
source: reference\createjournal.html
---

post https://broker-api.sandbox.alpaca.markets/v1/journals
A journal can be JNLC (move cash) or JNLS (move shares), dictated by `entry_type`. Generally, journal requests are subject to approval and starts from the `pending` status. The status changes are propagated through the Event API. Under certain conditions agreed for the partner, such journal transactions that meet the criteria are executed right away.
