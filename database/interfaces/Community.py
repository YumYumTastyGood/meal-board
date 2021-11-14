from database import db
from datetime import datetime
from settings import DEFAULT_PROFILE_URL
from database.interfaces.User import User


class Community(db.DynamicDocument):
    _id = db.SequenceField(primary_key=True)
    user = db.ReferenceField(User, required=True)
    title = db.StringField(required=True)
    date = db.DateTimeField(default=datetime.now, required=True)
    content = db.StringField(required=True)
    image_url = db.StringField()
    like_count = db.IntField(default=0)
    like_users = db.ListField(db.StringField())

    def __repr__(self):
        # return f"<MealInfo {self.date}_{self.school_code}>"
        return f"<MealInfo {self._id}>"
