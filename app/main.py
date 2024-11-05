import streamlit as st
from dotenv import load_dotenv
import os
from chat.chat_manager import ChatManager

# Carrega as variáveis de ambiente
load_dotenv()

# Inicializa o chatbot
chat_manager = ChatManager()

# Interface do chatbot
st.title("Chatbot de Aprendizado Contínuo")

# Campo de entrada do usuário
user_input = st.text_input("Digite sua pergunta:")

# Exibe a resposta do chatbot
if user_input:
    try:
        resposta = chat_manager.get_response(user_input)
        st.write("Chatbot:", resposta)
        
        # Feedback do usuário
        feedback = st.radio("Essa resposta está correta?", ("Sim", "Não"))
        if feedback == "Sim":
            chat_manager.save_interaction(user_input, resposta)
            st.success("Interação salva com sucesso.")
        else:
            st.warning("A resposta não foi salva.")
    except Exception as e:
        st.error(f"Erro ao processar a resposta: {e}")
