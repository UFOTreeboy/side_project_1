from flask import Flask
from database.database import connect_to_mongodb

app = Flask(__name__)

def create_collection():
    database_name = 'treeboy'
    collection_name = 'new_users'
    data_collection = connect_to_mongodb(database_name, collection_name)

    if collection_name not in data_collection.database.list_collection_names():
        collection = data_collection.database.create_collection(collection_name)
        collection.create_index([('name')], unique=True)
        collection.create_index([('profession')])
        collection.create_index([('text')])