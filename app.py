from flask import Flask, jsonify, request
from emails.email_handler import *
from browser.browser_handler import *


class EmailCommands:
    def __init__(self):
        self.emailHandler = EmailHandler()
    
    def requires_login(func):
        def wrapper(self, *args, **kwargs):
            if self.emailHandler.loggedIn:
                return {"message": "Erro ao fazer login. Verifique suas credenciais."}
            return func(self, *args, **kwargs)
        return wrapper
    
    @requires_login
    def verifyEmails(self):
        return {"message": self.emailHandler.verifyNewEmails()}
    
    @requires_login
    def readEmails(self):
        return {"message": self.emailHandler.getEmails()}


class BrowserCommands:
    def __init__(self):
        self.browserHandler = BrowserHandler()

    def openBrowser(self, dados):
        url = dados.get('site')
        methods = {
            'youtube': self.browserHandler.youtube,
            'google': self.browserHandler.google,
            'github': self.browserHandler.github,
            'mangalivre': self.browserHandler.mangalivre,
            'chatgpt': self.browserHandler.chatgpt,
        }
        if url == 'email':
            emailType = dados.get('emailType')
            if emailType not in ['formal', 'jogos']:
                return {"message": "O tipo de email deve ser 'formal' ou 'jogos'"}
            
            return {"url": self.browserHandler.email(emailType)}
    
        if url in methods:
            return {"url": f'{methods[url]()}'}
        
        return {'message': 'Não possuo esse site, favor cadastrar no banco de dados'}

email_commands = EmailCommands()
browser_commands = BrowserCommands()


app = Flask(__name__)

@app.route('/emails/verify_emails')
def verifyEmails(): 
    return jsonify(email_commands.verifyEmails())

@app.route('/emails/read_emails')
def readEmails():
    return jsonify(email_commands.readEmails())

@app.route('/browser/open', methods=['POST'])
def openBrowser():
    dados = request.get_json()
    return jsonify(browser_commands.openBrowser(dados))

@app.route('/browser/search', methods=['POST'])
def search():
    dados = request.get_json()
    query = dados.get('query')
    site = dados.get('site')

    if query == None:
        return jsonify({'message': 'Você não incluiu a chave "query" na requisição'})
    
    if site == None:
        return jsonify({'message': 'Você não incluiu a chave "site" na requisição'})
    
    if site.lower() not in ['google', 'youtube', 'github']:
        return jsonify({'message': 'O site deve ser "google" ou "youtube"'})
    
    return jsonify({"url": browser_commands.search(query.lower(), site.lower())})


if __name__ == "__main__":
    app.run()
