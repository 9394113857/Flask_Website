"""
math_toolkit_controller.py

Purpose
-------
Handles requests for the Math Toolkit page.
"""

from flask import Blueprint
from flask import render_template
from flask import request

from app.services.math_toolkit_service import MathToolkitService
from app.services.basic_operations_service import BasicOperationsService


math_toolkit_bp = Blueprint(
    "math_toolkit",
    __name__
)


@math_toolkit_bp.route(
    "/math-toolkit",
    methods=["GET", "POST"]
)
def math_toolkit():

    page_data = MathToolkitService.get_page_data()

    # ==========================================
    # Addition Variables
    # ==========================================

    add_number1 = ""

    add_number2 = ""

    addition_result = None

    addition_error = None

    # ==========================================
    # Subtraction Variables
    # ==========================================

    sub_number1 = ""

    sub_number2 = ""

    subtraction_result = None

    subtraction_error = None

    # ==========================================
    # Multiplication Variables
    # ==========================================

    mul_number1 = ""

    mul_number2 = ""

    multiplication_result = None

    multiplication_error = None

    # ==========================================
    # Division Variables
    # ==========================================

    div_number1 = ""

    div_number2 = ""

    division_result = None

    division_error = None
    
    # ==========================================
    # Modulus Variables
    # ==========================================

    mod_number1 = ""

    mod_number2 = ""

    modulus_result = None

    modulus_error = None
    
    
    # if the request method is POST, we will process the form data based on the selected operation. 
    # Otherwise, we will just render the page with the initial data without any calculations.
    if request.method == "POST":

        try:

            operation = request.form.get("operation")

            # ==========================================
            # Addition
            # ==========================================

            # if operation is None:
            # Why we are commented above line
            # becase of the fact
            # that we are using the "required" attribute in the HTML form,
            # which ensures that the user must select an operation before submitting the form.
            # Therefore, we can assume that the operation variable will always have a value
            # when the form is submitted.

            if operation == "add":

                add_number1 = float(
                    request.form["number1"]
                )

                add_number2 = float(
                    request.form["number2"]
                )

                addition_result = BasicOperationsService.add(
                    add_number1,
                    add_number2
                )

            # ==========================================
            # Subtraction
            # ==========================================

            elif operation == "subtract":

                sub_number1 = float(
                    request.form["sub_number1"]
                )

                sub_number2 = float(
                    request.form["sub_number2"]
                )

                subtraction_result = BasicOperationsService.subtract(
                    sub_number1,
                    sub_number2
                )            
                
            # ==========================================
            # Multiplication
            # ==========================================

            elif operation == "multiply":

                mul_number1 = float(
                    request.form["mul_number1"]
                )

                mul_number2 = float(
                    request.form["mul_number2"]
                )

                multiplication_result = BasicOperationsService.multiply(
                    mul_number1,
                    mul_number2
                )

            # ==========================================
            # Division
            # ==========================================

            elif operation == "divide":

                div_number1 = float(
                    request.form["div_number1"]
                )

                div_number2 = float(
                    request.form["div_number2"]
                )

                division_result = BasicOperationsService.divide(
                    div_number1,
                    div_number2
                )
                
            # ==========================================
            # Modulus Variables
            # ==========================================

            elif operation == "modulus":

                mod_number1 = float(
                    request.form["mod_number1"]
                )

                mod_number2 = float(
                    request.form["mod_number2"]
                )

                modulus_result = BasicOperationsService.modulus(
                    mod_number1,
                    mod_number2
                )

                # Commented because resetting these variables 
                # clears the calculated result and error.
                # Commnted Lines ✅:- 
                # modulus_result = None
                # modulus_error = None    


        except ValueError:

            if operation == "add":

                addition_error = "Please enter valid numbers."

            elif operation == "subtract":

                subtraction_error = "Please enter valid numbers."

            elif operation == "multiply":

                multiplication_error = "Please enter valid numbers."

            elif operation == "divide":

                division_error = "Please enter valid numbers."
                
            elif operation == "modulus":

                modulus_error = "Please enter valid numbers."    


        except ZeroDivisionError:

            if operation == "divide":

                division_error = "Cannot divide by zero."

            elif operation == "modulus":

                modulus_error = "Cannot divide by zero."


        except Exception:

            if operation == "add":

                addition_error = "Something went wrong."

            elif operation == "subtract":

                subtraction_error = "Something went wrong."

            elif operation == "multiply":

                multiplication_error = "Something went wrong."

            elif operation == "divide":

                division_error = "Something went wrong."

            elif operation == "modulus":

                modulus_error = "Something went wrong."

    return render_template(
        "math_toolkit.html",
        page_data=page_data,

        # Addition Data
        add_number1=add_number1,
        add_number2=add_number2,
        addition_result=addition_result,
        addition_error=addition_error,

        # Subtraction Data
        sub_number1=sub_number1,
        sub_number2=sub_number2,
        subtraction_result=subtraction_result,
        subtraction_error=subtraction_error,

        # Multiplication Data
        mul_number1=mul_number1,
        mul_number2=mul_number2,
        multiplication_result=multiplication_result,
        multiplication_error=multiplication_error,

        # Division Data
        div_number1=div_number1,
        div_number2=div_number2,
        division_result=division_result,
        division_error=division_error,

        # Modulus Data
        mod_number1=mod_number1,
        mod_number2=mod_number2,
        modulus_result=modulus_result,
        modulus_error=modulus_error
    )
    


################### END OF THE FILE ######################



# Now your controller has:

# ✅ Separate inputs for all calculators
# ✅ Separate results for all calculators
# ✅ Separate errors for all calculators
# ✅ No result leaking into the Addition card
# ✅ Ready for updating the HTML partials    