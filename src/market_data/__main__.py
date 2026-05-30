from market_data.connectors.binance.client import create_binance_client
from market_data.connectors.binance.klines import fetch_klines

def main():
    client = create_binance_client()

    data = fetch_klines(
        client=client,
        symbol="BTCUSDT",
        interval="1m",
        limit=10,
    )

    print(data)


if __name__ == "__main__":
    main()
