import os
<<<<<<< HEAD
<<<<<<< HEAD
 
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
=======

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

class ProdConfig(Config):
    '''
    Production configuration child class

    Args: 
        Config: The parent configuration class with General configuration settings
    '''


    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    pass


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringaschool:maroon5@localhost/hostel_test'

class DevConfig(Config):
    '''
    Development configuration child class
    Args:
        Config: The parent configuration class with general configuration settings 
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringaschool:maroon5@localhost/hostel'
    DEBUG = True
>>>>>>> review

config_options = {
    'development':DevConfig,
    'production':ProdConfig,
<<<<<<< HEAD
    'test':TestConfig
}

class ProdConfig(Config):
    '''
    Production Config class
    '''
    pass
=======
    'test': TestConfig
}




>>>>>>> review

=======

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kevine:2001kevi@localhost/hostel'
    
class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kevine:2001kevi@localhost/hostel'
    DEBUG = True

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    pass

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kevine:2001kevi@localhost/hostel'

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}
>>>>>>> searchHostel
