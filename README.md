# 🧠 Cyber Mind — Chatbot inteligente

Chatbot desenvolvido com Python, utilizando [Streamlit](https://streamlit.io/) para a interface web e a API da [OpenAI](https://platform.openai.com/) para geração de respostas com inteligência artificial, mantendo o histórico da conversa de forma contínua.

## 🛠️ Tecnologias utilizadas

- Python
- Streamlit
- OpenAI Python SDK
- python-dotenv

## 📦 Instalação

1. Clone o repositório:

```bash
git clone https://github.com/JosielJrr/cyber-mind.git
cd cyber-mind
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Configure o `.env`:

Use o comando abaixo para criar um arquivo `.env` com base no modelo:

```bash
cp .env.example .env
```

Em seguida, abra o arquivo `.env` e insira a sua chave de API da OpenAI.

## ▶️ Como executar

Inicie a aplicação com o comando:

```bash
streamlit run main.py
```

## 📌 Observação

Para que a aplicação funcione corretamente, é necessário possuir uma **chave de API válida** da OpenAI. O arquivo `.env.example` fornece orientações para obtê-la e adicioná-la ao projeto.

> Projeto criado na **Jornada Python** da [Hashtag Programação](https://www.youtube.com/@HashtagProgramacao).
