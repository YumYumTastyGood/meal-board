from typing import Union, Tuple
from database.interfaces.Community import Community
from database.interfaces.User import User


def get_best_meal() -> list:
    result = list()
    try:
        result = list(Community.objects.order_by("-like_count").limit(3))
    except Exception as e:
        return []
    finally:
        return result


def get_meal_list() -> list:
    result = list()
    try:
        result = list(Community.objects.order_by("-date").limit(20))
    except Exception as e:
        return []
    finally:
        return result


def get_next_meal(id: int) -> Tuple[bool, Community]:
    try:
        # find lower than _id
        result = Community.objects(_id__lt=id).order_by("-_id").limit(3)
    except Exception as e:
        return (False, [])
    finally:
        return (True, result)


def write_new_meal(user: User, title: str, content: str, image_url=None) -> bool:
    try:
        user = user.save()
        Community.objects.create(
            user=user.to_dbref(),
            title=title,
            content=content,
            image_url=image_url,
        )
        return True
    except Exception as e:
        print(e)
        # if you wanna check error, please import Sentry or other error report SDK
        # just print error is okay, but do not use print in production
        return False
