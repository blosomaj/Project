from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField
from wtforms.validators import DataRequired
from app import User

class NewForm(FlaskForm):
    carbrand = StringField('CarBrand', validators=[DataRequired()])
    carmodel = StringField('CarModel', validators=[DataRequired()])
    submit = SubmitField('Submit')

class EditForm(FlaskForm):
    carbrand = StringField('CarBrand', validators=[DataRequired()])
    carmodel = StringField('CarModel', validators=[DataRequired()])
    submit = SubmitField('Submit')
