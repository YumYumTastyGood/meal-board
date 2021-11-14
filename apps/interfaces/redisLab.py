from apps.interfaces import *


class RedisGetValidator(FlaskForm):
    key = StringField("key", validators=[DataRequired()])


class RedisSetValidator(FlaskForm):
    key = StringField("key", validators=[DataRequired()])
    value = StringField("value", validators=[DataRequired()])
