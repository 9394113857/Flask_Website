# app/__init__.py

from flask import Flask

from app.config import Config

from app.controllers.home_controller import home_bp
from app.controllers.calculator_controller import calculator_bp
from app.controllers.bmi_controller import bmi_bp
from app.controllers.flames_controller import flames_bp
from app.controllers.guess_controller import guess_bp
from app.controllers.about_controller import about_bp
from app.controllers.contact_controller import contact_bp


def create_app():
    """
    Application Factory Function.

    Creates and configures the Flask application.
    Registers all Blueprints.
    Returns the ready-to-use Flask application.
    """

    app = Flask(__name__)

    # Load configuration
    app.config.from_object(Config)

    # Register Blueprints
    app.register_blueprint(home_bp)
    app.register_blueprint(calculator_bp)
    app.register_blueprint(bmi_bp)
    app.register_blueprint(flames_bp)
    app.register_blueprint(guess_bp)
    app.register_blueprint(about_bp)
    app.register_blueprint(contact_bp)

    return app