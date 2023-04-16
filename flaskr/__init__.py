from flask import Flask
import os

DATABASE_URL = os.getenv(
    'DATABASE_URL', 'postgresql://postgres:ABCD1234@db-black-list.cqhvrt5vquda.us-east-1.rds.amazonaws.com:5432/postgres')


def create_app(config_name):
    application = Flask(__name__)

    application.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
    application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    return application
