# How to Add Webhook Alerts to Your Pine Script Strategy

This guide explains how to modify your Pine Script strategy to generate webhook alerts that can be consumed by the AlgoAlp system.

## Step 1: Add Alert Conditions to Your Strategy

Your strategy already has trading logic. You need to add specific alert conditions to send signals to your webhook server.

Here's how to modify your existing Pine Script to add webhook alert capability:

```pinescript
//@version=6 
strategy("Simplified Strat w Background 0.001", overlay=true, pyramiding=2)

// === Original strategy code remains unchanged ===
// ... (all your existing strategy code)

// === Add Alert Conditions ===
// These variables will be referenced in TradingView alerts

// Create variables to store alert messages
var string longAlertMessage = ""
var string shortAlertMessage = ""

// Update alert messages when signals occur
if compositeBuy and strategy.position_size <= 0 and (trendState == 1 or trendState == 0)
    longAlertMessage := "BUY SIGNAL\nSymbol: " + syminfo.ticker + "\nPrice: " + str.tostring(close) + "\nTime: " + str.tostring(year) + "-" + str.tostring(month) + "-" + str.tostring(dayofmonth) + " " + str.tostring(hour) + ":" + str.tostring(minute)
    alert(longAlertMessage, alert.freq_once_per_bar_close)

if compositeSell and strategy.position_size >= 0 and (trendState == -1 or trendState == 0)
    shortAlertMessage := "SELL SIGNAL\nSymbol: " + syminfo.ticker + "\nPrice: " + str.tostring(close) + "\nTime: " + str.tostring(year) + "-" + str.tostring(month) + "-" + str.tostring(dayofmonth) + " " + str.tostring(hour) + ":" + str.tostring(minute)
    alert(shortAlertMessage, alert.freq_once_per_bar_close)

// === Rest of your original script ===
// ... (your plotting code and other logic)
```

## Step 2: Create Alerts in TradingView

After adding the alert conditions to your script, follow these steps to create the actual alerts:

1. Apply your updated script to a chart
2. Click on the "Alerts" tab in the right sidebar
3. Click the "+" button to create a new alert
4. In the "Condition" section, select "strategy signals" from the dropdown
5. Set "Alert triggering" to "Once Per Bar Close"
6. In the "Alert name" field, enter a descriptive name like "AlgoAlp Buy Signal"
7. In the "Message" field, paste the JSON template provided in the README
8. Make sure to set "Webhook URL" to your server's webhook URL
9. Click "Create"
10. Repeat steps 3-9 to create another alert for sell signals if needed

## Important Notes:

1. **Do not modify your strategy logic** - Only add the alert code; your strategy's entry and exit conditions should remain the same
2. The alert conditions should exactly match your strategy entry/exit conditions
3. The `alert()` function must use `alert.freq_once_per_bar_close` to prevent duplicate signals
4. Make sure your TradingView account supports webhook alerts (Premium plan or higher)

## Testing Your Alerts

1. Switch to a smaller timeframe to see more frequent signals
2. Enable your alerts and watch for signals
3. Check your webhook server logs to confirm that alerts are being received
4. Verify in Alpaca that orders are being placed according to your alerts
