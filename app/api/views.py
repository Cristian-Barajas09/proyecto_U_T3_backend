"""API views."""
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema,OpenApiParameter
from drf_spectacular.types import OpenApiTypes
from rest_framework import viewsets ,permissions
from .models import Profile
from .serializers import ProfileSerializers
# Create your views here.

class ExampleView(APIView):
    """Example View"""
    @extend_schema(
        parameters=[
            OpenApiParameter(
                name='example',
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                description='Example query parameter',
            ),
        ],
        responses={200: OpenApiTypes.OBJECT},
    )
    def get(self, request):
        """GET request."""
        return Response(
            {'message': 'Hello, World!', 'example': request.query_params.get('example')}
        )



class ProfileViewset(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProfileSerializers



