from .models import Token
from rest_framework.authentication import TokenAuthentication

class NewTokenAuthentication(TokenAuthentication):
    model = Token
