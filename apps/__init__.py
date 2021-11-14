from flask import Flask
from flask_cors import CORS
from utils.env import get_database_uri
from utils.auth import generate_key
from settings import GOOGLE_LOGIN_CLIENT_ID, GOOGLE_LOGIN_CLIENT_SECRET
from flask_oauthlib.client import OAuth
from settings import *
from database import db
from . import home, mypage, misc, school, redisLab, meal, community, about


app = Flask(__name__)
app.secret_key = generate_key(16)
app.config["MONGODB_SETTINGS"] = {
    "db": DATABASES.get("name"),
    "host": get_database_uri(DATABASES),
    "port": int(DATABASES.get("port")),
    "username": DATABASES.get("username"),
    "password": DATABASES.get("password"),
}

oauth = OAuth()
google = oauth.remote_app(
    "google",
    consumer_key=GOOGLE_LOGIN_CLIENT_ID,
    consumer_secret=GOOGLE_LOGIN_CLIENT_SECRET,
    request_token_params={"scope": "email"},
    base_url="https://www.googleapis.com/oauth2/v1/",
    request_token_url=None,
    access_token_method="POST",
    access_token_url="https://accounts.google.com/o/oauth2/token",
    authorize_url="https://accounts.google.com/o/oauth2/auth",
)
db.init_app(app)


app.register_blueprint(home.home)
app.register_blueprint(about.about)
app.register_blueprint(mypage.mypage)
app.register_blueprint(school.school)
app.register_blueprint(meal.meal)
app.register_blueprint(misc.misc)
app.register_blueprint(redisLab.redis_lab)
app.register_blueprint(community.community)


CORS(app, support_credentials=True)
