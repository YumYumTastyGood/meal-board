import json
from flask import render_template, make_response, request
from flask_restx import Resource, Namespace

Board = Namespace("Board")


@Board.route("/post")
class BoardRoot(Resource):
    """
    급식판: 유저 참여형
    게시물 정보 조회
    """

    def get(self):
        return {"test": "get hello"}

    def post(self):

        # -- request
        formdata = request.form
        files = request.files

        response = {k: v for k, v in formdata.items()}
        response.update({k: v.filename for k, v in files.items()})

        # TODO: DB에 게시물 정보 저장

        # -- response
        print(f"response: {response}")
        return response
