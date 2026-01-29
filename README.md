# Python chatbot

Aplicação simples de chatbot em terminal utilizando **Python** e **Google Gemini**.  
O projeto mantém o histórico das mensagens, permitindo preservar o contexto da conversa durante sua execução.

## Como rodar

Para executar o projeto, é necessário ter o **Python** instalado em sua máquina e uma **API Key do Google Gemini**, que pode ser obtida em:

https://ai.google.dev/gemini-api/docs/api-key

### 1 - Clone o projeto

```bash
git clone https://github.com/gabrielferreira02/python-chatbot
cd python-chatbot
```

### 2 - Instale as dependências
```
pip install -r requirements.txt
```

### 3 - crie um arquivo .env na raiz do projeto e adicione:
```env
GEMINI_KEY=sua_api_key
```

### 4 - Inicialize o projeto
```bash
python3 main.py
# ou
python main.py
```
