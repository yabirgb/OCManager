from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import authentication, permissions

from users.serializers import UserSerializer
from users.models import CustomUser

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'user__username'
