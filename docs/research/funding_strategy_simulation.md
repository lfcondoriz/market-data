# 📊 Rendimiento teórico del funding (Binance Spot vs Binance Futures)

* 10.95% anual (0.01% cada 8 horas):

$$
0.01\% \times 3 \, periodos/día \times 365 , días/año = 10.95\% \, anual
$$

---

## ⚙️ Supuestos del modelo

* Sin interés compuesto
* Capital fijo bloqueado en hedge
* Sin apalancamiento
* Estrategia delta-neutral:

  * Spot buy: 1,000 USDT
  * Short futures: 1,000 USDT

---

## 💸 Fees de entrada y salida (taker)

Sin BNB para fees, sin VIP, sin descuentos:

| |Maker (Order limitada) | Taker (Order de mercado)|
|---|---|---|
|**Spot**|0.1%|0.10%|
|**Futures**|0.02%|0.02%|

---

## 💰 Capital total inmovilizado

$$
Capital = 2,000 \, USDT
$$

---

## 📉 Costos de ejecución (entrada + salida)

### Entrada:

* Spot buy (Maker):
  $$
  1000 \times 0.10\% = 1 \, USDT
  $$

* Futures short (Maker):
  $$
  1000 \times 0.02\% = 0.2 \, USDT
  $$

### Salida:

* Spot sell (Maker): 1 USDT
* Futures close (Maker): 0.2 USDT

### Total fees:

$$
Fees_{total} = (1 + 0.2) \times 2 = 2.4 \, USDT
$$

---

## 💰 Ganancia bruta por funding

(Asumiendo funding constante y sin variación)

$$
Ganancia_{bruta} = 1000 \times 10.95\% = 109.5 \, USDT
$$

---

## 📊 Ganancia neta anual

$$
Ganancia_{neta} = 109.5 - 2.4 = 107.1 \, USDT
$$

---

## 📈 Rendimiento sobre capital inmovilizado

$$
Rendimiento = \frac{107.1}{2000} \times 100 = 5.355\% \, anual
$$

---

## 🧠 Nota importante

Este resultado asume:

* funding constante y simétrico durante todo el año
* ejecución perfecta sin slippage
* liquidez suficiente en spot y futuros
* ausencia de cambios de régimen de mercado


# 📊 Rendimiento teórico del funding (Quantfury Spot vs Binance Futures)
* 10.95% anual (0.01% cada 8 horas):

$$
0.01\% \times 3 \, periodos/día \times 365 , días/año = 10.95\% \, anual
$$

---

## ⚙️ Supuestos del modelo

* Sin interés compuesto
* Capital fijo bloqueado en hedge
* Con apalancamiento
* Estrategia delta-neutral:

  * Quantfury Spot buy: 1,000 USDT
  * Binance Short futures: 1,000 USDT

---

## 💸 Fees de entrada y salida (taker)

Sin BNB para fees, sin VIP, sin descuentos:

| |Maker (Order limitada) | Taker (Order de mercado)|
|---|---|---|
|**Spot**|0.1%|0.10%|
|**Futures**|0.02%|0.02%|
||||
|**Quantfury Spot**|0%|0%|

---

## 💰 Capital total inmovilizado

$$
Capital = 2,000 \, USDT
$$

## Apalancamiento:

Ajustamos el apalancamientto a $15 \%$ (se liquida la posición si el activo baja/sube un 15%):

$$
Leverage = \frac{1}{0.15} = 6.67x
$$

Osea que el capital efectivo que ve el mercado por posición es:
$$
Capital_{efectivo} = 1000 \times 6.67 = 6670 \, USDT
$$

## 📉 Posiciones Efectivas
* Quantfury Spot buy: 6,670 USDT
* Binance Short futures: 6,670 USDT
  * Comisión de entrada y salida se calcula sobre el capital efectivo:
    $$ 
    FeesTotal = 2 \times 0.02\% \times 6,670 = 2.668 \, USDT
    $$

## 💰 Ganancia bruta por funding

(Asumiendo funding constante y sin variación)

$$
Ganancia_{bruta} = 6,670 \times 10.95\% = 730.965 \, USDT
$$

## 📊 Ganancia neta anual

$$
Ganancia_{neta} = 730.965 - 2.668 = 728.297 \, USDT
$$

---

## 📈 Rendimiento sobre capital inmovilizado

$$
Rendimiento = \frac{728.297}{2000} \times 100 = 36.415\% \, anual
$$