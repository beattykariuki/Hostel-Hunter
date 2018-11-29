from app import create_app,db
<<<<<<< HEAD
<<<<<<< HEAD
from app.models import User,Role,Review
from flask_migrate import MigrateCommand
=======
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from app.models import Review

# Creating app instance
app = create_app('development')


manager = Manager(app)
manager.add_command('server', Server)
>>>>>>> review

migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

<<<<<<< HEAD
@manage.shell
def make_shell_context():
    return dict(app = app, db = db, User = User, Role = Role )



if __name__ == '__main__':
    manage.run()
=======

@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('test')
    unittest.TextTestRunner(verbosity=2).run(tests)


@manager.shell
def make_shell_context():
    return dict(app=app, db=db, User=User)
    
if __name__ == '__main__':
    manager.run()
>>>>>>> review
=======
from app.models import University
from flask_script import Manager,Server
from flask_migrate import Migrate, MigrateCommand

app = create_app('development')
manager = Manager(app)
manager.add_command('server',Server)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

@manager.command
def test():
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db)
    
if __name__ == '__main__':
    manager.run()
>>>>>>> searchHostel
