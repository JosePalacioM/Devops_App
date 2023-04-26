from flask import Flask
import os

DATABASE_URL = os.getenv(
    'DATABASE_URL', 'sqlite:///block_email.db')


def create_app(config_name):
    application = Flask(__name__)

    application.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
    application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    return application
