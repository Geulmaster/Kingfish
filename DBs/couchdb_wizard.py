import couchdb
from Kingfish.DBs.configuration import read_config

class CouchDB:

    def __init__(self, host, username, password, db_name = None):
        self.couch = couchdb.Server(f"http://{username}:{password}@{host}:5984/")
        self.db = self.couch[db_name]
        print(self.db)

    def create_document(self, document:dict, db_name = None):
        if not self.db:
            self.db = db_name
        self.db.save(document)

    def update_document(self, doc_id, document, db_name = None):
        if not self.db:
            self.db = db_name
        new_doc = self.db.get(doc_id)
        for key in document.keys():
            new_doc[key] = document[key]
        new_doc = self.db.save(new_doc)
        print(f"{new_doc} successfully saved")

    def create_db(self, db_name = None):
        self.db = self.couch.create(db_name)
        return True

    def delete_document(self, document, db_name = None):
        if not self.db:
            self.db = db_name
        self.db.delete(document)

    def get_document(self, key, value, db_name = None):
        if not self.db:
            self.db = db_name
        document_list = self.db.find({"selector": {key:value}})
        print(document_list[0])
        return document_list[0]

    def get_documents(self, key, value, db_name = None):
        if not self.db:
            self.db = db_name
        docs_list = []
        for document in self.db.find({'selector': {key:value}}):
            docs_list.append(document)
        print(docs_list)
        return docs_list


if __name__ == "__main__":
    credentials = read_config()["COUCHDB"]
    couch_instance = CouchDB(credentials["HOST"], credentials["USERNAME"], credentials["PASSWORD"], db_name = "non_part")
