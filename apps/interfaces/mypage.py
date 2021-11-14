from apps.interfaces import *


class NicknameValidator(FlaskForm):
    nickname = StringField("nickname", validators=[DataRequired()])


class MessageValidator(FlaskForm):
    message = StringField("message", validators=[DataRequired()])


class MealValidator(FlaskForm):
    date = StringField("date", validators=[DataRequired()])
    meal_info = StringField("meal_info", validators=[DataRequired()])
    region_name = StringField("region_name")
    region_code = StringField("region_code")
    school_code = StringField("school_code", validators=[DataRequired()])
    school_name = StringField("school_name")
