import pymongo
from DBs import read_config

mongo_section = read_config()["MONGODB"]

DEFAULT_MONGODB_HOST = mongo_section["MONGODB_HOST"]
DEFAULT_MONGODB_DB_NAME = mongo_section["MONGODB_DB_NAME"]

data_base = None
IS_CONNECTED = False
collections = []

def connect_to_mongodb(mongodb_host = DEFAULT_MONGODB_HOST, mongodb_db_name = DEFAULT_MONGODB_DB_NAME):
    global data_base
    print(f"hostname is {mongodb_host} and the DB name is {mongodb_db_name}")
    client = pymongo.MongoClient(mongodb_host, 27017)
    data_base = client[mongodb_db_name]
    IS_CONNECTED = True
    return IS_CONNECTED

def get_collection():
    global collections
    if not IS_CONNECTED:
        connect_to_mongodb()
    for collection in mongo_section["COLLECTIONS"]:
        collections.append(data_base[collection])

def find_documents(value = None):
    relevant_docs = []
    for col in collections:
        for document in col.find():
            if value in document.values():
                print(document)
                relevant_docs.append(document)
    return relevant_docs
    
if __name__ == '__main__':
    get_collection()
    find_documents()