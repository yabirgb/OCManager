import jwt
from settings import SECRET_KEY

def generate_token(data):
    return jwt.encode(data, SECRET_KEY, algorithm='HS256')

print(generate_token({"user":"Yábir", "admin": True}))
