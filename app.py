from os import environ

from utils.env import init_json_env
from utils.timer import get_datetime, calc_uptime
from database import Mongo

from flask import Flask, jsonify, render_template, request
from flask_restx import Api, Resource
from flask_cors import CORS
from apps.school import School
from apps.meal import Meal

# if json env file is provided, use it
mongo = Mongo()
wokeup = get_datetime()
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
api = Api(app, version="1.0", title="MealBoard API")
api.add_namespace(School, "/school")
api.add_namespace(Meal, "/meal")
# please add your namespace here
# `add_namespace(namespace, path)`


@app.route("/uptime")
def uptime():
    return {"uptime": calc_uptime(wokeup)}


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
