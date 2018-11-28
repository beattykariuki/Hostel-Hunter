from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy

#optional whooshalchemy
from flask_whooshalchemy import WHOOSHAlchemy

bootstrap = Bootstrap()
db = SQLAlchemy()
db = WHOOSHAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_options[config_name])
    config_options[config_name].init_app(app)

    bootstrap.init_app(app)
    db.init_app(app)

    return app
