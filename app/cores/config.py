from environs import Env

env = Env()
env.read_env()
debugMode = True


class Config:
    APP_ENV = env.str('APP_ENV', default="development")
    ARRAY_ENV = ['development', 'staging']
    PORT = env.int('APP_PORT', default=5000)
    MYSQL_DATABASE_CHARSET = 'utf8mb4'

    HOST = env.str("DB_HOST", default="127.0.0.1")
    DATABASE = env.str("DB_DATABASE", default="local")
    USERNAME = env.str("DB_USERNAME", default="user")
    PASSWORD = env.str("DB_PASSWORD", default="secret")
    MONGO_URL = env.str("MONGO_URL", default=f'mongodb://{HOST}:27017/{DATABASE}')
