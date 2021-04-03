"""Users app views"""

from django.contrib.auth import login
from knox.models import AuthToken
from knox.views import LoginView as KnoxLoginView
from rest_framework import generics, permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response

from .serializers import LoginSerializer, RegisterSerializer, UserSerializer


class UserAPIView(generics.RetrieveAPIView):
    """
    View to retrieve a data about request user
    Only authenticated users can access this view
    """

    permission_classes = [
        permissions.IsAuthenticated,
    ]

    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class RegisterAPIView(generics.GenericAPIView):
    """
    View which registers a new user
    """

    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        """
        Creates a new user and returns authentication token and data about new user
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        instance, token = AuthToken.objects.create(user)
        return Response(
            {
                "user": UserSerializer(
                    user, context=self.get_serializer_context()
                ).data,
                "token": token,
                "expiry": instance.expiry,
            }
        )


class LoginAPIView(KnoxLoginView):
    """
    View which logins user in system
    Inherits :see: `KnoxLoginView`
    """

    serializer_class = LoginSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        """
        Logins user with provided data
        :returns Auth token and data about logged in user
        """
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        login(request, user)
        return super().post(request, format=None)

    def get_user_serializer_class(self):
        """Overrides default user serializer """
        return UserSerializer
