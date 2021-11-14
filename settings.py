from os import getenv, environ
from utils.env import init_json_env
from datetime import datetime

init_json_env(environ.get("ENVIRONMENT", "dev"))
WOKEUP_TIME = datetime.now()
DATABASES = {
    "host": getenv("MONGO_HOST"),
    "port": getenv("MONGO_PORT", 27017),
    "user": getenv("MONGO_USER"),
    "password": getenv("MONGO_PASSWORD"),
    "name": getenv("MONGO_NAME"),
}

REDIS = {
    "expire": int(getenv("REDIS_EXPIRE", 3600)),
    "host": getenv("REDIS_HOST", "localhost"),
    "port": getenv("REDIS_PORT", 6379),
    "password": getenv("REDIS_PASSWORD", None),
}

GOOGLE_LOGIN_CLIENT_ID = getenv("GOOGLE_CLIENT_ID")
GOOGLE_LOGIN_CLIENT_SECRET = getenv("GOOGLE_CLIENT_SECRET")

FLASK_SECRET = getenv("FLASK_SECRET")

NEIS_API_KEY = getenv("NEIS_API_KEY")
NEIS_API_URL = getenv("NEIS_SERVICE_INFO")

MESSAGES = [
    "급식 어서오고-",
    "회원가입 허싈? 어? 이미 했네?",
    "급식먹고싶은 급식- 소리질러ㅓㅓ-!",
    "비둘기야 먹자- 마시쩡? 마시쩡-!",
    "ㄹㅇ ㅋㅋ국그릇삥뽕-",
    "급식 오지고 지리고 레릿고- 레릿고-",
    "밥도둑? ㄴㄴ 밥경찰",
    "밥경찰? ㄴㄴ 대검찰청",
    "내 동생은 태권도 검은띠, 나는 앙 기모 띠?",
    "ㅇㅈ? ㅇ ㅇㅈ?",
    "선생님... 한끼라도.. 맛있는 급식이.. 먹고싶어요..",
    "'급식의 모든 것'에 오신 것을 환영합니다",
]

DEFAULT_PROFILE_URL = "/static/images/profile.png"
