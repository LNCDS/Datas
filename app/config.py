class Config(object):
    host = "0.0.0.0"
    port = 4000

class ProdConfig(Config):
    pass
class DevConfig(Config):
    DEBUG = True
    