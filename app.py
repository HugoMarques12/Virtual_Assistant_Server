from flask import Flask, jsonify, request
from emails.email_handler import *
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

class SteamCommands:
    def __init__(self):
        self.steamHandler = SteamHandler()

    def runGame(self, data):
        name = data.get('name')
        return {'command': self.steamHandler.runGame(name)}

    def registerApp(self, appNames):
        return {'message': self.steamHandler.verifyGame()}

    def setGame(self, apps):
        self.steamHandler.setGame(apps)
        return {'message': 'Jogo adicionado com sucesso'}
    

email_commands = EmailCommands()
steam_commands = SteamCommands()


app = Flask(__name__)

@app.route('/emails/verify_emails')
def verifyEmails(): 
    return jsonify(email_commands.verifyEmails()), 200

@app.route('/emails/read_emails')
def readEmails():
    return jsonify(email_commands.readEmails()), 200

@app.route('/steam/run', methods=['POST'])
def runGame():
    data = request.get_json()
    if 'name' not in data:
        return jsonify({'message': 'você não incluiu o nome do jogo'}), 400
    
    return jsonify(steam_commands.runGame(data)), 200

if __name__ == "__main__":
    app.run()
