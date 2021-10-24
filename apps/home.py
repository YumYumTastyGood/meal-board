import json
from flask import render_template, make_response
from flask_restx import Resource, Namespace

Home = Namespace("Home")


@Home.route("")
class Index(Resource):
    """
    학교 위치 정보를 제공하기 위한 API
    """

    def get(self):
        headers = {"Content-Type": "text/html"}
        return make_response(
            render_template(
                template_name_or_list="home.html",
                hello="asdfqwer",
            ),
            200,
            headers,
        )
