import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

df_tron = pd.read_csv('data/tron_april.csv')
df_tron['Date'] = pd.to_datetime(df_tron['Date'])


fig = plt.figure(figsize=(10, 5))
fig.set_facecolor('white')
ax = fig.add_subplot()


ax.plot(df_tron['Date'], df_tron['Price'], marker='o', markersize=10)

plt.xticks(rotation=45)
plt.title('Daily Market Price Change in April 2023', fontsize=15)
plt.show()
