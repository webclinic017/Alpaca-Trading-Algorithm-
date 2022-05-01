#%%
from calendar import month
import datetime
from winreg import REG_DWORD_LITTLE_ENDIAN
import alpaca_trade_api as tradeapi
from alpaca_trade_api.rest import TimeFrame
import pandas as pd
import statistics as st
import statsmodels.tsa.api as tsa
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px

# PAPER KEYS
APCA_API_KEY_ID_paper = 'PK2887AEKCPBT1FSOMCC'
APCA_API_SECRET_KEY_paper = 'qYoY7sc0LHAVy9bVcyk4nQuKiQtsfokIhDtAvyKP'
APCA_API_BASE_URL_paper = 'https://paper-api.alpaca.markets'

# Market data endpoint
APCA_API_DATA_URL = 'https://data.alpaca.markets/v2'

api = tradeapi.REST(
        APCA_API_KEY_ID_paper,
        APCA_API_SECRET_KEY_paper,
        APCA_API_DATA_URL
    )

#%%
# EDA
stock_universe = ("AAPL","MSFT","FB" )
stock_universe_2 = ("AMZN","GOOG")
stock_universe_3 = ("AMZN")
df = api.get_bars(stock_universe_3, TimeFrame.Day, "2021-01-01", "2022-01-01").df

#candle stick graph
fig = go.Figure(data=[go.Candlestick(x=df.index,
                open=df['open'],
                high=df['high'],
                low=df['low'],
                close=df['close'])])
fig.show()

#%%
# Rolling averages

ninety_day_rolling_avg = df.rolling(window=90).mean()
df['close_90_day_avg'] = ninety_day_rolling_avg['close']
ninety_day_rolling_std = df.rolling(90).std()
df['close_90_day_std'] = ninety_day_rolling_std['close']

thirty_day_rolling_avg = df.rolling(30).mean()
df['close_30_day_avg'] = ninety_day_rolling_avg['close']
ninety_day_rolling_std = df.rolling(30).std()
df['close_30_day_std'] = ninety_day_rolling_std['close']



# Graphing 90 day moving avg close price against the close price
fig = go.Figure()
fig.add_trace(go.Scatter(x=df.index, y=df['close'],
                    mode='lines',
                    name='close'))
fig.add_trace(go.Scatter(x=df.index, y=df['close_90_day_avg'],
                    mode='lines',
                    name='close_90_day_avg'))
fig.add_trace(go.Scatter(x=df.index, y=df['close_90_day_std'],
                    mode='lines',
                    name='close_90_day_std'))
fig.show()

fig = px.histogram(df, x=df['close_90_day_std'])
fig.show()
fig = px.histogram(df, x=df['close_30_day_std'])
fig.show()

#%%

# std from varying timeframes from today
df.index.sort_values('asc')
df_sigma_10_days = df.head(10).std()
df_sigma_20_days = df.head(20).std()
df_sigma_30_days = df.head(30).std()

close_sigma_10_days = df_sigma_10_days['close']
close_sigma_20_days = df_sigma_20_days['close']
close_sigma_30_days = df_sigma_30_days['close']


#%%

# Standard deviation, Bollinger Bands, Money Flow, distance from a moving average, can all be used to locate extreme or unusual price moves. A good mean reversion indicator identifies extremes in prices that are likely to be temporary, not permanent.
# CAR / MDD is your Compound Annual Return divided by your Maximum Draw Down.

# set up bolinger bands to trigger buy/sell

#%%
def buy(symbol):
    pass

def sell(symbol):
    pass


class universe:
    def __init__(self, stock_universe, timeframe=None):
        if timeframe == None:
            self.timeframe = []
        self.stock_universe = stock_universe
        self.timeframe = timeframe
        self.start = timeframe[0]
        self.end = timeframe[1]
        self.universe_dict = {} 
        for count, stock in enumerate(self.stock_universe):
            self.universe_dict["stock" + str(count)] = api.get_bars(self.stock_universe[stock], TimeFrame.Day, self.start, self.end, adjustment='raw').df

        self.std = {}
        for count, stock in enumerate(self.stock_universe):
            self.std["stock" + str(count)] = st.stdev(self.universe_dict["stock" + str(count)])
        



    pass



class mean_reversion:
    def __init__(self, data):
        pass

    def backtest(self, data):
        pass

    def results(self,):
        pass

# %%
