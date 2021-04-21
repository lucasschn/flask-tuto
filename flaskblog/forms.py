from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                            validators=[DataRequired(), Length(min=2, max=20)]
                            )
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        """ Checks that the username is not already taken."""
        user = User.query.filter_by(username=username.data).first() # returns None if no entry is found inside the database with username column equal to username from form
        if user: # is not None
            raise ValidationError('That username is already taken. Please choose a different one.')

    def validate_email(self, email):
        """ Checks that the email is not already taken."""
        user = User.query.filter_by(email=email.data).first() # returns None if no entry is found inside the database with username column equal to username from form
        if user: # is not None
            raise ValidationError('An account already exists for that email. Please log in.')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')