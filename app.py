from os import environ
from datetime import timedelta

from utils.env import init_json_env
from utils.timer import get_datetime, calc_uptime
from database import Mongo
from authlib.integrations.flask_client import OAuth

from flask import Flask, jsonify, render_template, request
from flask_restx import Api, Resource
from flask_cors import CORS
from apps.home import Home
from apps.school import School
from apps.meal import Meal
from apps.misc import Misc
from apps.user import User

# if json env file is provided, use it
wokeup = get_datetime()
api = Api()
app = Flask(__name__)
app.secret_key = "mealboard-secret-key"
app.config["SESSION_COOKIE_NAME"] = "google-login-session"
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=5)
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)
oauth = OAuth(app)
google = oauth.register(
    name="google",
    client_id=environ.get("GOOGLE_CLIENT_ID"),
    client_secret=environ.get("GOOGLE_CLIENT_SECRET"),
    access_token_url="https://accounts.google.com/o/oauth2/token",
    access_token_params=None,
    authorize_url="https://accounts.google.com/o/oauth2/auth",
    authorize_params=None,
    api_base_url="https://www.googleapis.com/oauth2/v1/",
    userinfo_endpoint="https://openidconnect.googleapis.com/v1/userinfo",  # This is only needed if using openId to fetch user info
    client_kwargs={"scope": "openid email profile"},
)

api.init_app(app, title="Wokeup API", version="1.0", description="Wokeup API")
api.add_namespace(Home, "/home")
api.add_namespace(School, "/school")
api.add_namespace(Meal, "/meal")
api.add_namespace(Misc, "/misc")
api.add_namespace(User, "/user")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
