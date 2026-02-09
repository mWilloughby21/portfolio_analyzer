# market_data.py
# Fetch prices & Historical data for stocks and ETFs using yfinance

import yfinance as yf
from typing import List
from portfolio import Portfolio, Position

class MarketData:
    @staticmethod
    def get_curr_price(ticker: str) -> float:
        stock = yf.Ticker(ticker)
        return stock.history(period='1d')['Close'].iloc[-1]
    
    @classmethod
    def get_prices(cls, positions: List[Position]) -> dict:
        prices = {}
        for pos in positions:
            prices[pos.ticker] = round(float(cls.get_curr_price(pos.ticker)), 2)
        return prices

if __name__ == "__main__":
    from portfolio import Position
    from pathlib import Path
    
    BASE_DIR = Path(__file__).resolve().parent.parent
    CSV_PATH = BASE_DIR / 'data' / 'portfolio.csv'
    
    portfolio = Portfolio.from_csv(CSV_PATH)
    prices = MarketData.get_prices(portfolio.positions)
    print(prices)