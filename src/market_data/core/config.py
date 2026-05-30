import os


class Settings:
    BINANCE_API_KEY = os.getenv("API_KEY", "")
    BINANCE_API_SECRET = os.getenv("API_SECRET", "")
