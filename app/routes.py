from flask import Flask, render_template, url_for, flash, redirect
from pitch import app
from pitch.forms import RegistrationForm, LoginForm
from pitch.models import User, Post

posts = [
    

    {
        'author': 'Hans Seyle',
        'title' : 'Quote',
        'content': 'He who has conquered doubt and fear will conquer failure.',
        'date_posted': 'May 9, 2019'
    }
    
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts = posts)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/register", methods = ['GET', 'POST'] )
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'primary')
        return redirect(url_for('home'))
    return render_template('register.html', titile='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for('home'))    
    return render_template('login.html', title='Login', form=form)