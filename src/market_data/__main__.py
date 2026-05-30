from market_data.connectors.binance.client import create_binance_client
from market_data.connectors.binance.klines import fetch_klines
from market_data.transform.candles import transform_binance_klines


def main():
    client = create_binance_client()

    raw = fetch_klines(
        client=client,
        symbol="BTCUSDT",
        interval="1m",
        limit=10,
    )

    candles = transform_binance_klines(raw)

    print(candles)


if __name__ == "__main__":
    main()
