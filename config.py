import os

class Config:

    SECRET_KEY = os.environ.get('SECRET_KEY')
    QUOTE_URL ='http://quotes.stormconsultancy.co.uk/quotes.json'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kev:@Y0a!yAV@localhost/blog'


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}