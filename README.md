## TRON 분석

## 사용 스택 / 라이브러리

- [Python](https://www.python.org/downloads/)

  - [Pandas](https://pandas.pydata.org/)

    ```bash
    # Install Pandas
    pip install pandas
    ```

  - [pyupbit](https://pyupbit.readthedocs.io/en/latest/)

    ```bash
    # Install pyupbit
    pip install pyupbit
    ```

    파이썬에서 업비트 API를 손쉽게 사용하기 위해 사용하는 모듈

    - 주요 메서드

      - `pyupbit.get_tickers(fiat='국가')`
        - 국가별 마켓 종목 코드 조회
      - `pyupbit.get_ohlcv(ticker='종목', interval='조회주기', count=조회수)`
        - 과거 종목 데이터 조회 (파라미터에 따라 범위 조절 가능)

### [1. daily_deals.py](https://github.com/augusstt06/tron_analysis/blob/main/daliy_deals.py)

TRON에 대한 Daily Hourly Graph 분석

#### 코드

```bash
import pandas as pd
import matplotlib.pyplot as plt
import pyupbit

# 기본적인 그래프 세팅
plt.style.use('fivethirtyeight')

fig = plt.figure(figsize=(20, 5))
fig.set_facecolor('white')
ax = fig.add_subplot()

# pyupbit를 이용하여 한국거래소의 TRON (TRX)를 하루 주기로 최근 2주간 (14번) 조회
data = pyupbit.get_ohlcv(ticker='KRW-TRX', interval='day', count=14)

# TRON의 시가와 종가 컬럼을 따로 데이터프레임화
df_tron = pd.DataFrame(
    {
        "Open Price": data["open"],
        "Close Price": data["close"]
        }
    )

tron_open = df_tron['Open Price']
tron_close = df_tron['Close Price']

# 시가와 종가의 차이를 알기위한 변수 선언 (가장 시가와 종가의 차이가 큰 지점을 나타내는 difference key와 날짜를 나타내는 index key)
max_difference = {"index": 0, "difference": 0}

# 반복문을 이용하여 2주간의 데이터 loop, 시가와 종가의 차이를 계산하여 가장 큰 차이가격을 계속해서 difference에 갱신하여 최대 차이 날짜와 가격을 계산한다.
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

# 위의 데이터들을 이용하여 그래프 생성
ax.plot(df_tron.index, tron_open, marker='o', markersize=10, label='open')
ax.plot(df_tron.index, tron_close,
        marker='o', markersize=10, label='close')

plt.fill_between(df_tron.index, tron_close, tron_open,
                interpolate=True, alpha=0.25)
ax.legend()

plt.title('Daily Market Price(Open/Close) for TRX')
# 가장 큰 차이가격과 날짜를 나타내는 max_difference를 이용하여 해당 지점을 그래프에 표기한다.
plt.text(df_tron.index[max_difference['index']],
        max_difference['more big'], f"Max Difference Point \n {max_difference['difference']}", weight="heavy", color="red", ha="center", position=(df_tron.index[max_difference['index']], max_difference['more big']+0.05))

plt.show()

```

#### 그래프 결과

![그래프](https://velog.velcdn.com/images/cnffjd95/post/1579dbfc-3f12-4d2e-8902-0ecd6e1d05ae/image.png)

### [2. price_comparision.py](https://github.com/augusstt06/tron_analysis/blob/main/price_comparision.py)

국내 거래소에서 거래되는 TRON의 가격과 해외거래소에서 거래되는 TRON의 가격을 비교하여 김치 프리미엄이 있는지 확인해본다.

#### 코드

```bash
import pandas as pd
import pyupbit
import matplotlib.pyplot as plt

# 기본적인 그래프 세팅
plt.style.use('fivethirtyeight')
fig = plt.figure(figsize=(20, 5))
fig.set_facecolor('white')
ax = fig.add_subplot()

# 국내 거래소 TRON가격을 domestic으로, 해외거래소 foreign으로 설정하여 최근 30일간의 데이터 조회
domestic = pyupbit.get_ohlcv(
    ticker="KRW-TRX", interval="day", count=30)

foreign = pyupbit.get_ohlcv(
    ticker="USDT-TRX", interval="day", count=30)

# 두 거래소의 데이터의 시가, 종가 컬럼을 데이터프레임으로 제작
tron_domestic = pd.DataFrame({
    "open": domestic['open'],
    "close": domestic['close']
}, index=domestic.index)

# 해외거래소의 경우 화폐단위가 다르기 때문에 환율을 맞추기위하여 환율계수 사용
tron_foreign = pd.DataFrame({
    "open": foreign['open'] * 1320.84,
    "close": foreign['close'] * 1320.84
}, index=foreign.index)

# 두 거래소를 그래프로 제작
ax.plot(tron_domestic.index,
        tron_domestic['open'], marker='o', markersize=10, label='Domestic Price')

ax.plot(tron_foreign.index,
        tron_foreign['open'], marker='o', markersize=10, label="Foreign Price")

plt.fill_between(tron_domestic.index,
                 tron_domestic['open'], tron_foreign['open'], interpolate=True, alpha=0.25)

ax.legend()
plt.xticks(fontsize=8)
plt.title("TRON price between domestic and overseas exchanges")
plt.show()

```
