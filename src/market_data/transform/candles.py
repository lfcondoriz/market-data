from market_data.models.candle import Candle


def transform_binance_klines(raw: list[list]) -> list[Candle]:
    return [
        Candle(
            open_time=c[0],
            open=float(c[1]),
            high=float(c[2]),
            low=float(c[3]),
            close=float(c[4]),
            volume=float(c[5]),
        )
        for c in raw
    ]