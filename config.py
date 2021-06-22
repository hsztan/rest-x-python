from os import getenv

db = getenv("DATABASE_NAME")
user = getenv("DATABASE_USER")
password = getenv("DATABASE_PASS")
host = getenv("DATABASE_HOST")
port = getenv("DATABASE_PORT")

class Config:
    SQLALCHEMY_DATABASE_URI = f"postgresql://{user}:{password}@{host}:{port}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = getenv('SECRET_KEY')