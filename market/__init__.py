#render_template helps to render an html page located under templates directory
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

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

from market import routes
