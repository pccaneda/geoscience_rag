import json


def parse_weather(data: dict) -> str:
  """Parses weather forecast json.

  Parameters
  ----------
  data : dict
    Raw weather data in JSON format.

  Returns
  -------
  weather : str
    Parsed JSON weather data as string.
  """

  # Parses weather description
  weather = []
  for i in range(len(data['weather'])):
    weather.append(data['weather'][i]['description'])
  weather_str = ', '.join(weather)

  # Selects common weather data
  data = {
      'Clima': weather_str,
      'Temperatura': data['main']['temp'],
      'Temperatura minima': data['main']['temp_min'],
      'Temperatura maxima': data['main']['temp_max'],
      'Humidade': data['main']['humidity'],
      'Velocidade do vento': data['wind']['speed'],
      'Direcao do vento': data['wind']['deg'],
      'Visibilidade': data['visibility'],
      'Cobertura das nuvens': data['clouds']['all']
  }

  return json.dumps(data)