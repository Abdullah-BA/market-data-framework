# Market Data Framework

A flexible and extensible Python framework for fetching, validating, and storing financial market data from multiple sources.

## Features

- Multiple data source support (Alpha Vantage, Yahoo Finance)
- Built-in data validation
- Persistent storage with metadata
- Automatic failover between providers
- Comprehensive logging
- Easy to extend with new data sources

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/market-data-framework.git
cd market-data-framework
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Copy `config.example.py` to `config.py` and add your API keys:
```bash
cp config.example.py config.py
```

## Quick Start

1. Set up your configuration in `config.py`:
```python
ALPHA_VANTAGE_API_KEY = "your_api_key_here"
```

2. Run the example script:
```bash
python main.py
```

## Usage

### Basic Usage

```python
from market_data import (
    DataFrequency,
    MarketDataRequest,
    AlphaVantageProvider,
    DataValidator,
    DataPersistence
)

# Initialize components
provider = AlphaVantageProvider("your_api_key")
validator = DataValidator()
storage = DataPersistence()

# Create request
request = MarketDataRequest(
    symbol="AAPL",
    frequency=DataFrequency.MINUTE_5,
    start_date=datetime.now() - timedelta(days=1),
    end_date=datetime.now()
)

# Fetch and process data
response = provider.get_market_data(request)
issues = validator.validate(response)
if not issues:
    storage.save_data(response)
```

### Adding a New Data Provider

1. Create a new provider class in `market_data/providers.py`:
```python
class MyNewProvider(MarketDataProvider):
    def get_market_data(self, request: MarketDataRequest) -> MarketDataResponse:
        # Implement your data fetching logic here
        pass
```

2. Register it in your code:
```python
provider = MyNewProvider()
response = provider.get_market_data(request)
```

## Project Structure

```
market_data_framework/
├── market_data/              # Main package
│   ├── __init__.py          # Package initialization
│   ├── models.py            # Data models
│   ├── providers.py         # Data providers
│   ├── validation.py        # Data validation
│   └── persistence.py       # Data storage
├── tests/                   # Test directory
│   ├── __init__.py
│   ├── test_providers.py
│   ├── test_validation.py
│   └── test_persistence.py
├── examples/                # Example scripts
├── config.example.py        # Example configuration
├── config.py               # Local configuration (git-ignored)
├── main.py                 # Main script
├── requirements.txt        # Project dependencies
├── setup.py               # Package setup
└── README.md              # This file
```

## Configuration

The following settings can be configured in `config.py`:

- `ALPHA_VANTAGE_API_KEY`: Your Alpha Vantage API key
- `DATA_DIRECTORY`: Where to store market data
- `MAX_PRICE_CHANGE_PCT`: Maximum allowed price change percentage
- `MAX_VOLUME_SPIKE_FACTOR`: Maximum allowed volume spike factor

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request