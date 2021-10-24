from flask import jsonify


class User:
    def signup(self):

        user = {
            "_id": "",
            "name": "",
            "email": "",
            "profile_pic": "",
        }

        return jsonify(user), 200
