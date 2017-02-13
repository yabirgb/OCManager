from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework import viewsets
from rest_framework import authentication, permissions
from rest_framework.response import Response

from .serializers import (EventSerializer, CommunitySerializer)
from .models import Event, Community

# Create your views here.
class EventViewSet(viewsets.ModelViewSet):

    serializer_class = EventSerializer
    queryset = Event.objects.all()
    lookup_field='pk'

    def list(self, request):
        queryset = Event.objects.all().order_by("-date")
        serializer = EventSerializer(queryset, many=True)
        return Response(serializer.data)
"""
    def retrieve(self, request, pk=None):
        queryset = Event.objects.all()
        event = get_object_or_404(queryset, pk=pk)
        serializer = EventSerializer(event)
        return Response(serializer.data)
"""
