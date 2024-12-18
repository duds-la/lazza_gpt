import os

import streamlit as st
import openai
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

openai_key = os.getenv('OPENAI_API_KEY')

def resposta_reposta_modelo(mensagens,
                            openai_key,
                            modelo='gpt-3.5-turbo',
                            temperatura=0,
                            stream=False):
    openai.api_key = openai_key
    response = openai.ChatCompletion.create(
        model=modelo,
        messages=mensagens,
        temperature=temperatura,
        stream=stream
    )
    return response

def pagina_principal():
    
    if not 'mensagens' in st.session_state:
        st.session_state.mensagens = []
    
    mensagens = st.session_state['mensagens']
    
    st.header('😡 BabacaGPT', divider=True)

    for mensagem in mensagens:
        chat = st.chat_message(mensagem['role'])
        chat.markdown(mensagem['content'])
    
    prompt = st.chat_input('Pergunte algo...')
    if prompt:
        nova_mensagem = {'role':'user',
                        'content': prompt}
        chat = st.chat_message(nova_mensagem['role'])
        chat.markdown(nova_mensagem['content'])
        mensagens.append(nova_mensagem)
        




        st.session_state['mensagens'] = mensagens


pagina_principal()