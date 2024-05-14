from rest_framework import serializers
from .models import PayMethod, Order, OrderPlates, Payment

class PayMethodSerializers(serializers.ModelSerializer):
    class Meta:
        model = PayMethod
        fields = ('id','currency','method')

class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model: Order
        fields= '__all__'

class OrderPlatesSerializers(serializers.ModelSerializer):
    class Meta:
        model: OrderPlates
        fields='__all__'

class PaymentSerializers(serializers.ModelSerializer):
    class Meta:
        model: Payment
        fields= '__all__'