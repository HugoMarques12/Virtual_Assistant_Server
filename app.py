from flask import Flask, jsonify
from emails.email_handler import *

app = Flask(__name__)

class Commands:
    @app.route('/ler_emails')
    def readEmails():
        email_handler = EmailHandler()
        if email_handler.login():
            return jsonify({"message": "Erro ao fazer login. Verifique suas credenciais."})

        return jsonify({"message": email_handler.verifyNewEmails()})


if __name__ == "__main__":
    app.run()
