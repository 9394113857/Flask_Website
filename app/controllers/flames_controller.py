from flask import Blueprint, render_template

flames_bp = Blueprint("flames", __name__)


@flames_bp.route("/flames")
def flames():

    return render_template("flames.html")