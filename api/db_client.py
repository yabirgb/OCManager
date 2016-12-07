import os
import rethinkdb as r
from rethingdb.errors import RqlRuntimeError, RqlDriverError

RDB_HOST = 'localhost'
RDB_PORT = 28015
db_connection = r.connect(RDB_HOST,RDB_PORT)

PROJECT_DB = "communities"
TABLES = ["users", "communities"]

def dbSetup():
    try:
        r.db_create(PROJECT_DB).run(db_connection)
        print("DB setup completed!")

    except RqlRuntimeError:
        for table in TABLES:
            try:
                r.db(PROJECT_DB).table_create(table).run(db.connection)
                print("Created table: " + table)
            except:
                print(table + " already exits")


dbSetup()
            
        
