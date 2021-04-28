from market import app
from flask import render_template
from market.model import Item

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
