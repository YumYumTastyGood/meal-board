import json
from flask import Blueprint, render_template, session
from database.user import get_user_by_user_auth

about = Blueprint("about", __name__, url_prefix="/about")


@about.route("/")
def get_about():
    if "auth" not in session:
        return render_template("about.html", auth=False)
    return render_template("about.html", auth=True)
