import os

SECRET_KEY = os.urandom(32)

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://apisia_eveningpig:e92524fd04a76910e273959ead17d08ad1612af9@6kr.h.filess.io:3307/apisia_eveningpig'

SQLALCHEMY_TRACK_MODIFICATIONS = False