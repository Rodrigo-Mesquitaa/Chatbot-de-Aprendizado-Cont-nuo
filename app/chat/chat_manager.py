from langchain.llms import LLMChain
from .learning import save_to_db
import os

class ChatManager:
    def __init__(self):
        api_key = os.getenv("LLM_API_KEY")
        if not api_key:
            raise ValueError("LLM_API_KEY não encontrada. Verifique o arquivo .env")
        self.llm = LLMChain(api_key=api_key)

    def get_response(self, user_input):
        try:
            # Gera resposta do modelo de linguagem
            return self.llm(user_input)
        except Exception as e:
            return f"Erro ao gerar resposta: {e}"

    def save_interaction(self, user_input, response):
        try:
            # Salva a interação se o feedback for positivo
            data = {"input": user_input, "response": response}
            save_to_db(data)
        except Exception as e:
            print(f"Erro ao salvar interação: {e}")
