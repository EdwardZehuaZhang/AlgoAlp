"""
AlgoAlp Webhook Server for TradingView Alerts
"""

from flask import Flask, request, render_template, jsonify
import alpaca_trade_api as tradeapi
import json
import os
from datetime import datetime
import requests
import logging
from dotenv import load_dotenv

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# Configuration
WEBHOOK_PASSPHRASE = os.getenv('WEBHOOK_PASSPHRASE', 'your_secure_passphrase')  # Set a strong passphrase
ALPACA_API_KEY = os.getenv('ALPACA_API_KEY')
ALPACA_API_SECRET = os.getenv('ALPACA_API_SECRET')
ALPACA_BASE_URL = os.getenv('ALPACA_BASE_URL', 'https://paper-api.alpaca.markets')
DISCORD_WEBHOOK_URL = os.getenv('DISCORD_WEBHOOK_URL', '')  # Optional

# Initialize Alpaca API
api = tradeapi.REST(
    ALPACA_API_KEY, 
    ALPACA_API_SECRET, 
    ALPACA_BASE_URL
)

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def dashboard():
    """Display a dashboard with recent orders"""
    try:
        # Get recent orders from Alpaca
        orders = api.list_orders(status='all', limit=50)
        
        # Get account information
        account = api.get_account()
        
        return render_template('dashboard.html', 
                              orders=orders, 
                              account=account,
                              last_updated=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    except Exception as e:
        logger.error(f"Dashboard error: {str(e)}")
        return render_template('error.html', error=str(e))

@app.route('/webhook', methods=['POST'])
def webhook():
    """Receive webhook alerts from TradingView"""
    if request.method == 'POST':
        try:
            # Parse the webhook data
            webhook_message = json.loads(request.data)
            logger.info(f"Received webhook: {webhook_message}")
            
            # Verify passphrase
            if 'passphrase' not in webhook_message or webhook_message['passphrase'] != WEBHOOK_PASSPHRASE:
                logger.warning("Invalid passphrase")
                return jsonify({"code": "error", "message": "Invalid passphrase"})
            
            # Extract trading parameters
            ticker = webhook_message.get('ticker', 'SPY')  # Default to SPY
            action = webhook_message.get('strategy', {}).get('order_action', '').upper()
            contracts = int(webhook_message.get('strategy', {}).get('order_contracts', 0))
            
            # Skip if no action or zero contracts
            if not action or contracts <= 0:
                return jsonify({"code": "error", "message": "Invalid order details"})
            
            # Determine order parameters based on action
            side = None
            if action == 'BUY':
                side = 'buy'
            elif action == 'SELL':
                side = 'sell'
            else:
                return jsonify({"code": "error", "message": f"Unknown order action: {action}"})
            
            # Submit the order
            order = api.submit_order(
                symbol=ticker,
                qty=contracts,
                side=side,
                type='market',
                time_in_force='gtc'
            )
            
            logger.info(f"Order submitted: {order.__dict__}")
            
            # Post to Discord if webhook URL is provided
            if DISCORD_WEBHOOK_URL:
                send_discord_notification(ticker, action, contracts, order.id)
                
            return jsonify({
                "code": "success",
                "message": f"Order {action} {contracts} shares of {ticker} submitted successfully",
                "order_id": order.id
            })
            
        except Exception as e:
            logger.error(f"Error processing webhook: {str(e)}")
            return jsonify({"code": "error", "message": str(e)})
    
    return jsonify({"code": "error", "message": "Invalid request method"})

def send_discord_notification(ticker, action, quantity, order_id):
    """Send notification to Discord"""
    try:
        message = {
            "username": "AlgoAlp Trader",
            "avatar_url": "https://cdn-icons-png.flaticon.com/512/2431/2431438.png",
            "content": f"🤖 AlgoAlp Strategy Alert 🤖\n**{action}** {quantity} shares of **{ticker}**\nOrder ID: {order_id}\nTime: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        }
        
        response = requests.post(
            DISCORD_WEBHOOK_URL,
            json=message
        )
        
        if response.status_code == 204:
            logger.info("Discord notification sent successfully")
        else:
            logger.warning(f"Failed to send Discord notification: {response.status_code} - {response.text}")
            
    except Exception as e:
        logger.error(f"Discord notification error: {str(e)}")

if __name__ == "__main__":
    # Use this for local development
    app.run(debug=True, host='0.0.0.0', port=5000)
