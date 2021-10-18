from flask import request
from flask_restx import Resource, Api, Namespace

Meal = Namespace("Meal")


@Meal.route("")
class MealInfo(Resource):
    """
    급식정보를 제공하기위한 API
    """

    def get(self):
        paramdict = request.args.to_dict()
        print(paramdict)
        return {"hello": "meal"}
