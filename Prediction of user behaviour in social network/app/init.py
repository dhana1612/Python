from flask import Flask
from .utils.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Register blueprints
    from .routes.auth_routes import auth_bp
    from .routes.text_routes import text_bp
    from .routes.voice_routes import voice_bp
    from .routes.chat_routes import chat_bp
    from .routes.para_routes import para_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(text_bp)
    app.register_blueprint(voice_bp)
    app.register_blueprint(chat_bp)
    app.register_blueprint(para_bp)
    
    return app