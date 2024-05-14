from rest_framework import viewsets ,permissions
from .models import Order, OrderPlates, Payment, PayMethod
from .serializers import OrderSerializers, OrderPlatesSerializers, PaymentSerializers, PayMethodSerializers

class OrderViewset(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = OrderSerializers

class OrderPlatesViewset(viewsets.ModelViewSet):
    queryset = OrderPlates.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = OrderPlatesSerializers

class PaymentViewset(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    permission_classes= [permissions.IsAuthenticated]
    serializer_class = PaymentSerializers

class PayMethodViewset(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PayMethodSerializers
