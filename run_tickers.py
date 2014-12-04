import time

import stocks
import weather

SLEEP_DELAY = 3 * 60

while(True):
  stocks.update_ticker()
  time.sleep(SLEEP_DELAY)
  weather.update_ticker()
  time.sleep(SLEEP_DELAY)
  news.update_ticker()
  time.sleep(SLEEP_DELAY)