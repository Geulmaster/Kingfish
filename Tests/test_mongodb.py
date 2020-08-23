from Kingfish.DBs import mongodb_wizard

def test_connections():
    mongodb_wizard.connect_to_mongodb()

def test_insertion_to_db():
    mongodb_wizard.insert_to_mongodb("users", data = "dodo", dsdsd = "dsds")
    mongodb_wizard.find_documents(value = "dodo", key = "data")

