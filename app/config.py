# app/config.py

# Configuration file for the Flask application.
import os


class Config: 
    """
    Base configuration class for the Flask application.

    This class stores all application-level settings in one place.
    As the project grows, more configuration variables can be added here.
    """

    # Secret key used by Flask for securely signing sessions and flash messages.
    SECRET_KEY = os.getenv("SECRET_KEY", "this_is_my_secret_key")

    # Enables or disables debug mode.
    DEBUG = True