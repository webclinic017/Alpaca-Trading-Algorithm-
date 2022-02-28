#%%
# Alpaca Algorithmic Trading
import alpaca_trade_api as tradeapi
from alpaca_trade_api.rest import TimeFrame
import pandas as pd
import statsmodels.tsa.api as tsa

#LIVE KEYS


# PAPER KEYS
APCA_API_BASE_URL_paper = 'https://paper-api.alpaca.markets'
APCA_API_KEY_ID_paper = 'PK2887AEKCPBT1FSOMCC'
APCA_API_SECRET_KEY_paper = 'qYoY7sc0LHAVy9bVcyk4nQuKiQtsfokIhDtAvyKP'

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

stock_pairs = [["AAPL","GOOG"], []]
pair_dict = {} 
for count, pair in enumerate(stock_pairs):
    pair_dict["pair" + str(count)] = api.get_bars(stock_pairs[pair], TimeFrame.Day, "2021-01-01", "2022-01-01", adjustment='raw').df

stock_A_df = pairs_df.loc[pairs_df['symbol'] == stock_pairs[0][0]]
stock_B_df = pairs_df.loc[pairs_df['symbol'] == stock_pairs[0][1]]
stock_A_closing_prices = stock_A_df['close']
stock_B_closing_prices = stock_B_df['close']

#%%

pairs_df = api.get_bars(stock_pairs[pair], TimeFrame.Day, "2021-01-01", "2022-01-01", adjustment='raw').df
class Pairs:
    def __init__(self, stock_pairs, timeframe=[]): # Don't use mutable object in arguments.
        self.stock_pairs = stock_pairs
        self.timeframe = timeframe
        self.start = timeframe[0]
        self.end = timeframe[1]
        self.pairs_df = api.get_bars(stock_pairs[0], TimeFrame.Day, self.start, self.end, adjustment='raw').df
        # might need to use setattr() while in class
        # for count, pair in enumerate(stock_pairs):
        #     setattr(self, "group"+str(i),api.get_bars(stock_pairs[pair], TimeFrame.Day, "2021-01-01", "2022-01-01", adjustment='raw').df)
        self.stock_A_df = self.pairs_df.loc[self.pairs_df['symbol'] == stock_pairs[0][0]]                                    
         # Need to generlize this for a full list of stock pairs.
        self.stock_B_df = self.pairs_df.loc[self.pairs_df['symbol'] == stock_pairs[0][1]]
        self.stock_A_closing_prices = self.stock_A_df['close']
        self.stock_B_closing_prices = self.stock_B_df['close']
        self.returns_A = []
        self.returns_B = []


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


class pair_algo:
    def __init__(self, data):
        self.data = data

    def backtest(self, data):
        pass

    def results(self, ):
        pass
        
