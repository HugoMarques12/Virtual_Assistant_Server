from flask import Flask, jsonify
from emails.email_handler import *

class EmailCommands:
    def __init__(self):
        self.emailHandler = EmailHandler()

    def verifyEmails(self):
        return {"message": self.emailHandler.verifyNewEmails()}
    
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
