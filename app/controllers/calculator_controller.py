from flask import Blueprint
from flask import render_template
from flask import request

from app.services.calculator_service import CalculatorService


calculator_bp = Blueprint(
    "calculator",
    __name__
)


@calculator_bp.route(
    "/calculator",
    methods=["GET", "POST"]
)
def calculator():

    result = None

    error = None

    if request.method == "POST":

        try:

            number1 = float(
                request.form["number1"]
            )

            number2 = float(
                request.form["number2"]
            )

            operation = request.form["operation"]

            result = CalculatorService.calculate(
                number1,
                number2,
                operation
            )

        except ValueError:

            error = "Please enter valid numbers."

        except Exception:

            error = "Something went wrong."

    return render_template(
        "calculator.html",
        result=result,
        error=error
    )