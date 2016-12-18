import falcon
from wsgiref import simple_server


from middleware import AuthMiddleware
from router import populate_routes

app = falcon.API(middleware=[
    AuthMiddleware(),
])

populate_routes(app)

"""
Arrancar con: gunicorn app:app
Ejemplo de llamada:

curl -H "Authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXNzd29yZCI6Im11Y2ggd293In0.oINalNkcc2bjo3wv_tnCyufvyTBCY6Y0wr9sQ25qacE" http://localhost:8000/hello
"""
