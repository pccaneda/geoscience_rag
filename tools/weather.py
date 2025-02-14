import requests
from utils.parse_weather import parse_weather
from config.core import config
import streamlit as st


def weather_forecast(city: str, country: str) -> str:
  """GET weather forecast information.

  Parameters
  ----------
  city : str
    City name.

  country : str
    Two letter country code, e.g. BR for Brazil, UK for the United Kingdom.

  Returns
  -------
  data : str
    Weather data.
  """

  # Call to OpenWeatherMap API
  url = f'http://api.openweathermap.org/data/2.5/weather?q={city},{country}&APPID={st.secrets["WEATHER_API_KEY"]}&lang=pt_br&units=metric'
  response = requests.get(url)

  # Returns processed json response
  if response.status_code == 200:
    return parse_weather(response.json())
  else:
    return f'Erro ao obter a previsão do tempo.'