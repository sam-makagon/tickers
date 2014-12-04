# stock ticker for led message board

import sys
import time
from led import *

API_URL  = "http://api.feedzilla.com/v1/categories/26/articles.json"

def get_data():
  response = requests.get(API_URL)
  response_data = response.json()
  data = []
  for article in response_data['articles']:
    title = article['title'].encode(sys.stdout.encoding, errors='replace')
    print(title)
    data.append(title)
  return data
  
def update_ticker():
  run_display_command(CLEAR_TEXT)
  data = get_data()

  for article in data:
    print(article)
    run_display_command(DISPLAY_TEXT, article)

if __name__ == "__main__":
  update_ticker()