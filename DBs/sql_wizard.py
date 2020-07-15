from Kingfish.DBs.mongodb_wizard import find_documents

def convert_json_to_table(value = None):
    sql_commands = []
    for document in find_documents(value):
        columns = ', '.join("`" + str(val).replace('/', '_') + "`" for val in document.keys())
        values = ', '.join("'" + str(val).replace('/', '_') + "'" for val in document.values())
        sql_command = f"INSERT INTO {TABLE_NAME} ({columns}) VALUES ({values});"
        sql_commands.append(sql_command)