import os


class Config(object):

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
