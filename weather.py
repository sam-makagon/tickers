# stock ticker for led message board

import time
from led import *

API_URL  = "http://api.openweathermap.org/data/2.5/weather?q=new%20york,ny"

def format_temp(temp):
  return int(temp - 235.67)

def get_data():
  response = requests.get(API_URL)
  response_data = response.json()
  data = response_data['main']['temp'], response_data['main']['temp_min'], \
    response_data['main']['temp_max'], response_data['wind']['speed']
  print(data)
  return data
  
def update_ticker():
  run_display_command(CLEAR_TEXT)
  data = get_data()

  print(data)
  run_display_command(DISPLAY_TEXT, "temp %s low %s high %s wind %s" % ( 
    format_temp(data[0]),
    format_temp(data[1]), 
    format_temp(data[2]), 
    data[3]
    )
  )

if __name__ == "__main__":
  update_ticker()
