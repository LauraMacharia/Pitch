from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = 'd46a72d607a329542dc093c8f1edcc4f'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)