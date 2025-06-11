"""
Monitor and analyze trading strategy performance
"""
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import logging
from dotenv import load_dotenv
from alpaca_trade_api.rest import REST

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("monitor.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger()

# Load environment variables
load_dotenv()

# Initialize Alpaca API
API_KEY = os.getenv("ALPACA_API_KEY")
API_SECRET = os.getenv("ALPACA_API_SECRET")
PAPER = os.getenv("ALPACA_PAPER", "True").lower() in ("true", "1", "t")
BASE_URL = "https://paper-api.alpaca.markets" if PAPER else "https://api.alpaca.markets"

api = REST(API_KEY, API_SECRET, BASE_URL, api_version='v2')

def format_dollar(value):
    """Format value as dollar amount"""
    return f"${value:.2f}"

def format_percent(value):
    """Format value as percentage"""
    return f"{value:.2f}%"

def get_account_summary():
    """Get account summary information"""
    try:
        account = api.get_account()
        
        # Calculate key metrics
        equity = float(account.equity)
        cash = float(account.cash)
        buying_power = float(account.buying_power)
        
        # Calculate day's P&L
        portfolio_value = float(account.portfolio_value)
        prev_close = float(account.last_equity)
        day_change = portfolio_value - prev_close
        day_change_percent = (day_change / prev_close) * 100 if prev_close > 0 else 0
        
        return {
            "equity": equity,
            "cash": cash,
            "buying_power": buying_power,
            "day_change": day_change,
            "day_change_percent": day_change_percent
        }
    
    except Exception as e:
        logger.error(f"Error getting account summary: {str(e)}")
        return None

def get_positions_summary():
    """Get summary of current positions"""
    try:
        positions = api.list_positions()
        
        if not positions:
            logger.info("No open positions")
            return None
        
        position_data = []
        for position in positions:
            symbol = position.symbol
            qty = float(position.qty)
            entry_price = float(position.avg_entry_price)
            current_price = float(position.current_price)
            market_value = float(position.market_value)
            unrealized_pl = float(position.unrealized_pl)
            unrealized_plpc = float(position.unrealized_plpc) * 100
            
            position_data.append({
                "symbol": symbol,
                "quantity": qty,
                "entry_price": entry_price,
                "current_price": current_price,
                "market_value": market_value,
                "unrealized_pl": unrealized_pl,
                "unrealized_pl_percent": unrealized_plpc
            })
        
        return position_data
    
    except Exception as e:
        logger.error(f"Error getting positions summary: {str(e)}")
        return None

def get_orders_today():
    """Get all orders from today"""
    try:
        today = datetime.now().date()
        today_iso = today.isoformat()
        
        orders = api.list_orders(
            status='all',
            limit=500,
            after=today_iso
        )
        
        order_data = []
        for order in orders:
            order_data.append({
                "id": order.id,
                "symbol": order.symbol,
                "side": order.side,
                "qty": float(order.qty),
                "type": order.type,
                "status": order.status,
                "filled_avg_price": float(order.filled_avg_price) if order.filled_avg_price else None,
                "filled_at": order.filled_at,
                "submitted_at": order.submitted_at
            })
        
        return order_data
    
    except Exception as e:
        logger.error(f"Error getting today's orders: {str(e)}")
        return None

def get_trade_stats(days=7):
    """Calculate trading statistics for the specified number of days"""
    try:
        # Get start date
        start_date = (datetime.now() - timedelta(days=days)).date()
        start_iso = start_date.isoformat()
        
        # Get all filled orders in the time period
        orders = api.list_orders(
            status='filled',
            limit=500,
            after=start_iso
        )
        
        if not orders:
            logger.info(f"No completed trades in the last {days} days")
            return None
        
        # Organize the orders by symbol and side
        trades = []
        
        # Group orders that are part of the same trade
        symbols = set(order.symbol for order in orders)
        for symbol in symbols:
            symbol_orders = [o for o in orders if o.symbol == symbol]
            
            # Sort by filled timestamp
            symbol_orders.sort(key=lambda x: x.filled_at if x.filled_at else x.submitted_at)
            
            # Find pairs of buys and sells
            i = 0
            while i < len(symbol_orders) - 1:
                current = symbol_orders[i]
                next_order = symbol_orders[i+1]
                
                # Skip if current order isn't filled
                if not current.filled_at:
                    i += 1
                    continue
                
                # Check if we have a buy followed by a sell or vice versa
                if ((current.side == 'buy' and next_order.side == 'sell') or 
                    (current.side == 'sell' and next_order.side == 'buy')):
                    
                    # Calculate P&L for this trade
                    entry_price = float(current.filled_avg_price) if current.filled_avg_price else 0
                    exit_price = float(next_order.filled_avg_price) if next_order.filled_avg_price else 0
                    qty = min(float(current.qty), float(next_order.qty))
                    
                    if current.side == 'buy':
                        pnl = (exit_price - entry_price) * qty
                        pnl_percent = ((exit_price / entry_price) - 1) * 100 if entry_price > 0 else 0
                    else:  # sell first (short)
                        pnl = (entry_price - exit_price) * qty
                        pnl_percent = ((entry_price / exit_price) - 1) * 100 if exit_price > 0 else 0
                    
                    duration = None
                    if current.filled_at and next_order.filled_at:
                        start_time = pd.to_datetime(current.filled_at)
                        end_time = pd.to_datetime(next_order.filled_at)
                        duration = (end_time - start_time).total_seconds() / 60  # minutes
                    
                    trades.append({
                        "symbol": symbol,
                        "entry_time": current.filled_at,
                        "exit_time": next_order.filled_at,
                        "direction": 'long' if current.side == 'buy' else 'short',
                        "quantity": qty,
                        "entry_price": entry_price,
                        "exit_price": exit_price,
                        "pnl": pnl,
                        "pnl_percent": pnl_percent,
                        "duration_minutes": duration
                    })
                    
                    i += 2  # Skip to next pair
                else:
                    i += 1  # Move to next order
        
        if not trades:
            logger.info("No complete trades found (no matching buy/sell pairs)")
            return None
        
        # Calculate overall statistics
        trade_df = pd.DataFrame(trades)
        
        total_trades = len(trade_df)
        winning_trades = len(trade_df[trade_df['pnl'] > 0])
        losing_trades = len(trade_df[trade_df['pnl'] <= 0])
        
        win_rate = (winning_trades / total_trades) * 100 if total_trades > 0 else 0
        
        total_pnl = trade_df['pnl'].sum()
        avg_pnl = trade_df['pnl'].mean()
        avg_win = trade_df[trade_df['pnl'] > 0]['pnl'].mean() if winning_trades > 0 else 0
        avg_loss = trade_df[trade_df['pnl'] <= 0]['pnl'].mean() if losing_trades > 0 else 0
        
        profit_factor = abs(trade_df[trade_df['pnl'] > 0]['pnl'].sum() / 
                         trade_df[trade_df['pnl'] <= 0]['pnl'].sum()) if losing_trades > 0 else float('inf')
        
        avg_duration = trade_df['duration_minutes'].mean()
        
        stats = {
            "period_days": days,
            "total_trades": total_trades,
            "winning_trades": winning_trades,
            "losing_trades": losing_trades,
            "win_rate": win_rate,
            "total_pnl": total_pnl,
            "avg_pnl": avg_pnl,
            "avg_win": avg_win,
            "avg_loss": avg_loss,
            "profit_factor": profit_factor,
            "avg_duration_minutes": avg_duration,
            "trades": trades
        }
        
        return stats
    
    except Exception as e:
        logger.error(f"Error calculating trade statistics: {str(e)}")
        return None

def generate_performance_report(days=7):
    """
    Generate a comprehensive performance report
    """
    try:
        # Get account summary
        account_summary = get_account_summary()
        positions_summary = get_positions_summary()
        trade_stats = get_trade_stats(days=days)
        
        # Print report to console
        print("\n" + "="*50)
        print(f"PERFORMANCE REPORT - Last {days} Days")
        print("="*50)
        
        if account_summary:
            print("\nACCOUNT SUMMARY")
            print(f"Equity: {format_dollar(account_summary['equity'])}")
            print(f"Cash: {format_dollar(account_summary['cash'])}")
            print(f"Buying Power: {format_dollar(account_summary['buying_power'])}")
            print(f"Day Change: {format_dollar(account_summary['day_change'])} ({format_percent(account_summary['day_change_percent'])})")
        
        if positions_summary:
            print("\nCURRENT POSITIONS")
            for pos in positions_summary:
                print(f"{pos['symbol']}: {pos['quantity']} shares @ {format_dollar(pos['entry_price'])}, "
                      f"P&L: {format_dollar(pos['unrealized_pl'])} ({format_percent(pos['unrealized_pl_percent'])})")
        else:
            print("\nCURRENT POSITIONS: None")
        
        if trade_stats:
            print("\nTRADING STATISTICS")
            print(f"Total Trades: {trade_stats['total_trades']}")
            print(f"Win Rate: {format_percent(trade_stats['win_rate'])}")
            print(f"Profit Factor: {trade_stats['profit_factor']:.2f}")
            print(f"Total P&L: {format_dollar(trade_stats['total_pnl'])}")
            print(f"Average P&L per Trade: {format_dollar(trade_stats['avg_pnl'])}")
            print(f"Average Winner: {format_dollar(trade_stats['avg_win'])}")
            print(f"Average Loser: {format_dollar(trade_stats['avg_loss'])}")
            print(f"Average Trade Duration: {trade_stats['avg_duration_minutes']:.1f} minutes")
            
            print("\nRECENT TRADES")
            for trade in trade_stats['trades'][-5:]:  # Show last 5 trades
                print(f"{trade['symbol']} {trade['direction'].upper()}: "
                      f"{format_dollar(trade['pnl'])} ({format_percent(trade['pnl_percent'])}), "
                      f"Duration: {trade['duration_minutes']:.1f} min")
        
        # Generate plots if we have trade data
        if trade_stats and trade_stats['trades']:
            # Convert trades to DataFrame
            df = pd.DataFrame(trade_stats['trades'])
            
            # Convert timestamps to datetime
            df['entry_time'] = pd.to_datetime(df['entry_time'])
            df['exit_time'] = pd.to_datetime(df['exit_time'])
            df['date'] = df['exit_time'].dt.date
            
            # Cumulative P&L plot
            plt.figure(figsize=(10, 6))
            plt.plot(df['exit_time'], df['pnl'].cumsum(), 'b-', linewidth=2)
            plt.xlabel('Date')
            plt.ylabel('Cumulative P&L ($)')
            plt.title('Cumulative P&L Over Time')
            plt.grid(True, alpha=0.3)
            plt.savefig('cumulative_pnl.png')
            
            # P&L per trade
            plt.figure(figsize=(10, 6))
            colors = ['g' if x > 0 else 'r' for x in df['pnl']]
            plt.bar(range(len(df)), df['pnl'], color=colors)
            plt.xlabel('Trade Number')
            plt.ylabel('P&L ($)')
            plt.title('P&L per Trade')
            plt.axhline(y=0, color='black', linestyle='-', alpha=0.3)
            plt.grid(True, alpha=0.3)
            plt.savefig('pnl_per_trade.png')
            
            # Win rate by day of week
            if len(df) > 5:  # Only if we have enough data
                df['day_of_week'] = df['entry_time'].dt.day_name()
                win_rate_by_day = df.groupby('day_of_week')['pnl'].apply(lambda x: (x > 0).mean() * 100)
                
                plt.figure(figsize=(10, 6))
                days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
                days_present = [day for day in days_order if day in win_rate_by_day.index]
                plt.bar(days_present, [win_rate_by_day.get(day, 0) for day in days_present])
                plt.xlabel('Day of Week')
                plt.ylabel('Win Rate (%)')
                plt.title('Win Rate by Day of Week')
                plt.ylim(0, 100)
                plt.grid(True, alpha=0.3)
                plt.savefig('win_rate_by_day.png')
            
            print("\nPerformance charts saved to:")
            print("- cumulative_pnl.png")
            print("- pnl_per_trade.png")
            if len(df) > 5:
                print("- win_rate_by_day.png")
        
        print("\n" + "="*50)
        return True
    
    except Exception as e:
        logger.error(f"Error generating performance report: {str(e)}")
        return False

if __name__ == "__main__":
    print("Generating trading performance report...")
    generate_performance_report(days=30)  # Default to last 30 days 