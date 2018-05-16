import os

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from api import db, create_app


config_name = os.getenv('APP_ENV') # config_name = "development"
app = create_app("development")

manager = Manager(app)
migrate = Migrate(app,db)

manager.add_command("db",MigrateCommand)

@manager.command
def create_db():

    db.create_all()


if __name__ == '__main__':
    manager.run()






