# market_data/providers.py

from abc import ABC, abstractmethod
import pandas as pd
import requests
import yfinance as yf
from datetime import datetime
import time
from typing import Dict, Any

from .models import MarketDataRequest, MarketDataResponse, DataFrequency, MarketDataError

class MarketDataProvider(ABC):
    """Base class for all data providers"""
    
    @abstractmethod
    def get_market_data(self, request: MarketDataRequest) -> MarketDataResponse:
        pass

    def _standardize_columns(self, df: pd.DataFrame) -> pd.DataFrame:
        """Standardize column names"""
        standard_columns = {
            'open': 'Open',
            'high': 'High',
            'low': 'Low',
            'close': 'Close',
            'volume': 'Volume',
            'adj close': 'Adj_Close',
        }
        df.columns = [col.lower() for col in df.columns]
        return df.rename(columns=standard_columns)

class AlphaVantageProvider(MarketDataProvider):
    """Alpha Vantage API provider"""
    
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.session = requests.Session()
        
    def get_market_data(self, request: MarketDataRequest) -> MarketDataResponse:
        # API endpoint parameters
        params = {
            "function": "TIME_SERIES_INTRADAY",
            "symbol": request.symbol,
            "interval": request.frequency.value,
            "apikey": self.api_key,
            "outputsize": "full"
        }
        
        try:
            # Make API request
            response = self.session.get(
                "https://www.alphavantage.co/query",
                params=params
            )
            data = response.json()
            
            # Extract time series data
            time_series_key = f"Time Series ({request.frequency.value})"
            if time_series_key not in data:
                raise MarketDataError(
                    f"Error: {data.get('Note', 'Unknown error')}"
                )
            
            # Convert to DataFrame
            df = pd.DataFrame.from_dict(
                data[time_series_key],
                orient='index',
                dtype=float
            )
            df.index = pd.to_datetime(df.index)
            df = self._standardize_columns(df)
            
            return MarketDataResponse(
                data=df,
                source="alpha_vantage",
                symbol=request.symbol,
                frequency=request.frequency,
                start_date=df.index.min(),
                end_date=df.index.max(),
                metadata=data.get("Meta Data")
            )
            
        except Exception as e:
            raise MarketDataError(f"Alpha Vantage error: {str(e)}")

class YahooFinanceProvider(MarketDataProvider):
    """Yahoo Finance provider"""
    
    def get_market_data(self, request: MarketDataRequest) -> MarketDataResponse:
        try:
            # Get data using yfinance
            ticker = yf.Ticker(request.symbol)
            df = ticker.history(
                interval=request.frequency.value,
                start=request.start_date,
                end=request.end_date
            )
            
            df = self._standardize_columns(df)
            
            return MarketDataResponse(
                data=df,
                source="yahoo_finance",
                symbol=request.symbol,
                frequency=request.frequency,
                start_date=df.index.min(),
                end_date=df.index.max(),
                metadata={"info": ticker.info}
            )
            
        except Exception as e:
            raise MarketDataError(f"Yahoo Finance error: {str(e)}")