import falcon
import rethinkdb as r
import json
from jsonschema import validate
import datetime
from playhouse.shortcuts import model_to_dict, dict_to_model

from models import Event, Community

class Communities(object):

    def __init__(self):
        self.table_name = "communities"

    def _validate(self, data):
        schema = {
            "type":"object",
            "description": "A representation of needed info for a community",
            "items":{
                "name": {"type": "string"},
                "location": {"type": "string"},
            },
            "required":["name", "location"],
        }

        try:
            validate(data, schema)
            return True
        except:
            return False

    def add_community(self, data):
        Community.create(c_id = str(int(datetime.datetime.now().strftime("%s")) * 1000)[:7] , name=data["name"], location = data["location"]).save()

    def on_post(self, req, resp):

        raw_json = str(req.stream.read().decode('utf-8'))
        data = json.loads(raw_json)

        if self._validate(data):
            self.add_community(data)
            resp.body = "Correctly inserted\n"
            resp.status = falcon.HTTP_201
        else:
            resp.body = "Invalid data\n"
            resp.status = falcon.HTTP_422

    def on_get(self, req, resp):
        query = Community.select()
        resp.body = json.dumps({'communities':[model_to_dict(result) for result in query]})

class Event(object):

    def _validate(self, data):
        schema = {
            "type":"object",
            "items":{
                "name": {"type": "string"},
                "place": {"type": "string"},
                "date": {"type": "string", "format": "date"},
                "summary": {"type": "string"}
            },
            "required":["name", "place", "date", "summary"],
            "description": "A representation of an event"
        }


communities = Communities()
