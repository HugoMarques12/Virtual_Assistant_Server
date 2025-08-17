from configparser import ConfigParser

config = ConfigParser()
config.read('endpoints.ini')

default_endpoint = config.get('steam', 'default_endpoint')
apps_endpoint = config.get('steam', 'apps_endpoint')
