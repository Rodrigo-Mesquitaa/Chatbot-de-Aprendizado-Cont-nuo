import pinecone
import os

# Inicializa o cliente Pinecone
api_key = os.getenv("PINECONE_API_KEY")
environment = os.getenv("PINECONE_ENVIRONMENT")
if not api_key or not environment:
    raise ValueError("PINECONE_API_KEY ou PINECONE_ENVIRONMENT não encontrado.")

pinecone.init(api_key=api_key, environment=environment)

index_name = "chatbot_interactions"
if index_name not in pinecone.list_indexes():
    pinecone.create_index(index_name)

index = pinecone.Index(index_name)

def save_to_db(data):
    try:
        index.upsert(vectors=[{
            "id": data["input"],
            "values": data["response"],
            "metadata": data
        }])
    except Exception as e:
        print(f"Erro ao salvar no Pinecone: {e}")
