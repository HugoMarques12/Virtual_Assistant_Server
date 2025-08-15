from flask import Flask, jsonify, request
from steam.steam_handler import *

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
    

steam_commands = SteamCommands()


app = Flask(__name__)


@app.route('/steam/run', methods=['POST'])
def runGame():
    data = request.get_json()
    if 'name' not in data:
        return jsonify({'message': 'você não incluiu o nome do jogo'}), 400
    
    return jsonify(steam_commands.runGame(data)), 200

if __name__ == "__main__":
    app.run()
