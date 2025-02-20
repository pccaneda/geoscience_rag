from litellm import completion
import json
from utils.tool_handler import tool_handler
from config.core import config, tools
import streamlit as st


def call_groq_api(messages: list[dict[str, str]]) -> str:
  """Calls GROQ API for a LLM.

  Parameters
  ----------
  messages : list[dict[str,str]]
    List of messages passed with role and content.

  Returns
  -------
  response : str
    First response text generated by LLM.
  """

  response = completion(
    messages=messages,
    api_key=st.secrets["GROQ_API_KEY"],
    **config['llm']['parameters'],
    **tools
  )

  text_response = response.choices[0].message
  tool_calls = text_response.tool_calls

  # Checks if external APIs have been called
  if tool_calls:
    for tool_call in tool_calls:
      function_name = tool_call.function.name
      function_args = json.loads(tool_call.function.arguments)
      
      print(f'Function Args: {function_args}')
      print('')

      function_response = tool_handler(function_name, function_args)

      # Appends external APIs' responses to messages
      messages.append({
          'tool_call_id': tool_call.id,
          'role': 'tool',
          'name': function_name,
          'content': function_response
      })

    # Generates new and informed response
    # Tools are not called here to prevent the LLM talking to itself
    informed_response = completion(
        messages=messages,
        api_key=st.secrets["GROQ_API_KEY"],
        **config['llm']['parameters']
    )

    return informed_response.choices[0].message.content

  else:
    return text_response.content
