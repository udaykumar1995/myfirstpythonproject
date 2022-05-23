import os

class BaseConfig:
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = os.getenv("DB_PORT", 5432)
    DB_USER = os.getenv("DB_USER", "postgres")
    DB_PASS = os.getenv("DB_PASS", "postgres")
    DB_NAME = os.getenv("DB_NAME", "sample")
    DB_TYPE = os.getenv("DB_TYPE", "postgresql")
    DEBUG = os.getenv("FLASK_DEBUG", False)

class LocalConfig(BaseConfig):
    DEBUG = os.getenv("FLASK_DEBUG", True)

CONFIG_BY_ENV = dict(local=LocalConfig)
        

