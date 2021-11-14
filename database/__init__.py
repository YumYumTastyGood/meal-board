from settings import REDIS
from flask_mongoengine import MongoEngine
from database.redis import RedisDb

db = MongoEngine()
redis = RedisDb(
    REDIS.get("host", "localhost"), REDIS.get("port", 6379), REDIS.get("password", None)
)
