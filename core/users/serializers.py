from collections import OrderedDict

from rest_framework import serializers

from .models import CustomUser
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("username", "email", "password")

    def create(self, validated_data, **kwargs):
        print(validated_data, **kwargs)
        # create user
        user = User(
            username=validated_data['username'],
            email = validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        # create profile

        return user


class ProfileSerializer(serializers.ModelSerializer):

    PUBLIC_FIELDS = ('uid')

    username = serializers.CharField(source='user.username')
    email = serializers.CharField(source='user.email')

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'public', 'following', 'uid', 'user', 'name')


    def to_representation(self, obj):
        response = super(ProfileSerializer, self).to_representation(obj)

        remove = []

        if not obj.public:
            for field in response:
                if field not in self.PUBLIC_FIELDS:
                    remove.append(field)
        for i in remove:
            del response[i]
        return response

    def create(self, validated_data, **kwargs):
        print(validated_data, **kwargs)

        user = CustomUser(
            user= User.objects.get(username=validated_data["user"]['username']),
            name = validated_data["name"]
        )
        user.save()
        # create profile

        return user
        # create user
