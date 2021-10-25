import json
from settings import WOKEUP_TIME
from utils.timer import calc_uptime
from __main__ import app


@app.route("/misc/uptime", methods=["GET"])
def get_uptime():
    return {"uptime": calc_uptime(WOKEUP_TIME)}, 200
