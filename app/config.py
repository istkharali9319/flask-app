import os
from datetime import timedelta
from dotenv import load_dotenv
load_dotenv() 

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL", "sqlite:///flask_project.db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # JWT settings
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "jwt-secret-key")
    # Access token expiry
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=2)
    #  Refresh token expiry
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=7)