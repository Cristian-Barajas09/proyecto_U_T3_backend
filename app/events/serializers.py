"""Events serializers."""
from dataclasses import dataclass
from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    """Event serializer"""
    @dataclass
    class Meta:
        """Meta class"""
        model = Event
        fields = '__all__'
