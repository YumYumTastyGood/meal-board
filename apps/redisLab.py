import json
from flask import Blueprint, request
from database import redis
from apps.interfaces.redisLab import RedisGetValidator, RedisSetValidator

redis_lab = Blueprint("redis", __name__, url_prefix="/redis")


@redis_lab.route("/set", methods=["POST"])
def set_key():
    """
    메인 화면
    """
    message = "fail"
    body = RedisSetValidator(meta={"csrf": False})
    if body.validate():
        redis._set(body.data["key"], body.data["value"])
        message = "success"
        return {"result": message}, 200
    return {"result": message}, 400


@redis_lab.route("/get", methods=["get"])
def get_key():
    message = "fail"
    query = RedisGetValidator(request.args, meta={"csrf": False})
    if query.validate():
        message = redis._get(query.data["key"])
        return {"result": message}, 200
    return {"result": message}, 400
