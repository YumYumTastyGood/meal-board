import json
from flask import Blueprint, render_template, url_for, session, request, redirect

home = Blueprint("home", __name__, url_prefix="/")


@home.route("/")
def get_home():
    """
    메인 화면
    """
    if session.get("google_token") is None:
        return redirect(url_for("home.get_login"))
    print(session["google_token"])
    return render_template(
        "home.html",
        hello="Greeting",
    )


@home.route("/login")
def get_login():
    from apps import google

    return google.authorize(callback=url_for("home.callback", _external=True))


@home.route("/logout")
def get_logout():
    session.pop("google_token", None)
    return redirect(url_for("home.get_home"))


@home.route("/login/callback")
def callback():
    from apps import google
    from database.user import User

    user = User()

    @google.tokengetter
    def get_google_oauth_token():
        return session.get("google_token")

    resp = google.authorized_response()
    foot_print = resp
    print(foot_print)
    if resp is None:
        return "Access denied: reason=%s error=%s" % (
            request.args["error"],
            request.args["error_description"],
        )
    session["google_token"] = (resp["access_token"], "")

    resp.get("id_token")
    user_info = google.get("userinfo")
    user.set_google_user(user_id, user_info)

    return {"data": user_info.data}


{
    "access_token": "ya29.a0ARrdaM_EBHpSb6sK2oCyzppmbX-G28SvBPdWmOVOB5xOoVPFCGwHj2BcKNv7X2Nb6eIMxdVssNcBBHilpgZjSyiBiYpqYHG0K8V33Dg-vuM_2B9DCceojpz_iIOIKbXP5LbRmS418_bHU4VV02-HUCU9UhK8",
    "expires_in": 3599,
    "scope": "https://www.googleapis.com/auth/userinfo.email openid",
    "token_type": "Bearer",
    "id_token": "eyJhbGciOiJSUzI1NiIsImtpZCI6ImJiZDJhYzdjNGM1ZWI4YWRjOGVlZmZiYzhmNWEyZGQ2Y2Y3NTQ1ZTQiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJhY2NvdW50cy5nb29nbGUuY29tIiwiYXpwIjoiMTIzNTg1NDg0MjA5LW9uazVhNzA4MWJsMHQ2aGQ4ZjdnMzRsZG52MjNkZ2c3LmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwiYXVkIjoiMTIzNTg1NDg0MjA5LW9uazVhNzA4MWJsMHQ2aGQ4ZjdnMzRsZG52MjNkZ2c3LmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwic3ViIjoiMTE1Nzc2Njg1NzUzNjAwMDgzNDg2IiwiZW1haWwiOiJhY2lkZHVzdDIwQGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJhdF9oYXNoIjoiMUdsa2Z0Ulc4T2ppemtsVDUwQVBRQSIsImlhdCI6MTYzNTQzNDkwOCwiZXhwIjoxNjM1NDM4NTA4fQ.icN9pxY5GYr1aljIqNuDLEBgpdAbG1UA9rBWq0BfUX0QsmsExwLk5qCkrwr31MbeVikj1L54z02us9RFavdP3XWZQlj4itexzFIN6omBTYBlFC-2y7afyHREGDaxs9fEHs27kZ0momuzA_lDqT0LJ8cfqiFsbSxVxoKkqtf6m7LzzRKmVRdZopuAO44TqpT1shVaAVRr7sroLIDOyeU7KjGm2nBilzPvMNCmkOr94zUsVq65FAJW4q0apfNjgiZjIAozBBBr_Cx1vuu_5y9CThgbnhGizALVVuPobKbhDqT3nReJX4Sm6bNBsRnLTaCfTVahcgXh0CeDy1q5LkWJBw",
}
