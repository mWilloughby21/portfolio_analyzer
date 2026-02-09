# visualization.py
# Display results using Matplotlib

import matplotlib.pyplot as plt
from typing import Dict

class Visualization:
    
    # Bar chart of each position's current value
    @staticmethod
    def plot_portfolio_value(values: Dict[str, float]):
        tickers = list(values.keys())
        vals = list(values.values())
        
        plt.figure(figsize=(8, 5))
        plt.bar(tickers, vals, color='skyblue')
        plt.title('Portfolio Position Values')
        plt.xlabel('Ticker')
        plt.ylabel('Value ($)')
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.show()
    
    # Pie chart of portfolio allocation
    @staticmethod
    def plot_allocation(allocation: Dict[str, float]):
        labels = list(allocation.keys())
        sizes = list(allocation.values())
        
        plt.figure(figsize=(6, 6))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=plt.cm.tab20.colors)
        plt.title('Portfolio Allocation')
        plt.show()

if __name__ == "__main__":
    from portfolio import Portfolio
    from market_data import MarketData
    from analytics import Analytics
    from pathlib import Path
    
    BASE_DIR = Path(__file__).resolve().parent.parent
    CSV_PATH = BASE_DIR / 'data' / 'portfolio.csv'
    
    portfolio = Portfolio.from_csv(CSV_PATH)
    prices = MarketData.get_prices(portfolio.positions)
    
    # Calculate position values and allocation
    position_values = {p.ticker: Analytics.position_value(p, prices[p.ticker]) for p in portfolio.positions}
    allocation = Analytics.allocation(portfolio.positions, prices)
    
    # Plot the results
    Visualization.plot_portfolio_value(position_values)
    Visualization.plot_allocation(allocation)