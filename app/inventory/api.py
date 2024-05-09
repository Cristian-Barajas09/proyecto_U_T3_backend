from rest_framework import viewsets ,permissions
from .models import Plates
from .serializers import PlatesSerializers

class PlatesViewset(viewsets.ModelViewSet):
    queryset = Plates.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PlatesSerializers


