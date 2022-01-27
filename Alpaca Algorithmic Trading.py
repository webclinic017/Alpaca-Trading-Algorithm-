#%%
# Alpaca Algorithmic Trading
import alpaca_trade_api as tradeapi


#LIVE KEYS
APCA_API_BASE_URL = 'https://api.alpaca.markets'
APCA_API_KEY_ID = 'AKHJJTAOR8BIPM8NGBVS'
APCA_API_SECRET_KEY = '7ECpCBy7MkAPLaxlqvlZQv7vj8i1zdPJ7ONemUM9'

# PAPER KEYS
APCA_API_BASE_URL_paper = 'https://paper-api.alpaca.markets'
APCA_API_KEY_ID_paper = 'PK2887AEKCPBT1FSOMCC'
APCA_API_SECRET_KEY_paper = 'qYoY7sc0LHAVy9bVcyk4nQuKiQtsfokIhDtAvyKP'

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

#%%

# Submit a market order to buy 1 share of Apple at market price
api.submit_order(
    symbol='AAPL',
    qty=1,
    side='buy',
    type='market',
    time_in_force='gtc'
)

# Submit a limit order to attempt to sell 1 share of AMD at a
# particular price ($20.50) when the market opens
api.submit_order(
    symbol='AMD',
    qty=1,
    side='sell',
    type='limit',
    time_in_force='opg',
    limit_price=20.50
)