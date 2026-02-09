# analytics.py
# Compute metrics like volatility, Sharpe ratio, and drawdown for the portfolio

from typing import List, Dict
from portfolio import Position

class Analytics:
    
    # Current value of a position
    @staticmethod
    def position_value(position: Position, curr_price: float) -> float:
        return position.shares * curr_price
    
    # Current value of the portfolio
    @classmethod
    def portfolio_value(cls, positions: List[Position], prices: Dict[str, float]) -> float:
        return sum(
            cls.position_value(p, prices[p.ticker]) for p in positions
        )
    
    # Calculate gains/losses for each position
    @classmethod
    def gains_losses(cls, positions: List[Position], prices: Dict[str, float]) -> Dict[str, float]:
        return {
            p.ticker: round(cls.position_value(p, prices[p.ticker]) - (p.shares * p.purchase_price), 2) for p in positions
        }
    
    # Calculate % returns for each position based on portfolio value
    @classmethod
    def allocation(cls, positions: List[Position], prices: Dict[str, float]) -> Dict[str, float]:
        total_value = cls.portfolio_value(positions, prices)
        return {
            p.ticker: round(cls.position_value(p, prices[p.ticker]) / total_value, 2) for p in positions
        }