from pymongo.mongo_client import MongoClient
import os

def connect_to_mongodb(database_name, collection_name):
    uri = os.environ.get('MONGODB_DATABASE_URL')
    client = MongoClient(uri)
    db = client[database_name]
    collection = db[collection_name]
    return collection
