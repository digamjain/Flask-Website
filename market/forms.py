#Flask package to create form
from flask_wtf import FlaskForm
#Special Fields
from wtforms import StringField, PasswordField, SubmitField
#Flask validation package
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from market.model import User

class RegisterForm(FlaskForm):
    """
    The name of the functions starting with validate_ are autochecked by the FlaskForm class and the next field (username in this case) is checked by the FlaskForm for the declared fields and the function is automatically executed without even calling it in the project.
    This name is kind of a convention to FlaskForm
    """
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('already exists.')

    def validate_email_address(self, email_to_check):
        email_address = User.query.filter_by(email=email_to_check.data).first()
        if email_address:
            raise ValidationError('already exists.')
    username = StringField(label = 'User Name', validators = [Length(min=3,max=24), DataRequired()])
    email_address = StringField(label = 'Email Address:',validators = [Email(), DataRequired()])
    password1 = PasswordField(label = 'Password', validators = [Length(min=6), DataRequired()])
    password2 = PasswordField(label = 'Confirm Password',validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label = 'Create Account')

class LoginForm(FlaskForm):
    username = StringField(label = 'User Name', validators = [DataRequired()])
    password = PasswordField(label = 'Password', validators = [DataRequired()])
    submit = SubmitField(label = 'Login')

class PurchaseItemForm(FlaskForm):
    submit = SubmitField(label = 'Purchase Item')

class SellItemForm(FlaskForm):
    submit = SubmitField(label = 'Sell Item')
