# config.py
import os

class Config:
    # General configurations
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_default_secret_key')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Database configurations
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')  # Read from environment variable
