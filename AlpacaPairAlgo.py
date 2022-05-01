#%%
import alpaca_trade_api as tradeapi
from alpaca_trade_api.rest import TimeFrame
import pandas as pd
import statistics as st
import statsmodels.tsa.api as tsa
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

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
