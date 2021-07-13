import pymongo
import atexit
from Kingfish.DBs.configuration import read_config
import Core.logger as logger

mongo_section = read_config()["MONGODB"]

DEFAULT_MONGODB_HOST = mongo_section["MONGODB_HOST"]
DEFAULT_MONGODB_DB_NAME = mongo_section["MONGODB_DB_NAME"]

class MongoDB:

    def __init__(self, mongodb_host=DEFAULT_MONGODB_HOST, mongodb_db_name=DEFAULT_MONGODB_DB_NAME):
        self.mongodb_host = mongodb_host
        self.mongodb_db_name = mongodb_db_name
        self.data_base = None
        self.client = None
        self.IS_CONNECTED = False
        self.collections_names = mongo_section["COLLECTIONS"]
        self.collections = []

    def connect_to_mongodb(self):
        print(f"hostname is {self.mongodb_host} and the DB name is {self.mongodb_db_name}")
        client = pymongo.MongoClient(self.mongodb_host, 27017)
        self.data_base = client[self.mongodb_db_name]
        self.IS_CONNECTED = True
        return self.data_base

    def get_collection(self):
        if not self.IS_CONNECTED:
            self.connect_to_mongodb()
        for collection in self.collections_names:
            self.collections.append(self.data_base[collection]) #cursor

    def find_documents(self, key = None, value = None):
        if not self.IS_CONNECTED:
            self.get_collection()
        if not key and not value:
            cross_collecions_documents = []
            for col in self.collections:
                arr = [document for document in col.find()]
                cross_collecions_documents.append(arr) if len(arr) > 0 else None
            print(cross_collecions_documents)
            return cross_collecions_documents
        relevant_docs = []
        for col in self.collections:
            for document in col.find():
                if value in document.values():
                    print(document)
                    relevant_docs.append(document)
                elif key in document.keys():
                    print(document)
                    relevant_docs.append(document)
        if len(relevant_docs) == 0:
            print("Didn't find relevant documents")
        return relevant_docs

    def create_document(self, **data):
        document = {}
        for key in data.keys():
            document[str(key)] = data.get(key)
        return document

    def insert_to_mongodb(self, collection_name, doc = None, **data):
        if not self.IS_CONNECTED:
            self.connect_to_mongodb()
        collection = self.data_base[collection_name]
        if doc:
            collection.insert_one(doc)
            logger.info("Inserted successfully the document")
        else:
            document = {}
            for key in data.keys():
                document[str(key)] = data.get(key)
            collection.insert_one(document)
            logger.info("Inserted successfully the dictionary")

    def find_document(self, collection_name, key, value):
        db = self.connect_to_mongodb()
        collection = db[collection_name]
        document = collection.find_one({key:value})
        print(document)
        return document

    def delete_document(self, collection_name, key, value):
        db = self.connect_to_mongodb()
        collection = db[collection_name]
        collection.delete_one({key:value})

    def edit_document(self, collection_name, key, value,
     new_key = None, new_value = None):
        document = self.find_document(collection_name, key, value)
        if new_key:
            document.pop(key)
            document[new_key] = value
            old_key = key
            key = new_key
        if new_value:
            document[key] = new_value
        self.delete_document(collection_name, old_key, value)
        self.insert_to_mongodb(collection_name, doc = document)
        logger.info("Successfully updated the document")

    def create_collection(self, collection_name):
        if not self.IS_CONNECTED:
            self.connect_to_mongodb()
        new_collection = self.data_base[collection_name]
        collections = self.data_base.list_collection_names()
        if collection_name in collections:
            logger.info(f"Successfully creted {new_collection} in {self.data_base}")
            return True
        else:
            logger.fatal(f"Created empty collection named {collection_name}")
        
    def close_session(self):
        self.client.close()
        print("Session closed")

"""
***Running examples:***

instance = MongoDB()
instance.find_documents()

"""
