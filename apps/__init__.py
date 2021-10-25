from os import environ, urandom
from datetime import timedelta
from flask_cors import CORS
from flask import Flask
from . import home, meal, misc, school

app = Flask(__name__)

app.register_blueprint(home.home)
app.register_blueprint(meal.meal)
app.register_blueprint(misc.misc)
app.register_blueprint(school.school)
