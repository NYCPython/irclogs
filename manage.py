from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.script import Manager

from irclogs.core import create_app, db
from irclogs.views import frontend

app = create_app()
manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
