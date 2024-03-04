from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class MyForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    profession = StringField('profession', validators=[DataRequired()])
    text = StringField('text', validators=[DataRequired()])