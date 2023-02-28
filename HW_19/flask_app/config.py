import os

class Config(object):
    PATH = '/usr/logs'

class DevelopmentConfig(Config):
    DEBUG = True