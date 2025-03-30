from .auth_routes import auth_bp
from .text_routes import text_bp
from .voice_routes import voice_bp
from .chat_routes import chat_bp
from .para_routes import para_bp

__all__ = ['auth_bp', 'text_bp', 'voice_bp', 'chat_bp', 'para_bp']