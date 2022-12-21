from flask import Blueprint, render_template, redirect, url_for, session, request

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, EmailField
from wtforms.validators import DataRequired, Length, Email, ValidationError, InputRequired, Optional
from wtforms import validators

from password_validator import PasswordValidator

from functools import wraps

import authentication.services as services
import adapters.repository as repo

authentication_blueprint = Blueprint(
    'authentication_bp', __name__, url_prefix='/authentication')

@authentication_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    user_name_not_unique = None

    if request.method == 'POST' and form.validate_on_submit():
        try:
            services.add_user(form.username.data, form.email.data, form.age.data, form.password.data, repo.repo_instance)
            # All is well, redirect the user to the login page.
            return redirect(url_for('authentication_bp.login'))
        except services.NameNotUniqueException:
            user_name_not_unique = 'Your user name is already taken - please supply another'

    return render_template('register.html',
                           user_name_error_message=user_name_not_unique,
                           email_error_message=None,
                           password_error_message=None,
                           form=form)

@authentication_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    user_name_not_found = None
    password_does_not_match = None
    
    return render_template('login.html', handler_url='/',
                           user_name_error_message=None,
                           email_error_message=None,
                           age_error_message=None,
                           form=form)

class PasswordValid:
    def __init__(self, message=None):
        if not message:
            message = u'Your password must be at least 8 characters, and contain an upper case letter,\
            a lower case letter and a digit'
        self.message = message

    def __call__(self, form, field):
        schema = PasswordValidator()
        schema \
            .min(8) \
            .has().uppercase() \
            .has().lowercase() \
            .has().digits()
        if not schema.validate(field.data):
            raise ValidationError(self.message)


class RegistrationForm(FlaskForm):
    username = StringField('Name', validators=[
        InputRequired(message='Your user name is required'),
        Length(min=3, max=30, message='Your user name is too short')])
    email = EmailField('Email', validators=[
        InputRequired(message='Your email is required')
    ])
    age = IntegerField('Age', validators=[
        Optional(),
        validators.number_range(min=1, max=100)
    ])
    password = PasswordField('Password', validators=[
        InputRequired(message='Your password is required'),
        Length(min=8, message='Your password is too short'),
        PasswordValid()])
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[
        InputRequired(message='Your username is needed'), Length(min=3, max=30)])
    password = PasswordField('Password', validators=[
        InputRequired(message='Your password is needed'), Length(min=8, max=50)])
    remember_btn = BooleanField('Remember me?')
    submit = SubmitField('Login')