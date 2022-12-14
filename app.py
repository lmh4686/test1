from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#protocol+adoptor://user:password@localIPaddress:port/name_of_database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://trello_dev:password123@127.0.0.1:5432/trello'

db = SQLAlchemy(app)

print(db)

@app.route('/')
def index():
    return "Hello World!"
