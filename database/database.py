from pymongo.mongo_client import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

def connect_to_mongodb(collection_name):
    uri = os.environ.get('MONGODB_DATABASE_URL')
    client = MongoClient(uri)
    database_name = os.environ.get('DATABASE_NAME')
    db = client[database_name]
    collection = db[collection_name]
    return collection
