---
title: Exercise an Options Position
source: reference\optionexercise.html
---

post https://paper-api.alpaca.markets/v2/positions/{symbol_or_contract_id}/exercise
This endpoint enables users to exercise a held option contract, converting it into the underlying asset based on the specified terms.  
All available held shares of this option contract will be exercised.  
By default, Alpaca will automatically exercise in-the-money (ITM) contracts at expiry.  
Exercise requests will be processed immediately once received. Exercise requests submitted between market close and midnight will be rejected to avoid any confusion about when the exercise will settle.  
To cancel an exercise request or to submit a Do-not-exercise (DNE) instruction, please contact our support team.
