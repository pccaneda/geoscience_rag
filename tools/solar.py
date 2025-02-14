import requests


def solar_storm_check() -> str:
  """Obtains data about solar storm."""

  url = 'https://services.swpc.noaa.gov/products/noaa-planetary-k-index.json'
  response = requests.get(url)

  if response.status_code == 200:
    data = response.json()
    latest_kp = float(data[-1][1])

    if latest_kp >= 5:
      return f'Alerta de tempestade solar! Íncide Kp atual: {latest_kp}'
    else:
      return f'Sem alertas de tempestade solar. Índice Kp atual: {latest_kp}'

  else:
    return 'Erro ao buscar dados do NOAA'