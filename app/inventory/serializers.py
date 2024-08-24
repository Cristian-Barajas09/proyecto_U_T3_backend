"""Serializers for inventory app"""
from dataclasses import dataclass
from rest_framework import serializers
from inventory.models import Plates, Category

class PlatesSerializers(serializers.ModelSerializer):
    """Serializer for Plates"""

    @dataclass
    class Meta:
        """Meta class for PlatesSerializers"""
        model = Plates
        fields = ('id','title','description','image','price','categories')


class CategorySerializers(serializers.ModelSerializer):
    """Serializer for Category"""

    @dataclass
    class Meta:
        """Meta class for CategorySerializers"""
        model = Category
        fields = ('id','title','description')
