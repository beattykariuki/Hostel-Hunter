import os
 
 class Config():
     '''
     Configuration parent class
     '''
     SECRET_KEY = os.environ.get('SECRET_KEY') or 'HOSTELHUNTER'

class DevConfig(Config):
    '''
    Development config class
    '''
    DEBUG = True
    ENV = 'development'

class ProdConfig(Config):
    '''
    Production Config class
    '''
    pass

