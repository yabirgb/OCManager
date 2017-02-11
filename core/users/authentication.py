from rest_framework import parsers, renderers
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Token

class AuthTokenSerializer(serializers.Serializer):
    username = serializers.CharField(label=_("Username"))
    password = serializers.CharField(label=_("Password"), style={'input_type': 'password'})
    device = serializers.CharField(label=_("Device"))

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        device = attrs.get('device')

        if username and password:
            print("validating")
            user = authenticate(username=username, password=password)

            if user:
                # From Django 1.10 onwards the `authenticate` call simply
                # returns `None` for is_active=False users.
                # (Assuming the default `ModelBackend` authentication backend.)
                if not user.is_active:
                    msg = _('User account is disabled.')
                    raise serializers.ValidationError(msg, code='authorization')
            else:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        data = {"user": username, "name":device}

        return data


class ObtainAuthToken(APIView):
    authentication_classes = ()
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenSerializer


    def post(self, request, *args, **kwargs):
        print("obtain")
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        device = serializer.validated_data['name']

        user_object = User.objects.get(username = user)
        token, created = Token.objects.get_or_create(user=user_object, name=device)
        return Response({'token': token.key})


obtain_auth_token = ObtainAuthToken.as_view()
