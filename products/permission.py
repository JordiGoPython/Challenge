from rest_framework import permissions
from rest_framework.authtoken.models import Token


class IsAuthenticatedPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            if 'HTTP_AUTHORIZATION' in request.META.keys():
                key = request.META['HTTP_AUTHORIZATION']
                Token.objects.get(key=key)
                return True
            else:
                return False
        except Exception as e:
            return False