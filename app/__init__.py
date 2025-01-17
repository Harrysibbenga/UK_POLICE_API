from flask import Flask

def create_app():
    app = Flask(__name__)

    from .config import Config
    app.config.from_object(Config)

    from .routes import bp
    app.register_blueprint(bp)

    return app