from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap
app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)