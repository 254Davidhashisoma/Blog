import os 


class Config:

    
    # SECRET_KEY = os.urandom(32)
    # app.config['SECRET_KEY'] = SECRET_KEY
    SECRET_KEY = os.environ.get("SECRET_KEY")
    UPLOADED_PHOTOS_DEST = "app/static/photos"
    # SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://moringa:hashi123@localhost/blog"
           # email configurations
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProdConfig(Config):
    
    SQLALCHEMY_DATABASE_URI = os.environ.get("HEROKU_POSTGRESQL_CRIMSON_URL")

class TestConfig(Config):
    
    pass

class DevConfig(Config):

    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://moringa:hashi123@localhost/blog"
    DEBUG = True


config_options = {
    "development": DevConfig,
    "production": ProdConfig,
    # "test": TestConfig
}