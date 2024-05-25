"""Serializers for inventory app"""
from dataclasses import dataclass
from rest_framework import serializers
from .models import Plates,Category,Ingredient

class PlatesSerializers(serializers.ModelSerializer):
    """Serializer for Plates"""

    @dataclass
    class Meta:
        """Meta class for PlatesSerializers"""
        model = Plates
        fields = ('id','title','description','image','price','categories','ingredients')





class IngredientSerializers(serializers.ModelSerializer):
    """Serializer for Ingredient"""

    @dataclass
    class Meta:
        """Meta class for IngredientSerializers"""
        model = Ingredient
        fields = ('id','title','description')

class CategorySerializers(serializers.ModelSerializer):
    """Serializer for Category"""

    @dataclass
    class Meta:
        """Meta class for CategorySerializers"""
        model = Category
        fields = ('id','title','description')
