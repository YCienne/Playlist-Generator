from flask import Flask
from website.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    from website.routes import main
    app.register_blueprint(main)

    return app
