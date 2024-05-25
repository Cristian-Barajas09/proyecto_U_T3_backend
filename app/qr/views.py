"""Views for the QR app."""
from django.http import FileResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import segno


# Create your views here.

@api_view(['POST','GET'])
def qr_view(request):
    if request.method == 'POST':
        try:

            url = request.data.get('url')


            qr = segno.make_qr(url)
            qr.save(
                'static/qr.png',scale=5,border=10
            )
            return Response({'message': 'QR code generated successfully!'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)



    return FileResponse(open('static/qr.png', 'rb'))
