from database import db
from datetime import datetime


class MealInfo(db.DynamicDocument):
    user_id = db.StringField(required=True)
    date: db.StringField(required=True)
    region_code: db.StringField()
    school_code: db.StringField(required=True)
    school_name: db.StringField()
    meal_info: db.ListField(required=True)
    created_at: db.DateTimeField(default=datetime.utcnow)

    def __repr__(self):
        # return f"<MealInfo {self.date}_{self.school_code}>"
        return f"<MealInfo {self.user_id}_{self.date}_{self.school_code}>"
