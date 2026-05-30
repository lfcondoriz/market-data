from binance_sdk_derivatives_trading_usds_futures.derivatives_trading_usds_futures import (
    DERIVATIVES_TRADING_USDS_FUTURES_REST_API_PROD_URL,
    ConfigurationRestAPI,
    DerivativesTradingUsdsFutures,
)

from market_data.core.config import Settings


def create_binance_client():
    config = ConfigurationRestAPI(
        api_key=Settings.BINANCE_API_KEY,
        api_secret=Settings.BINANCE_API_SECRET,
        base_path=DERIVATIVES_TRADING_USDS_FUTURES_REST_API_PROD_URL,
    )

    return DerivativesTradingUsdsFutures(config_rest_api=config)
