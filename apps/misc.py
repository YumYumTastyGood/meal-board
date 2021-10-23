import json
from flask_restx import Resource, Namespace
from settings import WOKEUP_TIME
from utils.timer import calc_uptime

Misc = Namespace("Misc")


@Misc.route("/uptime")
class Uptime(Resource):
    """
    학교 위치 정보를 제공하기 위한 API
    """

    def get(self):
        return {"uptime": calc_uptime(WOKEUP_TIME)}, 200
