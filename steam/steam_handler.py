from configparser import ConfigParser
import requests
from . import *

class SteamHandler:
    def __init__(self):
        self.apps = ConfigParser()
        self.apps.read('steam/appId.ini')
    
    def _normalizeGameNames(self, gameNames):
        if isinstance(gameNames, str):
            return {gameNames[0].lower(): True}
        
        elif isinstance(gameNames, list):
            games = {item.lower(): True for item in gameNames}
            return games
        
        raise TypeError('gameNames deve ser uma string ou uma lista de strings.')
    
    def _saveFile(self):
        with open('steam/appId.ini', 'w') as file:
            self.apps.write(file)
    
    def getAppIds(self, gameNames):
        gameNames = self._normalizeGameNames(gameNames)
        
        response = requests.get(f'{default_endpoint}{apps_endpoint}')
        response = response.json()

        for app in response['applist']['apps']:
            if app['name'].lower() in gameNames:
                gameNames[app['name'].lower()] = False
                self.apps.set('apps', app['name'].lower().replace(' ', '_'), str(app['appid']))

        self._saveFile()
        return self._verifyGames(gameNames)

    def _verifyGames(self, games):
        message = 'Jogos não encontrados '
        for value in games:
            if games[value]:
                message += f'{value}, '
        
        return message
    
    def runGame(self, name):
        id = self.apps.get('apps', name)
        return f'steam://run/{id}'
