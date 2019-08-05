from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
from flask_bootstrap import Bootstrap
app = Flask(__name__)

app.config['SECRET_KEY'] = 'd46a72d607a329542dc093c8f1edcc4f'

posts = [
    

    {
        'author': 'Hans Seyle'
        'pitch': 'He who has conquered doubt and fear will conquer failure.'
        'date_posted': 'May 9, 2019'
    }
    
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html' posts=posts)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/register")
def register():
    form = RegistrationForm
    return render_template('register.html', titile='Register' form=form)

@app.route("/login")
def login():
    form = LoginForm
    return render_template('login.html', titile='Login' form=form)

if __name__ == '__main__':
    app.run(debug=True)