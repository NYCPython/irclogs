from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('irclogs.settings')
    db.init_app(app)
    from .views import bp
    app.register_blueprint(bp)
    return app
