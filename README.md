# Chat FURIA

Chat FURIA é um assistente conversacional para o time de CS:GO da FURIA Esports. Ele fornece informações para os fãs sobre o time, incluindo a escalação atual, conquistas recentes e próximos jogos ou torneios.

## Funcionalidades

- Chatbot interativo desenvolvido com Django e React.
- Busca dados em tempo real sobre a FURIA Esports utilizando a API PandaScore.
- Oferece uma interface amigável para os fãs interagirem com o assistente.

---

## Pré-requisitos

Antes de executar o projeto, certifique-se de ter os seguintes itens instalados:

- `Python 3.12` ou superior
- `uv` gerenciador de pacotes python (powershell -c "irm https://astral.sh/uv/install.ps1 | iex")
- `Node.js` e `npm`
- Uma ferramenta de ambiente virtual (ex.: `venv` ou `virtualenv`)
- Variáveis de ambiente para as chaves de API:
  - `DJANGO_KEY` (chave secreta do Django)
  - `PANDA_API` (chave da API PandaScore)
  - `GEMINI_API` (chave da API Google Generative AI)

---

## Instruções de Configuração

### 1. Clonar o Repositório

```bash
git clone https://github.com/Gustavo0121/chat-furia.git
cd chat-furia
```

### 2. Configuração do Backend (Django)
**Criar um Ambiente Virtual:**
```bash
uv venv
```

**Ativar o Ambiente Virtual:**
```bash
.venv/Scripts/activate
```

**Instalar Dependências:**
```bash
uv sync
```

**Configurar Variáveis de Ambiente:**
***Crie um arquivo .env no diretório raiz e adicione o seguinte conteúdo:***
```bash
DJANGO_KEY=your_django_secret_key
PANDA_API=your_pandascore_api_key
GEMINI_API=your_gemini_api_key
```

**Navegar até o Diretório do servidor:**
```bash
cd chatbot/
```

**Executar Migrações:**
```bash
python manage.py migrate
```

**Iniciar o Servidor Backend:**
```bash
python manage.py runserver
```

**O backend estará disponível em http://localhost:8000**

### 3. Configuração do Frontend (React)
**Navegar até o Diretório do Frontend:**
```bash
cd chatbot/frontend
```

**Instalar Dependências:**
```bash
npm install
```

**Iniciar o Servidor de Desenvolvimento do Frontend:**

***O frontend estará disponível em http://localhost:3000***

### 4. Acessar a Aplicação
#### Com os servidores backend e frontend em execução:

- Abra o navegador e acesse http://localhost:3000
- Interaja com o chatbot para obter informações sobre a FURIA Esports.

### Licença
Este é um projeto de fãs para a FURIA Esports e não é oficialmente afiliado à organização.
