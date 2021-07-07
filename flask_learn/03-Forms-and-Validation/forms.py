from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

"""
Note:

- When using these forms, we need to a `secret key` for our application. This prevent cookies modification and cross-site request forgery attacks
    - ADD THIS KEY TO `flaskblog.py`
"""

class RegistrationForm(FlaskForm):
    # create user input fields
    # where validators: used to add constraints
    username = StringField('Username',
                           validators=[DataRequired(),
                                       Length(min=2, max=20)])
    # email
    email = StringField('Email',
                        validators=[DataRequired(),
                                    Email()])

    # pw
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(),
                                                 EqualTo('password')])
    # create submit button
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    # we can either choose to login with email OR username
    # note: its ezier to forget username than email
    email = StringField('Email',
                        validators=[DataRequired(),
                                    Email()])
    # pw
    password = PasswordField('Password', validators=[DataRequired()])

    # remember: allow user to stay login after closing their browser for some time
    # this is done using a secured cookies
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
