# Usa uma imagem base do Python
FROM python:3.9-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos para o contêiner
COPY . /app

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta do Streamlit
EXPOSE 8501

# Comando para iniciar o Streamlit
CMD ["streamlit", "run", "app/main.py"]
