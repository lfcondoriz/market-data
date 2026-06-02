from market_data.connectors.binance.client import create_binance_client
from market_data.transform.candles import transform_binance_klines
from market_data.connectors.binance.klines import kline_candlestick_data


def main():
    client = create_binance_client()

    symbol = "BTCUSDT"
    interval = "1M"

    raw = kline_candlestick_data(
        client=client,
        symbol=symbol,
        interval=interval,
        limit=10,
    )

    candles = transform_binance_klines(
        raw=raw,
        symbol=symbol,
        interval=interval,
        exchange="binance",
    )

    print(candles)


if __name__ == "__main__":
    main()
