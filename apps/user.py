import os
import json
from flask import render_template, make_response, redirect, session, abort, request
from flask_restx import Resource, Namespace

from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
import pathlib

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

client_secrets_file = os.path.join(
    pathlib.Path(__file__).parent.parent, "mealboard-google-secret.json"
)

User = Namespace("User")


flow = Flow.from_client_secrets_file(
    client_secrets_file=client_secrets_file,
    scopes=[
        "https://www.googleapis.com/auth/userinfo.profile",
        "https://www.googleapis.com/auth/userinfo.email",
        "openid",
    ],
    redirect_uri="http://127.0.0.1:5000/user/callback",
)


def login_is_required(func):
    def wrapper(*args, **kwargs):
        if "google_id" not in session:
            return abort(401)
        else:
            return func()

    return wrapper


@User.route("/login")
class UserLogin(Resource):
    def get(self):
        authorizational_url, state = flow.authorization_url()
        session["state"] = state

        # if u wanna render template uncomment this block
        # headers = {"Content-Type": "text/html"}
        # return make_response(render_template("login.html", test="hello"), 200, headers)

        return redirect(authorizational_url, code=302)


@User.route("/callback")
class UserLoginCallback(Resource):
    def get(self):
        flow.fetch_token(authorization_response=request.url)

        if not session["state"] == request.args["state"]:
            abort(500)

        credentials = flow.credentials
        request_session = request.session()
        cached_session = cachecontrol.CacheControl(request_session)
        token_request = google.auth.transport.requests.Request(cached_session)

        # print(f"request >> {request}")
        # print(f'state >> {request.args.get("state")}')
        # if not session.get("state") == request.args.get("state"):
        #     abort(500)  # State does not match!
        # credentials = flow.credentials
        # request_session = requests.session()
        # cached_session = cachecontrol.CacheControl(request_session)
        # token_request = google.auth.transport.requests.Request(session=cached_session)

        # id_info = id_token.verify_oauth2_token(
        #     id_token=credentials._id_token,
        #     request=token_request,
        #     audience=GOOGLE_CLIENT_ID,
        # )

        # session["google_id"] = id_info.get("sub")
        # session["name"] = id_info.get("name")
        # return redirect("/user/protected_area")
        return {"hello": "world"}


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
