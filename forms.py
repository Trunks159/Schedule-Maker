from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError\

class AddWorker(FlaskForm):
    first_name =  StringField('First Name', validators=[DataRequired()])
    last_name =  StringField('Last Name', validators=[DataRequired()])
    availability =  TextAreaField('Availability', validators = [Length(min=0, max=140)])
    off_days =  TextAreaField('Off Days. Dates seperated by commas: DD,MM,YYYY', validators = [Length(min=0, max=140)])
    age = StringField('Age', validators=[DataRequired()])
    competence = StringField('Competence')
    position = StringField('Position', validators=[DataRequired()])
    submit = SubmitField('Register Worker')

class EditWorker(FlaskForm):
    pass


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators= [DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
    	user = User.query.filter_by(username = username.data).first()
    	if user is not None:
    		raise ValidationError("Please use a different Username")

    def validate_email(self, email):
    	user = User.query.filter_by(email = email.data).first()
    	if user is not None:
    		raise ValidationError("Please use a different Email")

class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    about_me = TextAreaField('About me', validators = [Length(min=0, max=140)])
    submit = SubmitField('Submit')