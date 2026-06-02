from market_data.models.candle import Candle


def transform_binance_klines(
    raw: list[list],
    symbol: str,
    interval: str,
    exchange: str,
) -> list[Candle]:

    return [
        Candle(
            open_time=c[0],
            open=float(c[1]),
            high=float(c[2]),
            low=float(c[3]),
            close=float(c[4]),
            volume=float(c[5]),
            close_time=c[6],
            quote_asset_volume=float(c[7]),
            number_of_trades=int(c[8]),
            taker_buy_base_asset_volume=float(c[9]),
            taker_buy_quote_asset_volume=float(c[10]),
            symbol=symbol,
            interval=interval,
            category="spot",
            exchange=exchange,
        )
        for c in raw
    ]
