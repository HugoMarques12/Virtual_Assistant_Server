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


if __name__ == "__main__":
    steamApp = SteamAppList()