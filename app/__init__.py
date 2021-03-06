<<<<<<< HEAD
<<<<<<< HEAD
from flask import Flask 
from flask_bootstrap import Bootstrap 
from config import config_options
from flask_login import LoginManager
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_mail import Mail

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
bootstrap = Bootstrap

mail = Mail()

photos = Uploadset('photos',IMAGES)
def create_app(config_name):
    app = Flask(__name__)
    from .auth import auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')
    mail.init_app(app)

    #configure UploadSet
    configure_uploads(app,photos)

    #Creating app configurations
    app.config.from_object(config_options[config_name])

    #Initializing flask extensions
    bootstrap.init_app(app)
    
    #Initializing Flask Extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
=======
from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_uploads import UploadSet, configure_uploads, IMAGES
from flask_mail import Mail
from flask_simplemde import SimpleMDE

bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
photos = UploadSet('photos',IMAGES)
mail = Mail()
simple = SimpleMDE()

def create_app(config_name):
    app = Flask(__name__)

    # Creating the app congigurations
    app.config.from_object(config_options[config_name])

    # Configure UploasSet
    configure_uploads(app,photos)

    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    
    simple.init_app(app)
    
    #Registering the blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix = '/authenticate')
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)     

    return app
>>>>>>> review
=======
from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy

bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_options[config_name])
    bootstrap.init_app(app)
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    db.init_app(app)

    return app
>>>>>>> searchHostel
