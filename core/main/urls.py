from django.conf.urls import url, include
from django.contrib import admin

from rest_framework import routers
from rest_framework.authtoken import views

from users import urls as userUrl
from community import urls as cUrls

from users.authentication import obtain_auth_token

urlpatterns = [
    url(r'^users/', include(userUrl)),
    url(r'^events/', include(cUrls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^token-auth/', obtain_auth_token),
    url(r'^admin/', admin.site.urls),
]
