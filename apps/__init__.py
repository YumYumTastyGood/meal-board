def create_app():
    from flask import Flask
    from flask_cors import CORS
    from utils.env import get_database_uri
    from utils.auth import generate_key, oauth, google
    from settings import GOOGLE_LOGIN_CLIENT_ID, GOOGLE_LOGIN_CLIENT_SECRET
    from flask_oauthlib.client import OAuth
    from settings import DATABASES
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

    db.init_app(app)
    CORS(app, support_credentials=True)

    app.register_blueprint(home.home)
    app.register_blueprint(about.about)
    app.register_blueprint(mypage.mypage)
    app.register_blueprint(school.school)
    app.register_blueprint(meal.meal)
    app.register_blueprint(misc.misc)
    app.register_blueprint(redisLab.redis_lab)
    app.register_blueprint(community.community)

    return app
