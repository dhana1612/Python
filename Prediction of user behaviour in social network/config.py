import os

class Config:
    SECRET_KEY = os.environ.get('123') or 'dev-secret-key'
    TEMPLATES_AUTO_RELOAD = True
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB upload limit