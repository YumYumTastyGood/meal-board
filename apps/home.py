import json
from flask import Blueprint, render_template

home = Blueprint("home", __name__, url_prefix="/")


@home.route("/")
def get_home():
    """
    메인 화면
    """
    return render_template(
        "home.html",
        hello="asdfqwer",
    )
