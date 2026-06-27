"""
calculator_service.py

Purpose
-------
Contains all calculator business logic.
"""

class CalculatorService:

    @staticmethod
    def calculate(number1, number2, operation):

        if operation == "+":
            return number1 + number2

        elif operation == "-":
            return number1 - number2

        elif operation == "*":
            return number1 * number2

        elif operation == "/":

            if number2 == 0:
                return "Cannot divide by zero."

            return number1 / number2

        return "Invalid Operation"