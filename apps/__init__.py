from os import environ
from datetime import timedelta
from routes import api

# from database import Mongo
# from authlib.integrations.flask_client import OAuth

# from flask import Flask, jsonify, render_template, request

app = Flask(__name__)
app.secret_key = urandom(12)
app.config["SESSION_COOKIE_NAME"] = "google-login-session"
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=5)

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
