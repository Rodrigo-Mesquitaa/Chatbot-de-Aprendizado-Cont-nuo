# Usa uma imagem base do Python
FROM python:3.9-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos para o contêiner
COPY ../.. .

# Instala o cliente Pinecone
RUN pip install pinecone-client

# Comando padrão
CMD ["python", "db_manager.py"]
