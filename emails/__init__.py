from configparser import ConfigParser

config = ConfigParser()
config.read('credentials.ini')

emailAddress = config.get('email', 'address')
emailPassword = config.get('email', 'password')
