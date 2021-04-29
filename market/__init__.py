#render_template helps to render an html page located under templates directory
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#Flask library for hashed bcrypt passwords
from flask_bcrypt import Bcrypt
#Flask library to manage login page
from flask_login import LoginManager

app = Flask(__name__)

"""
Creating configuration of app instance so that flask can identify its database
URI = Uniform Resource Identifier
'SQLALCHEMY_DATABASE_URI' is the key value
market.db is the name of the database
sqlite:/// is the convetion to declare the URI
"""
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'

#Initializing the SECRET_KEY for the forms to take in values from the users
app.config['SECRET_KEY'] = 'b7534db2613d0afb6c72ea05'

#Initialize the instance of SQLAlchemy class with our flask instance
db = SQLAlchemy(app)

#Initialize the instance of bcrypt class
bcrypt = Bcrypt(app)

#Initializing the instance of LoginManager class
login_manager = LoginManager(app)
#To redirect users to login page and show the in built message when they try to go to market page
login_manager.login_view = 'login_page'
login_manager.login_message_category = 'info'
from market import routes
