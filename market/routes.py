from market import app
from flask import render_template
from market.model import Item
from market.forms import RegisterForm

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

#Registration page
@app.route('/register')
def register_page():
    form = RegisterForm()
    return render_template('register.html', form = form)
