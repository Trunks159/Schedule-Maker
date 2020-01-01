from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from models import User, Worker

class AddWorker(FlaskForm):
    first_name =  StringField('First Name', validators=[DataRequired()])
    last_name =  StringField('Last Name', validators=[DataRequired()])
    off_days =  TextAreaField('Off Days. Dates seperated by commas: DD,MM,YYYY', validators = [Length(min=0, max=140)])
    level = StringField('Level', validators=[DataRequired()])
    submit = SubmitField('Submit')

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
    name = StringField('Full Name', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username = username.data).first()
        if user is not None:
            raise ValidationError("Please use a different Username")

    def validate_name(self, name):
        name = name.data.replace(' ', '').lower()
        workers = Worker.query.all()
        flag = False
        for worker in workers:
            if (worker.first_name + worker.last_name) == name:
                flag = True
                if worker.user.first():
                    raise ValidationError('This worker already has a user')
        if flag == False:
            raise ValidationError('Name was not found among registered workers')

class AddSchedule(FlaskForm):
    date =  StringField('Enter Date', validators=[DataRequired()])
    submit = SubmitField('Submit')
   # RegistrationForm().validate_name('Bob')
