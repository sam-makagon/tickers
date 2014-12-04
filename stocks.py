# stock ticker for led message board

import time
import requests

from led import *

SLEEP_MINS = 3
STOCK_API_URL = "http://dev.markitondemand.com/Api/v2/Quote/json"
BITCOIN_API_URL = "https://api.bitcoinaverage.com/ticker/global/USD/"

STOCKS = ['AAPL', 'TMUS', 'TSLA']

def get_bitcoin_price():
  key = 'last'
  response = requests.get(BITCOIN_API_URL, verify=False)
  data = response.json()
  print("bitcoin price: %s" % (data[key]))
  return data[key]

def get_stock_price(stock):
  key = 'LastPrice'
  data = {'symbol': stock}
  response = requests.get(STOCK_API_URL, params=data)
  data = response.json()
  print("%s price: %s" % (stock, data[key]))
  return data[key]
  
def update_ticker():
  run_display_command(CLEAR_TEXT)
  for stock in STOCKS:
    price = get_stock_price(stock)
    run_display_command(DISPLAY_TEXT, "%s %s" % (stock, price))
  run_display_command(DISPLAY_TEXT, "BTC %s" % get_bitcoin_price())

if __name__ == "__main__":
  update_ticker()
