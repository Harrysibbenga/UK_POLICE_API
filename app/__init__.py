from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

def create_app():
    """
        Create and configure the Flask application.
        
        This function initializes the Flask application, loads the configuration,
        initializes extensions, and registers blueprints.
        
        Returns:
            Flask: The configured Flask application instance.
    """
    
    app = Flask(__name__)
    
    # Load configuration
    from .config import Config
    app.config.from_object(Config)
    
    # Initialize extensions
    limiter = Limiter(
        get_remote_address,
        app=app,
        default_limits=[Config.RATE_LIMIT]
    )
    
    # Register blueprints
    from .routes import bp as routes_bp
    app.register_blueprint(routes_bp)
    
    return app

