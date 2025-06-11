---
title: Daily Processes and Reconcilations
source: docs\daily-processes-and-reconcilations.html
---

# 
Daily Processes
[](daily-processes-and-reconcilations.html#daily-processes)
There are a few daily timings you want to keep in mind when you think about the operation. Note that these schedules follow daylight savings time.
Process| Timing| Notes  
---|---|---  
Beginning-of-day Sync (BOD)| 02:15AM-02:30AM EST| Trading accounts are updated with the previous day end-of-day values. Trade confirms are also synchronized around this time.  
Incoming wire processing| 08:00AM-08:30AM EST| The incoming wires with FFC instructions are booked  
Outgoing wire cutoff| 04:00PM EST| The outgoing wire requests before the cutoff will be processed for the day.  
ACH cutoff| 02:00PM EST| The credit/debit of ACH requests before the cutoff will be processed for the day.  
Trade reporting| 06:30PM-07:30PM EST| The day’s trades are finalized and reported.  
End-of-day calculation (EOD)| 11:00PM-11:30PM EST| Close the day’s book, mark to market positions, cost basis calculation, margin requirements calculation etc.  
# 
Mandatory Corporate Actions
[](daily-processes-and-reconcilations.html#mandatory-corporate-actions)
Currently the corporate actions are processed a semi-automated way, and you will see such records in Activity API as they happen. We are working to provide upfront information separately in the future.
## 
Dividends
[](daily-processes-and-reconcilations.html#dividends)
Dividends are the most common corporate actions. The cash is paid (credited) to the customer accounts after the pay date, as we receive the cash from DTC. Please note that the actual credit transactions may be after the pay date if we don’t receive the cash from DTC. When such payout is transacted, you will see the account activity in Activity API as the DIV entry type.
Dividends are income gain. If your end customers are non-US residents, 30% withholding is applied by default. In case you claim to apply different rates for the tax treaty, please contact us.
Dividends are processed without waiting for DTC in the sandbox environment. This may not reflect the live side operation.
## 
Forward Splits and Reverse Splits
[](daily-processes-and-reconcilations.html#forward-splits-and-reverse-splits)
Share splits are processed as they happen and the beginning-of-day process will update the positions of the customer accounts. Both appear as a SPLIT entry type in the activity. In the case of reverse splits, there might be the cash in lieu for non-divisible shares which will not be processed immediately until we receive the cash from DTC.
## 
Symbol/CUSIP Change and Listing/Delisting
[](daily-processes-and-reconcilations.html#symbolcusip-change-and-listingdelisting)
The symbol or CUSIP can change one day for a particular asset. The asset master data is refreshed on a daily basis and we do recommend you retrieve the asset endpoint every morning before the market open (or after the beginning-of-day timing). While Alpaca does not currently participate in the initial public offering, such stock on the IPO day will become tradable on the day it is listed, and start filling orders once the secondary market opens.
## 
Other Events
[](daily-processes-and-reconcilations.html#other-events)
Mergers, acquisitions, and other type events are processed manually in our back office as they are rare and each case is often unique. Please contact Alpaca’s broker-dealer operation team if you have any questions.
# 
ACATS
[](daily-processes-and-reconcilations.html#acats)
Alpaca processes both sending and receiving ACATS requests. As of today, you can request our operation team for the receiving request, but we plan to provide this service as an API in the future.
# 
Monthly Processes
[](daily-processes-and-reconcilations.html#monthly-processes)
Monthly statement emails should be sent for the prior month on or before the 10th of the following month - for example, for the monthly statement for August, delivery via email must be on or prior to September 10.
__Updated 8 months ago
* * *
