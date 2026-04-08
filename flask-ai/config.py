"""
Application Configuration
"""

import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Base configuration"""

    # Flask Settings
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DEBUG = os.getenv('FLASK_DEBUG')

    # API Settings
    API_TIMEOUT = 30
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024

    # CORS Settings
    CORS_HEADERS = 'Content-Type'

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    TESTING = False

class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    TESTING = False

class TestingConfig(Config):
    """Testing configuration"""
    DEBUG = True
    TESTING = True

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}