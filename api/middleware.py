import jwt
import falcon
import json
from settings import SECRET_KEY, CRYPT_ALGORITHMS


class AuthMiddleware(object):
    def process_request(self, req, resp):
        token = req.get_header('Authorization')
        challenges = ['Token error']
        method = req.method
        
        if token is None and method != "OPTIONS":
            description = ("Provide a valir token")
            print("No token")
            raise falcon.HTTPUnauthorized('Auth token required',
                                          description,
                                          challenges,
                                          href='http://docs.com')
            
        if not self._token_is_valid(token) and method != "OPTIONS":
            description = ("The provided auth token is not valid."
                           "Please request a new token and try again.")
            raise falcon.HTTPUnauthorized('Authentication required',
                                          description,
                                          challenges,
                                          href='http://docs.com/auth')

    def _token_is_valid(self, token):
        try:
            jwt.decode(token, SECRET_KEY, algorithms=CRYPT_ALGORITHMS)
            return True
        except jwt.exceptions.InvalidTokenError:
            return False
