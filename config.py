from flask import Flask
import pymongo

def create_app():
    app = Flask(__name__)
    app.secret_key = 'dcnv12345'

    client = pymongo.MongoClient('localhost', 27017)
    db = client['auth_db'] # nama database
    app.config['db'] = db

    return app
