#Flask package to create form
from flask_wtf import FlaskForm
#Special Fields
from wtforms import StringField, PasswordField, SubmitField
#Flask validation package
from wtforms.validators import Length, EqualTo, Email, DataRequired

class RegisterForm(FlaskForm):
    username = StringField(label = 'User Name', validators = [Length(min=3,max=24), DataRequired()])
    email_address = StringField(label = 'Email Address:',validators = [Email(), DataRequired()])
    password1 = PasswordField(label = 'Password', validators = [Length(min=6), DataRequired()])
    password2 = PasswordField(label = 'Confirm Password',validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label = 'Create Account')
