# 🤖 Virtual Assistant
Um assistente virtual simples e funcional, acessível via API, com integração a serviços como Steam, e-mail e navegador web.

## 🚀 Objetivo
Desenvolver uma API leve e eficiente que centralize funções cotidianas de um assistente virtual.

## 🧰 Tecnologias e Bibliotecas
- Bibliotecas Externas
  - Flask: Criação da API web.
  - Imap-tools: Gerenciamento e leitura de e-mails via IMAP.
  - Requests: Requisições HTTP para recursos externos.
- Bibliotecas Nativas
  - Configparser: Leitura de arquivos .ini para configurações.

## 🎯 Funcionalidades
- 🎮 Steam
  - Armazena os IDs dos jogos configurados
  - Abrir jogos
- 📧 E-mail
  - Verifica a caixa de entrada e retorna a quantidade de e-mails novos
- 🌐 Navegador
  - Abre sites pré-configurados: YouTube, Google, GitHub, MangaLivre, ChatGPT, E-mail
  - Pesquisa tópicos automaticamente no Google ou YouTube

## Instalação
### Criando ambiente virtual
Criar um ambiente virtual python como o nome desejável, substituindo "nome da pasta" pelo nome que você desejar
```
python -m venv <nome da pasta>
```

### Ativar ambiente virtual
Após criar o ambiente virtual, ative ele utilizando o seguinte comando
```
<nome da pasta>\Scripts\activate
```

### Instalando dependências
Agora você deve instalar os pacotes e bibliotecas
```
pip install -r requirements.txt
```