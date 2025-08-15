from flask import Flask, jsonify, request
from emails.email_handler import *
from browser.browser_handler import *
from steam.steam_handler import *


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

    def openBrowser(self, data):
        url = data.get('site')
        methods = {
            'youtube': self.browserHandler.youtube,
            'google': self.browserHandler.google,
            'github': self.browserHandler.github,
            'mangalivre': self.browserHandler.mangalivre,
            'chatgpt': self.browserHandler.chatgpt,
        }
        if url == 'email':
            emailType = data.get('emailType')
            if emailType not in ['formal', 'jogos']:
                return {"message": "O tipo de email deve ser 'formal' ou 'jogos'"}
            
            return {"url": self.browserHandler.email(emailType)}
    
        if url in methods:
            return {"url": f'{methods[url]()}'}
        
        return {'message': 'Não possuo esse site, favor cadastrar no banco de dados'}
    
    def search(self, site, query):
        return {'url': self.browserHandler.search(query, site)}


class SteamCommands:
    def __init__(self):
        self.steamHandler = SteamHandler()

    def runGame(self, data):
        name = data.get('name')
        return {'command': self.steamHandler.runGame(name)}
    

email_commands = EmailCommands()
browser_commands = BrowserCommands()
steam_commands = SteamCommands()


app = Flask(__name__)

@app.route('/emails/verify_emails')
def verifyEmails(): 
    return jsonify(email_commands.verifyEmails()), 200

@app.route('/emails/read_emails')
def readEmails():
    return jsonify(email_commands.readEmails()), 200

@app.route('/browser/open', methods=['POST'])
def openBrowser():
    data = request.get_json()

    chavesExtras = all(key in ['site', 'emailType'] for key in data.keys())
    chavesFaltando = all(key in data.keys() for key in ['site', 'emailType'])

    if 'site' not in data:
        return jsonify({'message': 'você não disse o site.'}), 400
    
    elif not chavesExtras and chavesFaltando:
        return jsonify({'message': ''})
        
    elif data['site'] == 'email' and any(key not in data for key in ['site', 'emailType']):
        return jsonify({'message': 'você não incluiu o tipo do email.'}), 400
        
    return jsonify(browser_commands.openBrowser(data)), 200

@app.route('/browser/search', methods=['POST'])
def search():
    data = request.get_json()
    query = data.get('query')
    site = data.get('site')

    if query == None:
        return jsonify({'message': 'você não incluiu a chave "query" na requisição'}), 400
    
    if site == None:
        return jsonify({'message': 'você não incluiu a chave "site" na requisição'}), 400
    
    if site.lower() not in ['google', 'youtube', 'github']:
        return jsonify({'message': 'o site deve ser "google", "youtube" ou "github"'}), 400
    
    return jsonify(browser_commands.search(site.lower(), query.lower())), 200

@app.route('/steam/run', methods=['POST'])
def runGame():
    data = request.get_json()
    if 'name' not in data:
        return jsonify({'message': 'você não incluiu o nome do jogo'}), 400
    
    return jsonify(steam_commands.runGame(data)), 200

if __name__ == "__main__":
    app.run()
