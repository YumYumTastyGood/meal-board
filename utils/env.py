import json
from bson import json_util
import pipes
from os import getenv, environ, path


def init_json_env(env) -> None:
    """
    init env from json file
    if env not exist, pass it
    """
    try:
        secrets = path.join(path.dirname(path.dirname(__file__)), f"config.{env}.json")
        with open(secrets, "r") as json_file:
            for k, v in json.load(json_file).items():
                environ[k] = str(v)
    except FileNotFoundError:
        return None


def parse_json(data):
    return json.loads(json_util.dumps(data), encoding="utf-8")
