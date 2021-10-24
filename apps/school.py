from flask import request, jsonify
from flask_restx import Resource, Namespace
from database.school import get_location, get_school
import json

School = Namespace("School")


@School.route("")
class SchoolList(Resource):
    """
    학교 정보를 제공하기 위한 API
    """

    def get(self):
        paramdict = request.args.to_dict()
        location = paramdict.get("location", "")
        if not location:
            return {"message": "location is required"}, 400
        school = paramdict.get("school", None)
        if not school:
            return {"message": "school is required"}, 400
        school_list = get_school(location, school)
        return {"school_list": school_list}, 200


@School.route("/location")
class SchoolLocation(Resource):
    """
    학교 위치 정보를 제공하기 위한 API
    """

    def get(self):
        get_location_list = get_location()
        return {"location": get_location_list}, 200
