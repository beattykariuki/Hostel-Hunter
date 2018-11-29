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
