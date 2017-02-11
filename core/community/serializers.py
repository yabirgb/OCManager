from rest_framework import serializers

from .models import Community, Event

class CommunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = ('name', 'city', 'description', 'events')

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('name', 'place', 'date', 'going', 'notGoing')
