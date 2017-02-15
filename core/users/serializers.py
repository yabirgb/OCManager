from rest_framework import serializers

from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):

    username = serializers.CharField(source='user.username')
    email = serializers.CharField(source='user.email')

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'public', 'following')


class UserSerializerPublic(serializers.ModelSerializer):
    #username = serializers.CharField(source='user.username')

    class Meta:
        model = CustomUser
        fields = ('uid',)
