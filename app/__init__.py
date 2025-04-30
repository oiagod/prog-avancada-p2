from config import Config
from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.config.from_object(Config)

CORS(app, resources={r'/*': {'origins': '*'}})

app.config["MONGO_URI"] = "mongodb+srv://iagodoarte2009:KXqiK9fSzJikm9Lc@cluster0.snje5la.mongodb.net/nome_do_banco?retryWrites=true&w=majority"
mongo = PyMongo(app)
db = mongo.db

from app import routes
