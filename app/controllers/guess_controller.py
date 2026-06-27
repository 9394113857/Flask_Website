from flask import Blueprint, render_template

guess_bp = Blueprint("guess", __name__)


@guess_bp.route("/guess")
def guess():

    return render_template("guess.html")