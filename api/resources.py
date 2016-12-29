import falcon
import rethinkdb as r
import json

from db_client import *

class Communities(object):

    def __init__(self):
        self.table_name = TABLES[1]

    def add_community(self, data):
        print(r.db(PROJECT_DB).table_list().run(db_connection))
        r.db(PROJECT_DB).table(self.table_name).insert(data).run(db_connection)
    
    def on_post(self, req, resp):

        raw_json = str(req.stream.read().decode('utf-8'))
        result = json.loads(raw_json)
        self.add_community(result)
        
        resp.body = "Correctly inserted"
        resp.status = falcon.HTTP_201

    def on_get(self, req, resp):
        cursor = r.db(PROJECT_DB).table(self.table_name).run(db_connection)
        result = {self.table_name: [i for i in cursor]}
        resp.body = json.dumps(result)
        

communities = Communities()
