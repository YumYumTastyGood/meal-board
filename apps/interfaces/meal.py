from apps.interfaces import *


class NeisMealValidator(FlaskForm):
    begin = StringField("begin", validators=[DataRequired()])
    end = StringField("end", validators=[DataRequired()])
    region_code = StringField("region_code", validators=[DataRequired()])
    school_code = StringField("school_code", validators=[DataRequired()])
