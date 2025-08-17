from flask import Blueprint, jsonify, request
from modules.browser.browser_handler import *


browserBp = Blueprint('browser', __name__, url_prefix='/browser')

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
                return {"message": "o tipo de email deve ser 'formal' ou 'jogos'"}
            
            return {"url": self.browserHandler.email(emailType)}
    
        if url in methods:
            return {"url": f'{methods[url]()}'}
        
        return {'message': 'não possuo esse site, favor cadastrar no banco de dados'}
    
    def search(self, site, query):
        return {'url': self.browserHandler.search(query, site)}
    

browser_commands = BrowserCommands()


@browserBp.route('/open', methods=['POST'])
def openBrowser():
    data = request.get_json()

    extraKeys = any(key not in ['site', 'emailType'] for key in data.keys())

    if 'site' not in data:
        return jsonify({'message': 'você não disse o site.'}), 400
    
    elif data['site'] != 'email' and extraKeys:
        return jsonify({'message': 'você incluiu mais dados do que deveria, deve conter apenas a chave site'}), 400
    
    elif data['site'] == 'email' and extraKeys:
        return jsonify({'message': 'você incluiu mais dados do que deveria, deve conter apenas a chave email e site'}), 400
        
    elif data['site'] == 'email' and all(key in data for key in ['site', 'emailType']):
        return jsonify({'message': 'você não incluiu o tipo do email.'}), 400
        
    return jsonify(browser_commands.openBrowser(data)), 200

@browserBp.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    query = data.get('query')
    site = data.get('site')

    if query == None:
        return jsonify({'message': 'você não incluiu a chave "query" na requisição'}), 400
    
    elif site == None:
        return jsonify({'message': 'você não incluiu a chave "site" na requisição'}), 400
    
    elif site.lower() not in ['google', 'youtube', 'github']:
        return jsonify({'message': 'o site deve ser "google", "youtube" ou "github"'}), 400
    
    elif any(key not in ['site', 'query'] for key in data.keys()):
        return jsonify({'message': 'você incluiu mais dados do que deveria, deve conter apenas as chaves site e query'}), 400
    
    return jsonify(browser_commands.search(site.lower(), query.lower())), 200
