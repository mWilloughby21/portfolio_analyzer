# market_data.py
# Fetch prices & Historical data for stocks and ETFs using yfinance

import yfinance as yf
from typing import List
from portfolio import Portfolio, Position

class MarketData:
    
    # Get current price for a single ticker
    @staticmethod
    def get_curr_price(ticker: str) -> float:
        stock = yf.Ticker(ticker)
        return stock.history(period='1d')['Close'].iloc[-1]
    
    # Get current prices for all positions in the portfolio
    @classmethod
    def get_prices(cls, positions: List[Position]) -> dict:
        prices = {}
        for pos in positions:
            prices[pos.ticker] = round(float(cls.get_curr_price(pos.ticker)), 2)
        return prices