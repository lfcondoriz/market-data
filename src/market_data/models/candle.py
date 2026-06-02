from dataclasses import dataclass
from datetime import datetime


@dataclass
class Candle:
    open_time: datetime
    open: float
    high: float
    low: float
    close: float

    volume: float               # Volumen en la moneda base (ej. BTC)
    close_time: datetime
    quote_asset_volume: float   # Volumen en la moneda cotizada (ej. USDT)
    number_of_trades: int       # Número de trades en el intervalo
    taker_buy_base_asset_volume: float  # Volumen comprado por takers en la moneda base
    taker_buy_quote_asset_volume: float # Volumen comprado por takers en la moneda cotizada

    symbol: str
    interval: str
    category: str
    exchange: str
