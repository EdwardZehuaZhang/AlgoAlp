# Webhook Configuration Guide

## How to Set Up Webhook Communication

### Step 1: Create your Webhook Passphrase
1. The webhook passphrase is a security measure to ensure that only your authorized alerts are processed
2. Create a secure passphrase (like a strong password) that will be used in both:
   - Your TradingView alert message
   - Your server's environment variables

3. Example of generating a secure passphrase:
   ```python
   import secrets
   import string
   
   # Generate a 16-character secure passphrase
   characters = string.ascii_letters + string.digits + string.punctuation
   passphrase = ''.join(secrets.choice(characters) for i in range(16))
   print(f"Your secure passphrase: {passphrase}")
   ```

### Step 2: Set Up Your Environment Variables
1. Create or modify your `.env` file in the project root directory
2. Add the following line with your chosen passphrase:
   ```
   WEBHOOK_PASSPHRASE=your_secure_passphrase
   ```
3. Make sure to also include your Alpaca API credentials:
   ```
   ALPACA_API_KEY=your_alpaca_api_key
   ALPACA_API_SECRET=your_alpaca_api_secret
   ALPACA_PAPER=True  # Set to False for live trading
   ```

### Step 3: Start Your Webhook Server
1. Run the webhook server to start listening for alerts:
   ```bash
   python webhook_server.py
   ```
2. You should see a message indicating the server is running, similar to:
   ```
   * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
   ```

### Step 4: Expose Your Local Server to the Internet
Unless your server is already hosted on a public URL, you'll need to expose your local server to receive webhooks from TradingView. You can use ngrok as described in the README.

### Step 5: Test Your Webhook
1. Send a test webhook using a tool like Postman or curl:
   ```bash
   curl -X POST \
     -H "Content-Type: application/json" \
     -d '{
       "passphrase": "your_secure_passphrase",
       "time": "2023-05-01T12:34:56Z",
       "ticker": "SPY",
       "bar": {
         "time": "2023-05-01T12:34:56Z",
         "open": 400.0,
         "high": 401.0,
         "low": 399.0,
         "close": 400.5,
         "volume": 10000
       },
       "strategy": {
         "position_size": 100,
         "order_action": "buy",
         "order_contracts": 1,
         "order_price": 400.5,
         "order_id": "test",
         "market_position": "long",
         "market_position_size": 1,
         "prev_market_position": "flat",
         "prev_market_position_size": 0
       }
     }' \
     http://localhost:5000/webhook
   ```

2. Your webhook server should receive this test message and respond accordingly
