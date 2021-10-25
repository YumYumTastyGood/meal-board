from flask import request, jsonify
from database.school import get_location, get_school
import json
from __main__ import app


@app.route("/school", methods=["GET"])
def get_school_info():
    """
    학교 정보를 제공하기 위한 API
    """
    paramdict = request.args.to_dict()
    location = paramdict.get("location", "")
    if not location:
        return {"message": "location is required"}, 400
    school = paramdict.get("school", None)
    if not school:
        return {"message": "school is required"}, 400
    school_list = get_school(location, school)
    return {"school_list": school_list}, 200


@app.route("/school/location", methods=["GET"])
def get_location_info():
    """
    학교 위치 정보를 제공하기 위한 API
    """
    get_location_list = get_location()
    return {"location": get_location_list}, 200
