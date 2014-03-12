import os

ROOT = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(ROOT, 'dev.db'))
ANGULAR_RESOURCE_DIRECTORY = os.path.join(ROOT, 'angular')
