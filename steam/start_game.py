from configparser import ConfigParser
from __init__ import *
import requests
# from . import *

class SteamAppList:
    def __init__(self):
        self.apps = ConfigParser()
        self.apps.read('appId.ini')
    
    def _normalizeGameNames(self, gameNames):
        if isinstance(gameNames, str):
            return [gameNames]
        elif isinstance(gameNames, list):
            return gameNames
        
        raise TypeError("gameNames deve ser uma string ou uma lista de strings.")
    
    def getAppIds(self, gameNames):
        gameNames = self._normalizeGameNames(gameNames)
        
        response = requests.get(f'{default_endpoint}{apps_endpoint}')
        response = response.json()

        for app in response['applist']['apps']:
            if app['name'] in gameNames:
                self.apps.append({"appId": app['appId'], "appName": app['name'].lower()})


if __name__ == "__main__":
    steamApp = SteamAppList()