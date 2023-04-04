from flask import Flask

def create_app(config_name):
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = ""
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    if(app.config['SQLALCHEMY_DATABASE_URI'] == "" or app.config['SQLALCHEMY_DATABASE_URI'] is None):
        app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///correos.db"

    return app