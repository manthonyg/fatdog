from flask_wtf import FlaskForm, RecaptchaField
from wtforms import (StringField,
                     TextAreaField,
                     SubmitField,
                     PasswordField,
                     DateField,
                     SelectField)
from wtforms.validators import (DataRequired,
                                Email,
                                EqualTo,
                                Length,
                                URL)


class RegistrationForm(FlaskForm):
    """Registration form."""
    username = StringField('Username', [
        DataRequired()])
    password = PasswordField('Password', [
        DataRequired(),
        EqualTo('confirm_password', message='Passwords must match'),
        Length(min=4, message=('Your password is too short.'))])
    confirm_password = PasswordField('Confirm Password', [
        DataRequired()])
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    """Login form."""
    username = StringField('Username', [
        DataRequired()])
    password = PasswordField('Password', [
        DataRequired()])
    submit = SubmitField('Login')
