# 🤖 Virtual Assistant
Um assistente virtual simples e funcional, acessível via API, com integração a serviços como Steam, e-mail e navegador web.

## 🚀 Objetivo
Desenvolver uma API leve e eficiente que centralize funções cotidianas de um assistente virtual.

## 🧰 Tecnologias e Bibliotecas
- **Bibliotecas Externas**
  - **Flask:** Criação da API web.
  - **Imap-tools:** Gerenciamento e leitura de e-mails via IMAP.
  - **Requests:** Requisições HTTP para recursos externos.
- **Bibliotecas Nativas**
  - **Configparser:** Leitura de arquivos .ini para configurações.

## 🎯 Funcionalidades
- **🎮 Steam**
  - Armazena os IDs dos jogos configurados.
  - Abrir jogos steam.
- **📧 E-mail**
  - Verifica a caixa de entrada e retorna a quantidade de e-mails novos.
- **🌐 Navegador**
  - Abre sites pré-configurados: YouTube, Google, GitHub, MangaLivre, ChatGPT, E-mail.
  - Pesquisa tópicos automaticamente no Google ou YouTube.

---

## Instalação
### Criando ambiente virtual
Criar um ambiente virtual python como o nome desejável, substituindo "nome da pasta" pelo nome que você desejar.

```bash
python -m venv <nome da pasta>
```

### Ativar ambiente virtual
Após criar o ambiente virtual, ative ele utilizando o seguinte comando.

```bash
<nome da pasta>\Scripts\activate
```

### Instalando dependências
Agora você deve instalar os pacotes e bibliotecas.

```bash
pip install -r requirements.txt
```

---

## Endpoints API

### 📧 E-mails

#### `GET /emails/verify_emails`

**Descrição:** Ao receber uma requisiao HTTP, a API verifica se vc tem novos emails e retorna uma mensagem com a quantidade de emails novos e não lidos.

**Response (200):**
```json
{
  "message": "Você tem 10 email novos."
}
```

#### `GET /emails/read_emails`

**Descrição:** Cliente faz uma requisição para esse endpointe a API retorna os dados dos emails novos não lidos.

**Response (200):**
```json
{
  "from": "email@email.com",
  "subject": "API Assistente Virtual",
  "date": "yyyy-mm-dd hh:mm:ss-time-zone",
  "text": "Este é um exemplo de texto que pode vir na resposta"
}
```

### 🌐 Navegador

#### `POST /browser/open`

**Descrição:** Abrir site específico,o cliente deve enviar um json com a chave "site", caso o cliente faça uma requisição para o email, o json deverá conter as chaves "site" e "emailType", mostrarei abaixo.

**Body (JSON)**
```json
{
  "site": "email",
  "emailType": "formal"
}
```
ou
```json
{
  "site": "youtube"
}
```

**Response (200):**
```json
{
  "url": "https://www.youtube.com/"
}
```

#### `POST /browser/search`

**Descrição:** O cliente faz uma requisição HTTP para esse endpoint e a API retorna uma URL para o código cliente executar no navegador e abrir o site desejado com a pesquisa desejada.

**Body (JSON)**

Deve ter o seguinte formato:
```json
{
  "query": "Como criar uma API",
  "site": "youtube"
}
```

**Response (200):**
```json
{
  "url": "https://www.youtube.com/results?search_query=Como+criar+uma+API"
}
```