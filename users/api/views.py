from django.contrib.auth import get_user_model
from rest_framework import viewsets as viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from . import permissions, serializers


class AuthMixin:
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticatedOrOptions,)


class UsersViewSet(AuthMixin, viewsets.ModelViewSet):
    """
    This endpoint presents the list of users in the system
    """
    queryset = get_user_model().objects.all()
    serializer_class = serializers.UserSerializer

    def retrieve(self, request, pk=None):
        """
        If provided 'pk' is "me" then return the current user.
        """
        if pk == 'me':
            return Response(serializers.UserSerializer(request.user).data)
        return super(UsersViewSet, self).retrieve(request, pk)
