from rest_framework import permissions
from rest_framework.views import Request, Response, View


class IsAdminOrReadOnly(permissions.BasePermission):

    def has_permission(self, request: Request, view: View) -> Response:

        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_superuser
        )