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

ax.plot(df_tron.index, tron_open, marker='o', markersize=10, label='open')
ax.plot(df_tron.index, tron_close,
        marker='o', markersize=10, label='close')

ax.legend()

plt.title('Daily Market Price(Open/Close) for TRX')
plt.show()
