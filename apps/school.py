from flask import request
from flask_restx import Resource, Api, Namespace

School = Namespace("School")


@School.route("")
class SchoolList(Resource):
    """
    학교 정보를 제공하기 위한 API
    """

    def get(self):
        return {"hello": "world"}


@School.route("/location")
class SchoolLocation(Resource):
    """
    학교 위치 정보를 제공하기 위한 API
    """

    def get(self):
        return {"what": "the"}
