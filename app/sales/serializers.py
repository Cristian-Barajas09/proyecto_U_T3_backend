"""This module contains the serializers for the sales app."""
from dataclasses import dataclass
from rest_framework import serializers
from .models import PayMethod, Order, OrderPlates, Payment

class PayMethodSerializers(serializers.ModelSerializer):
    """This module contains the serializers for the sales app."""
    @dataclass
    class Meta:
        """This class contains the metadata for the PayMethodSerializer."""
        model = PayMethod
        fields = ('id','currency','method')

class OrderSerializers(serializers.ModelSerializer):
    """This module contains the serializers for the sales app."""
    @dataclass
    class Meta:
        """This class contains the metadata for the OrderSerializer."""
        model = Order
        fields= '__all__'


class OrderPlatesSerializers(serializers.ModelSerializer):
    """This module contains the serializers for the sales app."""
    @dataclass
    class Meta:
        """This class contains the metadata for the OrderPlatesSerializer."""
        model = OrderPlates
        fields='__all__'


class PaymentSerializers(serializers.ModelSerializer):
    """This module contains the serializers for the sales app."""
    @dataclass
    class Meta:
        """This class contains the metadata for the PaymentSerializer."""
        model =  Payment
        fields= '__all__'
