import os
 
 class Config():
     '''
     Configuration parent class
     '''
     SECRET_KEY = os.environ.get('SECRET_KEY') or 'HOSTELHUNTER'
     UPLOADED_PHOTOS_DEST ='app/static/photos'

     #email configurations
     MAIL_SERVER = 'smtp.gmail.com'
     MAIL_PORT = 587
     MAIL_USE_TLS = True 
     MAIL_USERNAME = o.s.environ.get("MAIL_USERNAME")
     MAIL_PASSWORD = o.s.environ.get("MAIL_PASSWORD")

class TestConfig(config):
    SQALCHEMY_DATABASE_URI = 'postgresql+psycopg2://beatty:password@localhost/hostel_test':password@localhost/hostel_test
    
class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://beatty:password@localhost/hostel'
    '''
    Development config class
    '''
    DEBUG = True
    ENV = 'development'

config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig
}

class ProdConfig(Config):
    '''
    Production Config class
    '''
    pass

