#%%
# Alpaca Algorithmic Trading
import alpaca_trade_api as tradeapi
from alpaca_trade_api.rest import TimeFrame
import pandas as pd
import statistics as st
import statsmodels.tsa.api as tsa
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

#LIVE KEYS
##########################

# PAPER KEYS
APCA_API_KEY_ID_paper = 'PK2887AEKCPBT1FSOMCC'
APCA_API_SECRET_KEY_paper = 'qYoY7sc0LHAVy9bVcyk4nQuKiQtsfokIhDtAvyKP'
APCA_API_BASE_URL_paper = 'https://paper-api.alpaca.markets'

# Market data endpoint
APCA_API_DATA_URL = 'https://data.alpaca.markets/v2'

api = tradeapi.REST(
        APCA_API_KEY_ID_paper,
        APCA_API_SECRET_KEY_paper,
        APCA_API_BASE_URL_paper
    )

# Get our account information.
account = api.get_account()

# Check if our account is restricted from trading.
if account.trading_blocked:
    print('Account is currently restricted from trading.')

# Check how much money we can use to open new positions.
print('${} is available as buying power.'.format(account.buying_power))

# Check our current balance vs. our balance at the last market close
balance_change = float(account.equity) - float(account.last_equity)
print(f'Today\'s portfolio balance change: ${balance_change}')
#%%

# # Submit a market order to buy 1 share of Apple at market price
# api.submit_order(
#     symbol='AAPL',
#     qty=1,
#     side='buy',
#     type='market',
#     time_in_force='gtc'
# )

# # Submit a limit order to attempt to sell 1 share of AMD at a
# # particular price ($20.50) when the market opens
# api.submit_order(
#     symbol='AMD',
#     qty=1,
#     side='sell',
#     type='limit',
#     time_in_force='opg',
#     limit_price=20.50
# )

#%%
# testing code that will be in Pairs class
# generalizing pair data for a list of stock pairs

stock_pairs = [["AAPL","GOOG"], []]
pair_dict = {} 
for count, pair in enumerate(stock_pairs):
    pair_dict["pair" + str(count)] = api.get_bars(stock_pairs[pair], TimeFrame.Day, "2021-01-01", "2022-01-01", adjustment='raw').df

# stock_A_df = pairs_df.loc[pairs_df['symbol'] == stock_pairs[0][0]]
# stock_B_df = pairs_df.loc[pairs_df['symbol'] == stock_pairs[0][1]]
# stock_A_closing_prices = stock_A_df['close']
# stock_B_closing_prices = stock_B_df['close']

#%%

pairs_df = api.get_bars(stock_pairs[pair], TimeFrame.Day, "2021-01-01", "2022-01-01", adjustment='raw').df
class Pairs:
    def __init__(self, stock_pairs, timeframe=None): # Don't use mutable object in arguments.
        if timeframe == None:
            self.timeframe = []
        self.stock_pairs = stock_pairs
        self.timeframe = timeframe
        self.start = timeframe[0]
        self.end = timeframe[1]
        self.pair_dict = {} 
        for count, pair in enumerate(self.stock_pairs):
            self.pair_dict["pair" + str(count)] = api.get_bars(self.stock_pairs[pair], TimeFrame.Day, self.start, self.end, adjustment='raw').df

        ########### might need to use setattr() while in class. Ex:
        # for count, pair in enumerate(stock_pairs):
        #     setattr(self, "group"+str(i),api.get_bars(stock_pairs[pair], TimeFrame.Day, "2021-01-01", "2022-01-01", adjustment='raw').df)

        # self.stock_A_df = self.pairs_df.loc[self.pairs_df['symbol'] == stock_pairs[0][0]]                                    
        # self.stock_B_df = self.pairs_df.loc[self.pairs_df['symbol'] == stock_pairs[0][1]]
        ########### Need to generlize this for a full list of stock pairs.

        # self.stock_A_closing_prices = self.stock_A_df['close']
        # self.stock_B_closing_prices = self.stock_B_df['close']
        # self.returns_A = []
        # self.returns_B = []


    def returns(self):
        for period in range(1,self.stock_A_closing_prices.size):
            self.returns_A.append((self.stock_A_closing_prices[period-1] - self.stock_A_closing_prices[period])/self.stock_A_closing_prices[period-1])
        for period in range(1,self.stock_B_closing_prices.size):
            self.returns_B.append((self.stock_B_closing_prices[period-1] - self.stock_B_closing_prices[period])/self.stock_B_closing_prices[period-1])
        self.returns_A_series = pd.Series(self.returns_A, copy=False)
        self.returns_B_series = pd.Series(self.returns_B, copy=False)
    
    def corr(self):
        print(self.returns_A_series.corr(self.returns_B_series))

    def rank_pairs_corr(self):
        pass




        
# %%
pairs = Pairs(stock_pairs=stock_pairs, timeframe=["2020-01-01", "2021-01-01"])

pairs.returns()

pairs.corr()


#%%
# stationary = time series having constant mean and variance
# stationary relation is needed for pairs trading 
# check for co-intergration using Augmented Dickey-Fuller test
# regression residuals may be stationary


# This class will take in the data of the pairs that are determined by the Pairs class
class pair_algo:
    def __init__(self, data):
        self.data = data

    def backtest(self, data):
        pass

    def results(self, ):
        pass


#%%
# Exploritory next algorithm    
#     
# Standard deviation, Bollinger Bands, Money Flow, distance from a moving average, can all be used to locate extreme or unusual price moves. A good mean reversion indicator identifies extremes in prices that are likely to be temporary, not permanent.
# CAR / MDD is your Compound Annual Return divided by your Maximum Draw Down.
stock_universe = ("AAPL","GOOG","MSFT","AMZN","FB" )

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

