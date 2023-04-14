from flask import Flask

def create_app(config_name):
    application = Flask(__name__)

    application.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:ABCD1234@db-black-list.cqhvrt5vquda.us-east-1.rds.amazonaws.com:5432/"
    application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    if(application.config['SQLALCHEMY_DATABASE_URI'] == "" or application.config['SQLALCHEMY_DATABASE_URI'] is None):
        application.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///correos.db"

    return application