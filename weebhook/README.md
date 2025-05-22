# AlgoAlp

A Python implementation of an automated trading strategy using TradingView alerts with Alpaca Markets.

## Overview
This project connects TradingView Pine Script strategy alerts to the Alpaca Trading API. It uses a webhook server to receive alerts from TradingView and automatically execute trades through Alpaca.

## Features
- Multi-timeframe technical analysis in TradingView
- Webhook server for receiving TradingView alerts
- Integration with Alpaca Markets API for trade execution
- Real-time notifications via Discord (optional)
- Dashboard for monitoring trades and account status
- Visualization tools for strategy performance

## Setup

### 1. TradingView Alert Setup
1. After applying your Pine Script strategy to a chart in TradingView, click on "Alerts" in the right sidebar
2. Click the "+" button to create a new alert
3. Configure the alert as follows:
   - Condition Type: "Strategy Signals"
   - Alert triggering: Choose "Once Per Bar Close"
   - Alert name: Give it a descriptive name like "AlgoAlp Strategy Alert"
   - Alert message: Use this exact format (copy and paste):
   ```
   {
     "passphrase": "your_secure_passphrase",
     "time": "{{time}}",
     "ticker": "{{ticker}}",
     "bar": {
       "time": "{{time}}",
       "open": {{open}},
       "high": {{high}},
       "low": {{low}},
       "close": {{close}},
       "volume": {{volume}}
     },
     "strategy": {
       "position_size": {{strategy.position_size}},
       "order_action": "{{strategy.order.action}}",
       "order_contracts": {{strategy.order.contracts}},
       "order_price": {{strategy.order.price}},
       "order_id": "{{strategy.order.id}}",
       "market_position": "{{strategy.market_position}}",
       "market_position_size": {{strategy.market_position_size}},
       "prev_market_position": "{{strategy.prev_market_position}}",
       "prev_market_position_size": {{strategy.prev_market_position_size}}
     }
   }
   ```
   - Webhook URL: Enter your webhook server URL (see Server Setup section)
   - Click "Create" to save the alert

4. **Important**: The "passphrase" in the alert message must match the WEBHOOK_PASSPHRASE in your .env file

### 2. Server Setup
1. Clone this repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Copy `.env.example` to `.env` and fill in your Alpaca API credentials and webhook passphrase
6. Start the webhook server: `python webhook_server.py`

### 3. Deployment Options

#### Local Deployment with ngrok
1. Install ngrok: https://ngrok.com/download
2. Start your Flask app: `python webhook_server.py`
3. In another terminal, run: `ngrok http 5000`
4. Copy the HTTPS URL provided by ngrok
5. Use this URL as your webhook URL in TradingView alerts

#### Cloud Deployment with Heroku
1. Install the Heroku CLI: https://devcenter.heroku.com/articles/heroku-cli
2. Login to Heroku: `heroku login`
3. Create a new Heroku app: `heroku create your-app-name`
4. Add a Procfile to your repository with: `web: gunicorn webhook_server:app`
5. Set your environment variables:
   ```
   heroku config:set ALPACA_API_KEY=your_key
   heroku config:set ALPACA_API_SECRET=your_secret
   heroku config:set WEBHOOK_PASSPHRASE=your_passphrase
   ```
6. Deploy your app: `git push heroku main`
7. Use your Heroku app URL as the webhook URL in TradingView

## JSON Payload Example

This is the format you should use for TradingView webhook alerts:

```json
{
  "passphrase": "your_secure_passphrase",
  "time": "{{time}}",
  "ticker": "{{ticker}}",
  "bar": {
    "time": "{{time}}",
    "open": {{open}},
    "high": {{high}},
    "low": {{low}},
    "close": {{close}},
    "volume": {{volume}}
  },
  "strategy": {
    "position_size": {{strategy.position_size}},
    "order_action": "{{strategy.order.action}}",
    "order_contracts": {{strategy.order.contracts}},
    "order_price": {{strategy.order.price}},
    "order_id": "{{strategy.order.id}},
    "market_position": "{{strategy.market_position}}",
    "market_position_size": {{strategy.market_position_size}},
    "prev_market_position": "{{strategy.prev_market_position}}",
    "prev_market_position_size": {{strategy.prev_market_position_size}}
  }
}
```

## Visualization

To visualize your strategy performance:

```bash
python visualize.py --symbol SPY --days 60 --trades trade_history.json --type both --save charts/my_strategy.png
```

## Disclaimer
This is for educational purposes only. Trading involves risk of financial loss. Past performance is not indicative of future results.