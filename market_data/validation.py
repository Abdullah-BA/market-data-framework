# market_data/validation.py

from typing import List
import pandas as pd
from .models import MarketDataResponse

class DataValidator:
    """Validates market data quality"""
    
    def __init__(self, max_price_change_pct: float = 50, 
                 max_volume_spike_factor: float = 10):
        self.max_price_change_pct = max_price_change_pct
        self.max_volume_spike_factor = max_volume_spike_factor
    
    def validate(self, response: MarketDataResponse) -> List[str]:
        """Run all validations on the data"""
        issues = []
        df = response.data
        
        # Check for missing values
        if df.isnull().any().any():
            issues.append("Data contains missing values")
        
        # Validate price data
        price_issues = self._validate_prices(df)
        issues.extend(price_issues)
        
        # Validate volume data
        volume_issues = self._validate_volume(df)
        issues.extend(volume_issues)
        
        return issues
    
    def _validate_prices(self, df: pd.DataFrame) -> List[str]:
        """Validate price data quality"""
        issues = []
        
        # Check high >= low
        if not (df['High'] >= df['Low']).all():
            issues.append("Found High price lower than Low price")
        
        # Check for zero prices
        if (df[['Open', 'High', 'Low', 'Close']] == 0).any().any():
            issues.append("Found zero prices")
        
        # Check for suspicious price changes
        pct_change = df['Close'].pct_change().abs() * 100
        if (pct_change > self.max_price_change_pct).any():
            issues.append(
                f"Found price changes greater than {self.max_price_change_pct}%"
            )
        
        return issues
    
    def _validate_volume(self, df: pd.DataFrame) -> List[str]:
        """Validate volume data quality"""
        issues = []
        
        # Check for negative volume
        if (df['Volume'] < 0).any():
            issues.append("Found negative volume")
        
        # Check for volume spikes
        avg_volume = df['Volume'].mean()
        if (df['Volume'] > avg_volume * self.max_volume_spike_factor).any():
            issues.append(
                f"Found volume spikes >{self.max_volume_spike_factor}x average"
            )
        
        return issues