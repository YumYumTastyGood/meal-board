import json
from bson import json_util
import pipes
from os import getenv, environ, path
from urllib.parse import quote_plus


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


def get_database_uri(db: dict) -> str:
    """
    get database uri
    """
    host = db.get("host")
    port = int(db.get("port"))
    collection = db.get("collection")
    user = db.get("user")
    password = quote_plus(str(db.get("password")))

    uri = f"mongodb+srv://{user}:{password}@{host}:{port}?retryWrites=true&w=majority"
    print("env.py >> ", uri)
    return uri


# mongodb+srv://mealboard:T7kflnxdY5OwnmgX@cluster0.xclq8.mongodb.net/myFirstDatabase:27017/mealboard?retryWrites=true&w=majority
