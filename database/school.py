from apps import mongo

mealboard = mongo.db.client.get_database("mealboard")


def get_location() -> dict:
    result = mealboard.location.find_one({}, {"_id": False})
    return result


def get_school(location: str, school: str) -> list:
    result = mealboard.school_info.find(
        {
            "$and": [
                {"region_code": location},
                {"school_name": {"$regex": f".*{school}.*"}},
            ]
        },
        {"_id": False},
    )
    return list(result)
