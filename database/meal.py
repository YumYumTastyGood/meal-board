from typing import Union
from database.interfaces.User import User
from database.interfaces.Meal import MealInfo


def update_user_meal(user_id: str, info: dict) -> bool:
    try:
        MealInfo(
            user_id=user_id,
            date=info["date"],
            region_code=info["region_code"],
            region_name=info["region_name"],
            school_code=info["school_code"],
            school_name=info["school_name"],
            meal_info=info["meal_info"],
        ).save()
    except Exception as e:
        return False
    return True


def get_user_meal(auth: str) -> dict:
    try:
        user = User.objects(auth=auth).first()
        meals = MealInfo.objects(user_id=user._id).order_by("-date").limit(10)
    except Exception as e:
        return {"message": "조회 중 오류가 발생했습니다."}, 404
    return {"message": "조회 성공", "meals": meals.to_json()}, 200
