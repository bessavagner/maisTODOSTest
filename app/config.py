import os
import random
import string
from decouple import config

basedir = os.path.dirname(os.path.realpath(__file__))

gen = string.ascii_letters + string.digits + string.ascii_uppercase
key = ''.join(random.choice(gen) for i in range(12))


class Config:
    SECRET_KEY = key
    SQLALCHEMY_DATABASE_URI = config('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
