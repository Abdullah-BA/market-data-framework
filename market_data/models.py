# market_data/models.py

from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Optional, Dict, Any
import pandas as pd

class DataFrequency(Enum):
    """Available data frequencies"""
    MINUTE_1 = "1min"
    MINUTE_5 = "5min"
    MINUTE_15 = "15min"
    MINUTE_30 = "30min"
    HOUR_1 = "1h"
    DAY_1 = "1d"

@dataclass
class MarketDataRequest:
    """Standard format for requesting market data"""
    symbol: str
    frequency: DataFrequency
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None

@dataclass
class MarketDataResponse:
    """Standard format for market data responses"""
    data: pd.DataFrame
    source: str
    symbol: str
    frequency: DataFrequency
    start_date: datetime
    end_date: datetime
    metadata: Dict[str, Any] = None

class MarketDataError(Exception):
    """Custom exception for market data errors"""
    pass