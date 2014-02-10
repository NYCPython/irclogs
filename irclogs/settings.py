import os

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(os.path.dirname(__file__), 'dev.db'))
