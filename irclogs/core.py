from flask import Flask
from flask.ext.restless import APIManager
from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()
api = APIManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('irclogs.settings')
    db.init_app(app)
    api.init_app(app, flask_sqlalchemy_db=db)
    from .views import angular_blueprint
    app.register_blueprint(angular_blueprint)
    from . import api as apistuff
    return app
