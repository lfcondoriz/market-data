from typing import Any

from market_data.utils.utils import get_interval_milliseconds


def kline_candlestick_data(
    client: Any,
    symbol: str,
    interval: str,
    start_time: int | None = None,
    end_time: int | None = None,
    limit: int | None = None,
) -> list[list]:

    MAX_REQUEST_LIMIT = 1500

    # -------------------------
    # Validaciones
    # -------------------------

    if limit is not None and limit <= 0:
        raise ValueError("limit must be greater than 0")

    if start_time is not None and end_time is not None and start_time > end_time:
        raise ValueError("start_time must be less than or equal to end_time")

    # -------------------------
    # Caso:
    # últimas 1500 velas
    # -------------------------

    if start_time is None and end_time is None and limit is None:
        response = client.rest_api.kline_candlestick_data(
            symbol=symbol,
            interval=interval,
            limit=MAX_REQUEST_LIMIT,
        )

        return response.data() if hasattr(response, "data") else []

    # -------------------------
    # Caso:
    # últimas N velas
    # -------------------------

    if start_time is None and end_time is None and limit is not None:
        if limit > MAX_REQUEST_LIMIT:
            raise ValueError(f"limit > {MAX_REQUEST_LIMIT} requires start_time")

        response = client.rest_api.kline_candlestick_data(
            symbol=symbol,
            interval=interval,
            limit=limit,
        )

        return response.data() if hasattr(response, "data") else []

    # -------------------------
    # Caso:
    # últimas velas antes de end_time
    # -------------------------

    if start_time is None and end_time is not None and limit is None:
        response = client.rest_api.kline_candlestick_data(
            symbol=symbol,
            interval=interval,
            end_time=end_time,
            limit=MAX_REQUEST_LIMIT,
        )

        return response.data() if hasattr(response, "data") else []

    # -------------------------
    # Caso:
    # últimas N velas antes de end_time
    # -------------------------

    if start_time is None and end_time is not None and limit is not None:
        if limit > MAX_REQUEST_LIMIT:
            raise ValueError(f"limit > {MAX_REQUEST_LIMIT} requires start_time")

        response = client.rest_api.kline_candlestick_data(
            symbol=symbol,
            interval=interval,
            end_time=end_time,
            limit=limit,
        )

        return response.data() if hasattr(response, "data") else []

    # -------------------------
    # Casos con start_time
    # (paginación)
    # -------------------------

    interval_ms = get_interval_milliseconds(interval)

    collected_klines: list[list] = []

    current_start_time = start_time

    while True:
        remaining = None

        if limit is not None:
            remaining = limit - len(collected_klines)

            if remaining <= 0:
                break

        request_limit = (
            min(MAX_REQUEST_LIMIT, remaining)
            if remaining is not None
            else MAX_REQUEST_LIMIT
        )

        response = client.rest_api.kline_candlestick_data(
            symbol=symbol,
            interval=interval,
            start_time=current_start_time,
            end_time=end_time,
            limit=request_limit,
        )

        klines = response.data() if hasattr(response, "data") else []

        if not klines:
            break

        # Protección ante APIs defectuosas
        if remaining is not None:
            klines = klines[:remaining]

        collected_klines.extend(klines)

        latest_open_time = max(int(kline[0]) for kline in klines)

        next_start_time = latest_open_time + interval_ms

        if current_start_time is not None and next_start_time <= current_start_time:
            break

        if end_time is not None and next_start_time > end_time:
            break

        current_start_time = next_start_time

        # Última página
        if len(klines) < request_limit:
            break

    return collected_klines
