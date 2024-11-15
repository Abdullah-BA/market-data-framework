# market_data/persistence.py

from pathlib import Path
from datetime import datetime
import json
from typing import Optional, List
import pandas as pd
from .models import MarketDataResponse, DataFrequency

class DataPersistence:
    """Handles saving and loading market data"""
    
    def __init__(self, base_dir: str = "market_data_storage"):
        self.base_dir = Path(base_dir)
        self.base_dir.mkdir(parents=True, exist_ok=True)
    
    def save_data(self, response: MarketDataResponse) -> Path:
        """Save market data with metadata"""
        # Create directory structure
        symbol_dir = self.base_dir / response.symbol / response.frequency.value
        symbol_dir.mkdir(parents=True, exist_ok=True)
        
        # Create filenames with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        data_file = symbol_dir / f"data_{timestamp}.csv"
        meta_file = symbol_dir / f"metadata_{timestamp}.json"
        
        # Save data
        response.data.to_csv(data_file)
        
        # Save metadata
        metadata = {
            "source": response.source,
            "symbol": response.symbol,
            "frequency": response.frequency.value,
            "start_date": response.start_date.isoformat(),
            "end_date": response.end_date.isoformat(),
            "rows": len(response.data),
            "columns": list(response.data.columns),
            "saved_at": timestamp
        }
        
        with meta_file.open('w') as f:
            json.dump(metadata, f, indent=2)
        
        return data_file
    
    def load_latest(self, symbol: str, frequency: DataFrequency,
                   max_age_days: int = 1) -> Optional[pd.DataFrame]:
        """Load the most recent data file"""
        symbol_dir = self.base_dir / symbol / frequency.value
        
        if not symbol_dir.exists():
            return None
        
        # Find all data files
        data_files = list(symbol_dir.glob("data_*.csv"))
        if not data_files:
            return None
        
        # Get most recent file
        latest_file = max(data_files, key=lambda p: p.stat().st_mtime)
        
        # Check file age
        file_age = datetime.now() - datetime.fromtimestamp(
            latest_file.stat().st_mtime
        )
        
        if file_age.days > max_age_days:
            return None
        
        return pd.read_csv(latest_file, index_col=0, parse_dates=True)