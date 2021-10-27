from flask import Blueprint, request, jsonify
import json

school = Blueprint("school", __name__, url_prefix="/school")


@school.route("/", methods=["GET"])
def get_school_info():
    """
    학교 정보를 제공하기 위한 API
    """
    from database.school import get_school

    paramdict = request.args.to_dict()
    location = paramdict.get("location", "")
    if not location:
        return {"message": "location is required"}, 400
    school = paramdict.get("school", None)
    if not school:
        return {"message": "school is required"}, 400
    school_list = get_school(location, school)
    return {"school_list": school_list}, 200


@school.route("/location", methods=["GET"])
def get_location_info():
    """
    학교 위치 정보를 제공하기 위한 API
    """
    from database.school import get_location

    get_location_list = get_location()
    return {"location": get_location_list}, 200
