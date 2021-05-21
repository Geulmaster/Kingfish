import json
import os

def read_config():
    with open(os.path.join(os.getcwd(), "configuration.json"), "r") as db_config:
        credentials = json.load(db_config)
    return credentials
