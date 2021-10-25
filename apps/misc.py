import json
from settings import WOKEUP_TIME
from utils.timer import calc_uptime
from flask import Blueprint

misc = Blueprint("misc", __name__, url_prefix="/misc")


@misc.route("/uptime", methods=["GET"])
def get_uptime():
    return {"uptime": calc_uptime(WOKEUP_TIME)}, 200
