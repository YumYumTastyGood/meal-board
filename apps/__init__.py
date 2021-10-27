from settings import *
from os import urandom
from datetime import timedelta
from flask_cors import CORS
from flask import Flask
from utils.env import get_database_uri
from . import home, meal, misc, school
from flask_pymongo import PyMongo

app = Flask(__name__)
CORS(app, support_credentials=True)
app.secret_key = urandom(12)
app.config["SESSION_COOKIE_NAME"] = "google-login-session"
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=5)
app.config["MONGO_URI"] = get_database_uri(DATABASES)
mongo = PyMongo(app)
app.register_blueprint(home.home)
app.register_blueprint(meal.meal)
app.register_blueprint(misc.misc)
app.register_blueprint(school.school)
