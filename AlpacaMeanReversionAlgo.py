#%%
from datetime import datetime
import alpaca_trade_api as tradeapi
from alpaca_trade_api.rest import TimeFrame
import pandas as pd
import statistics as st
import statsmodels.tsa.api as tsa
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import plotly.graph_objects as go

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
stock_universe = ("AAPL","GOOG","MSFT","AMZN","FB" )

df = api.get_bars(stock_universe, TimeFrame.Day, "2012-01-01", "2022-01-01").df
df = df.reset_index(level=0)

line_chart = sb.lineplot(data=df, x="timestamp", y='close', hue='symbol')


fig = go.Figure(data=[go.Candlestick(x=df['timestamp'],
                open=df['open'],
                high=df['high'],
                low=df['low'],
                close=df['close'])])

fig.show()

#%%
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
