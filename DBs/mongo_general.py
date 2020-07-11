import pymongo
from DBs import read_config

DEFAULT_MONGODB_HOST = read_config()["MONGODB_HOST"]
DEFAULT_MONGODB_DB_NAME = read_config()["MONGODB_DB_NAME"]

data_base = None
IS_CONNECTED = False
collections = []

def connect_to_db(mongodb_host = DEFAULT_MONGODB_HOST, mongodb_db_name = DEFAULT_MONGODB_DB_NAME):
    global data_base
    print(f"hostname is {mongodb_host} and the DB name is {mongodb_db_name}")
    client = pymongo.MongoClient(mongodb_host, 27017)
    data_base = client[mongodb_db_name]
    IS_CONNECTED = True

def get_collection():
    global collections
    if not IS_CONNECTED:
        connect_to_db()
    for collection in read_config()["COLLECTIONS"]:
        collections.append(data_base[collection])

def find_documents():
    for col in collections:
        for document in col.find():
            print(document)
    
if __name__ == '__main__':
    get_collection()
    find_documents()