"""Serializers module"""

from django.contrib.auth import authenticate, get_user_model
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Public user data serializer"""

    class Meta:
        """Meta class"""

        model = get_user_model()
        fields = ("id", "username", "email")


class RegisterSerializer(serializers.ModelSerializer):
    """Serializer for data needed for registration"""

    class Meta:
        """Meta class"""

        model = get_user_model()
        fields = ("id", "username", "email", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        """

        :param validated_data: Validated data handled from request
        :type validated_data: User
        :return: returns new user
        :rtype: User
        """
        user = get_user_model().objects.create_user(
            validated_data["username"],
            validated_data["email"],
            validated_data["password"],
        )
        return user


class LoginSerializer(serializers.Serializer):
    """Serializer for data needed for login"""

    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        """validates data needed for login"""
        user = authenticate(**attrs)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")
