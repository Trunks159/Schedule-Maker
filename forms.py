from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, EqualTo, ValidationError
from models import User

class EditAvailability(FlaskForm):
    monday =  StringField('Monday', validators=[DataRequired()])
    tuesday =  StringField('Tuesday', validators=[DataRequired()])
    wednesday =  StringField('Wednesday', validators=[DataRequired()])
    thursday =  StringField('Thursday', validators=[DataRequired()])
    friday =  StringField('Friday', validators=[DataRequired()])
    saturday =  StringField('Saturday', validators=[DataRequired()])
    sunday =  StringField('Sunday', validators=[DataRequired()])
    submit = SubmitField('Submit')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    position = StringField('Position', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username = username.data).first()
        if user is not None:
            raise ValidationError("Please use a different Username")

#May want to add functionality that restricts multiple users with the same name

