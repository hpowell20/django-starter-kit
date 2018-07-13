from rest_framework import permissions


class IsAuthenticatedOrOptions(permissions.BasePermission):
    """
    The request is authenticated as a user, or is an OPTIONS request.
    """
    def has_permission(self, request, view):
        user_is_authenticated = self.is_authenticated(request.user)

        if request.method == "OPTIONS" or request.user and user_is_authenticated:
            return True
        return False

    @staticmethod
    def is_authenticated(user):
        if callable(user.is_authenticated):
            return user.is_authenticated()

        return user.is_authenticated
