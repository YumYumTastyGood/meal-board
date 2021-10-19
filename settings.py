from os import getenv, environ
from utils.env import init_json_env

init_json_env(environ.get("MEALS_ENVIRONMENT", "dev"))
DATABASES = {
    "host": getenv("MEALS_MONGO_HOST"),
    "port": getenv("MEALS_MONGO_PORT", 27017),
    "user": getenv("MEALS_MONGO_USER"),
    "password": getenv("MEALS_MONGO_PASSWORD"),
    "collection": getenv("MEALS_MONGO_COLLECTION", "mealboard"),
}

NEIS_API_KEY = getenv("MEALS_NEIS_API_KEY")
NEIS_API_URL = getenv("MEALS_NEIS_SERVICE_INFO")
