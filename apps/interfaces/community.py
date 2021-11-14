from apps.interfaces import *


class MealWrite(FlaskForm):
    content = StringField("content", validators=[DataRequired()])
    title = StringField("title", validators=[DataRequired()])


class MealNext(FlaskForm):
    feed_id = IntegerField("_id", validators=[DataRequired()])
