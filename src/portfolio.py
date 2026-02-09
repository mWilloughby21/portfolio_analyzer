# portfolio.py
# Load portfolio from CSV file and calculate returns

import pandas as pd
from dataclasses import dataclass
from typing import List
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
CSV_PATH = BASE_DIR / 'data' / 'portfolio.csv'

@dataclass
class Position:
    ticker: str
    shares: float
    purchase_price: float
    purchase_date: str

class Portfolio:
    # Initialize with a list of positions
    def __init__(self, positions: List[Position]):
        self.positions = positions
    
    # Load portfolio from a CSV file
    @classmethod
    def from_csv(cls, file_path: str) -> 'Portfolio':
        df = pd.read_csv(file_path)
        
        positions = []
        for _, row in df.iterrows():
            position = Position(
                ticker=row['ticker'],
                shares=row['shares'],
                purchase_price=row['purchase_price'],
                purchase_date=row['purchase_date']
            )
            positions.append(position)
        
        return cls(positions)
    
    # Calculate total cost basis of the portfolio
    def total_cost_basis(self) -> float:
        return sum(
            p.shares * p.purchase_price for p in self.positions
        )