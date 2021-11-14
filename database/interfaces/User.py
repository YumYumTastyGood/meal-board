from database import db


class User(db.Document):
    provider = db.StringField(required=True)
    auth = db.StringField(required=True)
    _id = db.StringField(required=True)
    email = db.StringField(required=True)
    verified_email = db.BooleanField(required=True)
    picture = db.StringField()
    nickname = db.StringField()
    message = db.StringField()

    def __repr__(self):
        return "<User %r>" % self.email
