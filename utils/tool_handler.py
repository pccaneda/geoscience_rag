from tools.weather import weather_forecast
from tools.seismic import seismic_events
from tools.solar import solar_storm_check
from tools.geology import geology_info


available_functions = {
  'weather_forecast': weather_forecast,
  'solar_storm_check': solar_storm_check,
  'seismic_events': seismic_events,
  'geology_info': geology_info
}

def tool_handler(function_name: str, function_args: dict) -> str:
  """Handles tool calls from the LLM.
  
  Parameters
  ----------
  function_name: str
    The name of the function to be called.

  function_args: dict
    Arguments taken by the function.

  Returns
  -------
  function_response: str
    Function response as text string.
  """
  
  function_to_call = available_functions[function_name]

  # Gets response from any external API
  match function_name:
    case 'weather_forecast':
      function_response = function_to_call(
        city=function_args.get('city'),
        country=function_args.get('country')
      )

    case 'solar_storm_check':
      function_response = function_to_call()

    case 'seismic_events':
      function_response = function_to_call()

    case 'geology_info':
      function_response = function_to_call(
        query=function_args.get('query')
      )

  return function_response