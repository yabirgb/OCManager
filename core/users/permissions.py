from rest_framework import permissions
from rest_framework.compat import is_authenticated

class IsAdminOrPost(permissions.BasePermission):

    def has_permission(self, request, view):
        grant = False
        ALLOWED = ('PUT', 'POST')

        if request.user.is_staff:
            grant = True
        elif request.method in ALLOWED:
            grant = True

        return grant
