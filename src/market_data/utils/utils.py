from datetime import UTC, datetime

INTERVAL_TO_MILLISECONDS = {
    "1m": 60_000,
    "3m": 3 * 60_000,
    "5m": 5 * 60_000,
    "15m": 15 * 60_000,
    "30m": 30 * 60_000,
    "1h": 60 * 60_000,
    "2h": 2 * 60 * 60_000,
    "4h": 4 * 60 * 60_000,
    "6h": 6 * 60 * 60_000,
    "8h": 8 * 60 * 60_000,
    "12h": 12 * 60 * 60_000,
    "1d": 24 * 60 * 60_000,
    "3d": 3 * 24 * 60 * 60_000,
    "1w": 7 * 24 * 60 * 60_000,
    "1M": 30 * 24 * 60 * 60_000,
}


def to_milliseconds(date_value: str) -> int:
    date = datetime.fromisoformat(date_value)

    if date.tzinfo is None:
        date = date.replace(tzinfo=UTC)
    else:
        date = date.astimezone(UTC)

    return int(date.timestamp() * 1000)


def get_interval_milliseconds(interval: str) -> int:
    try:
        return INTERVAL_TO_MILLISECONDS[interval]
    except KeyError as exc:
        supported_intervals = ", ".join(INTERVAL_TO_MILLISECONDS)
        raise ValueError(
            f"Unsupported interval '{interval}'. "
            f"Supported intervals: {supported_intervals}"
        ) from exc
