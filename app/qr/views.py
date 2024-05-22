"""Views for the QR app."""
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import segno


# Create your views here.

@api_view(['POST'])
def generate_qr(request):
    try:

        qr = segno.make('Hello, World!')
        qr.save('app/qr/static/{}.png')
        return Response({'message': 'QR code generated successfully!'}, status=status.HTTP_200_OK)
    except Exception as e:
        pass