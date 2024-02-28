from flask import Flask
from database.database import connect_to_mongodb

app = Flask(__name__)

def create_collection():
    database_name = 'treeboy'
    collection_name = 'new_users'
    db = connect_to_mongodb(database_name, collection_name)

    if collection_name not in db.database.list_collection_names():
        collection = db.database.create_collection(collection_name)
        collection.create_index([('name')], unique=True)
        collection.create_index([('profession')])
        collection.create_index([('text')])