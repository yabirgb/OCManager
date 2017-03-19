from rest_framework import serializers

from .models import Community, Event
from users.serializers import UserSerializer
from users.models import CustomUser

class CommunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = ('name', 'city', 'slug', 'description')

class EventSerializer(serializers.ModelSerializer):

    going = UserSerializer(read_only=True, many=True)
    notGoing = UserSerializer(read_only=True, many=True)
    organizer = CommunitySerializer(serializers.ModelSerializer)

    class Meta:
        model = Event
        fields = ('name', 'place', 'description', 'date', 'going', 'notGoing', 'slug', 'organizer')
