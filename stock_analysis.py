import yfinance as yf
import quantstats as qs
import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import datetime, timedelta

def get_stock_returns(stock_symbol, period="1y"):

    try:
        # Fetch stock data using yfinance
        stock = yf.Ticker(stock_symbol)
        
        # Get historical data
        hist = stock.history(period=period)
        
        if hist.empty:
            raise ValueError(f"No data found for {stock_symbol}")
        
        # Calculate daily returns
        returns = hist['Close'].pct_change().dropna()
        
        return returns
    
    except Exception as e:
        raise Exception(f"Error fetching data for {stock_symbol}: {str(e)}")

def plot_daily_returns(returns, stock_symbol, save_path="plots"):
    """
    Alternative plotting function using pure matplotlib (more reliable) - single plot
    """
    try:
        # Create plots directory if it doesn't exist
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        
        # Create the plot
        fig, ax = plt.subplots(figsize=(12, 6))
        
        # Plot: Daily returns over time
        ax.plot(returns.index, returns.values, alpha=0.7, linewidth=0.8)
        ax.set_title(f'{stock_symbol.upper()} Daily Returns Over Time')
        ax.set_xlabel('Date')
        ax.set_ylabel('Daily Return')
        ax.grid(True, alpha=0.3)
        ax.axhline(y=0, color='red', linestyle='--', alpha=0.5)
        
        plt.tight_layout()
        
        # Save the plot
        plot_filename = f"{stock_symbol}_daily_returns.png"
        plot_path = os.path.join(save_path, plot_filename)
        
        plt.savefig(plot_path, dpi=300, bbox_inches='tight', facecolor='white')
        plt.close()
        
        return plot_path
    
    except Exception as e:
        raise Exception(f"Error creating plot for {stock_symbol}: {str(e)}")

def get_stock_info(stock_symbol):
    try:
        stock = yf.Ticker(stock_symbol)
        info = stock.info
        
        return {
            'name': info.get('longName', 'N/A'),
            'sector': info.get('sector', 'N/A'),
            'industry': info.get('industry', 'N/A'),
            'market_cap': info.get('marketCap', 'N/A'),
            'current_price': info.get('currentPrice', 'N/A')
        }
    except Exception as e:
        return {'error': f"Could not fetch info for {stock_symbol}: {str(e)}"}