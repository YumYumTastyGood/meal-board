from os import urandom
from datetime import timedelta
from flask_cors import CORS
from flask import Flask
from . import home, meal, misc, school

app = Flask(__name__)
app.secret_key = urandom(12)
app.config["SESSION_COOKIE_NAME"] = "google-login-session"
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=5)
CORS(app, support_credentials=True)
app.register_blueprint(home.home)
app.register_blueprint(meal.meal)
app.register_blueprint(misc.misc)
app.register_blueprint(school.school)
