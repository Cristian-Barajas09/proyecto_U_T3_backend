from rest_framework import serializers
from .models import Profile


class ProfileSerializers (serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields= '__all__'
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }