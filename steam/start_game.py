import requests
# from . import *
import json
from __init__ import *

class SteamAppList:
    def __init__(self):
        self.apps = self._openJsonFile()

    def _openJsonFile(self):
        with open('steam/appId.json', 'r') as file:
            return json.load(file)
        
    def _saveJsonFile(self):
        with open('steam/appId.json', 'w') as file:
            json.dump(self.apps, file, indent=4)
    
    def _normalizeGameNames(self, gameNames):
        if isinstance(gameNames, str):
            return [gameNames]
        elif isinstance(gameNames, list):
            return gameNames
        
        raise TypeError("gameNames deve ser uma string ou uma lista de strings.")


if __name__ == "__main__":
    steamApp = SteamAppList()