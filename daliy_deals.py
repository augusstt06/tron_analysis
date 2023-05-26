# TRON의 일일 시장가 변동 그래프 (일 기준)

import pandas as pd
import matplotlib.pyplot as plt
import pyupbit

plt.style.use('fivethirtyeight')


# df_tron = pd.read_csv('data/tron_april.csv')
# df_tron['Date'] = pd.to_datetime(df_tron['Date'])


# fig = plt.figure(figsize=(10, 5))
# fig.set_facecolor('white')
# ax = fig.add_subplot()


# ax.plot(df_tron['Date'], df_tron['Price'], marker='o', markersize=10)

# plt.xticks(rotation=45)
# plt.title('Daily Market Price Change in April 2023', fontsize=15)
# plt.show()

fig = plt.figure(figsize=(20, 5))
fig.set_facecolor('white')
ax = fig.add_subplot()

data = pyupbit.get_ohlcv(ticker='KRW-TRX', interval='day', count=14)

df_tron = pd.DataFrame(
    {
        "Open Price": data["open"],
        "Close Price": data["close"]
    }
)

tron_open = df_tron['Open Price']
tron_close = df_tron['Close Price']
max_difference = {"index": 0, "difference": 0}
print(tron_open, "시가")
print(tron_close, "종가")

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

ax.plot(df_tron.index, tron_open, marker='o', markersize=10, label='open')
ax.plot(df_tron.index, tron_close,
        marker='o', markersize=10, label='close')

plt.fill_between(df_tron.index, tron_close, tron_open,
                 interpolate=True, alpha=0.25)
ax.legend()

plt.title('Daily Market Price(Open/Close) for TRX')
plt.text(df_tron.index[max_difference['index']],
         max_difference['more big'], f"Max Difference Point \n {max_difference['difference']}", weight="heavy", color="red", ha="center", position=(df_tron.index[max_difference['index']], max_difference['more big']+0.05))
plt.show()
