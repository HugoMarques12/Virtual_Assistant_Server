from flask import Flask
from routes.browser import browserBp
from routes.emails import emailsBp
from routes.steam import steamBp

app = Flask(__name__)
app.register_blueprint(browserBp)
app.register_blueprint(emailsBp)
app.register_blueprint(steamBp)


if __name__ == "__main__":
    app.run()
