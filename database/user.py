from os import urandom
from apps import mongo
import jwt


class User:
    def __init__(self, db_name="user"):
        self.secret = urandom(16)
        self.db = mongo.db.client.get_database(db_name)

    def generate_token(payload: str, secret_key="secret", algorithm="HS256"):
        return jwt.encode(payload, secret_key, algorithm)

    def decode_jwt(encoded_jwt: str, secret_key="secret", algorithms=["HS256"]):
        return jwt.decode(encoded_jwt, secret_key, algorithms=algorithms)

    def get_google_user(self, user_id: str) -> dict:
        result = self.db.google.find_one({"user_id": user_id}, {"_id": False})
        return result

    def set_google_user(self, user_id: str, user_info: dict) -> bool:
        try:
            self.db.google.update_one(
                {"user_id": user_id}, {"$set": user_info}, upsert=True
            )
            return True
        except Exception as e:
            return False
