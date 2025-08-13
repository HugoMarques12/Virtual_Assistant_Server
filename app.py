from flask import Flask, jsonify
from emails.email_handler import *

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

app = Flask(__name__)

@app.route('/emails/verify_emails')
def verifyEmails(): 
    return jsonify(email_commands.verifyEmails())

@app.route('/emails/read_emails')
def readEmails():
    return jsonify(email_commands.readEmails())

if __name__ == "__main__":
    app.run()
