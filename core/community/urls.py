from django.conf.urls import url, include
from django.contrib import admin

from rest_framework import routers
from rest_framework.routers import DefaultRouter


from .views import EventViewSet

router = DefaultRouter()
router.register(r'', EventViewSet, base_name="event")
urlpatterns = router.urls
