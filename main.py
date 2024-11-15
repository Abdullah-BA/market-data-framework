# main.py

from datetime import datetime, timedelta
import logging
from market_data import (
    DataFrequency,
    MarketDataRequest,
    AlphaVantageProvider,
    YahooFinanceProvider,
    DataValidator,
    DataPersistence
)
from config import (
    ALPHA_VANTAGE_API_KEY,
    MAX_PRICE_CHANGE_PCT,
    MAX_VOLUME_SPIKE_FACTOR,
    DATA_DIRECTORY
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def main():
    # Initialize components
    alpha_vantage = AlphaVantageProvider(ALPHA_VANTAGE_API_KEY)
    yahoo = YahooFinanceProvider()
    validator = DataValidator(
        max_price_change_pct=MAX_PRICE_CHANGE_PCT,
        max_volume_spike_factor=MAX_VOLUME_SPIKE_FACTOR
    )
    persistence = DataPersistence(DATA_DIRECTORY)
    
    # Create data request
    request = MarketDataRequest(
        symbol="AAPL",
        frequency=DataFrequency.MINUTE_5,
        start_date=datetime.now() - timedelta(days=1),
        end_date=datetime.now()
    )
    
    try:
        # Try Yahoo Finance first
        logger.info("Fetching data from Yahoo Finance...")
        response = yahoo.get_market_data(request)
        
        # Validate the data
        issues = validator.validate(response)
        if issues:
            logger.warning("Data quality issues found:")
            for issue in issues:
                logger.warning(f"- {issue}")
            
            # Try Alpha Vantage as backup
            logger.info("Trying Alpha Vantage as backup...")
            response = alpha_vantage.get_market_data(request)
            issues = validator.validate(response)
            if issues:
                logger.warning("Alpha Vantage data also has issues:")
                for issue in issues:
                    logger.warning(f"- {issue}")
        
        # Save the data
        logger.info("Saving data...")
        file_path = persistence.save_data(response)
        logger.info(f"Data saved to {file_path}")
        
        # Show some basic stats
        df = response.data
        logger.info("\nData Summary:")
        logger.info(f"Rows: {len(df)}")
        logger.info(f"Date Range: {df.index.min()} to {df.index.max()}")
        logger.info(f"Price Range: ${df['Low'].min():.2f} - ${df['High'].max():.2f}")
        logger.info(f"Average Volume: {df['Volume'].mean():.0f}")
        
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())