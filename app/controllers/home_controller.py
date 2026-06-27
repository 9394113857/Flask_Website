"""
home_controller.py

Purpose:
--------
Handles requests for the Home page.

Responsibilities:
-----------------
1. Receive browser requests.
2. Return the Home HTML page.
3. No business logic.
4. No database operations.
"""

from flask import Blueprint, render_template


# Blueprint for Home page
home_bp = Blueprint("home", __name__)


@home_bp.route("/", methods=["GET"])
def home():
    """
    Home Page

    URL:
        /

    Method:
        GET

    Description:
        Displays the Home page.
    """

    return render_template("home.html")