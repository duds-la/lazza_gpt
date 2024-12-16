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
    st.header('🤖 Lazza ChatBot', divider=True)

pagina_principal()