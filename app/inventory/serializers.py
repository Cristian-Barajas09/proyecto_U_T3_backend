from rest_framework import serializers
from .models import Plates

class PlatesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Plates
        fields = ('id','title','description','image','price',)