import streamlit as st  # Biblioteca para criação de aplicações web interativas com Python
from openai import OpenAI, RateLimitError  # Cliente da API da OpenAI e exceção para controle de limite de uso
from dotenv import load_dotenv  # Biblioteca para carregar variáveis de ambiente de um arquivo .env
import os  # Módulo padrão para acessar variáveis de ambiente do sistema

# Carrega as variáveis definidas no arquivo .env
load_dotenv()

# Recupera a chave da API da OpenAI armazenada no arquivo .env
api_key = os.getenv("OPENAI_API_KEY")

# Cria uma instância do cliente da OpenAI com a chave de autenticação
modelo = OpenAI(api_key=api_key)

# Exibe o título da aplicação na interface do Streamlit
st.write("### 🧠 Cyber Mind")

# Inicializa a lista de mensagens no estado da sessão, se ainda não estiver criada
if "lista_mensagens" not in st.session_state:
    st.session_state["lista_mensagens"] = []

# Exibe o histórico de mensagens já trocadas (tanto do usuário quanto do assistente)
for mensagem in st.session_state["lista_mensagens"]:
    role = mensagem["role"]      # Identifica o remetente da mensagem ("user" ou "assistant")
    content = mensagem["content"]  # Conteúdo textual da mensagem
    st.chat_message(role).write(content)  # Renderiza a mensagem no chat

# Campo de entrada para o usuário enviar uma nova pergunta
prompt = st.chat_input("Pergunte alguma coisa")

if prompt:
    # Exibe a mensagem enviada pelo usuário no chat
    st.chat_message("user").write(prompt)

    # Armazena a mensagem do usuário no histórico da conversa
    mensagem_user = {"role": "user", "content": prompt}
    st.session_state["lista_mensagens"].append(mensagem_user)

    try:
        # Envia o histórico completo para o modelo da OpenAI e obtém uma nova resposta
        resposta_modelo = modelo.chat.completions.create(
            messages=st.session_state["lista_mensagens"],
            model="gpt-3.5-turbo"
        )

        # Extrai apenas o conteúdo da resposta gerada
        resposta_ia = resposta_modelo.choices[0].message.content

        # Exibe a resposta da IA no chat
        st.chat_message("assistant").write(resposta_ia)

        # Armazena a resposta da IA no histórico
        mensagem_ia = {"role": "assistant", "content": resposta_ia}
        st.session_state["lista_mensagens"].append(mensagem_ia)

    # Trata o erro de limite de uso da conta OpenAI
    except RateLimitError:
        st.error("⚠️ Seu limite de uso foi atingido. Verifique o plano e saldo na sua conta OpenAI para continuar utilizando o serviço.")
