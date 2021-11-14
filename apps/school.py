from flask import Blueprint, request, jsonify
from apps.interfaces.school import SchoolValidator
from database.school import get_school_list, get_location_list
import json

school = Blueprint("school", __name__, url_prefix="/school")


@school.route("/", methods=["GET"])
def get_school_info():
    """
    학교 정보를 제공하기 위한 API
    """

    query = SchoolValidator(request.args, meta={"csrf": False})
    if not query.validate():
        return jsonify(query.errors), 400
    location = query.data.get("location")
    school_name = query.data.get("school_name")
    data = get_school_list(location, school_name)
    return {"school_list": data}, 200


@school.route("/location", methods=["GET"])
def get_location_info():
    """
    학교 위치 정보를 제공하기 위한 API
    """
    locations = get_location_list()
    return {"location": locations}, 200
