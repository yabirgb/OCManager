import falcon

class ThingResource(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = ("hello")


thing = ThingResource()
