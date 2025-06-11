---
title: List FPSL Loans
source: reference\get-v1-list-fpsl-loans.html
---

get https://broker-api.sandbox.alpaca.markets/v1/fpsl/loans
Returns a list of all FPSL loans that match the specified filter criteria, ordered in ascending order by `date`, `account_number`, and `symbol`. Each entry represents a loan of a `symbol` on a given `date`, made on behalf of the specified `account_number`.
