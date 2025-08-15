from configparser import ConfigParser

config = ConfigParser()
config.read('configs/credentials.ini')

emailAddress = config.get('email', 'address')
emailPassword = config.get('email', 'password')
