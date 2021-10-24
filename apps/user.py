import os
import json
from flask import (
    render_template,
    make_response,
    redirect,
    session,
    abort,
    request,
    url_for,
)
from flask_restx import Resource, Namespace
import pathlib
from authlib.integrations.flask_client import OAuth
from functools import wraps
from app import oauth


os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

client_secrets_file = os.path.join(
    pathlib.Path(__file__).parent.parent, "mealboard-google-secret.json"
)

User = Namespace("User")


def login_is_required(function):
    @wraps(function)
    def decorated_function(*args, **kwargs):
        user = dict(session).get("profile", None)
        if user:
            return f(*args, **kwargs)
        return redirect("/user/login")

    return decorated_function


@User.route("/login")
class UserLogin(Resource):
    def get(self):
        google = oauth.create_client("google")
        redirect_uri = url_for("/user/authorize", _external=True)
        return google.authorize_redirect(redirect_uri)


@User.route("/authorize")
class UserAuthorize(Resource):
    def get(self):
        google = oauth.create_client("google")
        token = google.authorize_access_token()
        resp = google.get("userinfo")
        user_info = resp.json()
        session["profile"] = user_info
        session.permanent = True
        return redirect(url_for("/user/protected_area"))


@User.route("/logout")
class UserLogout(Resource):
    def get(self):
        session.clear()
        return redirect("/")


@User.route("/protected_area")
class UserProtectedArea(Resource):
    @login_is_required
    def get(self):
        return f"Hello {session['name']}! <br/> <a href='/logout'><button>Logout</button></a>"
