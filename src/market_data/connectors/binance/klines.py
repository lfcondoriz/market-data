from typing import Any


def fetch_klines(
    client: Any,
    symbol: str,
    interval: str,
    start_time: int | None = None,
    end_time: int | None = None,
    limit: int = 1500,
) -> list[list]:
    response = client.rest_api.kline_candlestick_data(
        symbol=symbol,
        interval=interval,
        start_time=start_time,
        end_time=end_time,
        limit=limit,
    )

    return response.data() if hasattr(response, "data") else []