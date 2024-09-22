class Config(object):
    def __init__(self) -> None:
        self.host = "0.0.0.0"
        self.port = 4000
    
class ProdConfig(Config):
    pass
class DevConfig(Config):
    DEBUG = True
    