from dataclasses import dataclass


@dataclass
class Candle:
    open_time: int
    close_time: int

    open: float
    high: float
    low: float
    close: float

    volume: float

    symbol: str
    interval: str