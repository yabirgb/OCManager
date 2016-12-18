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

curl -H "Authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiWVx1MDBlMWJpciIsImFkbWluIjp0cnVlfQ.xtvKyxq26b7K02mVv21vkt7PbeOUatMbgxLOHIj7CQg" http://localhost:8000/hello

curl -H "Authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiWVx1MDBlMWJpciIsImFkbWluIjp0cnVlfQ.xtvKyxq26b7K02mVv21vkt7PbeOUatMbgxLOHIj7CQg" --data '{"name":"Python Granada", "location": "Granada"}' http://localhost:8000/communities



"""
