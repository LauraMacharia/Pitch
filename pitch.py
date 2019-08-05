from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
from flask_bootstrap import Bootstrap
app = Flask(__name__)

app.config['SECRET_KEY'] = 'd46a72d607a329542dc093c8f1edcc4f'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from models import User, Post

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

if __name__ == '__main__':
    app.run(debug=True)