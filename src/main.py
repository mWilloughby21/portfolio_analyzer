# main.py

from portfolio import Portfolio
from market_data import MarketData
from analytics import Analytics
from visualization import Visualization
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
CSV_PATH = BASE_DIR / 'data' / 'portfolio.csv'

def main():
    portfolio = Portfolio.from_csv(CSV_PATH)
    prices = MarketData.get_prices(portfolio.positions)

    position_values = {
        p.ticker: Analytics.position_value(p, prices[p.ticker]) for p in portfolio.positions
    }
    allocation = Analytics.allocation(portfolio.positions, prices)
    gains = Analytics.gains_losses(portfolio.positions, prices)

    print("Total Cost Basis:", portfolio.total_cost_basis())
    print("Portfolio Value:", Analytics.portfolio_value(portfolio.positions, prices))
    print("Gains/Losses:", gains)
    print("Allocation:", allocation)

    Visualization.plot_portfolio_value(position_values)
    Visualization.plot_allocation(allocation)


if __name__ == "__main__":
    main()