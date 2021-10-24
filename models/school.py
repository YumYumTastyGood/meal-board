from models.database import mongo


def get_location() -> dict:
    result = mongo.db.location.find_one({}, {"_id": False})
    return result


def get_school(school: str) -> list:
    print("school > ", school)
    result = mongo.db.school_info.find({"school_name": school}, {"_id": False})
    return list(result)
