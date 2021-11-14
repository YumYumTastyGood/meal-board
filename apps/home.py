import json
from flask import Blueprint, render_template, url_for, session, request, redirect
from database.user import set_user, get_user_by_user_id, get_user_by_user_auth
from apps.auth import google

home = Blueprint("home", __name__, url_prefix="/")


@home.route("/")
def get_home():
    """
    메인 화면
    """
    if "auth" not in session:
        return render_template("home.html", auth=False)
    return render_template("home.html", auth=True)


@home.route("/login")
def get_login():
    if "auth" not in session:
        return google.authorize(callback=url_for("home.callback", _external=True))
    return redirect(url_for("home.get_home"))


@home.route("/logout")
def get_logout():
    session.pop("google_token", None)
    session.pop("auth", None)
    return redirect(url_for("home.get_home"))


@home.route("/login/callback")
def callback():
    @google.tokengetter
    def get_google_oauth_token():
        return session.get("google_token")

    resp = google.authorized_response()
    if resp is None:
        return "Access denied: reason=%s error=%s" % (
            request.args["error"],
            request.args["error_description"],
        )
    session["google_token"] = (resp["access_token"], "")
    me = google.get("userinfo")
    user = get_user_by_user_id(provider="google", user_id=me.data.get("id"))
    if not user:
        auth = set_user(provider="google", info=me.data)
        session["auth"] = auth
    else:
        session["auth"] = user.auth
    return redirect(url_for("home.get_home"))
