import os
from dotenv import load_dotenv


base_dir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(base_dir, '.env'))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secretKey333son'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
