from apps.interfaces import *


class SchoolValidator(FlaskForm):
    location = StringField("Location", validators=[DataRequired()])
    school_name = StringField("School", validators=[DataRequired()])
