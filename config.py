import os


class Config:
    '''
    General configuration parent class
    '''
    #  email configurations

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")
    MAIL_USERNAME = os.environ.get("EMAIL_USERNAME")
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringaschool:maroon5@localhost/hostel'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    DEBUG = True

    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://beatty:password@localhost/hostel'
    '''
    Development config class
    '''
    DEBUG = True
    ENV = 'development'



class ProdConfig(Config):
    '''
    Production configuration child class

    Args: 
        Config: The parent configuration class with General configuration settings
    '''

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class TestConfig(config):
    SQALCHEMY_DATABASE_URI = 'postgresql+psycopg2://beatty:password@localhost/hostel_test':password@localhost/hostel_test
    
config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    'test': TestConfig
}




