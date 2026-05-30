from market_data.models.candle import Candle


def transform_binance_klines(
    raw: list[list],
    symbol: str,
    interval: str,
) -> list[Candle]:

    return [
        Candle(
            open_time=c[0],
            close_time=c[6],
            open=float(c[1]),
            high=float(c[2]),
            low=float(c[3]),
            close=float(c[4]),
            volume=float(c[5]),
            symbol=symbol,
            interval=interval,
        )
        for c in raw
    ]