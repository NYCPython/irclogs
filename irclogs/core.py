from flask import Flask
from flask.ext.foundation import Foundation
from flask.ext.restless import APIManager
from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()
api = APIManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('irclogs.settings')
    db.init_app(app)
    api.init_app(app, flask_sqlalchemy_db=db)
    Foundation(app)
    from .views import frontend
    app.register_blueprint(frontend, url_prefix='/')
    from . import api as apistuff
    return app
