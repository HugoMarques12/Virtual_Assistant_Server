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
    
    def getAppIds(self, gameNames):
        response = requests.get(f'{default_endpoint}{apps_endpoint}')
        response = response.json()

        for app in response['applist']['apps']:
            if app['name'].lower() in gameNames:
                self.apps.set('apps', app['name'].lower().replace(' ', '_'), str(app['appid']))

        self._saveFile()
    
    def runGame(self, name):
        id = self.apps.get('apps', name)
        return f'steam://run/{id}'
