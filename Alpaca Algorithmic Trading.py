#%%
# Alpaca Algorithmic Trading
import alpaca_trade_api as tradeapi
from alpaca_trade_api.rest import TimeFrame
import numpy as np
import statistics
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

stock_pairs = [["AAPL","GOOG"]]

pairs_df = api.get_bars(stock_pairs[0], TimeFrame.Day, "2021-01-01", "2022-01-01", adjustment='raw').df
stock_A_df = pairs_df.loc[pairs_df['symbol'] == stock_pairs[0][0]]
stock_B_df = pairs_df.loc[pairs_df['symbol'] == stock_pairs[0][1]]
stock_A_closing_prices = stock_A_df['close']
stock_B_closing_prices = stock_B_df['close']


class pairs:
    def __init__(self, stock_pairs, stock_A_closing_prices, stock_B_closing_prices):
        self.stock_pairs = stock_pairs
        self.stock_A_closing_prices = stock_A_closing_prices
        self.stock_B_closing_prices = stock_B_closing_prices
        

    def returns(self):
        returns_A = []
        returns_B = []
        for period in range(1,stock_A_closing_prices.len()):
            returns_A.append((stock_A_closing_prices[period-1] - stock_A_closing_prices[period])/stock_A_closing_prices[period-1])
        for period in range(1,stock_B_closing_prices.len()):
            returns_B.append((stock_B_closing_prices[period-1] - stock_B_closing_prices[period])/stock_B_closing_prices[period-1])

    def corr(self, returns_B, returns_A):
        statistics.correlation(returns_A, returns_B)

        


# stationary = time series having constant mean and variance
# stationary relation is needed for pairs trading 
# check for co-intergration using Augmented Dickey-Fuller test
# regression residuals may be stationary






#%%
class pair_algo:
    def __init__(self, data):
        self.data = api.get_bars()

    def backtest(self, data):
        pass

    def results(self, ):
        pass
        
