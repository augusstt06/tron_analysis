# 국내 거래소와 해외 거래소에서의 TRON 가격 비교

# USDT => KRW 변환계수 : # 1320.84

import pandas as pd
import pyupbit
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')
fig = plt.figure(figsize=(20, 5))
fig.set_facecolor('white')
ax = fig.add_subplot()

domestic = pyupbit.get_ohlcv(
    ticker="KRW-TRX", interval="day", count=30)

foreign = pyupbit.get_ohlcv(
    ticker="USDT-TRX", interval="day", count=30)

tron_domestic = pd.DataFrame({
    "open": domestic['open'],
    "close": domestic['close']
}, index=domestic.index)

tron_foreign = pd.DataFrame({
    "open": foreign['open'] * 1320.84,
    "close": foreign['close'] * 1320.84
}, index=foreign.index)

ax.plot(tron_domestic.index,
        tron_domestic['open'], marker='o', markersize=10, label='Domestic Price')

ax.plot(tron_foreign.index,
        tron_foreign['open'], marker='o', markersize=10, label="Foreign Price")

plt.fill_between(tron_domestic.index,
                 tron_domestic['open'], tron_foreign['open'], interpolate=True, alpha=0.25)

ax.legend()

plt.title("TRON price between domestic and overseas exchanges")
plt.show()
