import json
from flask import render_template
from __main__ import app


@app.route("/", methods=["GET"])
def get_home():
    """
    메인 화면
    """
    return render_template(
        "home.html",
        hello="asdfqwer",
    )
