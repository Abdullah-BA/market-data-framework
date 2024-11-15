# Example configuration file
# Copy this to config.py and update with your settings

# API Keys
ALPHA_VANTAGE_API_KEY = "your_api_key_here"
YAHOO_FINANCE_ENABLED = True

# Data Storage
DATA_DIRECTORY = "market_data_storage"

# Rate Limits
ALPHA_VANTAGE_RATE_LIMIT = 5  # calls per minute
YAHOO_FINANCE_RATE_LIMIT = 2000  # calls per day

# Validation Settings
MAX_PRICE_CHANGE_PCT = 50  # Alert on 50% price changes
MAX_VOLUME_SPIKE_FACTOR = 10  # Alert on 10x volume spikes

# Data Freshness
MAX_DATA_AGE_DAYS = 1  # Consider data older than this as stale