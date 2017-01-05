import os
import json

PRODUCTION = False
SECRET_KEY = ""
CRYPT_ALGORITHMS = ['HS256']

if PRODUCTION:
    secrets = os.path.join(os.path.abspath(__file__), "keys.json")
else:
    secrets = os.path.join(os.path.abspath(__file__), "keys_dev.json")



with open("keys_dev.json", "r") as f:
    data = f.read()
    secrets = json.loads(data)
    SECRET_KEY = secrets[0]["secret"]
