from flask import Blueprint, jsonify
from emails.email_handler import *


emailsBp = Blueprint('emails', __name__, url_prefix='/emails')

class EmailCommands:
    def __init__(self):
        self.emailHandler = EmailHandler()
    
    def requires_login(func):
        def wrapper(self, *args, **kwargs):
            if self.emailHandler.loggedIn:
                return {"message": "Erro ao fazer login. Verifique suas credenciais."}
            return func(self, *args, **kwargs)
        return wrapper
    
    @requires_login
    def verifyEmails(self):
        return {"message": self.emailHandler.verifyNewEmails()}
    
    @requires_login
    def readEmails(self):
        return {"message": self.emailHandler.getEmails()}
    

email_commands = EmailCommands()

@emailsBp.route('/verify_emails')
def verifyEmails(): 
    return jsonify(email_commands.verifyEmails()), 200

@emailsBp.route('/read_emails')
def readEmails():
    return jsonify(email_commands.readEmails()), 200
