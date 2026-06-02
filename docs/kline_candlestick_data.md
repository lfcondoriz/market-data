Comportamiento de la función kline_candlestick_data según los parámetros de entrada:

| start_time | end_time | limit    | comportamiento                     |
| ---------- | -------- | -------- | ---------------------------------- |
| ❌          | ❌        | ❌        | últimas 1500                       |
| ❌          | ✅        | ❌        | últimas 1500 antes de end_time     |
| ✅          | ❌        | ❌        | desde start_time hasta ahora       |
| ✅          | ✅        | ❌        | rango completo                     |
| ❌          | ❌        | ✅ ≤ 1500 | últimas N                          |
| ❌          | ❌        | ✅ > 1500 | error                              |
| ✅          | ❌        | ✅        | desde start_time hasta completar N |
| ✅          | ✅        | ✅        | rango limitado por N               |
