from configparser import ConfigParser
import requests
from . import *

class SteamHandler:
    def __init__(self):
        self.apps = ConfigParser()
        self.apps.read('steam/appId.ini')
    
    def _saveFile(self):
        with open('steam/appId.ini', 'w') as file:
            self.apps.write(file)
    
    def addGame(self, names):
        foundGames = set()
        response = requests.get(f'{default_endpoint}{apps_endpoint}')
        response = response.json()

        for app in response['applist']['apps']:
            appName = app['name'].lower()

            if appName in names:
                self.apps.set('apps', appName.replace(' ', '_'), str(app['appid']))
                foundGames.add(appName)

        self._saveFile()
        return foundGames

    def verifyGame(self, gameNames):
        missingGames = set(name.lower() for name in gameNames)
        foundGames = self.addGame(gameNames)

        missingGames -= foundGames
        if missingGames:
            return list(missingGames)
        
        return {'message': 'jogos adicionados com sucesso'}
    
    def runGame(self, name):
        name = name.replace(' ', '_')
        id = self.apps.get('apps', name)
        return f'steam://run/{id}'

