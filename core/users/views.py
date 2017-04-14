import json

from django.shortcuts import render
from django.contrib.auth.models import User


from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework import authentication, permissions

from users.serializers import UserSerializer, ProfileSerializer
from users.models import CustomUser, Token

from .permissions import IsAdminOrPost



class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CustomUser.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = 'user__username'
    permission_classes = (IsAdminOrPost, )

    def create(self, request):
        user_serializer = UserSerializer(data = request.data)
        if user_serializer.is_valid():
            user_obj = user_serializer.save()
            #We create a user object using the given data
            prof_serializer = ProfileSerializer(data = request.data)
            #Then create a Profile for that user
            if prof_serializer.is_valid():
                prof_serializer.save()
                token = Token.objects.get(user=user_obj).key
                res = json.dumps({"token": token})
                return Response(res, status=status.HTTP_201_CREATED)
            else:
                return Response(prof_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
