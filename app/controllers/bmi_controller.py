from flask import Blueprint, render_template

bmi_bp = Blueprint("bmi", __name__)


@bmi_bp.route("/bmi")
def bmi():

    return render_template("bmi.html")