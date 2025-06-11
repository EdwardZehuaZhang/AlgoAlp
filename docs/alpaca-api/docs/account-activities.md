---
title: Account Activities
source: docs\account-activities.html
---

# 
The TradeActivity Object
[](account-activities.html#the-tradeactivity-object)
## 
Sample TradeActivity
[](account-activities.html#sample-tradeactivity)
JSON
{
"activity_type": "FILL",
"cum_qty": "1",
"id": "20190524113406977::8efc7b9a-8b2b-4000-9955-d36e7db0df74",
"leaves_qty": "0",
"price": "1.63",
"qty": "1",
"side": "buy",
"symbol": "LPCN",
"transaction_time": "2019-05-24T15:34:06.977Z",
"order_id": "904837e3-3b76-47ec-b432-046db621571b",
"type": "fill"
}
## 
Properties
[](account-activities.html#properties)
Attribute| Type| Description  
---|---|---  
`activity_type`| string| For trade activities, this will always be `FILL`  
`cum_qty`| string| The cumulative quantity of shares involved in the execution.  
`id`| string| An ID for the activity. Always in `::` format. Can be sent as `page_token` in requests to facilitate the paging of results.  
`leaves_qty`| string| For `partially_filled` orders, the quantity of shares that are left to be filled.  
`price`| string| The per-share price that the trade was executed at.  
`qty`| string| The number of shares involved in the trade execution.  
`side`| string| `buy` or `sell`  
`symbol`| string| The symbol of the security being traded.  
`transaction_time`| string| The time at which the execution occurred.  
`order_id`| string| The id for the order that filled.  
`type`| string| `fill` or `partial_fill`  
# 
The NonTradeActivity (NTA) Object
[](account-activities.html#the-nontradeactivity-nta-object)
## 
Sample NTA
[](account-activities.html#sample-nta)
JSON
{
"activity_type": "DIV",
"id": "20190801011955195::5f596936-6f23-4cef-bdf1-3806aae57dbf",
"date": "2019-08-01",
"net_amount": "1.02",
"symbol": "T",
"cusip": "C00206R102",
"qty": "2",
"per_share_amount": "0.51"
}
## 
Properties
[](account-activities.html#properties-1)
Attribute| Type| Description  
---|---|---  
`activity_type`| string| See below for a list of possible values.  
`id`| string| An ID for the activity. Always in `::` format. Can be sent as `page_token` in requests to facilitate the paging of results.  
`date`| string| The date on which the activity occurred or on which the transaction associated with the activity settled.  
`net_amount`| string| The net amount of money (positive or negative) associated with the activity.  
`symbol`| string| The symbol of the security involved with the activity. Not present for all activity types.  
`cusip`| string| The CUSIP of the security involved with the activity. Not present for all activity types.  
`qty`| string| For dividend activities, the number of shares that contributed to the payment. Not present for other activity types.  
`per_share_amount`| string| For dividend activities, the average amount paid per share. Not present for other activity types.  
# 
Pagination of Results
[](account-activities.html#pagination-of-results)
Pagination is handled using the `page_token` and `page_size` parameters. 
`page_token` represents the ID of the end of your current page of results. If specified with a direction of desc, for example, the results will end before the activity with the specified ID. If specified with a direction of `asc`, results will begin with the activity immediately after the one specified. `page_size` is the maximum number of entries to return in the response. If `date` is not specified, the default and maximum value is 100. If `date` is specified, the default behavior is to return all results, and there is no maximum page size.
# 
Activity Types
[](account-activities.html#activity-types)
`activity_type`| Description  
---|---  
`FILL`| Order fills (both partial and full fills)  
`TRANS`| Cash transactions (both CSD and CSW)  
`MISC`| Miscellaneous or rarely used activity types (All types except those in TRANS, DIV, or FILL)  
`ACATC`| ACATS IN/OUT (Cash)  
`ACATS`| ACATS IN/OUT (Securities)  
`CFEE`| Crypto fee  
`CSD`| Cash deposit(+)  
`CSW`| Cash withdrawal(-)  
`DIV`| Dividends  
`DIVCGL`| Dividend (capital gain long term)  
`DIVCGS`| Dividend (capital gain short term)  
`DIVFEE`| Dividend fee  
`DIVFT`| Dividend adjusted (Foreign Tax Withheld)  
`DIVNRA`| Dividend adjusted (NRA Withheld)  
`DIVROC`| Dividend return of capital  
`DIVTW`| Dividend adjusted (Tefra Withheld)  
`DIVTXEX`| Dividend (tax exempt)  
`FEE`| Fee denominated in USD  
`INT`| Interest (credit/margin)  
`INTNRA`| Interest adjusted (NRA Withheld)  
`INTTW`| Interest adjusted (Tefra Withheld)  
`JNL`| Journal entry  
`JNLC`| Journal entry (cash)  
`JNLS`| Journal entry (stock)  
`MA`| Merger/Acquisition  
`NC`| Name change  
`OPASN`| Option assignment  
`OPEXP`| Option expiration  
`OPXRC`| Option exercise  
`PTC`| Pass Thru Charge  
`PTR`| Pass Thru Rebate  
`REORG`| Reorg CA  
`SC`| Symbol change  
`SSO`| Stock spinoff  
`SSP`| Stock split  
__Updated 3 months ago
* * *
