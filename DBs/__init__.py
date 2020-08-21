import json

def read_config():
    with open("DBs\configuration.json", "r") as db_config:
        credentials = json.load(db_config)
    return credentials