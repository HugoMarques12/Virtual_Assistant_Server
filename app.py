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

email_commands = EmailCommands()
browser_commands = BrowserHandler()


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
    url = dados.get('site')
    methods = {
        'youtube': browser_commands.youtube,
        'google': browser_commands.google,
        'github': browser_commands.github,
        'mangalivre': browser_commands.mangalivre
    }

    if url == 'email':
        email_name = dados.get('emailName')
        return jsonify({"message": browser_commands.email(email_name)})

    return jsonify({"message": f'{methods[url]() if url in methods else "Site não encontrado"}'})

@app.route('/browser/search', methods=['POST'])
def search():
    dados = request.get_json()
    query = dados.get('query')
    site = dados.get('site')
    return jsonify({"message": browser_commands.search(query, site)})

if __name__ == "__main__":
    app.run()
