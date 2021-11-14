import json
from flask import Blueprint, render_template, url_for, session, request, redirect
from apps.interfaces.mypage import NicknameValidator, MessageValidator, MealValidator
from database.user import *
from database.meal import *
from utils.timer import get_yyyymmdd_str

mypage = Blueprint("mypage", __name__, url_prefix="/mypage")


@mypage.route("/", methods=["GET"])
def get_mypage():
    """
    마이페이지
    """
    user = None
    if "auth" not in session:
        session.pop("auth")
        return redirect(url_for("home.get_login"))
    user = get_user_by_user_auth(auth=session["auth"])
    if not user:
        session.pop("auth")
        return redirect(url_for("home.get_login"))
    # TODO: Use WTF to validate userinfo for response
    return render_template(
        "mypage.html",
        auth=True,
        user={
            "_id": user._id,
            "email": user.email,
            "picture": user.picture,
            "nickname": user.nickname,
            "message": user.message,
        },
    )


@mypage.route("/name", methods=["POST"])
def modify_mypage_name():
    """
    마이페이지 이름 수정
    """
    if "auth" not in session:
        return json.dumps({"status": "fail"}), 403
    user = get_user_by_user_auth(auth=session["auth"])
    if not user:
        return json.dumps({"status": "fail"}), 403
    body = NicknameValidator(meta={"csrf": False})
    if body.validate():
        nickname = body.data["nickname"]
        success = update_user_nickname(session.get("auth"), nickname)
        if success:
            return json.dumps({"status": "success"}), 200
    return json.dumps({"status": "fail"}), 403


@mypage.route("/message", methods=["POST"])
def modify_mypage_message():
    """
    마이페이지 이름 수정
    """
    if "auth" not in session:
        session.pop("auth")
        return json.dumps({"status": "fail"}), 403

    user = get_user_by_user_auth(auth=session["auth"])
    if not user:
        return json.dumps({"status": "fail"}), 403
    body = MessageValidator(meta={"csrf": False})
    if body.validate():
        message = body.data["message"]
        success = update_user_message(session.get("auth"), message)
        if success:
            return json.dumps({"status": "success"}), 200
    return json.dumps({"status": "fail"}), 403


@mypage.route("/meal", methods=["POST"])
def new_meal():
    """
    마이페이지 식단 추가
    """

    if "auth" not in session:
        return json.dumps({"status": "fail"}), 403
    user = get_user_by_user_auth(auth=session["auth"])
    if not user:
        session.pop("auth")
        return json.dumps({"status": "fail"}), 403

    body = MealValidator(meta={"csrf": False})
    success = False
    if body.validate():
        data = {
            "date": body.data.get("date", get_yyyymmdd_str()),
            "region_code": body.data.get("region_code", ""),
            "region_name": body.data.get("region_name", ""),
            "school_code": body.data.get("school_code"),
            "school_name": body.data.get("school_name"),
            "meal_info": body.data.get("meal_info", "").split(","),
        }
        success = update_user_meal(user._id, data)

    if not success:
        return json.dumps({"status": "fail"}), 403
    return json.dumps({"status": "success"}), 200


@mypage.route("/meal", methods=["GET"])
def new_my_meal():
    """
    마이페이지 식단 추가
    """
    if "auth" not in session:
        return json.dumps({"message": "please login"}), 403
    data, status_code = get_user_meal(auth=session["auth"])
    return data, status_code
