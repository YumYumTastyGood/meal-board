from flask import Flask, request, abort
from os import environ, urandom
from datetime import timedelta
from flask_cors import CORS

app = Flask(__name__)

if __name__ == "__main__":
    from routes import *

    CORS(app, support_credentials=True)
    app.secret_key = urandom(12)
    app.config["SESSION_COOKIE_NAME"] = "google-login-session"
    app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=5)
    app.run(host="0.0.0.0", port=5000, debug=False)
