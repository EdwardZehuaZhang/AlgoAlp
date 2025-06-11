---
title: FIX Specification
source: docs\fix-messages.html
---

Version 1.0.4
## 
Supported Message Types
[](fix-messages.html#supported-message-types)
Message| MsgType| Description  
---|---|---  
[Logon](fix-messages.html-logon-a.md)| A| Sent by FIX client to authenticate and establish the FIX session  
[Heartbeat](fix-messages.html-heartbeat-0.md)| 0| Sent by either client or server at preset interval within the working FIX session  
[Test Request](fix-messages.html-test-request-1.md)| 1| Sent to force a heartbeat from the opposing application  
[Resend Request](fix-messages.html-resend-request-2.md)| 2| To request retransmission of messages which were missed  
[Reject](fix-messages.html-reject-3.md)| 3| Response to a message that could not be processed  
[Sequence Reset](fix-messages.html-sequence-reset-4.md)| 4| To reset the FIX session sequence number  
[Logout](fix-messages.html-logout-5.md)| 5| To safely disconnect the connected FIX session  
[New Order - Single](fix-messages.html-new-order-single-d.md)| D| To submit a new single order  
[Execution Report](fix-messages.html-execution-report-8.md)| 8| Sent whenever the state of the order changes  
[Order Cancel Request](fix-messages.html-order-cancel-request-f.md)| F| To request cancellation of an order  
[Order Cancel/Replace Request](fix-messages.html-order-cancelreplace-request-g.md)| G| To request modification of an order  
[Order Cancel Reject](fix-messages.html-order-cancel-reject-9.md)| 9| Sent if the Order Cancel Request (F) or Order Cancel/Replace Request (G) could not be executed  
## 
Message Header
[](fix-messages.html#message-header)
All messages should contain the following tags in the header:
Tag| Field| Mandatory| Description  
---|---|---|---  
8| BeginString| Y| FIX.4.2  
9| BodyLength| Y| Size of the message body in bytes  
34| MsgSeqNum| Y| Message sequence number  
35| MsgType| Y| Message type, should be one of the types supported in this doc  
49| SenderCompID| Y| Provided by Alpaca, must be present in all FIX messages. This will be returned as TargetCompID (56) in all FIX messages to clients  
52| SendingTime| Y| UTC timestamp of message transmission. Precision supported: Millis, Micros, Nanos  
56| TargetCompID| Y| Provided by Alpaca, must be present in all FIX messages. This will be returned as SenderCompID (49) in all FIX messages to clients  
## 
Message Trailer
[](fix-messages.html#message-trailer)
All messages should contain the following tags in the trailer:
Tag| Field| Mandatory| Description  
---|---|---|---  
10| CheckSum| Y| Last field in the messages with trailing `<SOH>`. Value calculated by the FIX engine from message data  
## 
Logon (A)
[](fix-messages.html#logon-a)
Tag| Field| Mandatory| Description  
---|---|---|---  
35| MsgType| Y| A - For Logon  
98| EncryptMethod| Y| 0 - None, only accepted value  
108| HeartBtInt| Y| Must be set to `30` for 30 seconds  
141| ResetSeqNumFlag| N| Y - Resets both sender and target sequence number to 1  
**Example FIX Message**
Logon (A)
|8=FIX.4.2|9=73|35=A|34=1|49=SENDER|52=20240524-16:02:42.003|56=ALPACA|98=0|108=30|141=Y|10=131|
## 
Heartbeat (0)
[](fix-messages.html#heartbeat-0)
Sent by either client or server if no message has been received since the last heartbeat interval. This is also sent in response to a Test Request (1).
Tag| Field| Mandatory| Description  
---|---|---|---  
35| MsgType| Y| 0 - For Heartbeat  
112| TestReqID| N| Required only when Heartbeat is sent in response to a Test Request (1)  
**Example FIX Message**
Heartbeat
|8=FIX.4.2|9=91|35=0|49=SENDER|56=ALPACA|34=2|52=20230330-16:52:321.029|10=049|
## 
Test Request (1)
[](fix-messages.html#test-request-1)
May be sent by either client or server, to force a Heartbeat (0) from the other party.
Tag| Field| Mandatory| Description  
---|---|---|---  
35| MsgType| Y| 1 - For Test Request  
112| TestReqID| Y| Identifier to be returned in the resulting Heartbeat (0)  
**Example FIX Message**
Test Request
|8=FIX.4.2|9=91|35=1|49=SENDER|56=ALPACA|34=2|52=20230330-16:52:321.029|112=TEST|10=049|
## 
Resend Request (2)
[](fix-messages.html#resend-request-2)
Sent to request retransmission of messages which were missed.
Tag| Field| Mandatory| Description  
---|---|---|---  
35| MsgType| Y| 2 - For Resend Request  
7| BeginSeqNo| Y| Beginning sequence number of requested messages  
16| EndSeqNo| Y| Ending sequence number of requested messages  
**Example FIX Message**
Resend Request
|8=FIX.4.2|9=66|7=9|16=36|34=12|35=2|49=SENDER|52=20230627-14:10:21.769|56=ALPACA|10=126|
## 
Reject (3)
[](fix-messages.html#reject-3)
Sent when a message is rejected or cannot be processed by the FIX server.
Tag| Field| Mandatory| Description  
---|---|---|---  
35| MsgType| Y| 3 - For Reject  
45| RefSeqNum| Y| Sequence number of the rejected message  
58| Text| N| Reason for rejection  
371| RefTagID| N| The tag number of the FIX field being referenced  
372| RefMsgType| N| The MsgType (35) of the FIX message being referenced  
373| SessionRejectReason| N| Reject reason codes.  
0 - Invalid tag number  
1 - Required tag missing  
2 - Tag not defined for this message type  
3 - Unsupported Message Type  
4 - Tag specified without a value  
5 - Value is incorrect (out of range) for this tag  
6 - Incorrect data format for value  
9 - CompID problem  
10 - SendingTime accuracy problem  
11 - Invalid MsgType  
**Example FIX Message**
Reject
|8=FIX.4.2|9=0134|35=3|34=44196|49=ALPACA|56=TARGET|52=20230330-20:18:38.039|58=0005 Tag specified without a value|45=44196|371=11|372=8|373=4|10=092|
## 
Sequence Reset (4)
[](fix-messages.html#sequence-reset-4)
Sent to reset the incoming sequence number on the other side. The sequence reset should be used only to increase the sequence number. Any request to decrease the sequence number will result in a Reject (3) message.
Tag| Field| Mandatory| Description  
---|---|---|---  
35| MsgType| Y| 4 - For Sequence Reset  
36| NewSeqNo| Y| New sequence number  
123| GapFillFlag| N| N - Sequence reset to recover from an out-of-sequence condition, MsgSeqNum(34) is ignored  
Y - Gap fill message, MsgSeqNum(34) field must be valid  
**Example FIX Message**
Sequence Reset
|8=FIX.4.2|9=61|34=12|35=4|36=9|49=SENDER|52=20230627-14:14:51.732|56=ALPACA|10=156|
## 
Logout (5)
[](fix-messages.html#logout-5)
May be sent by either client or server, to terminate the session. The other party would respond with a confirming Logout message as an acknowledgement.
Tag| Field| Mandatory| Description  
---|---|---|---  
35| MsgType| Y| 5 - For Logout  
**Example FIX Message**
Logout
|8=FIX.4.2|9=56|34=12|35=5|49=SENDER|52=20230627-14:16:50.690|56=ALPACA|10=197|
## 
New Order - Single (D)
[](fix-messages.html#new-order---single-d)
Sent by the client to submit a new single order.
Tag| Field| Mandatory| Description  
---|---|---|---  
35| MsgType| Y| D - For New Order - Single  
1| Account| Y| Account number  
11| ClOrdID| Y| Unique identifier of the order assigned by the client (must be no longer than 48 characters)  
12| Commission| N| Commission to collect from the account holder  
13| CommType| N| 1 - per share  
2 - percentage, 5% should be represented as .05  
3 - absolute  
18| ExecInst| N| 1 - Not held  
5 - Held  
21| HandlInst| Y| 1 - Automated execution with no broker intervention, only accepted value  
38| OrderQty| N| Number of shares to trade, required if CashOrderQty (152) is not set  
40| OrdType| Y| 1 - Market  
2 - Limit  
3 - Stop  
4 - Stop limit  
5 - Market on close  
B - Limit on close  
44| Price| N| Required for Limit `40=2` and Stop Limit `40=4` orders  
54| Side| Y| 1 - Buy  
2 - Sell  
55| Symbol| Y| Ticker symbol  
59| TimeInForce| Y| 0 - Day (day)  
1 - Good Till Cancel (gtc)  
2 - At the Opening (opg)  
3 - Immediate or Cancel (ioc)  
4 - Fill or Kill (fok)  
7 - At the Close (cls)  
60| TransactTime| Y| UTC timestamp of order creation by client  
77| OpenClose| N| Indicates whether the resulting position from the trade would be an opening or closing position.  
O - Open  
C - Close  
99| StopPx| N| Required for Stop `40=3` and Stop Limit `40=4` orders  
109| ClientID| N| Sub-account tag for omnibus accounts  
152| CashOrderQty| N| Notional value to trade, required if OrderQty (38) is not set  
336| TradingSessionID| N| 8 - Extended Hours  
Required for extended hours orders only  
**Example FIX Messages**
Market order (quantity based)Market order (notional based)Limit orderStop orderStop limit orderExtended Hours Order
|8=FIX.4.2|9=139|1=TEST_ACCOUNT|11=c5bfc5f6-163d-450e-bb4a-fb25188cde8e|34=12|35=D|38=10|40=1|49=SENDER|52=20230613-14:01:37.330|54=1|55=SPY|56=ALPACA|59=1|10=030|
|8=FIX.4.2|9=141|1=TEST_ACCOUNT|11=c5bfc5f6-163d-450e-bb4a-fb25188cde8e|34=12|35=D|40=1|49=SENDER|52=20230613-14:43:47.572|54=1|55=SPY|56=ALPACA|59=0|152=100|10=130|
|8=FIX.4.2|9=149|1=TEST_ACCOUNT|11=c5bfc5f6-163d-450e-bb4a-fb25188cde8e|34=12|35=D|38=10|40=2|44=350.78|49=SENDER|52=20230613-14:45:58.303|54=1|55=SPY|56=ALPACA|59=0|10=005|
|8=FIX.4.2|9=149|1=TEST_ACCOUNT|11=c5bfc5f6-163d-450e-bb4a-fb25188cde8e|34=12|35=D|38=10|40=3|49=SENDER|52=20230613-14:50:51.223|54=1|55=SPY|56=ALPACA|59=0|99=350.78|10=006|
|8=FIX.4.2|9=159|1=TEST_ACCOUNT|11=c5bfc5f6-163d-450e-bb4a-fb25188cde8e|34=12|35=D|38=10|40=4|44=350.78|49=SENDER|52=20230613-15:26:35.992|54=1|55=SPY|56=ALPACA|59=0|99=350.78|10=246|
|8=FIX.4.2|9=149|1=TEST_ACCOUNT|11=c5bfc5f6-163d-450e-bb4a-fb25188cde8e|34=12|35=D|38=10|40=2|44=350.78|49=SENDER|52=20230613-14:45:58.303|54=1|55=SPY|56=ALPACA|59=5|10=005|
## 
Execution Report (8)
[](fix-messages.html#execution-report-8)
Sent by the server whenever an order receives an update. Each execution report contains field OrdStatus (39) which is used to convey the current status of the order as understood by Alpaca, as well as fields ExecType (150) and ExecTransType (20) which describe the purpose of the message.
Tag| Field| Mandatory| Description  
---|---|---|---  
35| MsgType| Y| 8 - For Execution Report  
1| Account| Y| Account number  
6| AvgPx| Y| Average price of all fills on this order  
11| ClOrdID| Y| Unique identifier of the order as assigned by the client  
12| Commission| N| Monetary commission value charged on a fill/partial fill  
14| CumQty| Y| Filled quantity on the order  
15| Currency| N| Account base currency, default USD  
17| ExecID| Y| Unique identifier of the execution assigned by Alpaca  
19| ExecRefID| N| ExecID (17) of the original execution being canceled or corrected when `20=1` or `20=2`  
20| ExecTransType| Y| Transaction type.  
0 - New  
1 - Cancel  
2 - Correct  
3 - Status, for Restated (D) message upon stop trigger  
30| LastMkt| N| Market of execution for this fill  
31| LastPx| N| Price of this fill  
32| LastShares| N| Quantity traded on this fill  
37| OrderID| Y| Unique identifier of the order assigned by Alpaca  
38| OrderQty| N| Either CashOrderQty (152) or OrderQty (38) is provided  
39| OrdStatus| Y| Identifies current status of order.  
0 - New  
1 - Partially filled  
2 - Filled  
3 - Done for day  
4 - Canceled  
5 - Replaced  
6 - Pending Cancel  
8 - Rejected  
A - Pending New  
C - Expired  
E - Pending Replace  
40| OrdType| N| Same as specified on the order.  
1 - Market  
2 - Limit  
3 - Stop  
4 - Stop limit  
5 - Market on close  
B - Limit on close  
41| OrigClOrdID| N| ClOrdID (11) of the original order in cancel and cancel/replace requests  
44| Price| N| Sent when specified on the order  
54| Side| Y| 1 - Buy  
2 - Sell  
55| Symbol| Y| Ticker symbol  
58| Text| N| Contains reject reason when `150=8`  
59| TimeInForce| N| Same as specified on the order.  
0 - Day (day)  
1 - Good Till Cancel (gtc)  
2 - At the Opening (opg)  
3 - Immediate or Cancel (ioc)  
4 - Fill or Kill (fok)  
7 - At the Close (cls)  
60| TransactTime| N| Server time in UTC when execution occurred, nanoseconds precision  
99| StopPx| N| Sent when specified on the order  
150| ExecType| Y| Describes the type of execution report.  
0 - New  
1 - Partial fill  
2 - Fill  
3 - Done for day  
4 - Canceled  
5 - Replaced  
6 - Pending Cancel, ack for Order Cancel Request (F)  
8 - Rejected  
A - Pending New  
C - Expired  
D - Restated, for stop price triggers  
E - Pending Replace, ack for Order Cancel/Replace Request (G)  
151| LeavesQty| Y| Unfilled quantity on the order. When order is closed (filled, done for day, canceled, replaced, rejected, expired) value could be 0  
152| CashOrderQty| N| Either CashOrderQty (152) or OrderQty (38) is provided. Specifies the notional amount conveyed on the order  
378| ExecRestatementReason| N| Populated when ExecType (150) = Restated (D).  
100 - Stop triggered, for stop and stop limit orders  
**Example FIX Messages**
Pending NewNewPartial FillFillPending ReplaceReplacedPending CancelCanceledRejected
|8=FIX.4.2|9=216|1=TEST_ACCOUNT|17=694bc450-3ca6-461e-8566-f977dcec9e2d|34=12|35=8|37=c5bfc5f6-163d-450e-bb4a-fb25188cde8e|39=A|40=1|49=ALPACA|52=20230615-18:14:29.702|54=1|55=SPY|56=SENDER|59=0|60=20230615-18:14:29.702|150=A|151=10|10=088|
|8=FIX.4.2|9=216|1=TEST_ACCOUNT|17=694bc450-3ca6-461e-8566-f977dcec9e2d|34=12|35=8|37=c5bfc5f6-163d-450e-bb4a-fb25188cde8e|39=0|40=1|49=ALPACA|52=20230615-18:14:45.263|54=1|55=SPY|56=SENDER|59=0|60=20230615-18:14:45.263|150=0|151=10|10=054|
|8=FIX.4.2|9=251|1=TEST_ACCOUNT|6=350.78|14=5|15=USD|17=694bc450-3ca6-461e-8566-f977dcec9e2d|31=350.78|32=5|34=12|35=8|37=c5bfc5f6-163d-450e-bb4a-fb25188cde8e|39=1|40=1|49=ALPACA|52=20230615-18:15:00.622|54=1|55=SPY|56=SENDER|59=0|60=20230615-18:15:00.622|150=1|151=5|10=185|
|8=FIX.4.2|9=253|1=TEST_ACCOUNT|6=350.78|14=10|15=USD|17=694bc450-3ca6-461e-8566-f977dcec9e2d|31=350.78|32=10|34=12|35=8|37=c5bfc5f6-163d-450e-bb4a-fb25188cde8e|39=2|40=1|49=ALPACA|52=20230615-18:15:21.920|54=1|55=SPY|56=SENDER|59=0|60=20230615-18:15:21.920|150=2|151=0|10=024|
|8=FIX.4.2|9=216|1=TEST_ACCOUNT|17=694bc450-3ca6-461e-8566-f977dcec9e2d|34=12|35=8|37=c5bfc5f6-163d-450e-bb4a-fb25188cde8e|39=E|40=1|49=ALPACA|52=20230615-18:26:53.971|54=1|55=SPY|56=SENDER|59=0|60=20230615-18:26:53.971|150=E|151=10|10=112|
|8=FIX.4.2|9=256|1=TEST_ACCOUNT|17=694bc450-3ca6-461e-8566-f977dcec9e2d|34=12|35=8|37=c5bfc5f6-163d-450e-bb4a-fb25188cde8e|39=5|40=1|41=56fcd203-7a97-430d-b14c-b0d9a7f59f2f|49=ALPACA|52=20230615-18:15:38.108|54=1|55=SPY|56=SENDER|59=0|60=20230615-18:15:38.108|150=5|151=10|10=144|
|8=FIX.4.2|9=216|1=TEST_ACCOUNT|17=694bc450-3ca6-461e-8566-f977dcec9e2d|34=12|35=8|37=c5bfc5f6-163d-450e-bb4a-fb25188cde8e|39=6|40=1|49=ALPACA|52=20230615-18:24:50.191|54=1|55=SPY|56=SENDER|59=0|60=20230615-18:24:50.191|150=6|151=10|10=060|
|8=FIX.4.2|9=216|1=TEST_ACCOUNT|17=694bc450-3ca6-461e-8566-f977dcec9e2d|34=12|35=8|37=c5bfc5f6-163d-450e-bb4a-fb25188cde8e|39=4|40=1|49=ALPACA|52=20230615-18:17:45.813|54=1|55=SPY|56=SENDER|59=0|60=20230615-18:17:45.813|150=4|151=10|10=070|
|8=FIX.4.2|9=227|1=TEST_ACCOUNT|17=694bc450-3ca6-461e-8566-f977dcec9e2d|34=12|35=8|37=c5bfc5f6-163d-450e-bb4a-fb25188cde8e|39=8|40=1|49=ALPACA|52=20230615-18:15:51.825|54=1|55=SPY|56=SENDER|59=0|60=20230615-18:15:51.825|103=Price too low|150=8|10=191|
## 
Order Cancel Request (F)
[](fix-messages.html#order-cancel-request-f)
Sent by the client to request cancellation of an order.
Tag| Field| Mandatory| Description  
---|---|---|---  
35| MsgType| Y| F - For Order Cancel Request  
1| Account| Y| Account number  
11| ClOrdID| Y| Unique identifier of cancel request assigned by the client  
41| OrigClOrdID| Y| ClOrdID (11) of the order to be canceled as assigned by the client  
54| Side| Y| As specified on the order to be canceled  
55| Symbol| Y| As specified on the order to be canceled  
60| TransactTime| Y| UTC timestamp when cancel request was initiated  
To acknowledge this message, an Execution Report (8) with `150=6` is sent immediately followed by an Execution Report (8) with `150=4` or an Order Cancel Reject (9) message. Sometimes an Order Cancel Reject (9) message might be sent directly without sending an Execution Report (8) with `150=6`.
**Example FIX Messages**
Cancel Request
|8=FIX.4.2|9=190|35=F|34=5|49=SENDER|52=20240524-16:02:44.709|56=ALPACA|1=account1|11=b165965d-0c9d-467e-a174-ee30f3fe6dbe|41=b5db0b8e-bbc1-4906-aff8-c58d18ba3398|54=1|55=AAPL|60=20240524-16:02:44.709206406|10=226|
## 
Order Cancel/Replace Request (G)
[](fix-messages.html#order-cancelreplace-request-g)
Sent by the client to request modification of an order.
Tag| Field| Mandatory| Description  
---|---|---|---  
35| MsgType| Y| G - For Order Cancel/Replace Request  
1| Account| Y| Account number  
11| ClOrdID| Y| Unique identifier of the replacement order assigned by the client (must be no longer than 48 characters)  
21| HandlInst| Y| 1 - Automated execution with no broker intervention, only accepted value  
38| OrderQty| N| Modified quantity for the order  
40| OrdType| Y| As specified on the original order  
41| OrigClOrdID| Y| ClOrdID (11) of the order to be modified as assigned by the client  
44| Price| N| Modified price for the order  
54| Side| Y| As specified on the original order  
55| Symbol| Y| As specified on the original order  
59| TimeInForce| N| Modified time in force for the order  
60| TransactTime| Y| UTC timestamp when cancel/replace request was initiated  
99| StopPx| N| Modified stop price for the order  
**Example FIX Messages**
Cancel/Replace Request
|8=FIX.4.2|9=212|35=G|34=21|49=SENDER|52=20240524-16:16:58.956|56=ALPACA|1=account1|11=45169819-088a-4089-9758-f28e830e95f0|21=3|40=2|41=f001f209-2c3e-42e3-9ab1-10e74ee39fe5|44=1.50000|54=1|55=AAPL|60=20240524-16:16:58.956849295|10=173|
## 
Order Cancel Reject (9)
[](fix-messages.html#order-cancel-reject-9)
Sent by the server if the Order Cancel Request (F) or Order Cancel/Replace Request (G) message could not be honored. Some common reject scenarios include:
* when order is already filled or closed
* when a previous Order Cancel Request (F) or Order Cancel/Replace Request (G) is pending for this order
Tag| Field| Mandatory| Description  
---|---|---|---  
35| MsgType| Y| 9 - For Order Cancel Reject  
1| Account| Y| Account number  
11| ClOrdID| Y| Unique identifier of cancel or cancel/replace request as assigned by the client  
37| OrderID| Y| Unique identifier of the order as assigned by Alpaca for which the cancel or cancel/replace request was rejected  
39| OrdStatus| Y| Order status after this cancel reject is applied  
41| OrigClOrdID| Y| ClOrdID (11) of the order for which the cancel or cancel/replace request was rejected  
58| Text| N| Reject reason  
60| TransactTime| N| Server time in UTC when cancel or replace reject occurred  
102| CxlRejReason| N| Code to identify reason for cancel rejection.  
0 - Too late to cancel  
1 - Unknown order  
2 - Broker Option  
3 - Order already in Pending Cancel or Pending Replace status  
434| CxlRejResponseTo| Y| 1 - Response to Order Cancel Request (F)  
2 - Response to Order Cancel/Replace Request (G)  
**Example FIX Messages**
Cancel RejectCancel/Replace Reject
|8=FIX.4.2|9=220|35=9|34=18|49=ALPACA|52=20240524-16:02:46.215|56=SENDER|1=account1|11=a7860828-4dc5-4f8f-bfb1-8fbca8855c88|37=f50af678-bba4-44ea-9b23-0fc452ed4921|39=6|41=2c017b79-a843-4146-a2b7-3bf83af89482|58=TOO_LATE_TO_CANCEL|434=1|10=116|
|8=FIX.4.2|9=198|35=9|34=45|49=ALPACA|52=20240524-16:16:59.085|56=SENDER|1=account1|11=5cdf9082-067b-4497-a90c-f5e8c666409b|37=UNKNOWN|39=8|41=c7feaf5a-54d2-458d-8ab2-9b2f337a28ec|58=replace pending for order|434=2|10=179|
## 
Version History
[](fix-messages.html#version-history)
Version| Date| Change  
---|---|---  
0.1.0| 08/05/2024| Document Creation  
0.1.1| 24/05/2024| Changed FIX version to FIX.4.2  
Removed ApplVerID (1128) from Message Header  
Added ClOrdID (11) and OrigClOrdID (41) as required in Order Cancel Request (F) and Order Cancel/Replace Request (G)  
Removed OrderID (37) from Order Cancel Request (F) and Order Cancel/Replace Request (G)  
Added OrderQty (38) to Order Cancel/Replace Request (G)  
Updated FIX examples  
0.1.2| 12/06/2024| Removed Account (1) and RawData (96) from Logon (A) message  
Added RefTagID (371), RefMsgType (372) and SessionRejectReason (373) to Reject (3) message  
Added HandlInst (21), TransactTime (60) and OpenClose (77) to New Order - Single (D)  
Added 1 (per share) as an accepted value for CommType (13) in New Order - Single (D)  
Updated AvgPx (6) to mandatory in Execution Report (8)  
Added Commission (12), ExecRefID (19), ExecTransType (20), LastMkt (30), OrderQty (38) and CashOrderQty (152) to Execution Report (8)  
Removed OrdRejReason (103) from Execution Report (8)  
Updated possible values for ExecType (150) in Execution Report (8)  
1.0.0| 13/06/2024| Added Side (54), Symbol (55) and TransactTime (60) to Order Cancel Request (F)  
Added OrderID (37) to Order Cancel Reject (9)  
Added HandlInst (21), OrdType (40), Side (54), Symbol (55) and TransactTime (60) to Order Cancel/Replace Request (G)  
1.0.1| 04/09/2024| Added Market on close (5) and Limit on close (B) as values for OrdType (40) on New Order - Single (D)  
Added At the Close (7) as a value for TimeInForce (59) on New Order - Single (D)  
1.0.2| 08/10/2024| Added Restated (D) as value for ExecType (150) on Execution Report (8)  
Added ExecRestatementReason (378) to Execution Report (8)  
Added Status (3) as value for ExecTransType (20) on Execution Report (8)  
Added TransactTime (60) to Order Cancel Reject (9)  
1.0.3| 14/01/2025| Added Good Till Crossing (5) as a value for TimeInForce (59) on New Order - Single (D)  
Added ClientID (109) to New Order - Single (D)  
1.0.4| 03/04/2025| Removed Good Till Crossing (5) as a valid value for TimeInForce (59) on New Order - Single (D)  
Added TradingSessionID (336) to New Order - Single (D)  
__Updated 2 months ago
* * *
