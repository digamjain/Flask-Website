#render_template helps to render an html page located under templates directory
from flask import Flask, render_template

app = Flask(__name__)

#Can have multiple routes for the same page
@app.route('/')
@app.route('/home')
def homepage():
    return render_template('home.html')

#Send data to templates
@app.route('/market')
def market_page():
    items = [
    {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
    {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
    {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
    ]
    return render_template('market.html', item = items)
