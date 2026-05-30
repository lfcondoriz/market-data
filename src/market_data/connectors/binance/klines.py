def fetch_klines(client, symbol, interval, start_time=None, end_time=None, limit=1500):
    response = client.rest_api.kline_candlestick_data(
        symbol=symbol,
        interval=interval,
        start_time=start_time,
        end_time=end_time,
        limit=limit,
    )

    return response.data() if hasattr(response, "data") else []