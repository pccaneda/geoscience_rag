import streamlit as st
from chatbot.chatbot import call_groq_api
from config.core import config
from litellm import exceptions


st.header('Chat Geociências 🌎')

# Initializes chat history
if 'messages' not in st.session_state:
    st.session_state.messages = [config['llm']['system_prompt']]

# Flux control variable for retry button in case of errors
if "retry" not in st.session_state:
    st.session_state.retry = False

# Retry button callback
def retry() -> None:
    """Resends the last prompt."""
    st.session_state.retry = True

# Displays chat messages from history on app rerun
for message in st.session_state.messages:
    if message['role'] in ('user', 'assistant'):
        with st.chat_message(message['role']):
            st.markdown(message['content'])

# Gets user input
new_prompt = st.chat_input("Sua mensagem")
prompt = None

if st.session_state.retry:
    # By design the last message is always from user when this is executed
    prompt = st.session_state.messages[-1]['content']
    st.session_state.retry = False
else:
    prompt = new_prompt

# Prevents polluting with duplicate user messages in case of errors
if new_prompt:
    st.session_state.messages.append({
        'role': 'user',
        'content': new_prompt
    })

    with st.chat_message('user'):
        st.markdown(new_prompt)

# Always True except when no new_prompt has been entered and it is not a retry
if prompt:
    try:
        response = call_groq_api(st.session_state.messages)

        with st.chat_message('assistant'):
            st.markdown(response)

        st.session_state.messages.append({
            'role': 'assistant',
            'content': response
        })

    except exceptions.RateLimitError:
        st.warning('Limite atingido. Espere alguns segundos antes de continuar a conversa.')
        st.button('Reenviar', on_click=retry)
