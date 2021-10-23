from database import Mongo
from flask import request, jsonify
from flask_restx import Resource, Api, Namespace
import json

mongo = Mongo()
School = Namespace("School")


@School.route("")
class SchoolList(Resource):
    """
    학교 정보를 제공하기 위한 API
    """

    def get(self):
        paramdict = request.args.to_dict()
        location = paramdict.get("location", "")
        print(location)
        if not location:
            return {"message": "location is required"}, 400
        school = paramdict.get("school", None)
        if not school:
            return {"message": "school is required"}, 400
        # result = mongo.db.school_info.find({"school_name": school}, {"_id": False})
        result = mongo.db.school_info.find(
            {
                "$and": [
                    {"region_code": location},
                    {"school_name": {"$regex": f".*{school}.*"}},
                ]
            },
            {"_id": False},
        )
        return {"school_list": list(result)}, 200


@School.route("/location")
class SchoolLocation(Resource):
    """
    학교 위치 정보를 제공하기 위한 API
    """

    def get(self):
        result = mongo.db.location.find_one({}, {"_id": False})
        return {"location": result}, 200
