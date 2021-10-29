import json
from flask import Blueprint, render_template, url_for, session, request, redirect

home = Blueprint("home", __name__, url_prefix="/")


@home.route("/")
def get_home():
    """
    메인 화면
    """
    return render_template(
        "home.html",
        hello="Greeting",
    )


@home.route("/login")
def get_login():
    from apps import google

    return google.authorize(callback=url_for("home.callback", _external=True))


@home.route("/logout")
def get_logout():
    session.pop("google_token", None)
    return redirect(url_for("home.get_home"))


@home.route("/login/callback")
def callback():
    from apps import google

    @google.tokengetter
    def get_google_oauth_token():
        return session.get("google_token")

    resp = google.authorized_response()
    foot_print = resp

    if resp is None:
        return "Access denied: reason=%s error=%s" % (
            request.args["error"],
            request.args["error_description"],
        )
    session["google_token"] = (resp["access_token"], "")
    me = google.get("userinfo")

    return render_template("login.html", data=me.data)
