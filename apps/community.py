import json
from flask import Blueprint, render_template, url_for, session, request, redirect
from database.user import set_user, get_user_by_user_id, get_user_by_user_auth
from database.community import (
    get_best_meal,
    write_new_meal,
    get_meal_list,
    get_next_meal,
)
from apps.interfaces.community import MealWrite, MealNext

community = Blueprint("community", __name__, url_prefix="/community")


@community.route("/", methods=["GET"])
def community_home():
    """
    메인 화면
    """
    best_meal = get_best_meal()
    meal_list = get_meal_list()
    return render_template("community.html", meal_list=meal_list, best_meal=best_meal)


@community.route("/next", methods=["GET"])
def community_next():
    query = MealNext(request.args, meta={"csrf": False})
    if not query.validate():
        return json.dumps({"result": "fail"}), 400, {"ContentType": "application/json"}
    _id = query.data.get("feed_id")
    success, meal = get_next_meal(_id)
    if not success:
        return json.dumps({"result": "fail"}), 404, {"ContentType": "application/json"}
    return meal.to_json(), 200, {"ContentType": "application/json"}


@community.route("/write", methods=["GET"])
def community_write_page():
    user_auth = session.get("auth")
    print(user_auth)
    if user_auth is None:
        return redirect(url_for("home.get_login"))
    user = get_user_by_user_auth(user_auth)
    if user is None:
        return redirect(url_for("home.get_login"))
    return render_template("write.html")


@community.route("/write", methods=["POST"])
def community_write():
    user_auth = session.get("auth")
    user = get_user_by_user_auth(auth=user_auth)
    if user is None:
        return redirect(url_for("home.get_login"))
    body = MealWrite(meta={"csrf": False})
    if not body.validate():
        return json.dumps({"result": "fail"}), 400, {"ContentType": "application/json"}
    title = body.data.get("title", "안녕하세요")
    content = body.data.get("content", "오늘 급식은 어땠나요?")
    image_url = body.data.get("image_url", None)
    success = write_new_meal(user, title, content, image_url)
    if not success:
        return json.dumps({"result": "fail"}), 400, {"ContentType": "application/json"}
    return json.dumps({"result": "success"}), 200, {"ContentType": "application/json"}
