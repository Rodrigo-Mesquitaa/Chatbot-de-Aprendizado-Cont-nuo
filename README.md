# Chatbot-de-Aprendizado-Continuo
Este projeto implementa um chatbot interativo que aprende continuamente com as interações do usuário, utilizando LangChain, LangGraph e um banco de dados vetorial (Pinecone) para armazenar respostas confirmadas como corretas pelo usuário.

# Chatbot de Aprendizado Contínuo
Este projeto implementa um chatbot interativo que aprende continuamente com as interações do usuário, 
utilizando LangChain, LangGraph e um banco de dados vetorial (Pinecone) para armazenar respostas confirmadas
como corretas pelo usuário. O projeto usa Streamlit para a interface visual e Docker para orquestração dos contêineres.

# Estrutura do Projeto

## chatbot_projeto/
- ├── .env                    # Arquivo para variáveis de ambiente
- ├── Dockerfile              # Dockerfile para a aplicação principal
- ├── docker-compose.yml      # Arquivo de orquestração Docker
- ├── app/                    # Código principal da aplicação
- │   ├── main.py             # Interface do chatbot com Streamlit
- │   ├── chat/               # Módulos de chat e aprendizado
- │   │   ├── chat_manager.py # Lógica principal do chatbot
- │   │   ├── learning.py     # Funções de aprendizado e feedback
- │   └── db/                 # Código para o banco de dados vetorial
- │       ├── db_manager.py   # Gerenciamento do banco de dados vetorial
- │       └── docker/         # Configurações Docker para a base de dados vetorial
- │           ├── Dockerfile  # Dockerfile específico para o banco de dados vetorial
- │           └── init.sql    # Script SQL para inicialização do banco, se necessário
- └── requirements.txt        # Arquivo de dependências


## Pré-requisitos

. Docker e Docker Compose: Para orquestração dos contêineres.
. Python 3.9+: Para desenvolvimento e execução local.
. Conta Pinecone: Para configurar o banco de dados vetorial (gratuito para pequenos volumes de dados).
. Chave de API LLM: Pode-se utilizar uma chave da API Groq (recomendado por ser gratuito).

# Passos de Configuração

- 1. Configurar Variáveis de Ambiente
Crie um arquivo .env na raiz do projeto para armazenar as chaves de API e outras configurações. 
Este arquivo é necessário para a conexão com o banco de dados Pinecone e o modelo de linguagem.

### Exemplo
"*LLM_API_KEY="sua_chave_api_aqui"           # Substitua por sua chave de API para o modelo de linguagem
PINECONE_API_KEY="sua_chave_pinecone"       # Substitua por sua chave de API do Pinecone
PINECONE_ENVIRONMENT="us-west1-gcp"         # Ajuste conforme a região do Pinecone*"


## Executando o Projeto

Iniciar os Contêineres: No diretório raiz do projeto, execute:

- bash
Copiar código
- docker-compose up --build
Acessar a Interface: Após a inicialização, acesse o chatbot em http://localhost:8501 no navegador.

Testar a Função de Aprendizado: Pergunte ao chatbot e forneça feedback. As respostas confirmadas serão salvas no banco de dados Pinecone.


## Notas de Desenvolvimento

. Gerenciamento de Erros: Todas as interações com o LLM e Pinecone têm tratamento de erros para garantir que o chatbot 
  lide bem com exceções e falhas de conexão.
. Conexão com Pinecone: Certifique-se de que a chave API e o ambiente estão corretamente configurados no .env.
. Personalização: Você pode ajustar o chat_manager.py para usar diferentes modelos LLM ou configurações.


## Possíveis Melhorias

- Cache de Respostas: Armazenar respostas frequentes em cache para melhorar a velocidade de resposta.
- Feedback Avançado: Implementar feedback negativo para o chatbot reavaliar respostas.
- Armazenamento Local Opcional: Adicionar uma opção para armazenamento local, caso o Pinecone não esteja disponível.