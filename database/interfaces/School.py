from database import db


class SchoolInfo(db.DynamicDocument):
    region_code = db.StringField(required=True)
    school_name = db.StringField(required=True)
    school_code = db.StringField(required=True)
    school_estabilish = db.IntField(required=True)

    def __repr__(self):
        return "<School %r>" % self.school_name


class Location(db.Document):
    B10 = db.StringField(required=True)
    C10 = db.StringField(required=True)
    D10 = db.StringField(required=True)
    E10 = db.StringField(required=True)
    F10 = db.StringField(required=True)
    G10 = db.StringField(required=True)
    H10 = db.StringField(required=True)
    I10 = db.StringField(required=True)
    J10 = db.StringField(required=True)
    K10 = db.StringField(required=True)
    M10 = db.StringField(required=True)
    N10 = db.StringField(required=True)
    P10 = db.StringField(required=True)
    Q10 = db.StringField(required=True)
    R10 = db.StringField(required=True)
    S10 = db.StringField(required=True)
    T10 = db.StringField(required=True)
    V10 = db.StringField(required=True)

    def __repr__(self):
        return "<Location list>"
