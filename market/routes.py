from market import app,db
from flask import render_template, redirect, url_for, flash
from market.model import Item, User
from market.forms import RegisterForm, LoginForm
from flask_login import login_user,logout_user, login_required

#Can have multiple routes for the same page
@app.route('/')
@app.route('/home')
def homepage():
    return render_template('home.html')

#Send data to templates
@app.route('/market')
@login_required
def market_page():
    items = Item.query.all()
    return render_template('market.html', item = items)

#Registration page
#POST method was specified as the form will pot user data to the server back
@app.route('/register',methods = ['GET','POST'])
def register_page():
    form = RegisterForm()
    #Validate the forms for requirements
    if form.validate_on_submit():
        user_to_create = User(username = form.username.data,
                                email = form.email_address.data,
                                password = form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        flash(f'Account created successfully',category='success')
        return redirect(url_for('market_page'))
        #To check for errors
        #form.error is an dictionary
    if form.errors != {}:
        #Iterating over dictionary values
        for k,v in form.errors.items():
            #Printing error on the server side
            flash(str(str(k)+' '+str(v[0]).lower()).replace('_',' ').replace('password1','password').replace('password2','confirm password').capitalize(),category = 'danger')
    return render_template('register.html', form = form)

#Login page
@app.route('/login',methods = ["GET","POST"])
def login_page():
    form = LoginForm()
    #Validate the forms for requirements
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
            login_user(attempted_user)
            flash(f'Login successful as {attempted_user.username}',category='success')
            return redirect(url_for('market_page'))
        else:
            flash('Login failed! Incorrect User Name or Password',category='danger')
    return render_template('login.html', form = form)

#Logout Page
@app.route('/logout')
def logout_page():
    logout_user()
    flash('Successfully logged out',category = 'info')
    return redirect(url_for('login_page'))
