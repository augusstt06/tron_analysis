# TRON의 일일 시장가 변동 그래프 (시간 기준)

import pandas as pd
import matplotlib.pyplot as plt
import pyupbit

plt.style.use('fivethirtyeight')
fig = plt.figure(figsize=(20, 5))
fig.set_facecolor('white')
ax = fig.add_subplot()


data = pyupbit.get_ohlcv(ticker='KRW-TRX', interval='minute60', count=24)

df_tron = pd.DataFrame(
    {"Open Price": data["open"], "Close Price": data["close"]})

tron_open = df_tron['Open Price']
tron_close = df_tron['Close Price']

max_difference = {"index": 0, "difference": 0}

for i in range(len(tron_close)):
    difference = tron_close[i] - tron_open[i]
    if (max_difference["difference"] < abs(difference)):
        if difference > 0:
            max_difference = {
                "index": i,
                "difference": abs(difference),
                "more big": tron_close[i]
            }
        else:
            max_difference = {
                "index": i,
                "difference": abs(difference),
                "more big": tron_open[i]
            }

df_difference = pd.DataFrame({"Difference": tron_open - tron_close})

ax.plot(df_tron.index, tron_open, marker='o', markersize=10, label='open')
ax.plot(df_tron.index, tron_close,
        marker='o', markersize=10, label='close')

plt.fill_between(df_tron.index, tron_close, tron_open,
                 interpolate=True, alpha=0.25)
ax.legend()

plt.title('Daily Market Price(Open/Close) for TRX')
plt.text(df_tron.index[max_difference['index']],
         max_difference['more big'], f"Max Difference Point \n {0.5}", weight="heavy", color="red", ha="center", position=(df_tron.index[max_difference['index']], max_difference['more big']+0.05))
plt.show()
