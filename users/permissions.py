from rest_framework import permissions
from rest_framework.views import Request, Response, View


class IsAdminOrReadOnly(permissions.BasePermission):

    def has_permission(self, request: Request, view: View) -> Response:

        return (
            request.method in permissions.SAFE_METHODS
             
            or request.user.is_superuser
        )
    

class IsAdminOrAccountOwner(permissions.BasePermission):

    def has_object_permission(self, request: Request, view: View, obj: object) -> bool:

        return (
            request.user.is_authenticated
            and obj == request.user
            or request.user.is_superuser
        )