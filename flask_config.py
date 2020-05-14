


class Config:
    BABEL_DEFAULT_LOCALE = 'zh_CN'
    FLASKY_SLOW_DB_QUERY_TIME = 0.5
    # SQLALCHEMY_ECHO = True
    JSON_AS_ASCII = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    JSON_AS_ASCII = False


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    JSON_AS_ASCII = False


config = {
    'dev': DevelopmentConfig,
    'test': TestingConfig,
    'prod': ProductionConfig,
    'default': DevelopmentConfig
}
