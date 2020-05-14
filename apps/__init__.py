import os

from flask import Flask
from flask_config import config


def create_app(config_name=None):
    # create and configure the app
    _app = Flask(__name__)
    _app.config.from_object(config[config_name])
    config[config_name].init_app(_app)

    return _app


app = create_app(os.getenv('FLASK_CONFIG') or 'default')

if __name__ == "__main__":
    print(os.getenv('FLASK_CONFIG'))