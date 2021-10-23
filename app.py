from os import environ

from utils.env import init_json_env
from utils.timer import get_datetime, calc_uptime
from database import Mongo

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
api.init_app(app, title="Wokeup API", version="1.0", description="Wokeup API")
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)
api.add_namespace(Home, "/home")
api.add_namespace(School, "/school")
api.add_namespace(Meal, "/meal")
api.add_namespace(Misc, "/misc")
api.add_namespace(User, "/user")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
