from models.database import mongo


def get_location() -> dict:
    result = mongo.db.location.find_one({}, {"_id": False})
    return result


def get_school(location: str, school: str) -> list:
    result = mongo.db.school_info.find(
        {
            "$and": [
                {"region_code": location},
                {"school_name": {"$regex": f".*{school}.*"}},
            ]
        },
        {"_id": False},
    )
    return list(result)
