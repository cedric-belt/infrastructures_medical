from flask import Flask

from src.config import Config
from src.database import init_db
from src.routes import health_bp, equipment_bp, patient_bp


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)

    init_db()

    app.register_blueprint(health_bp)
    app.register_blueprint(equipment_bp, url_prefix="/api/v1")
    app.register_blueprint(patient_bp, url_prefix="/api/v1")

    @app.route("/")
    def index():
        return {
            "application": "infrastructures_medical",
            "status": "online",
            "version": "0.1.0",
            "docs": "/health",
        }

    return app
