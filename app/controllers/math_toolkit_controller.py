"""
math_toolkit_controller.py

Purpose
-------
Handles requests for the Math Toolkit page.
"""

from flask import Blueprint
from flask import render_template

from app.services.math_toolkit_service import MathToolkitService


math_toolkit_bp = Blueprint(
    "math_toolkit",
    __name__
)


@math_toolkit_bp.route(
    "/math-toolkit"
)
def math_toolkit():

    page_data = MathToolkitService.get_page_data()

    return render_template(
        "math_toolkit.html",
        page_data=page_data
    )