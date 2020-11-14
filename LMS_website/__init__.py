from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.debug = True
app.secret_key = '9a7c444be3c173a8ffd3fe77b52d2ecf'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

from LMS_website import routes