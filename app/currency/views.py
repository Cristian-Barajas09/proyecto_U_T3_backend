from rest_framework import viewsets ,permissions
from .models import Currency, CurrencyConverter
from .serializers import CurrencyConverterSerializers, CurrencySerializers

class CurrencyViewset(viewsets.ModelViewSet):
    queryset = Currency.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CurrencySerializers

class CurrencyConverterViewset(viewsets.ModelViewSet):
    queryset = CurrencyConverter.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CurrencyConverterSerializers

# Create your views here.
