import pandas as pd
from utils.parse_seismic import parse_dataframe


def seismic_events() -> pd.DataFrame:
  """Obtains seismic events data."""

  url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_day.csv'
  df = pd.read_csv(url)

  return parse_dataframe(df)