from django.conf.urls import url, include
from django.contrib import admin

from rest_framework import routers
from rest_framework.routers import DefaultRouter


from .views import EventViewSet, CommunityViewSet

router = DefaultRouter()
router.register(r'events', EventViewSet, base_name="event")
router.register(r'', CommunityViewSet, base_name="community")
urlpatterns = router.urls
