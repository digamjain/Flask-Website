#render_template helps to render an html page located under templates directory
from flask import Flask, render_template

app = Flask(__name__)

#Can have multiple routes for the same page
@app.route('/')
@app.route('/home')
def homepage():
    return render_template('home.html')
