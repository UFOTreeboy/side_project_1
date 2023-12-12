from pymongo.mongo_client import MongoClient

def connect_to_mongodb(database_name, collection_name):
    uri = f"mongodb+srv://BoJun:Pekorachen01234@cluster0.p28cofs.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(uri)
    db = client[database_name]
    collection = db[collection_name]
    return collection