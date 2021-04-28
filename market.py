#render_template helps to render an html page located under templates directory
from flask import Flask, render_template
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
#Initialize the instance of SQLAlchemy class with our flask instance
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer(),primary_key = True)
    name = db.Column(db.String(length = 30),nullable = False, unique = True)
    price = db.Column(db.Integer(), nullable = False)
    barcode = db.Column(db.String(length = 12), nullable = False, unique = True)
    description = db.Column(db.String(length = 1024), nullable = False, unique = True)

    #To get the string representation of the database
    ##Returns the name of the item
    def __repr__(self):
        return(f'Item: {self.name}')

#Can have multiple routes for the same page
@app.route('/')
@app.route('/home')
def homepage():
    return render_template('home.html')

#Send data to templates
@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('market.html', item = items)
