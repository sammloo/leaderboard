from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import logging

logger = logging.getLogger(__name__)

db = SQLAlchemy()

def create_app():
    try:
        app = Flask(__name__)
        app.config.from_object(Config)
        CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})

    
        db.init_app(app)
        with app.app_context():
            db.create_all()
        from app.routes import base_routes
        from app.routes import user_routes

        app.register_blueprint(base_routes, url_prefix="/")
        app.register_blueprint(user_routes, url_prefix="/users")

        return app
    except Exception as e:
        logger.error(f"Failed creating app: {e}")