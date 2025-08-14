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

**`GET /emails/verify_emails`**
**Descrição:** Verificar se vc tem novos emails.

Response (200):
```json
{
  "message": "Você tem 10 email novos."
}
```

**`GET /emails/read_emails`**
**Descrição:** Ler os emails novos não lidos.

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

**`POST /browser/open`**
**Descrição:** Abrir site específico.
**Body (JSON)**
Se o usuario desejar abrir o tipo email, deve ser nesse formato:
```json
{
  "site": "email",
  "emailType": "formal"
}
```
como "emailType" sendo "formal" ou "jogos".

Caso contrário deve manter esse formato:
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

**`POST /browser/search`**
**Descrição:** Pesquisar assunto em determinado site
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