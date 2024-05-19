from rest_framework import serializers
from .models import Currency, CurrencyConverter

class CurrencySerializers(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = '__all__'

class CurrencyConverterSerializers(serializers.ModelSerializer):
    class Meta:
        model = CurrencyConverter
        fields = '__all__'