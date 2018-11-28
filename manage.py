from app import create_app,db
from app.models import User,Role
from flask_migrate import, MigrateCommand

migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

@manage.shell
def make_shell_context():
    return dict(app = app, db = db, User = User, Role = Role )



if __name__ == '__main__':
    manage.run()