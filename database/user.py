from typing import Union
from database.interfaces.User import User
from utils.auth import generate_key
from settings import MESSAGES
from random import choice


def set_user(provider: str, info: dict) -> bool:
    # provider like google, facebook, kakao.. etc..
    auth = generate_key(64)
    user = User(
        provider=provider,
        auth=auth,
        _id=info["id"],
        email=info["email"],
        verified_email=info["verified_email"],
        picture=info["picture"],
        nickname=info["email"].split("@")[0],
        message=choice(MESSAGES),
    )
    user.save()
    return auth


def get_user_by_user_id(provider: str, user_id: str) -> Union[dict, None]:
    try:
        result = User.objects.get(provider=provider, _id=user_id)
        return result
    except User.DoesNotExist:
        return None


def get_user_by_user_auth(auth: str) -> Union[dict, None]:
    try:
        result = User.objects(auth=auth)[0]
        return result
    except User.DoesNotExist:
        return None


def get_users_by_email(email: str) -> list:
    result = User.objects(email__regex=f".*{email}.*")
    return result


def get_users_by_name_with_email(name: str, email: str) -> list:
    result = User.objects(name=name, email__regex=f".*{email}.*")
    return result


def update_user_nickname(auth: str, nickname: str) -> bool:
    try:
        result = User.objects(auth=auth).update(nickname=nickname)
        return True
    except User.DoesNotExist:
        return False


def update_user_message(auth: str, message: str) -> bool:
    try:
        result = User.objects(auth=auth).update(message=message)
        print(auth, message)
        return True
    except User.DoesNotExist:
        return False


# def update_meal_info(auth: str, meal_info: dict) -> bool:
#     try:
#         result = User.objects(auth=auth).update(meal_info=meal_info)
#         return True
#     except User.DoesNotExist:
#         return False

# def get_meal_info(auth: str) -> dict:
#     try:
#         result = User.objects(auth=auth).get()
#         return result.meal_info
#     except User.DoesNotExist:
#         return {}
