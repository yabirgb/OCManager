from django.conf.urls import url, include
from rest_framework import routers
from django.contrib import admin
from .views import (UserViewSet)

router = routers.DefaultRouter()
router.register(r'', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
]
