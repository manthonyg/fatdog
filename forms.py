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
    submit = SubmitField('Submit')


# class LoginForm(FlaskForm):
#     """Contact form."""

#     name = StringField('Name', [
#         DataRequired()])
#     email = StringField('Email', [
#         Email(message='Not a valid email address.'),
#         DataRequired()])
#     body = TextAreaField('Message', [
#         DataRequired(),
#         Length(min=4, message='Your message is too short.')])
#     submit = SubmitField('Register')
