import os 
from dotenv import load_dotenv 

load_dotenv()
class Config:
    SECRET_KEY = os.getenv('Secret_Key')
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True
    DATABASE_URI = os.getenv('DATABASE_URI')

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
