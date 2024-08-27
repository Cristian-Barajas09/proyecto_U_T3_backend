"""Serializers for the API."""
from dataclasses import dataclass
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer,
    AuthUser
)
from rest_framework_simplejwt.tokens import Token
from rolepermissions.roles import get_user_roles
from api.models import Profile


class ProfileSerializers (serializers.ModelSerializer):
    """Profile serializer."""

    @dataclass
    class Meta:
        """Meta class."""
        model = Profile
        fields= '__all__'

class UserSerializer(ModelSerializer):
    """User serializer."""
    @dataclass
    class Meta:
        """Meta class."""
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

class UserTokenReponseSerializer(serializers.Serializer):

    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    roles = serializers.ListField(child=serializers.CharField())



    @dataclass
    class Meta:
        """Meta class."""


class CustomObtainPairSerializer(TokenObtainPairSerializer):
    """Custom token serializer."""
    
    @classmethod
    def get_token(cls, user: AuthUser) -> Token:
        token = super().get_token(user)

        roles = get_user_roles(user)

        token['roles'] = roles

        return token
