import pytest
from datetime import datetime, timedelta
import pandas as pd
from market_data import (
    DataFrequency,
    MarketDataRequest,
    MarketDataResponse,
    MarketDataError,
    AlphaVantageProvider,
    YahooFinanceProvider
)

@pytest.fixture
def sample_request():
    return MarketDataRequest(
        symbol="AAPL",
        frequency=DataFrequency.MINUTE_5,
        start_date=datetime.now() - timedelta(days=1),
        end_date=datetime.now()
    )

@pytest.fixture
def mock_price_data():
    return pd.DataFrame({
        'Open': [100, 101, 102],
        'High': [102, 103, 104],
        'Low': [99, 100, 101],
        'Close': [101, 102, 103],
        'Volume': [1000, 1100, 1200]
    }, index=pd.date_range(start='2024-01-01', periods=3, freq='5min'))

def test_alpha_vantage_provider_initialization():
    provider = AlphaVantageProvider("test_key")
    assert provider.api_key == "test_key"

def test_yahoo_provider_initialization():
    provider = YahooFinanceProvider()
    assert isinstance(provider, YahooFinanceProvider)

def test_request_validation(sample_request):
    assert sample_request.symbol == "AAPL"
    assert sample_request.frequency == DataFrequency.MINUTE_5
    assert isinstance(sample_request.start_date, datetime)
    assert isinstance(sample_request.end_date, datetime)

# Add more tests as needed