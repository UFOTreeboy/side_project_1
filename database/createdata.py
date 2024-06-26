from flask import Flask
from database.database import connect_to_mongodb

app = Flask(__name__)

def create_collection():
    
    collection_name = 'new_users'
    db = connect_to_mongodb(collection_name)

    if collection_name not in db.database.list_collection_names():
        collection = db.database.create_collection(collection_name)
        collection.create_index([('profession')])
        collection.create_index([('text')])