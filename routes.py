from flask_restx import Api

from apps.home import Home
from apps.school import School
from apps.meal import Meal
from apps.misc import Misc
from apps.user import User

api = Api()
api.add_namespace(Home, "/home")
api.add_namespace(School, "/school")
api.add_namespace(Meal, "/meal")
api.add_namespace(Misc, "/misc")
api.add_namespace(User, "/user")
