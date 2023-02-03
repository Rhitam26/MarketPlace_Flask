from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_pymongo import PyMongo
from pymongo import MongoClient
from flask_login import LoginManager

app = Flask(__name__)
app.config['MONGO_URI'] ='mongodb+srv://rhitamdeb26:margherita26@cluster0.uokqy8w.mongodb.net/?retryWrites=true&w=majority'

app.config['SECRET_KEY'] = '2f94dd86a742ef135d1f1773'

mongo = MongoClient('mongodb+srv://rhitamdeb26:margherita26@cluster0.uokqy8w.mongodb.net/?retryWrites=true&w=majority')
# mongo_app = mongo(app)

# db= SQLAlchemy(app)
from market import model
from market import routes

